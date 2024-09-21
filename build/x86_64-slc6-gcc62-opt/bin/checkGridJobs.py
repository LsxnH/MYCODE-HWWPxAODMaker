#!/usr/bin/env python

# ==============================================================================
# File: resubmitGridJobs.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: Get some information from grid jobs
# ==============================================================================


import user  # look for .pythonrc.py for user init
import os,sys
import time
from datetime import datetime
from glob import glob
import subprocess
from optparse import OptionParser
import urllib2
import requests
import json
import unicodedata



#===================================
# The main function... everything starts here
#===================================
def checkGridJobs(options,startTime):
    # Let's first get the info from the panda server what JEDI tasks we have
    taskList = queryPandaWebPage(options)
    print "Found %s tasks" % len(taskList)
    # print taskList[0]

    # Create some counters
    nFilesTotal         = 0
    nFilesFinishedTotal = 0
    nFilesToBeDoneTotal = 0

    # Now, iterate over all tasks and resubmit the failed or finished ones
    print "Task Name                                                                                                                               :  nFiles, nFinished (%)      , nToBeDone (%)"
    for task in taskList:
        taskname = task['taskname']
        dsInfo = task['dsinfo']
        nFiles = dsInfo['nfiles']
        nFilesTotal += nFiles
        nFilesFinished = dsInfo['nfilesfinished']
        nFilesFinishedTotal += nFilesFinished
        nFilesToBeDone = nFiles - nFilesFinished
        nFilesToBeDoneTotal += nFilesToBeDone
        if options.printDetail or options.printFineDetail: print "{0:<136}: {1:>7}, {2:>9} ({3:>7.3f}), {4:>9} ({5:>7.3f})".format(taskname, nFiles, nFilesFinished, 100.0*nFilesFinished/nFiles, nFilesToBeDone, 100.0*nFilesToBeDone/nFiles)
        if options.printFineDetail:
            taskID = task['jeditaskid']
            checkIncompleteInputDatasets(options,taskID)
            pass
        pass
    if nFilesTotal == 0: nFilesTotal = 1
    print "Total (Date: {0:})                                                                                                : {1:>7}, {2:>9} ({3:>7.3f}), {4:>9} ({5:>7.3f})".format(str(datetime.now()), nFilesTotal, nFilesFinishedTotal, 100.0*nFilesFinishedTotal/nFilesTotal, nFilesToBeDoneTotal, 100.0*nFilesToBeDoneTotal/nFilesTotal)

    return 0



def checkIncompleteInputDatasets(options,taskid):
    # taskid = 10186220
    # task link
    url = 'http://bigpanda.cern.ch/tasks/?jeditaskid={taskid}&json'.format(taskid=taskid)
    # retrieve the task status
    r = requests.get(url)
    j = r.json()
    # Create a dictionary where the key will be the input dataset container name
    # and the values will be the number of files and the number of files finished
    nInFilesDict  = {}
    nFinishedDict = {}
    # input datasets status
    inDS = (d for d in j[0]['datasets'] if d['type']=='input' and ( d['datasetname'].startswith('mc') or d['datasetname'].startswith('data')) )
    for d in inDS:
        inContName     = d['containername']
        if inContName.__contains__("data"): inContName = d['datasetname']
        if inContName.__contains__(":"): inContName = inContName.split(":")[1]
        inNFiles       = d['nfiles']
        nFilesFinished = d['nfilesfinished']
        nInFilesDict[inContName]  = nInFilesDict.get(inContName, 0) + inNFiles
        nFinishedDict[inContName] = nFinishedDict.get(inContName, 0) + nFilesFinished
        #print d['containername'], d['nfiles'], d['nfilesfinished']
        # print d['datasetname'], d['nfiles'], d['nfilesfinished']
        pass
    sortedDSKeys = sorted(nInFilesDict)
    linestToPrint = []
    linestToPrint.append("    Input Dataset Container Name                                                                                                        :  nFiles, nFinished (%)      , nToBeDone (%)")
    for dsName in sortedDSKeys:
        nFiles    = nInFilesDict[dsName]
        nFinished = nFinishedDict[dsName]
        nFilesToBeDone = nFiles - nFinished
        if nFilesToBeDone:
            linestToPrint.append("    {0:<132}: {1:>7}, {2:>9} ({3:>7.3f}), {4:>9} ({5:>7.3f})".format(dsName, nFiles, nFinished, 100.0*nFinished/nFiles, nFilesToBeDone, 100.0*nFilesToBeDone/nFiles))
            pass
        pass
    if len(linestToPrint) > 1:
        for line in linestToPrint:
            print line
            pass
        print
        pass
    return 0




def queryPandaWebPage(options):
    request = urllib2.Request(options.query, headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'})
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

    parser.add_option('--printDetail', action="store_true", dest='printDetail', default=False,
                      help="If true, print detail for every dataset found")

    parser.add_option('--printFineDetail', action="store_true", dest='printFineDetail', default=False,
                      help="If true, print information about how many files from an input dataset are not yet done")

    parser.add_option('--query', action="store", type="string", dest='query',
                      default="http://bigpanda.cern.ch/tasks/?taskname=group.phys-higgs.*_13TeV.HWW*PAOD*V15*&display_limit=1000&days=200",
                      help="The full panda (web page) query/url")


    # Actually parse all options
    (options, args) = parser.parse_args()

    assert isinstance( options.printFineDetail, bool )
    if options.printFineDetail: print "Using: --printFineDetail=%s" % options.printFineDetail

    assert isinstance( options.printDetail, bool )
    if options.printDetail: print "Using: --printDetail=%s" % options.printDetail

    # Set the right user name
    assert isinstance( options.userName, str )
    if options.userName == "": options.userName = os.getenv("USER")
    if options.printDetail: print "Using: --statusName=%s" % options.userName

    # The actual query
    assert isinstance( options.query, str )
    if options.printDetail: print "Using: --query=%s" % options.query

    # Now, actually run the submit job function
    nJobsSubmitted = checkGridJobs(options,startTime)

    # End the timing and print out the resulting total time
    endTime = time.time()
    if options.printDetail: print "\n\ncheckGridJobs.py: Total time spend: %12.6f s\n" % ( (endTime - startTime)*1.0 )

    pass
