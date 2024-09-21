#!/usr/bin/env python

# ==============================================================================
# File: masterGridJobs.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: This is the master that steers the other grid job monitoring and
#              downloading scripts.
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
import datetime


def resubmitSetup(options):
    sessionLogPath = options.resubmitLogFilePath
    exitCode = os.system( "mkdir -p %s;" % sessionLogPath )
    if exitCode:
        print "Couldn't make directory: %s " % sessionLogPath
        exit(9)
    dateTime = datetime.datetime.utcnow().isoformat()
    sessionLogFile = sessionLogPath + "resubmitGridJobs_%s.log" % dateTime
    jobLogFile = sessionLogPath + "resubmitGridJobsCommand_%s.log" % dateTime
    print "Using resubmit session log file: %s" % sessionLogFile
    sshCommand = "ssh %s@lxplus.cern.ch '" % options.userName
    sshCommand += "export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase; "
    sshCommand += "source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh; "
    sshCommand += "cd %s; " % options.athenaGridSubmitArea
    sshCommand += "source $AtlasSetup/scripts/asetup.sh; "
    sshCommand += "lsetup panda; "
    sshCommand += "voms-proxy-init --valid 96:00 --voms atlas:/atlas/phys-higgs/Role=production; "
    sshCommand += "mkdir -p runAutomatic; "
    sshCommand += "cd runAutomatic; "
    sshCommand += "resubmitGridJobs.py -v %s --logFilePath %s " % (options.version, options.resubmitLogFilePath)
    if options.doSystematics: sshCommand += " --doSystematics"
    sshCommand += " | tee %s; " % jobLogFile
    sshCommand += "exit;' | tee %s" % sessionLogFile # exit the ssh session and make a log file
    print "Going to run resubmit:"
    print sshCommand
    return sshCommand


def downloadSetup(options):
    sessionLogPath = options.downloadLogFilePath
    exitCode = os.system( "mkdir -p %s;" % sessionLogPath )
    if exitCode:
        print "Couldn't make directory: %s " % sessionLogPath
        exit(9)
    dateTime = datetime.datetime.utcnow().isoformat()
    sessionLogFile = sessionLogPath + "downloadGridJobs_%s.log" % dateTime
    jobLogFile = sessionLogPath + "downloadGridJobsCommand_%s.log" % dateTime
    print "Using download session log file: %s" % sessionLogFile
    sshCommand = "ssh %s@lxplus.cern.ch '" % options.userName
    sshCommand += "export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase; "
    sshCommand += "source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh; "
    sshCommand += "cd %s; " % options.downloadLogFilePath
    sshCommand += "export RUCIO_ACCOUNT=${USER}; "
    sshCommand += "lsetup rucio; "
    sshCommand += "voms-proxy-init --valid 96:00; "
    sshCommand += "%sHWWPhysicsxAODMaker/PhysicsxAODConfig/scripts/downloadGridJobs.py -v %s --jsonFilePath %s " % (options.athenaGridSubmitArea, options.version, options.jsonFilePath)
    #sshCommand += "downloadGridJobs.py -v %s --jsonFilePath %s " % (options.version, options.jsonFilePath)
    if options.suffix : sshCommand += " --suffix %s " % options.suffix
    sshCommand += " --logFilePath %s | tee %s; " % (options.downloadLogFilePath, jobLogFile)
    sshCommand += "exit;' | tee %s" % sessionLogFile # exit the ssh session and make a log file
    print "Going to run download:"
    print sshCommand
    return sshCommand


def batchSubmitReduceJob(options, dsID, datasetSize, datamc="mc"):
    scratchOutPath = "${TMPDIR}/%s/reduce/" % options.userName
    runDir         = "${TMPDIR}/%s/runAutomatic/" % options.userName
    eosPAODInPath  = "%sPAOD_2L/%s/" % (options.eosDir, options.version)
    eosPAODOutPath = "%sPAOD_2L/%s_DFOnly/" % (options.eosDir, options.version)
    print " type(dsID) = %s " % type(dsID)
    scratchFinalOutPath = scratchOutPath + datamc +"/"+ dsID + "/"
    eosPAODFinalOutPath = eosPAODOutPath + datamc +"/"+ dsID + "/"
    if options.debug: print "scratchOutPath      = %s" % scratchOutPath
    if options.debug: print "runDir              = %s" % runDir
    if options.debug: print "eosPAODInPath       = %s" % eosPAODInPath
    if options.debug: print "eosPAODOutPath      = %s" % eosPAODOutPath
    if options.debug: print "scratchFinalOutPath = %s" % scratchFinalOutPath
    if options.debug: print "eosPAODFinalOutPath = %s" % eosPAODFinalOutPath
    # Make sure the directory that holds the submit script file is available
    if not os.path.exists(options.batchScriptPath):
        print "Going to create directory: "+options.batchScriptPath
        os.makedirs(options.batchScriptPath)
        pass
    batchSubmitScript = options.batchScriptPath + "%s_reduce_%s_%s.sh" % (options.userName, options.version, dsID)
    queueName = "1nd"
    if datasetSize > 500e6: queueName = "8nh" # Above 500 MB
    if datasetSize > 2e9:   queueName = "1nd" # Above 2 GB
    bsubCommand = "bsub -q %s -J %s_%s_reduce_%s %s" % (queueName, options.userName, options.version, dsID, batchSubmitScript)
    # Now, write the file
    with open(batchSubmitScript,'w') as fileObject:
        fileObject.write("#!/bin/bash\n")
        fileObject.write("shopt -s expand_aliases\n")
        fileObject.write("source /afs/cern.ch/project/eos/installation/user/etc/setup.sh\n")
        fileObject.write("export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n")
        fileObject.write("source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh\n")
        fileObject.write("cd %s\n" % options.athenaReductionJobArea)
        fileObject.write("source $AtlasSetup/scripts/asetup.sh\n")
        fileObject.write("mkdir -p %s\n" % scratchOutPath)
        fileObject.write("mkdir -p %s\n" % runDir)
        fileObject.write("cd %s\n" % runDir)
        fileObject.write("echo 'Using eosPAODFinalOutPath=%s'\n" % eosPAODFinalOutPath)
        fileObject.write("runLocalReduce.py --inDir %s --outDir %s --inDSIDs %s\n" % (eosPAODInPath, scratchOutPath, dsID))
        fileObject.write("eos mkdir -p %s\n" % eosPAODFinalOutPath)
        fileObject.write("xrdcopy --force %s*.root root://eosuser.cern.ch/%s\n" % (scratchFinalOutPath, eosPAODFinalOutPath))
        fileObject.write("xrdcopy --force %slogReduce.txt root://eosuser.cern.ch/%slogReduce.txt\n" % (scratchFinalOutPath, eosPAODFinalOutPath))
        pass
    os.chmod(batchSubmitScript, 0755)
    print "Going to run reduce:"
    print bsubCommand
    return bsubCommand



#===================================
# The main function... everything starts here
#===================================
def masterGridJobs(options,startTime):
    timeout = False
    doneEverything = False
    # Renew the kerberos ticked
    renewKerberosTicket()
    nKerberosTicketRenews = 1

    # Run as long as there is still something to be done
    while not timeout and not doneEverything \
          and ( options.doResubmit or options.doDownload or options.doReduce ) :
        # Time of last iteration
        lastTime = time.time()
        # Create an empty list of jobs to run
        jobListToRun = []

        # Get the info about the status of all grid tasks from panda
        taskList = queryPandaWebPage(options)

        # Test if we should re-submit failed grid jobs
        if options.doResubmit : testNeedResubmit(options,taskList)
        if options.doResubmit :
            resubmitCommand = resubmitSetup(options)
            print "Adding resubmission job"
            jobListToRun.append((resubmitCommand,"resubmit",""))
            pass

        # See if we need to download done grid jobs
        if options.doDownload : testNeedDownload(options,taskList)
        if options.doDownload :
            downloadCommand = downloadSetup(options)
            print "Adding downloading job"
            jobListToRun.append((downloadCommand,"download",""))
            pass

        # See if we need to send reduction jobs to lxbatch
        if options.doReduce : testNeedReduce(options,taskList)
        if options.doReduce :
            reduceJobs = reduceJobList(options)
            print "Adding %i reduction jobs" % len(reduceJobs)
            jobListToRun.extend( reduceJobs )
            pass

        # Now, going to actually launch the jobs
        if len(jobListToRun): runSubprocesses(options,jobListToRun,startTime)
        else:
            print "Nothing to be done any more"
            doneEverything = True
            pass

        # Do the following only if we need to continue
        if not timeout and not doneEverything \
           and ( options.doResubmit or options.doDownload ) :
            # Send this process to sleep. We want to only iterate once per interval
            interval = 3600.0 # seconds
            # options.doResubmit = False
            # options.doDownload = False
            #interval = 500.0 # seconds
            currentTime = time.time()
            durationTime = (currentTime - lastTime)*1.0
            diffTime = (durationTime - interval)
            if diffTime < 0.0 :
                # We go to sleep for this difference
                sleepTime = -1.0*diffTime
                print "Going to sleep for %7.1f seconds" % sleepTime
                time.sleep(sleepTime)
                pass

            # Renew the kerberos ticket every 20 hours
            interval = 72000.0
            currentTime = time.time()
            durationTime = (currentTime - startTime)*1.0
            diffTime = (durationTime - (interval*nKerberosTicketRenews))
            if diffTime > 0.0 :
                renewKerberosTicket()
                nKerberosTicketRenews += 1
                pass
            pass

        pass # End of while loop

    return



def renewKerberosTicket():
    exitCode = os.system( "kinit -R" )
    if exitCode :
        "Seems like we couldn't renew the kerberos ticket... exiting"
        exit(10)
    return



def testNeedResubmit(options, taskList):
    # Now, iterate over all tasks and see if there is still something to re-submit
    nNotDone = 0
    for task in taskList:
        status = task['superstatus']
        taskname = task['taskname']
        #print "Status=%s, taskname=%s" % (status, taskname)
        if status != 'done':
            nNotDone += 1
            #print "Status=%s, taskname=%s" % (status, taskname)
            pass
        pass
    if nNotDone == 0:
        print "All grid jobs are done. Nothing to re-submit any more"
        options.doResubmit = False
        pass
    return options.doResubmit



def testNeedDownload(options, taskList):
    # Now, check how many grid jobs are already done
    nDone = 0
    for task in taskList:
        status = task['superstatus']
        #print status
        if status == 'done': nDone += 1
        pass

    # Now, look at the local json files and see how many we have.
    myFileList = glob( options.jsonFilePath +"*.json")
    # If we have fewer json files than there are done grid jobs, we need to download more
    nDoneGridSamples = nDone * len(options.streamNameList)
    # if options.debug:
    print "Have found %i done grid jobs, times %i stream names, equals %i samples, and %i local json status files" % (nDone, len(options.streamNameList), nDoneGridSamples, len(myFileList))
    if len(myFileList) < nDoneGridSamples : return True
    # If the number matches, assume that the download already started
    options.doDownload = False
    return options.doDownload



def testNeedReduce(options, taskList):
    # Now, check how many grid jobs exist
    # TODO: Currently, for MC only!
    nGridTasks = 0
    for task in taskList:
        taskname = task['taskname']
        if taskname.__contains__("data15"): continue # We cannot deal with data files yet
        nGridTasks += 1
        pass

    # Now, look at the local json files and see how many we have.
    nReductionRunningOrDone = 0
    fileList = glob( options.jsonFilePath +"*.json")
    for fullFilePath in fileList:
        jsonFileName = fullFilePath.split("/")[-1]
        datasetName  = jsonFileName.rstrip(".json")
        if datasetName.__contains__("data15"): continue # We cannot deal with data files yet
        if not datasetName.__contains__("PAOD_2L"): continue # We only deal with the PAOD_2L
        sDict = getStatusDict(options,datasetName)
        # Now, count the batch jobs that were already submitted
        if sDict.has_key('reduce'): nReductionRunningOrDone += 1
        pass

    # Check if both numbers agree
    if nGridTasks == nReductionRunningOrDone: options.doReduce = False
    return options.doReduce



def queryPandaWebPage(options):
    taskSeachString = "group.phys-higgs.*15_13TeV*PAOD_HWW."+options.version+"/&display_limit=5000&days=200"
    pandaAddress = "http://bigpanda.cern.ch/tasks/?taskname="
    query = pandaAddress + taskSeachString
    print "Pande query: %s" % query
    request = urllib2.Request(query, headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'})
    response = urllib2.urlopen(request)
    responseJSONObj = json.load(response)
    return responseJSONObj


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



def reduceJobList(options):
    jobList = []
    # Now, look at the local json files and see how many we have.
    fileList = glob( options.jsonFilePath +"*.json")
    #if options.debug: print "In reduceJobList(): found %i dictionary files" % len(fileList)
    for fullFilePath in fileList:
        #if options.debug: print "In reduceJobList(): Have json file: %s" % fullFilePath
        jsonFileName = fullFilePath.split("/")[-1]
        datasetName  = jsonFileName.rstrip(".json")
        #if options.debug: print "In reduceJobList(): Have datasetName = %s" % datasetName
        if datasetName.__contains__("data15"): continue # We cannot deal with data files yet
        if not datasetName.__contains__("PAOD_2L"): continue # We only deal with the PAOD_2L
        #if options.debug: print "In reduceJobList(): checking dictionary"
        dsNameTokens = datasetName.split('.')
        dsID = dsNameTokens[3]
        sDict = getStatusDict(options,datasetName)
        if not sDict.has_key('download'): continue # The download has not even started
        #if options.debug: print "In reduceJobList(): download has started"
        if not sDict['download'] == "done": continue # The download is not yet done
        #if options.debug: print "In reduceJobList(): download is done"
        if sDict.has_key('reduce'): continue # The reduction has already started
        #if options.debug: print "In reduceJobList(): reduction is already running or done"
        datasetSize = 0
        if sDict.has_key("datasetSize"): datasetSize = sDict["datasetSize"]
        # Now, actually build the command
        reduceCmd = batchSubmitReduceJob(options, dsID, datasetSize)
        jobList.append((reduceCmd,"reduce",datasetName))
        pass

    return jobList



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
            jobToRun,jobType,dsName = jobListToRun.pop()

            # Update the status information for this dataset
            if jobType == "reduce": updateStatusFile(options,dsName,statusDict={ jobType : "submitting"})

            # Actually run the job submission for one job
            print "Going to run: %s" % jobToRun
            # print "with arguments: %s" % jobStdIn
            #jobToRun = "sleep 1" # For debugging
            # proc = subprocess.Popen( jobToRun, shell=True, stdin=subprocess.PIPE , stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
            # proc.stdin.write(jobStdIn)
            # proc.communicate()
            # proc.stdin.close()
            proc = subprocess.Popen( jobToRun, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
            procAndInfoTuple = (proc,jobToRun,jobType,dsName)
            runningJobs.append(procAndInfoTuple)
            # Print elapsed time
            elapsedTime = time.time()
            print "Elapsed time: %12.6f s\n" % ( (elapsedTime - startTime)*1.0 )
            pass

        # in the case that we have the maximum number of threads check if any of them
        # are done. (also do this when we run out of data, until all the threads are done)
        else:
            time.sleep(0.5)
            for procAndInfoTuple in runningJobs:
                proc     = procAndInfoTuple[0]
                jobToRun = procAndInfoTuple[1]
                jobType  = procAndInfoTuple[2]
                dsName   = procAndInfoTuple[3]
                if options.debug: print "Going to see if a process finished: proc.pid()=%s, proc.poll()=%s" % (proc.pid, proc.poll())
                if proc.poll() != None : # process is done with its work
                    returnTextTupel = proc.communicate()
                    doneProcessCounter += 1
                    # Going to print the returned stuff, i.e., the merged stdout and stderr
                    print
                    print "Done running "+str(doneProcessCounter)+" out of "+str(nJobsTotal)
                    print "Job was:",jobToRun
                    print "which returned:"
                    print returnTextTupel[0]
                    runningJobs.remove(procAndInfoTuple)
                    # Update the status information for this dataset
                    if jobType == "reduce": updateStatusFile(options,dsName,statusDict={ jobType : "submitted"})
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

    parser.add_option('--logFilePath', action="store", type="string", dest='logFilePath',
                      default="/afs/cern.ch/user/k/kkoeneke/testarea/HWWGridJobProcessing/",
                      help="The path where the log and JSON files are located (or will be created)."
                      +" The JSON files will store all state transitions for every dataset")

    parser.add_option('--athenaGridSubmitArea', action="store", type="string", dest='athenaGridSubmitArea',
                      default="/afs/cern.ch/user/k/kkoeneke/testarea/HWWProdV8",
                      help="The path where the athena release is setup for submitting grid jobs")

    parser.add_option('--athenaReductionJobArea', action="store", type="string", dest='athenaReductionJobArea',
                      default="/afs/cern.ch/user/k/kkoeneke/testarea/HWWReduceV8",
                      help="The path where the athena release is setup for submitting the reduction jobs")

    parser.add_option('--statusName', action="store", type="string", dest='statusName', default='download',
                      help="Name for the dictionary key that will be saved in the JSON file")

    parser.add_option('-v', '--version', action="store", type="string", dest='version', default='v8',
                      help="Version number for your production")

    parser.add_option('--suffix', action="store", type="string", dest='suffix', default='',
                      help="An additional suffix to be used for the final eos directory")

    parser.add_option('-s', '--doSystematics', action="store_true", dest='doSystematics', default=False,
                      help="If set to true, will change the output dataset name from containing, e.g., 'v8' to 'sysv8'.")

    parser.add_option('--streamNames', action="store", type="string", dest='streamNames',
                      default="PAOD_2L,PAOD_2LDF,PAOD_WH,PAOD_ZH",
                      help="List all stream names for a given dataset that we want to download")

    parser.add_option('--nDownloads', action="store", type="int", dest='nDownloads', default=5,
                      help="Use this number of simultaneous rucio file downloads.")

    parser.add_option('--nProcs', action="store", type="int", dest='nProcs', default=5,
                      help="Use multiprocessing to submit jobs in parallel. Keep this number rather small,"
                      +" such that your machine isn't going to be blocked! Say < 5 or so?"
                      +" 0 means that no multiprocessing is attempted.")

    parser.add_option('--doResubmit', action="store_true", dest='doResubmit', default=False,
                      help="If set to true (default: False), will resubmit failed grid jobs.")

    parser.add_option('--doDownload', action="store_true", dest='doDownload', default=False,
                      help="If set to true (default: False), will download done grid jobs.")

    parser.add_option('--doReduce', action="store_true", dest='doReduce', default=False,
                      help="If set to true (default: False), will start reduction jobs on lxbatch.")

    parser.add_option('--debug', action="store_true", dest='debug', default=False,
                      help="If set to true (default: False), will print more debug messages.")

    # Actually parse all options
    (options, args) = parser.parse_args()

    # Set the right user name
    assert isinstance( options.userName, str )
    if options.userName == "": options.userName = os.getenv("USER")
    print "Using: --statusName=%s" % options.userName

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
    if len(options.logFilePath) and not options.logFilePath.endswith("/"): options.logFilePath += "/"
    options.logFilePath = options.logFilePath.replace("kkoeneke",options.userName)
    options.logFilePath = options.logFilePath.replace("/k/","/%s/"%(options.userName[0]))
    options.logFilePath = options.logFilePath + options.version + options.suffix + "/"
    print "Using: --logFilePath=%s" % options.logFilePath
    options.downloadLogFilePath = options.logFilePath + "download/"
    print "Using (inferred): --downloadLogFilePath=%s" % options.downloadLogFilePath
    options.resubmitLogFilePath = options.logFilePath + "resubmit/"
    print "Using (inferred): --resubmitLogFilePath=%s" % options.resubmitLogFilePath
    options.batchScriptPath = options.logFilePath + "batchScripts/"
    print "Using (inferred): --batchScriptPath=%s" % options.batchScriptPath
    options.jsonFilePath = options.logFilePath + "jobState/"
    print "Using (inferred): --jsonFilePath=%s" % options.jsonFilePath

    assert isinstance( options.athenaGridSubmitArea, str )
    if len(options.athenaGridSubmitArea) and not options.athenaGridSubmitArea.endswith("/"): options.athenaGridSubmitArea += "/"
    options.athenaGridSubmitArea = options.athenaGridSubmitArea.replace("kkoeneke",options.userName)
    options.athenaGridSubmitArea = options.athenaGridSubmitArea.replace("/k/","/%s/"%(options.userName[0]))
    print "Using: --athenaGridSubmitArea=%s" % options.athenaGridSubmitArea

    assert isinstance( options.athenaReductionJobArea, str )
    if len(options.athenaReductionJobArea) and not options.athenaReductionJobArea.endswith("/"): options.athenaReductionJobArea += "/"
    options.athenaReductionJobArea = options.athenaReductionJobArea.replace("kkoeneke",options.userName)
    options.athenaReductionJobArea = options.athenaReductionJobArea.replace("/k/","/%s/"%(options.userName[0]))
    print "Using: --athenaReductionJobArea=%s" % options.athenaReductionJobArea

    assert isinstance( options.statusName, str )
    print "Using: --statusName=%s" % options.statusName

    assert isinstance( options.version, str )
    print "Using: --version=%s" % options.version

    assert isinstance( options.suffix, str )
    print "Using: --suffix=%s" % options.suffix

    assert isinstance( options.doSystematics, bool )
    print "Using: --doSystematics=%s" % options.doSystematics

    assert isinstance( options.streamNames, str )
    print "Using: --streamNames=%s" % options.streamNames
    options.streamNameList = options.streamNames.split(",")
    print "Using (inferred): streamNameList=%s" % options.streamNameList

    assert isinstance( options.nDownloads, int )
    print "Using: --nDownloads=%s" % options.nDownloads

    assert isinstance( options.nProcs, int )
    print "Using: --nProcs=%s" % options.nProcs

    assert isinstance( options.doResubmit, bool )
    print "Using: --doResubmit=%s" % options.doResubmit

    assert isinstance( options.doDownload, bool )
    print "Using: --doDownload=%s" % options.doDownload

    assert isinstance( options.doReduce, bool )
    print "Using: --doReduce=%s" % options.doReduce

    assert isinstance( options.debug, bool )
    print "Using: --debug=%s" % options.debug

    # Now, actually run the submit job function
    nJobsSubmitted = masterGridJobs(options,startTime)

    # End the timing and print out the resulting total time
    endTime = time.time()
    print "\n\downloadGridJobs.py: Total time spend: %12.6f s\n" % ( (endTime - startTime)*1.0 )

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
