#!/usr/bin/env python

# ==============================================================================
# File: runLocalReduce.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: Crawl a local directory and look for samples to run the reduce script on
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
def localReduceJobs(options,startTime):
    # Get the list of input datasets to submit jobs for
    subDirsToReduce = findSubDirsToReduce(options)

    nJobsTotal = len(subDirsToReduce)
    print "Going to submit %i reduction jobs" % (nJobsTotal)

    # Loop over all dataset names to run
    jobListToRun = []
    jobIdx       = 0
    for inDir, outDir in zip(*(subDirsToReduce, getOutPathList(options,subDirsToReduce))) :
        jobIdx += 1
        jobToRun = getCommandToRun(options,inDir)
        jobListToRun.append( (jobToRun,outDir) )
        pass
    # Now, call the running function
    runSubprocesses(options,jobListToRun,startTime)

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
            print "...starting reduction job..."
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
        secondLastSubDir = inDirTokens[-2]
        currentOutDir = options.OutDir
        if lastSubDir.__contains__("data"): currentOutDir += lastSubDir
        else: currentOutDir += secondLastSubDir + "/" + lastSubDir
        if os.path.exists(currentOutDir):
            print "The output directory: '"+currentOutDir+"' already exists... exiting!"
            exit(0)
            pass
        os.makedirs(currentOutDir)
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



def findSubDirsToReduce(options):
    """
    This function looks at all sub-directories and returns a list of all of those which
    have at least one root file in them, using the full absolute path.
    """
    # Initial values
    returnPathList = []

    # Get the list of valid dataset ID ranges
    beginEndDSIDTupleList = getValidDatasetIDRanges(options)

    # Now, iterate over the sub-dirs of the provided basePath and see how many files there are.
    basePath = options.InDir
    # Include the data files, if requested
    dataPath = basePath+"data/"
    mcPath   = basePath+"mc/"
    if options.doData: returnPathList.append(dataPath)
    inSubDirList = listDir(options,mcPath)
    for subDir in inSubDirList:
        # Get the potential input files
        currentInDir = mcPath+subDir
        if passValidDatasetID(subDir,beginEndDSIDTupleList):
            returnPathList.append(currentInDir)
            pass
        pass
    return sorted(returnPathList)


def listDir(options,path):
    if not path.startswith("/eos"): return sorted(os.listdir(path))
    eosLS = "%s ls %s" % (options.eosCommand, path)
    proc = subprocess.Popen( eosLS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
    result = proc.communicate()
    dirs = result[0]
    dirList = dirs.rstrip("\n").split("\n")
    return sorted(dirList)


def getFileNames(options,path):
    eosLS = "%s ls %s" % (options.eosCommand, path)
    proc = subprocess.Popen( eosLS, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
    result = proc.communicate()
    files = result[0]
    fileList = sorted(files.rstrip("\n").split("\n"))
    files = ""
    basePath = options.xrdEOSPrefix + path
    if not basePath.endswith("/"): basePath += "/"
    for fileName in fileList:
        files += basePath + fileName + ","
        pass
    files = files.rstrip(",")
    return files


def getCommandToRun(options,inDir):
    """
    Build the command that we will actually run
    """
    #return "sleep 1" # For debugging
    if not inDir.startswith("/eos"):
        runCommand = "time athena.py -c \"INDIR='"+inDir+"';\" "+options.reduceScript+" 2>&1 > logReduce.txt"
        return runCommand
    inFiles = getFileNames(options,inDir)
    runCommand = "time athena.py -c \"INFILELIST='"+inFiles+"';\" "+options.reduceScript+" 2>&1 > logReduce.txt"
    return runCommand




def cleanDir(dirToClean):
    """
    Remove all files that athena generated, except for the root file and the log file.
    """
    # Get the files in the directory
    for fileName in os.listdir(dirToClean):
        if fileName.__contains__("pool.root"): continue
        if fileName.__contains__("logReduce"): continue
        fullPath = dirToClean+"/"+fileName
        os.remove(fullPath)
        pass
    return




if __name__ == '__main__':
    # Start the timing
    startTime = time.time()

    # Get the command line arguments, if given
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    # Add all possible options
    parser.add_option('--inDir', action="store", type="string", dest='InDir',
                      default="/afs/cern.ch/user/n/ndang/work/public/PAOD/PAOD_2L/v7/",
                      help="Define the input directory to crawl for sub-directories")

    parser.add_option('--outDir', action="store", type="string", dest='OutDir',
                      default="/tmp/kkoeneke/reduceResults/",
                      help="Define the output directory")

    parser.add_option('--inDSIDs', action="store", type="string", dest='InDSIDs', default="",
                      help='The dataset ID numbers for the input datasets that we actually want to run over. '
                      +'This should be one string with comma-separated values; where ranges can be given with hypens. '
                      +'An example would be: --inDSIDs="110010,112233,201020-201040,303030". '
                      +'If this option is not provided (meaning the default empty string is used), all samples will be used.')

    parser.add_option('--doData', action="store_true", dest='doData', default=False,
                      help="If set to true (default: false), will also run over the data directory.")

    parser.add_option('--reduceScript', action="store", type="string", dest='reduceScript',
                      default='PhysicsxAODConfig/PAODReduce.py',
                      help="The actual reduce script to use")

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

    assert isinstance( options.doData, bool )
    print "Using: --doData=%s" % options.doData

    assert isinstance( options.reduceScript, str )
    print "Using: --reduceScript=%s" % options.reduceScript

    assert isinstance( options.nProcs, int )
    print "Using: --nProcs=%s" % options.nProcs

    options.eosCommand = "/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select"
    options.xrdEOSPrefix = "root://eosuser.cern.ch/"
    # options.readFromEOS = False
    # if options.InDir.startswith("/eos"): options.readFromEOS = True

    # Now, actually run the submit job function
    nJobsSubmitted = localReduceJobs(options,startTime)

    # End the timing and print out the resulting total time
    endTime = time.time()
    print "\n\nlocalReduceJobs.py: Total time spend for merging all jobs: %12.6f s\n" % ( (endTime - startTime)*1.0 )

    pass
