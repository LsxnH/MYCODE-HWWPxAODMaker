#!/usr/bin/env python

# ==============================================================================
# File: downloadGridJobs.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: Monitor the grid jobs and download done ones automatically.
#              Move fully downloaded ones into the right folder structure on eos.
# ==============================================================================


import user  # look for .pythonrc.py for user init
import os,sys
import time
from glob import glob
import subprocess
from optparse import OptionParser
import urllib2
import json
import unicodedata
import shutil



#===================================
# The main function... everything starts here
#===================================
def downloadGridJobs(options,startTime):
    # Let's first get the info from the panda server what JEDI tasks we have
    taskList = queryPandaWebPage(options)
    print "Found %s tasks" % len(taskList)

    # Now, get the list of tasks that are done
    taskDoneList = getDoneTasks(options, taskList)
    print "Found %s tasks that are done" % len(taskDoneList)

    # Now, get the list of datasets that still need to be downloaded
    # datasetsToDownloadList = datasetsToDownload(options, [taskDoneList[0]])
    datasetsToDownloadList = datasetsToDownload(options, taskDoneList)
    print "Found %s datasets to be downloaded" % len(datasetsToDownloadList)

    # Build the list of download commands
    jobListToRun = buildCommandList(options, datasetsToDownloadList)
    print "Found %s download commands to run" % len(jobListToRun)

    # Setup all needed directories
    setupDirs(options)


    # Now, going to actually launch the downloads
    runSubprocesses(options,jobListToRun,startTime)

    return



def getStatusDict(options,datasetName):
    fileName = options.jsonFilePath + datasetName + ".json"
    # Test if the file exists. If not, return an empty dictionary
    if not os.path.isfile(fileName): return {}
    # Otherwise, the file exists and we can quickly open it in read-only mode
    with open(fileName,'r') as fileObject:
        statusDict = json.load(fileObject)
        # The file will be automatically closed when we leave this with block
        return statusDict
    # If we get to here, something went wrong
    print "ERROR: Couldn't get the status dictionary!!!"
    sys.exit(10)



def updateStatusFile(options,datasetName,statusDict):
    fileName = options.jsonFilePath + datasetName + ".json"
    # Test if the file exists
    if not os.path.isfile(fileName):
        # Assume we write it for the first time
        # Make sure the directory that holds the pickle file is available
        if not os.path.exists(options.jsonFilePath):
            print "Going to create directory: "+options.jsonFilePath
            os.makedirs(options.jsonFilePath)
            pass
        # As the file doesn't exist, we simply dump the given stateDict into a new JSON file
        # First, we open the new JSON file for writing
        with open(fileName,'w') as fileObject:
            # Then, we dump the dict into the file
            json.dump(statusDict,fileObject)
            # The file will be automatically closed when we leave this with block
            pass
        return 0 # Everything worked
    # Now, if we really need to update the JSON file content. So lets open the file for (over-)writing
    currentStatusDict = getStatusDict(options,datasetName)
    with open(fileName,'w') as fileObject:
        currentStatusDict.update(statusDict)
        json.dump(currentStatusDict,fileObject)
        # The file will be automatically closed when we leave this with block
        pass
    return 0



def queryPandaWebPage(options):
    taskSeachString = "group.phys-higgs.*15_13TeV*PAOD_HWW."+options.version+"/&display_limit=5000&days=200"
    pandaAddress = "http://bigpanda.cern.ch/tasks/?taskname="
    query = pandaAddress + taskSeachString
    print "Going to send request to panda web page: "+query
    request = urllib2.Request(query, headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'})
    response = urllib2.urlopen(request)
    responseJSONObj = json.load(response)
    print "Got response from panda web server."
    return responseJSONObj



def getDoneTasks(options, taskList):
    # Create an empty lists
    taskDoneList = []
    # Now, iterate over all tasks and schedule the done ones for downloading
    for task in taskList:
        # Get first some information about the current task
        status   = task['superstatus']
        #print status
        if status == 'done': taskDoneList.append(task)
        pass
    return taskDoneList



def datasetsToDownload(options, taskToDownloadList):
    if len(taskToDownloadList) == 0: return []
    datasetsToDownloadList = []
    # Figure out which datasets to download
    for task in taskToDownloadList:
        # Get first some information about the current task
        taskname = task['taskname']
        taskNameTokens = taskname.split('.')
        dsID = taskNameTokens[3]
        dsNameBase = taskname.rstrip("/")
        for sName in options.streamNameList:
            dsName = dsNameBase + "_" + sName
            #print dsName
            # Also, need to check if this dataset is not already being downloaded
            statusDict = getStatusDict(options,dsName)
            # Basically, if nobody says yet that this dataset is being downloaded,
            # or already has been downloaded, the dictionary entry will not exist
            if not statusDict.has_key(options.statusName):
                print "Going to download: %s" % dsName
                datasetsToDownloadList.append(dsName)
                pass
            pass
        pass
    return datasetsToDownloadList




def buildCommandList(options, datasetsToDownloadList):
    if len(datasetsToDownloadList) == 0: return []
    baseCommand = "rucio download --ndownloader %i --dir %s   " % (options.nDownloads, options.downloadDir)
    commandsToRunList = []
    # Figure out which datasets to download
    for dsName in datasetsToDownloadList:
        commandToRun = baseCommand + dsName
        #print commandToRun
        commandsToRunList.append((commandToRun,dsName))
        pass
    return commandsToRunList




def setupDirs(options):
    # Make sure the download directory is available
    if not os.path.exists(options.downloadDir):
        print "Going to create directory: "+options.downloadDir
        os.makedirs(options.downloadDir)
        pass

    # Make sure the EOS mounting directory is available
    options.eosMountDir = options.downloadDir+"/eos"
    if not os.path.exists(options.eosMountDir):
        print "Going to create directory: "+options.eosMountDir
        os.makedirs(options.eosMountDir)
        pass

    # Try to mount eos in the aforementioned directory
    # Source the eos setup script
    eosSetupScript = "source /afs/cern.ch/project/eos/installation/user/etc/setup.sh"
    print "Going to run: "+eosSetupScript
    print "Going to mount EOS in directory: "+options.eosMountDir
    eosSetupCommand = "#!/bin/bash\n shopt -s expand_aliases;\n %s;\n eosforceumount %s;\n eosmount %s;\n ls %s" % (eosSetupScript, options.eosMountDir, options.eosMountDir, options.eosMountDir)
    #print eosSetupCommand
    proc = subprocess.Popen( eosSetupCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
    returnTextTupel = proc.communicate()
    # Going to print the returned stuff, i.e., the merged stdout and stderr
    print returnTextTupel[0]
    if returnTextTupel[1]: sys.exit(returnTextTupel[1])

    # Make the main directory, if it doesn't yet exist
    options.eosBasePath = options.downloadDir + options.eosDir
    if not os.path.exists(options.eosBasePath):
        print "Going to create directory: "+options.eosBasePath
        os.makedirs(options.eosBasePath)
        pass
    for sName in options.streamNameList:
        fullPath = options.eosBasePath + sName +"/"+ options.version + options.suffix
        if not os.path.exists(fullPath):
            print "Going to create directory: "+fullPath
            os.makedirs(fullPath)
            pass
        pass
    return




def getFullTargetPath(options, datasetName):
    streamName = ""
    for sName in options.streamNameList:
        if datasetName.__contains__(sName):
            streamName = sName
            break
        pass
    dataOrMc = "mc"
    if datasetName.__contains__(".data"): dataOrMc = "data"
    fullTargetPath = options.eosDir + streamName +"/"+ options.version + options.suffix +"/"+ dataOrMc +"/"
    fullLocalTargetPath = options.eosBasePath + streamName +"/"+ options.version + options.suffix +"/"+ dataOrMc +"/"
    taskNameTokens = datasetName.split('.')
    dsID = taskNameTokens[3]
    if dataOrMc == "mc":
        fullTargetPath += dsID +"/"
        fullLocalTargetPath += dsID +"/"
    if not os.path.exists(fullLocalTargetPath):
        print "Going to create directory: "+fullLocalTargetPath
        os.makedirs(fullLocalTargetPath)
        pass
    return fullTargetPath




def moveDatasetToEOS(options, datasetName):
    fullSourcePath = options.downloadDir +"/"+ datasetName +"/"
    fullTargetPath = getFullTargetPath(options, datasetName)
    myFileList = glob( fullSourcePath+"*.root*")
    datasetSize = 0
    for inFile in myFileList:
        fileSize = os.path.getsize(inFile)
        datasetSize += fileSize
        print "Moving: %s (size in bytes: %i)" % (inFile, fileSize)
        print "    to: %s" % (fullTargetPath)
        copyCmd = "xrdcopy --force %s root://eosuser.cern.ch/%s" % (inFile,fullTargetPath)
        proc = subprocess.Popen( copyCmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
        returnTextTupel = proc.communicate()
        print returnTextTupel[0]
        if returnTextTupel[1]: sys.exit(returnTextTupel[1])
        print "Done moving file"
        pass
    # Clean up
    shutil.rmtree(fullSourcePath)
    return datasetSize




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
            jobToRun,dsName = jobListToRun.pop()

            # Update the status information for this dataset
            updateStatusFile(options,dsName,statusDict={ options.statusName : "downloading"})

            # Actually run the job submission for one job
            print "Going to run download number "+str(processCounter)+" of "+str(nJobsTotal)
            print jobToRun
            #jobToRun = "sleep 1" # For debugging
            print "...starting download..."
            proc = subprocess.Popen( jobToRun, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
            procAndInfoTuple = (proc,jobToRun,dsName)
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
                dsName   = procAndInfoTuple[2]
                if proc.poll() != None : # process is done with its work
                    returnTextTupel = proc.communicate()
                    doneProcessCounter += 1
                    # Going to print the returned stuff, i.e., the merged stdout and stderr
                    print
                    print "Done running "+str(doneProcessCounter)+" out of "+str(nJobsTotal)
                    print "Job was:",jobToRun
                    print "which returned:"
                    print returnTextTupel[0]
                    # Print elapsed time
                    elapsedTime = time.time()
                    print "Elapsed time: %12.6f s\n" % ( (elapsedTime - startTime)*1.0 )
                    runningJobs.remove(procAndInfoTuple)

                    # Update the status information for this dataset
                    updateStatusFile(options,dsName,statusDict={ options.statusName : "copying"})
                    # Move the files to the final EOS location
                    datasetSize = moveDatasetToEOS(options, dsName)
                    # Update the status information for this dataset
                    updateStatusFile(options,dsName,statusDict={ options.statusName : "done", "datasetSize" : datasetSize})

                    # Print elapsed time
                    elapsedTime = time.time()
                    print "Elapsed time: %12.6f s\n" % ( (elapsedTime - startTime)*1.0 )
                    pass
                pass
            pass
        pass

    return




if __name__ == '__main__':
    # Start the timing
    startTime = time.time()

    # Get the command line arguments, if given
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    # Add all possible options
    parser.add_option('--userName', action="store", type="string", dest='userName', default="",
                      help="The user name of the current user. If empty string (default), "
                      +"user name will be determined from the shell environment variable USER. "
                      +"Otherwise, the given one will be used.")

    parser.add_option('--eosDir', action="store", type="string", dest='eosDir',
                      default="/eos/user/k/kkoeneke/DataMC/PAOD/",
                      help="Define the eos directory to where the final result should be moved")

    parser.add_option('--downloadDir', action="store", type="string", dest='downloadDir',
                      default="/tmp/kkoeneke/gridJobDownloads/",
                      help="Define the temporary directory to where the download is happening")

    parser.add_option('--logFilePath', action="store", type="string", dest='logFilePath', default="",
                      help="The path where the log and JSON files are located (or will be created)."
                      +" The JSON files will store all state transitions for every dataset")

    parser.add_option('--jsonFilePath', action="store", type="string", dest='jsonFilePath', default="",
                      help="The path where the JSON files are located (or will be created)."
                      +" The JSON files will store all state transitions for every dataset")

    parser.add_option('--statusName', action="store", type="string", dest='statusName', default='download',
                      help="Name for the dictionary key that will be saved in the JSON file")

    parser.add_option('-v', '--version', action="store", type="string", dest='version', default='v8',
                      help="Version number for your production")

    parser.add_option('--suffix', action="store", type="string", dest='suffix', default='',
                      help="An additional suffix to be used for the final eos directory")

    parser.add_option('--streamNames', action="store", type="string", dest='streamNames',
                      default="PAOD_2L,PAOD_2LDF,PAOD_WH,PAOD_ZH",
                      help="List all stream names for a given dataset that we want to download")

    parser.add_option('--nDownloads', action="store", type="int", dest='nDownloads', default=5,
                      help="Use this number of simultaneous rucio file downloads.")

    parser.add_option('--nProcs', action="store", type="int", dest='nProcs', default=5,
                      help="Use multiprocessing to submit jobs in parallel. Keep this number rather small,"
                      +" such that your machine isn't going to be blocked! Say < 5 or so?"
                      +" 0 means that no multiprocessing is attempted.")

    # Actually parse all options
    (options, args) = parser.parse_args()

    # Set the right user name
    assert isinstance( options.userName, str )
    if options.userName == "": options.userName = os.getenv("USER")
    print "Using: --userName=%s" % options.userName

    # Check that we got valid options
    assert isinstance( options.eosDir, str )
    if len(options.eosDir) and not options.eosDir.endswith("/"): options.eosDir += "/"
    options.eosDir = options.eosDir.replace("kkoeneke",options.userName)
    options.eosDir = options.eosDir.replace("/k/","/%s/"%(options.userName[0]))
    print "Using: --eosDir=%s" % options.eosDir

    assert isinstance( options.downloadDir, str )
    if len(options.downloadDir): options.downloadDir = options.downloadDir.rstrip("/")
    options.downloadDir = options.downloadDir.replace("kkoeneke",options.userName)
    print "Using: --downloadDir=%s" % options.downloadDir

    assert isinstance( options.logFilePath, str )
    assert isinstance( options.jsonFilePath, str )
    givenFilePath = True
    if options.logFilePath == "":
        givenFilePath = False
        options.logFilePath = "/afs/cern.ch/user/k/kkoeneke/testarea/HWWGridJobProcessing/"
        pass
    if len(options.logFilePath) and not options.logFilePath.endswith("/"): options.logFilePath += "/"
    options.logFilePath = options.logFilePath.replace("kkoeneke",options.userName)
    options.logFilePath = options.logFilePath.replace("/k/","/%s/"%(options.userName[0]))
    if not givenFilePath:
        options.logFilePath = options.logFilePath + options.version + options.suffix
        if options.jsonFilePath == "": options.jsonFilePath = options.logFilePath + "/jobState/"
        options.logFilePath = options.logFilePath + "/logFilesDownload/"
        pass
    print "Using: --logFilePath=%s" % options.logFilePath
    print "Using (inferred): --jsonFilePath=%s" % options.jsonFilePath

    assert isinstance( options.statusName, str )
    print "Using: --statusName=%s" % options.statusName

    assert isinstance( options.version, str )
    print "Using: --version=%s" % options.version

    assert isinstance( options.suffix, str )
    print "Using: --suffix=%s" % options.suffix

    assert isinstance( options.streamNames, str )
    print "Using: --streamNames=%s" % options.streamNames
    options.streamNameList = options.streamNames.split(",")
    print "Using (inferred): streamNameList=%s" % options.streamNameList

    assert isinstance( options.nDownloads, int )
    print "Using: --nDownloads=%s" % options.nDownloads

    assert isinstance( options.nProcs, int )
    print "Using: --nProcs=%s" % options.nProcs

    # Now, actually run the submit job function
    nJobsSubmitted = downloadGridJobs(options,startTime)

    # End the timing and print out the resulting total time
    endTime = time.time()
    print "\n\ndownloadGridJobs.py: Total time spend: %12.6f s\n" % ( (endTime - startTime)*1.0 )

    pass


'''
Setup procedure:

login to lxplus

setupATLAS
cd testarea/HWWGridJobProcessing
export RUCIO_ACCOUNT=${USER}
lsetup rucio
voms-proxy-init --valid 96:00
${HOME}/testarea/HWWProdV7/PhysicsAnalysis/HiggsPhys/Run2/HWW/HWWxAODCode/HWWCommonxAODConfig/scripts/downloadGridJobs.py


'''
