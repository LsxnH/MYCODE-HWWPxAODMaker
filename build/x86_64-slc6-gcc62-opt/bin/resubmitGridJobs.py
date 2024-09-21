#!/usr/bin/env python

# ==============================================================================
# File: resubmitGridJobs.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: Monitor the grid jobs and resubmit failed/finished ones.
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



#===================================
# The main function... everything starts here
#===================================
def resubmitGridJobs(options,startTime):
    # Set some defaults
    if options.doSystematics :
        options.mcSubmitCommand   = 'submitGridJobs.py --nProcs 20 --doSystematics --merge -v %s --prod --inDSTextFile %s --run ' % (options.version, options.sampleListMC)
        options.dataSubmitCommand = 'submitGridJobs.py --nProcs 20 --doSystematics --merge -v %s --prod --inDSTextFile %s --run ' % (options.version, options.sampleListData)
        pass
    else:
        options.mcSubmitCommand   = 'submitGridJobs.py --nProcs 20 --merge -v %s --prod --inDSTextFile %s --run ' % (options.version, options.sampleListMC)
        options.dataSubmitCommand = 'submitGridJobs.py --nProcs 20 --merge -v %s --prod --inDSTextFile %s --run ' % (options.version, options.sampleListData)
        pass
    if options.official:
        options.mcSubmitCommand   += ' --official '
        options.dataSubmitCommand += ' --official '
        pass
    options.mcSubmitCommand   += ' --inDSIDs '
    options.dataSubmitCommand += ' --inDSIDs '

    # Create the directory for the log files, if needed
    if not os.path.exists(options.logFilePath):
        print "Going to create directory: "+options.logFilePath
        os.makedirs(options.logFilePath)
        pass

    # Let's first get the info from the panda server what JEDI tasks we have
    taskList = queryPandaWebPage(options)
    print "Found %s tasks" % len(taskList)

    # Create some empty lists
    taskDoneList       = []
    taskToResubmitList = []
    taskOtherList      = []

    nDone       = 0
    nRegistered = 0
    nRunning    = 0
    nFinished   = 0
    nFailed     = 0
    nBroken     = 0
    nAborted    = 0
    nOther      = 0
    # Now, iterate over all tasks and resubmit the failed or finished ones
    for task in taskList:
        # Get first some information about the current task
        status = task['superstatus']
        #print status
        if status == 'done': taskDoneList.append(task)
        elif status == 'failed' or status == 'finished': # or status == 'aborted' :
            taskToResubmitList.append(task)
            pass
        else: taskOtherList.append(task)
        # bookkeeping
        if status == 'finished':     nFinished   += 1
        elif status == 'done':       nDone       += 1
        elif status == 'registered': nRegistered += 1
        elif status == 'running':    nRunning    += 1
        elif status == 'failed':     nFailed     += 1
        elif status == 'broken':     nBroken     += 1
        elif status == 'aborted':    nAborted    += 1
        else:                        nOther      += 1
        pass
    print "Found %s done tasks"        % nDone
    print "Found %s running tasks"     % nRunning
    print "Found %s finished tasks"    % nFinished
    print "Found %s failed tasks"      % nFailed
    print "Found %s broken tasks"      % nBroken
    print "Found %s aborted tasks"     % nAborted
    print "Found %s registered tasks"  % nRegistered
    print "Found %s other tasks"       % nOther
    resubmitTasks(options, taskToResubmitList)
    #resubmitTasks(options, taskDoneList)

    return 0


def resubmitTasks(options, taskToResubmitList):
    if len(taskToResubmitList) == 0: return

    dsIDsMC = ""
    dsIDsData = ""
    # Figure out which dataset IDs or runnumbers to use
    for task in taskToResubmitList:
        # Get first some information about the current task
        taskname = task['taskname']
        taskNameTokens = taskname.split('.')
        dsID = taskNameTokens[3]
        if taskname.__contains__(".data"): dsIDsData += dsID + ","
        else : dsIDsMC += dsID + ","
        pass
    if len(dsIDsMC):
        dsIDsMC = dsIDsMC.rstrip(",")
        mcSubmitCommand = options.mcSubmitCommand + dsIDsMC
        print mcSubmitCommand
        # Now, actually resubmit
        proc = subprocess.Popen( mcSubmitCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
        returnTextTupel = proc.communicate()
        # Going to print the returned stuff, i.e., the merged stdout and stderr
        logText = returnTextTupel[0]
        # Write the log file of this resubmission
        writeLogFile(options,logText,"logResubmitMC_*.txt")
        pass
    if len(dsIDsData):
        dsIDsData = dsIDsData.rstrip(",")
        dataSubmitCommand = options.dataSubmitCommand + dsIDsData
        print dataSubmitCommand
        # Now, actually resubmit
        proc = subprocess.Popen( dataSubmitCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
        returnTextTupel = proc.communicate()
        # Going to print the returned stuff, i.e., the merged stdout and stderr
        logText = returnTextTupel[0]
        # Write the log file of this resubmission
        writeLogFile(options,logText,"logResubmitData_*.txt")
        pass

    return



def writeLogFile(options,logText,fileSearchString):
    # Figure out which log files already exist
    thisNumber = 1
    logFileList = glob( options.logFilePath+fileSearchString)
    numberList = []
    for fileName in logFileList:
        part0 = fileName.split("/")[-1] # Get the file name without the path
        part1 = part0.split("_")[1] # Get the number.txt part
        part2 = part1.split(".")[0] # Get the number
        number = int(part2)
        numberList.append(number)
        pass
    numberList.sort(reverse=True)
    if len(numberList): thisNumber = numberList[0] + 1
    logFileName = options.logFilePath + (fileSearchString.replace("*",str(thisNumber)))
    with open(logFileName,'w') as fileObject:
        fileObject.write(logText)
        # The file will be automatically closed when we leave this with block
        pass
    return



def queryPandaWebPage(options):
    taskSeachString = ""
    if options.doSystematics :
        taskSeachString = "group.phys-higgs.*15_13TeV*PAOD_HWW.*.sys"+options.version+"/&display_limit=5000&days=200"
        pass
    else:
        taskSeachString = "group.phys-higgs.*15_13TeV*PAOD_HWW.*."+options.version+"/&display_limit=5000&days=200"
        pass
    pandaAddress = "http://bigpanda.cern.ch/tasks/?taskname="
    query = pandaAddress + taskSeachString
    request = urllib2.Request(query, headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'})
    response = urllib2.urlopen(request)
    responseJSONObj = json.load(response)
    return responseJSONObj




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

    parser.add_option('-v', '--version', action="store", type="string", dest='version', default="v8",
                      help="Version number for your production")

    parser.add_option('--official', action="store_true", dest='official', default=False,
                      help="If true, use higgs group priviliges and store output on higgs group disk space")

    parser.add_option('--sampleListMC', action="store", type="string", dest='sampleListMC', default="samplelist_HIGG3D1_mc15ab.txt",
                      help="Name of the file that lists the MC samples")

    parser.add_option('--sampleListData', action="store", type="string", dest='sampleListData', default="samplelist_HIGG3D1_data15_25ns",
                      help="Name of the file that lists the data samples")

    parser.add_option('--logFilePath', action="store", type="string", dest='logFilePath', default="",
                      help="The path where the log files will be written")

    parser.add_option('-s', '--doSystematics', action="store_true", dest='doSystematics', default=False,
                      help="If set to true, will change the output dataset name from containing, e.g., 'v8' to 'sysv8'.")

    # Actually parse all options
    (options, args) = parser.parse_args()

    # Set the right user name
    assert isinstance( options.userName, str )
    if options.userName == "": options.userName = os.getenv("USER")
    print "Using: --statusName=%s" % options.userName

    # Check that we got valid options
    assert isinstance( options.version, str )
    print "Using: --version=%s" % options.version

    assert isinstance( options.official, bool )
    print "Using: --official=%s" % options.official

    assert isinstance( options.sampleListMC, str )
    print "Using: --sampleListMC=%s" % options.sampleListMC

    assert isinstance( options.sampleListData, str )
    print "Using: --sampleListData=%s" % options.sampleListData

    assert isinstance( options.logFilePath, str )
    givenFilePath = True
    if options.logFilePath == "":
        givenFilePath = False
        options.logFilePath = "/afs/cern.ch/user/k/kkoeneke/testarea/HWWGridJobProcessing/"
        pass
    if len(options.logFilePath) and not options.logFilePath.endswith("/"): options.logFilePath += "/"
    options.logFilePath = options.logFilePath.replace("kkoeneke",options.userName)
    options.logFilePath = options.logFilePath.replace("/k/","/%s/"%(options.userName[0]))
    if not givenFilePath:
        options.logFilePath = options.logFilePath + options.version + "/logFilesResubmitGridJobs/"
        pass
    print "Using: --logFilePath=%s" % options.logFilePath

    assert isinstance( options.doSystematics, bool )
    print "Using: --doSystematics=%s" % options.doSystematics

    # Now, actually run the submit job function
    nJobsSubmitted = resubmitGridJobs(options,startTime)

    # End the timing and print out the resulting total time
    endTime = time.time()
    print "\n\nresubmitGridJobs.py: Total time spend: %12.6f s\n" % ( (endTime - startTime)*1.0 )

    pass
