#!/usr/bin/env python

# ==============================================================================
# File: prepareInputFileTextLists.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: Crawl a local directory and look for matching samples to put into
#              text files that will be used by athena jobs to process them.
# ==============================================================================


import user  # look for .pythonrc.py for user init
import os,sys, shutil
import time
from glob import glob
from optparse import OptionParser
import collections




#===================================
# The main function... everything starts here
#===================================
def prepareInputFileTextLists(options,startTime):
    # if not os.path.exists(options.InDir)
    if not os.path.isdir(options.InDir):
        print("Given InDir=%s does not exist... exiting!" % options.InDir)
        return 1
    # Get the absolute path
    options.InDir = os.path.abspath(options.InDir)

    # Create an empty dictionary that will contain for each dataset path
    # a list of tuples of (file size, file name, full path)
    foundInFilesDict = {}

    # Some global numbers that we need
    GBConversion = 1.0 / (1024.0 * 1024.0 * 1024.0)

    # Look for all files under the given input path
    for dirName, subdirList, fileList in os.walk(options.InDir):
        # print('Found directory: %s' % dirName)
        lastDirName = dirName.split("/")[-1]
        if not (lastDirName.__contains__("group.") or lastDirName.__contains__("user.")): continue
        #print('Found directory: %s' % dirName)
        for fname in fileList:
            if not fname.__contains__(".pool.root"): continue
            # We must have found at least one input file to use
            fileSize = os.path.getsize(os.path.join(dirName,fname))
            #print('\t%s %i' % (fname, fileSize))
            currentDictionaryList = foundInFilesDict.get(lastDirName,[])
            currentDictionaryList.append( (dirName+"/", fname, fileSize) )
            currentDictionaryList = sorted(currentDictionaryList)
            foundInFilesDict[lastDirName] = currentDictionaryList
            pass
        pass
    #print foundInFilesDict
    for dirName in foundInFilesDict.keys():
        print dirName
        # Create the output base directory, if it doesn't exist.
        if not os.path.exists(options.OutDir): os.makedirs(options.OutDir)
        # Remove the sub-directory, if it exists
        outDirName = options.OutDir + dirName
        if os.path.exists(outDirName): shutil.rmtree(outDirName)
        os.makedirs(outDirName)
        # Figure out if we are looking at MC (default) or data, based on the name
        # of the last directory (which should coincide with the rucio dataset name)
        isMC = True
        if dirName.__contains__("data"): isMC = False

        inFileList = foundInFilesDict[dirName]
        #print inFileList
        nMax = len(inFileList)
        i = 0
        currentNumber = 0
        runningTotal = 0
        aggregatedSize = 0
        totalSize = 0
        aggregatedFiles = []
        print "Number of found input files: %i" % nMax
        currentDSID = 0
        currentAMITag = ""
        outFileName = None
        previousOutFileName = ""
        for dirName, fname, fileSize in inFileList:
            i += 1
            currentNumber += 1
            #print "i=%i, file name: %s, file size: %8.4f GB" % (i, fname, fileSize * GBConversion)
            aggregatedSize += fileSize
            totalSize      += fileSize
            aggregatedFiles.append(dirName+fname)
            dumpFile = False
            if aggregatedSize >= options.MaxSize : dumpFile = True
            if i == nMax: dumpFile = True
            # If we reach the maximum allowed number of input files, we close this list and open a new one
            if currentNumber >= options.maxNumber:
                dumpFile = True
                currentNumber = 0
                pass
            currentDSID   = fname.split(".")[2]
            currentAMITag = fname.split(".")[3]
            # # Build the file name
            # if not outFileName:
            #     outFileName = fname.replace(".PAOD",".merge.PAOD")
            #     outFileName = outFileName.split(".pool.root")[0] + ".pool.root.txt"
            #     pass
            # Build the file name
            if not outFileName: outFileName = fname
            if not outFileName.endswith(".pool.root.txt"): outFileName = outFileName.split(".pool.root")[0] + ".pool.root.txt"
            if not dumpFile:# and isMC:
                nextFileName = inFileList[i][1]
                nextDSID   = nextFileName.split(".")[2]
                nextAMITag = nextFileName.split(".")[3]
                if currentDSID != nextDSID and isMC:
                    #print "Found changing DSID from %s to %s" % (currentDSID,nextDSID)
                    dumpFile = True
                    pass
                if currentAMITag != nextAMITag and isMC:
                    #print "Found changing AMITag from %s to %s" % (currentAMITag,nextAMITag)
                    dumpFile = True
                    pass
                pass
            if dumpFile == True:
                runningTotal += 1
                # Remove the double AMITag appearing in the name
                if currentAMITag == outFileName.split(".")[4]:
                    outFileName = outFileName.replace("."+currentAMITag+".", ".", 1)
                    pass
                print "Creating text file %s, containing %i files and total size %7.4f GB" \
                      % (outFileName, len(aggregatedFiles), aggregatedSize * GBConversion)
                outFile = open(outDirName + "/" + outFileName,"w")
                for filePathAndName in aggregatedFiles:
                    outFile.write(filePathAndName+"\n")
                    pass
                outFile.close()
                # Reset everything
                aggregatedSize = 0
                aggregatedFiles = []
                previousOutFileName = outFileName
                outFileName = None
            pass
        print "Number of created text files: %i out of %i files with total input size of %9.4f GB" \
              % (runningTotal, nMax, totalSize * GBConversion)

        pass



#group.phys-higgs.00310872.f756_m1710_p2840.10924440.PAOD_FakeL._000152.pool.root




    return



if __name__ == '__main__':
    # Start the timing
    startTime = time.time()

    # Get the command line arguments, if given
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    # Add all possible options
    parser.add_option('--inDir', action="store", type="string", dest='InDir',
                      default=".",
                      help="Define the input directory to crawl for sub-directories (NOT recursive!)")

    parser.add_option('--outDir', action="store", type="string", dest='OutDir',
                      default="/tmp/" + os.getenv("USER") + "/fileListsToProcess/",
                      help="Define the input directory to crawl for sub-directories (NOT recursive!)")

    parser.add_option('--maxSize', action="store", type="float", dest='MaxSize', default=5.0,
                      help="The maximal aggregated size of all files for one job (in GB)")

    parser.add_option('--maxNumber', action="store", type="int", dest='maxNumber', default=200,
                      help="The maximal number of input files for one job (in GB)")

    # Actually parse all options
    (options, args) = parser.parse_args()

    # Check that we got valid options
    assert isinstance( options.InDir, str )
    if len(options.InDir) and not options.InDir.endswith("/"): options.InDir += "/"
    print "Using: --inDir=%s" % options.InDir

    assert isinstance( options.OutDir, str )
    if len(options.OutDir) and not options.OutDir.endswith("/"): options.OutDir += "/"
    print "Using: --outDir=%s" % options.OutDir

    assert isinstance( options.MaxSize, float )
    print "Using: --maxSize=%s GB" % options.MaxSize
    # Transform into bytes
    options.MaxSize = options.MaxSize * 1024 * 1024 * 1024

    assert isinstance( options.maxNumber, int )
    print "Using: --maxNumber=%s" % options.maxNumber

    # Now, actually run the submit job function
    nJobsSubmitted = prepareInputFileTextLists(options,startTime)

    # End the timing and print out the resulting total time
    endTime = time.time()
    print "\n\nprepareInputFileTextLists.py: Total time spend for preparing all text files: %12.6f s\n" % ( (endTime - startTime)*1.0 )

    pass
