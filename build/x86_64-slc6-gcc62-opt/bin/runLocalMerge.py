#!/usr/bin/env python

# ==============================================================================
# File: runLocalMerge.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: Crawl a local directory and look for samples to merge
# ==============================================================================


import user  # look for .pythonrc.py for user init
import os,sys
import time
from glob import glob
import subprocess
from optparse import OptionParser




#===================================
# The main function... everything starts here
#===================================
def localMergeJobs(options,startTime):
    # Get the list of input datasets to submit jobs for
    subDirsToMerge, tooLargeDirsList, sizeOfAllDirsToProcess = findSubDirsToMerge(options)
    printTooLargeDirs(tooLargeDirsList)

    nJobsTotal = len(subDirsToMerge)
    print "Going to submit %i merging jobs (total size of all input files is %6.2f GB)" % (nJobsTotal, sizeOfAllDirsToProcess/1.0e9)

    # Loop over all dataset names to run
    jobListToRun = []
    jobIdx       = 0
    for inDir, outDir in zip(*(subDirsToMerge, getOutPathList(options,subDirsToMerge))) :
        jobIdx += 1
        jobToRun = getCommandToRun(options,inDir)
        jobListToRun.append( (jobToRun,outDir) )
        pass
    # Now, call the running function
    runSubprocesses(options,jobListToRun,startTime)

    # Make annother printout to tell the user of some dirs that were not merged
    printTooLargeDirs(tooLargeDirsList)

    return jobIdx




def runSubprocesses(options,jobListToRun,startTime):
    """
    This function deals with actually creating the sub-processes, one for each
    grid job submission.
    """
    # This list will contain the individual processes
    runningJobs = []

    # run until all the threads are done, and there is no job to submit left
    nJobsTotal = len(jobListToRun)
    processCounter     = 0
    doneProcessCounter = 0
    while runningJobs or jobListToRun:
        # if we aren't using all the processors AND there is still data left to
        # compute, then spawn another thread
        if (len(runningJobs) < options.nProcs) and jobListToRun:
            processCounter += 1
            jobToRun,outDir = jobListToRun.pop()

            # Actually run the job submission for one job
            print "Going to run job number "+str(processCounter)+" of "+str(nJobsTotal)
            print "Using output directory: "+outDir
            os.chdir(outDir)
            print jobToRun
            #jobToRun = "sleep 1" # For debugging
            print "...starting merge job..."
            proc = subprocess.Popen( jobToRun, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
            procAndInfoTuple = (proc,jobToRun,outDir)
            runningJobs.append(procAndInfoTuple)
            # Print elapsed time
            elapsedTime = time.time()
            print "Elapsed time: %12.6f s\n" % ( (elapsedTime - startTime)*1.0 )
            pass

        # in the case that we have the maximum number of threads check if any of them
        # are done. (also do this when we run out of data, until all the threads are done)
        else:
            time.sleep(0.1)
            for procAndInfoTuple in runningJobs:
                proc     = procAndInfoTuple[0]
                jobToRun = procAndInfoTuple[1]
                outDir   = procAndInfoTuple[2]
                if proc.poll() != None : # process is done with its work
                    returnTextTupel = proc.communicate()
                    doneProcessCounter += 1
                    # Going to print the returned stuff, i.e., the merged stdout and stderr
                    print
                    print "Done running "+str(doneProcessCounter)+" out of "+str(nJobsTotal)
                    print "Used output directory: "+outDir
                    print "Job was:",jobToRun
                    print "which returned:"
                    print returnTextTupel[0]
                    # Remove all unneeded files in that output directory
                    cleanDir(outDir)
                    # Print elapsed time
                    elapsedTime = time.time()
                    print "Elapsed time: %12.6f s\n" % ( (elapsedTime - startTime)*1.0 )
                    runningJobs.remove(procAndInfoTuple)
                    pass
                pass
            pass
        pass

    return


def getOutPathList(options,inDirList):
    """
    Build a list of output directories
    """
    outDirList = []
    for inDir in inDirList:
        inDirTokens = inDir.split("/")
        lastSubDir = inDirTokens[-1]
        currentOutDir = options.OutDir + lastSubDir
        if os.path.exists(currentOutDir):
            print "The output directory: '"+currentOutDir+"' already exists... exiting!"
            exit(0)
            pass
        os.mkdir(currentOutDir)
        outDirList.append( currentOutDir )
        pass
    if len(inDirList) != len(outDirList):
        print "Input directory list and output directory list don't have the same size!"
        print "Input directory list:  %s" % inDirList
        print "Output directory list: %s" % outDirList
        exit(0)
        pass
    return outDirList





def getValidDatasetIDRanges(options):
    """
    This function builds from the provided options.InDSIDs the list of allowed ranged of dataset IDs.
    """
    inDSSelectionString = options.InDSIDs
    beginEndDSIDTupleList = []
    if len(inDSSelectionString) == 0:
        # We have an empty dataset selection string, thus use all samples
        tmpTuple = (0,99999999)
        beginEndDSIDTupleList.append(tmpTuple)
        return beginEndDSIDTupleList
    inDSSelectionString = inDSSelectionString.rstrip(",")
    tmpList = inDSSelectionString.split(",")
    for tmp in tmpList:
        if tmp.__contains__("-") :
            tmpTuple = tuple(tmp.split("-"))
            beginEndDSIDTupleList.append( (int(tmpTuple[0]),int(tmpTuple[1])) )
            pass
        else :
            tmpTuple = (int(tmp),int(tmp))
            beginEndDSIDTupleList.append(tmpTuple)
            pass
        pass
    return beginEndDSIDTupleList



def passValidDatasetID(inDSID,beginEndDSIDTupleList):
    """
    Find if the current inDSID is in the provided valid ranges of dataset IDs.
    """
    # Convert to int
    inDSIDInt = int(inDSID)
    for matchTuple in beginEndDSIDTupleList :
        #print "Trying to match DSID=%i against tuple: %s" % (inDSID, matchTuple)
        if inDSIDInt >= matchTuple[0] and inDSIDInt <= matchTuple[1] :
            #print "Found a match"
            return True
        pass
    return False



def findSubDirsToMerge(options):
    """
    This function looks at all sub-directories and returns a list of all of those which
    have at least two root files in them, using the full absolute path.
    """
    # Initial values
    returnPathList = []
    tooLargeDirsList = []
    sizeOfAllDirsToProcess = 0

    # Get the list of valid dataset ID ranges
    beginEndDSIDTupleList = getValidDatasetIDRanges(options)

    # Now, iterate over the sub-dirs of the provided basePath and see how many files there are.
    basePath = options.InDir
    inSubDirList = sorted(os.listdir(basePath))
    for subDir in inSubDirList:
        # Get the potential input files
        currentInDir = basePath+subDir
        inFileList = glob( currentInDir+"/*.root*")
        #print "Found %i files in input directory: %s" % (len(inFileList), currentInDir)
        if len(inFileList) > 1 and passValidDatasetID(subDir,beginEndDSIDTupleList):
            # Only consider the directories where the total sum of file sizes is less than 10 GB
            totalSize  = 0
            for inFile in inFileList:
                fileSize = os.path.getsize(inFile)
                totalSize += fileSize
                pass
            if totalSize <= 10e9:
                returnPathList.append(currentInDir)
                sizeOfAllDirsToProcess += totalSize
                pass
            else:
                tooLargeDirsList.append(currentInDir)
                pass
            pass
        pass
    return sorted(returnPathList), sorted(tooLargeDirsList), sizeOfAllDirsToProcess



def getCommandToRun(options,inDir):
    """
    Build the command that we will actually run
    """
    #return "sleep 1" # For debugging
    mergeCommand = "time athena.py -c \"INDIR='"+inDir+"';\" "+options.MergeScript+" 2>&1 > logMerge.txt"
    return mergeCommand



def cleanDir(dirToClean):
    """
    Remove all files that athena generated, except for the root file and the log file.
    """
    # Get the files in the directory
    for fileName in os.listdir(dirToClean):
        if fileName.__contains__("pool.root"): continue
        if fileName.__contains__("logMerge"): continue
        fullPath = dirToClean+"/"+fileName
        os.remove(fullPath)
        pass
    return


def printTooLargeDirs(tooLargeDirsList):
    """
    Print a message for all directories where the total size exceeded 10 GB.
    """
    # If we have an empty list, there is nothing to be done
    if len(tooLargeDirsList) == 0: return

    print
    print
    print
    print "*** ATTENTION ***: There were %i directories whose total size exceeded 10 GB!" % len(tooLargeDirsList)
    print
    print "You should inspect them and decide if you want to submit merging jobs by hand using the commands below:"
    print
    for tooLargeDir in tooLargeDirsList:
        print getCommandToRun(options,tooLargeDir)
        pass
    print
    print
    return




if __name__ == '__main__':
    # Start the timing
    startTime = time.time()

    # Get the command line arguments, if given
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    # Add all possible options
    parser.add_option('--inDir', action="store", type="string", dest='InDir',
                      default="/afs/cern.ch/user/n/ndang/work/public/PAOD/PAOD_2L/v6_reduce/mc/",
                      help="Define the input directory to crawl for sub-directories (NOT recursive!)")

    parser.add_option('--outDir', action="store", type="string", dest='OutDir',
                      default="/tmp/kkoeneke/mergeResults/",
                      help="Define the input directory to crawl for sub-directories (NOT recursive!)")

    parser.add_option('--inDSIDs', action="store", type="string", dest='InDSIDs', default="",
                      help='The dataset ID numbers for the input datasets that we actually want to run over. '
                      +'This should be one string with comma-separated values; where ranges can be given with hypens. '
                      +'An example would be: --inDSIDs="110010,112233,201020-201040,303030". '
                      +'If this option is not provided (meaning the default empty string is used), all samples will be used.')

    parser.add_option('--mergeScript', action="store", type="string", dest='MergeScript',
                      default='PhysicsxAODConfig/PAODMerge.py',
                      help="The actual merge script to use")

    parser.add_option('--nProcs', action="store", type="int", dest='nProcs', default=5,
                      help="Use multiprocessing to submit jobs in parallel. Keep this number rather small,"
                      +"such that your machine isn't going to be blocked! Say < 5 or so?"
                      +" 0 means that no multiprocessing is attempted.")

    # Actually parse all options
    (options, args) = parser.parse_args()

    # Check that we got valid options
    assert isinstance( options.InDir, str )
    if len(options.InDir) and not options.InDir.endswith("/"): options.InDir += "/"
    print "Using: --inDir=%s" % options.InDir

    assert isinstance( options.OutDir, str )
    if len(options.OutDir) and not options.OutDir.endswith("/"): options.OutDir += "/"
    print "Using: --outDir=%s" % options.OutDir

    assert isinstance( options.InDSIDs, str )
    print "Using: --inDSIDs=%s" % options.InDSIDs

    assert isinstance( options.MergeScript, str )
    print "Using: --mergeScript=%s" % options.MergeScript

    assert isinstance( options.nProcs, int )
    print "Using: --nProcs=%s" % options.nProcs

    # Now, actually run the submit job function
    nJobsSubmitted = localMergeJobs(options,startTime)

    # End the timing and print out the resulting total time
    endTime = time.time()
    print "\n\nrunMerge.py: Total time spend for merging all jobs: %12.6f s\n" % ( (endTime - startTime)*1.0 )

    pass
