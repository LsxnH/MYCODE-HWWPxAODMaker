#!/usr/bin/env python

# ==============================================================================
# File: sumitGridJobs.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: This file is a python executable that is meant for grid submission
# ==============================================================================


import user  # look for .pythonrc.py for user init
import os,sys
import PyUtils.RootUtils as ru
ROOT = ru.import_root()
ROOT.gErrorIgnoreLevel = 2000 # to avoid printout when creating images
from ROOT import *
from optparse import OptionParser
import time
import subprocess
from string import split
from PhysicsxAODConfig.HWWCommonHelpers import search_file


#===================================
# The main function... everything is done here
#===================================
def SubmitJobs(options,startTime):
    nJobsSubmitted = 0
    # Do some option massaging
    if options.doSystematics:
        options.version = "sys"+options.version
        pass
    if options.doFakeWJets:   options.version += "_FakeWJets"
    elif options.doFakeZJets: options.version += "_FakeZJets"
    elif options.doFakeDiJet: options.version += "_FakeDiJets"

    # # Determine if we want to run the merging of the output on the grid or not
    # if options.InDSTextFile.__contains__("mc15") and not options.doEffiScaleFactors:
    #     options.Merge = False
    #     pass

    # See if we want to submit everything in one task (= one output dataset) or not
    if options.oneOutDS:
        nJobsSubmitted = SubmitOneTask(options,startTime)
        pass
    else:
        nJobsSubmitted = SubmitIndividualTasks(options,startTime)
        pass

    if not options.Run :
        print
        print
        print "*** ATTENTION ***:  Did NOT actually submit the above jobs. If you want to submit them, you need to add: --run"
        pass

    return nJobsSubmitted


def SubmitOneTask(options,startTime):
    # Build the one output dataset name
    outDSName = "group.phys-higgs."
    if not options.official: outDSName = "user.%s." % options.userName
    if options.InDSTextFile.__contains__("mc15"):     outDSName += "mc15_13TeV"
    elif options.InDSTextFile.__contains__("mc16"):   outDSName += "mc16_13TeV"
    elif options.InDSTextFile.__contains__("data15"): outDSName += "data15_13TeV"
    elif options.InDSTextFile.__contains__("data16"): outDSName += "data16_13TeV"
    elif options.InDSTextFile.__contains__("data17"): outDSName += "data17_13TeV"
    elif options.InDSTextFile.__contains__("data18"): outDSName += "data18_13TeV"
    else :                                            outDSName += "any_13TeV"

    middleName = ".HWW"
    if   options.InDSTextFile.__contains__("mc16a"):   middleName += "_mc16a"
    elif options.InDSTextFile.__contains__("mc16d"):   middleName += "_mc16d"
    elif options.InDSTextFile.__contains__("mc16e"):   middleName += "_mc16e"
    if options.doMediumOtherLeptons:                   middleName += "_Medium"
    elif options.doVeryLooseLH:                        middleName += "_VeryLooseLH"
    if options.doORNoMuNearJetRemoval and not options.doORNoMuNearJetRemovalNoBJetPrecedence:
        middleName += "_NoMuNearJetVeto"
    if options.doORNoMuNearJetRemovalNoBJetPrecedence: middleName += "_NoMuNearJetVetoNoBJetPrec"
    if options.doPFlowJets:                            middleName += "_EMPFlow"
    if not options.doEffiScaleFactors:                 middleName += "_NoEffiSF"
    middleName += options.middleNameExtra
    if options.InDSTextFile.__contains__("__"):
        middleName += "_"+options.InDSTextFile.split("__")[1].split(".")[0]
        pass
    outDSName += middleName

    reconmergeType = ".recon."
    if options.Merge: reconmergeType = ".merge."
    outDSName += reconmergeType + options.outDSType + "."
    if not options.Prod: outDSName += "TEST_"
    outDSName += options.version
    #partSuffix = "_Part" + str(options.partNumber).zfill(2) # fill up leading zero, if single-digit number given
    #outDSName += partSuffix
    outDSName += "/"

    # Test if the given filename corresponds to a physical file
    # # CMake should be automatically installing them now such that they are available in $PATH
    # search_path = os.environ["PATH"]
    # fullInFileName = search_file(options.InDSTextFile, search_path)
    # if not fullInFileName:
    #     print "Coudn't find input file name '"+options.InDSTextFile+"' in $PATH."
    #     print "Please check that it is in PhysicsxAODConfig/scripts and re-run cmake if so."
    #     exit(0)

    fullInFileName = os.getenv("TestArea")
    fullInFileName += "/PhysicsxAODConfig/scripts/"
    fullInFileName += options.InDSTextFile
    if not os.path.exists(fullInFileName) :
        print "Coudn't find input file name: ", fullInFileName
        exit(0)

    # Create the submit string
    jobToRun = 'pathena '
    if options.athenaOptions != "": jobToRun += ' -c "%s" ' % options.athenaOptions
    jobToRun += ' '+options.topOptionsPath+' '
    jobToRun += ' --dbRelease LATEST '
    if options.official: jobToRun += ' --official --voms=atlas:/atlas/phys-higgs/Role=production '
    jobToRun += ' --inDsTxt=' + fullInFileName
    jobToRun += ' --outDS ' + outDSName
    if options.NFilesPerJob : jobToRun += ' --nFilesPerJob=%s ' % options.NFilesPerJob
    else : jobToRun += ' --nGBPerJob=%s ' % options.NGBPerJob
    if options.official: jobToRun += ' --destSE ' + options.DestinationSE
    #jobToRun += ' --skipScout '
    if not options.InDSTextFile.__contains__("data"): jobToRun += ' --useContElementBoundary '
    jobToRun += ' --addNthFieldOfInDSToLFN=2,6 '
    if options.useNewCode: jobToRun += ' --useNewCode '
    if options.ForceStaged: jobToRun += ' --forceStaged '
    #jobToRun += ' --forceStaged '
    if options.ExcludedSite: jobToRun += ' --excludedSite='+options.ExcludedSite+' '
    #jobToRun += ' --noCompile --site=ANALY_AUSTRALIA'
    if options.Merge: jobToRun += ' --mergeOutput --mergeScript='+options.mergeScript+' '
    #jobToRun += ' --allowTaskDuplication '

    # Now, run the job that we just assambled
    runJob(options,jobToRun,1,1,len(outDSName),startTime)


    return 1


def SubmitIndividualTasks(options,startTime):
    # Get the list of input datasets to submit jobs for
    dsListToRun = selectInputDatasets( options.InDSIDs, options.InDSTextFile )

    nJobsTotal = len(dsListToRun)
    print "Going to submit %s jobs" % nJobsTotal

    # Loop over all dataset names to run
    jobListToRun = []
    jobIdx=0
    for inDSName in dsListToRun:
        jobIdx += 1
        # Create the output dataset name
        dsNameTokens = inDSName.split(".")
        dsNTIdx = 0
        if dsNameTokens[0] == "group" or dsNameTokens[0] == "user" : dsNTIdx = 2
        dsIDName = dsNameTokens[dsNTIdx+1]
        sampleTags = dsNameTokens[-1]
        # Add something to the output dataset ID if the input is AtlFast2
        #if sampleTags.__contains__("_a"): dsIDName += "AF2"
        outDSName = "group.phys-higgs."
        if not options.official: outDSName = "user.%s." % options.userName
        outDSName += dsNameTokens[dsNTIdx] +"."+ dsIDName +"."
        physShortName = dsNameTokens[dsNTIdx+2]
        physVeryShortName = physShortName[:32] if len(physShortName) > 32 else physShortName
        physVeryShortName = physVeryShortName.rstrip("_")
        outDSName += physVeryShortName
        if options.topOptionsPath.__contains__("PAODReduce"): outDSName += ".reduce"
        if options.topOptionsPath.__contains__("PAODMerge"):  outDSName += ".merge"
        outDSName += "."+options.outDSType+"."
        outDSName += sampleTags+"."
        if not options.Prod: outDSName += "TEST_"
        outDSName += options.version
        outDSName += "/"

        # Create the submit string
        jobToRun = 'pathena '
        if options.athenaOptions != "": jobToRun += ' -c "%s" ' % options.athenaOptions
        jobToRun += ' '+options.topOptionsPath+' '
        jobToRun += ' --dbRelease LATEST '
        if options.official: jobToRun += ' --official --voms=atlas:/atlas/phys-higgs/Role=production '
        jobToRun += ' --inDS ' + inDSName
        jobToRun += ' --outDS ' + outDSName
        if options.NFilesPerJob : jobToRun += ' --nFilesPerJob %s ' % options.NFilesPerJob
        else : jobToRun += ' --nGBPerJob=%s ' % options.NGBPerJob
        if options.official: jobToRun += ' --destSE ' + options.DestinationSE
        #jobToRun += ' --skipScout '
        jobToRun += ' --useContElementBoundary '
        jobToRun += ' --addNthFieldOfInDSToLFN=2,6 '
        if options.useNewCode: jobToRun += ' --useNewCode '
        if options.ForceStaged: jobToRun += ' --forceStaged '
        if options.ExcludedSite: jobToRun += ' --excludedSite='+options.ExcludedSite+' '
        #jobToRun += ' --noCompile --site=ANALY_AUSTRALIA'
        if options.Merge: jobToRun += ' --mergeOutput --mergeScript='+options.mergeScript+' '
        #jobToRun += ' --allowTaskDuplication '

        # Modify further if we want to reuse the tar-ball and the configuration
        # from the first job for all subsequent jobs
        if options.Reuse :
            tarBallName = 'gridJobTarBall.tar.gz'
            configName  = 'gridJobConfigCache.txt'
            if jobIdx == 1 :
                # We are at the first job and need to create the tar-ball
                jobToRun += ' --outTarBall ' +tarBallName+ ' --outRunConfig ' +configName
                pass
            else:
                # Now, reuse the tar-ball and configuration of the first job
                jobToRun += ' --inTarBall ' +tarBallName+ ' --inRunConfig ' +configName
                pass
            pass
        # jobToRun = "sleep 10; ls" # for debugging

        # Now, submit the job
        lenOutDSName = len(outDSName)
        # We always need to run the first job on its own since it produces the tar ball.
        if jobIdx==1 or options.nProcs==0 :
            runJob(options,jobToRun,jobIdx,nJobsTotal,lenOutDSName,startTime)
            pass
        else :
            jobListToRun.append( (jobToRun,lenOutDSName) )
            pass
        pass

    # If we want to run multiprocessing, we will run now the remaining jobs
    if options.nProcs!=0 :
        runSubprocesses(options,jobListToRun,startTime)
        pass

    return jobIdx



def runSubprocesses(options,jobListToRun,startTime):
    """
    This function deals with actually creating the sub-processes, one for each
    grid job submission.
    """
    # This list will contain the individual processes
    runningJobs = []

    # run until all the threads are done, and there is no job to submit left
    nJobsTotal = len(jobListToRun) + 1
    processCounter = 1 # We start at one since we already submitted the first job serially
    doneProcessCounter = 1
    while runningJobs or jobListToRun:
        # if we aren't using all the processors AND there is still data left to
        # compute, then spawn another thread
        if (len(runningJobs) < options.nProcs) and jobListToRun:
            processCounter += 1
            jobToRun,lenOutDSName = jobListToRun.pop()

            # Actually run the job submission for one job
            print "Going to submit job number "+str(processCounter)+" of "+str(nJobsTotal)+" (lenght of outDS name is "+str(lenOutDSName)+"):"
            print jobToRun
            if options.Run :
                print "...submitting..."
                # proc = subprocess.Popen( jobToRun, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
                proc = subprocess.Popen( jobToRun, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
                procAndInfoTuple = (proc,jobToRun,lenOutDSName)
                runningJobs.append(procAndInfoTuple)
                pass
            # Print elapsed time
            elapsedTime = time.time()
            print "Elapsed time: %12.6f s\n" % ( (elapsedTime - startTime)*1.0 )
            pass

        # in the case that we have the maximum number of threads check if any of them
        # are done. (also do this when we run out of data, until all the threads are done)
        else:
            time.sleep(0.1)
            for procAndInfoTuple in runningJobs:
                proc         = procAndInfoTuple[0]
                jobToRun     = procAndInfoTuple[1]
                lenOutDSName = procAndInfoTuple[2]
                if proc.poll() != None : # process is done with its work
                    returnTextTupel = proc.communicate()
                    doneProcessCounter += 1
                    # Going to print the returned stuff, i.e., the merged stdout and stderr
                    print
                    print "Done submitting "+str(doneProcessCounter)+" out of "\
                          +str(nJobsTotal)+" jobs (lenght of outDS name is "+str(lenOutDSName)+"). Job was:"
                    print jobToRun
                    print "which returned:"
                    print returnTextTupel[0]
                    # Print elapsed time
                    elapsedTime = time.time()
                    print "Elapsed time: %12.6f s\n" % ( (elapsedTime - startTime)*1.0 )
                    runningJobs.remove(procAndInfoTuple)
                    pass
                pass
            pass
        pass

    return


def runJob(options,jobToRun,jobIdx,nJobsTotal,lenOutDSName,startTime):
    """
    This short function is actually calling the command to submit one job
    to the grid.
    """
    print
    print "Going to submit job number "+str(jobIdx)+" of "+str(nJobsTotal)+" (lenght of outDS name is "+str(lenOutDSName)+"):"
    print jobToRun
    if options.Run :
        print "...submitting..."
        # os.system( jobToRun )
        # proc = subprocess.Popen( jobToRun, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
        proc = subprocess.Popen( jobToRun, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
        returnTextTupel = proc.communicate()
        # Going to print the returned stuff, i.e., the merged stdout and stderr
        print returnTextTupel[0]
        pass
    # Print elapsed time
    elapsedTime = time.time()
    print "Elapsed time: %12.6f s\n" % ( (elapsedTime - startTime)*1.0 )
    return



def selectInputDatasets(inDSSelectionString,filename):
    """
    This function selects from the input sample list which input datasets to run over.
    """
    inDSList = readSampleListFile(filename)
    if len(inDSSelectionString) == 0:
        # We have an empty dataset selection string, thus use all samples
        return inDSList
    inDSListToRun = []
    beginEndDSIDTupleList = []
    inDSSelectionString = inDSSelectionString.rstrip(",")
    tmpList = inDSSelectionString.split(",")
    for tmp in tmpList:
        if tmp.__contains__("-") :
            tmpTuple = tuple(tmp.split("-"))
            beginEndDSIDTupleList.append(tmpTuple)
            pass
        else :
            tmpTuple = (tmp,tmp)
            beginEndDSIDTupleList.append(tmpTuple)
            pass
        pass
    for inDSName in inDSList :
        # inDSID = int(inDSName.split(".")[1])
        inDSID = getDatasetID(inDSName)
        #print "Now looking at input DSID =", inDSID
        for matchTuple in beginEndDSIDTupleList :
            #print "Trying to match against tuple:", matchTuple
            if inDSID >= int(matchTuple[0]) and inDSID <= int(matchTuple[1]) :
                #print "Found a match"
                inDSListToRun.append(inDSName)
                pass
            pass
        pass
    #print "Got inDSListToRun:", inDSListToRun
    return inDSListToRun


def getDatasetID(datasetName) :
    """
    This function tries to extract the dataset ID number from the name of the dataset.
    """
    dsNameList = datasetName.split(".")
    # Assume the first part that is convertable to an int is the dataset ID
    dsID = 0
    for dsName in dsNameList:
        try:
            dsID = int(dsName)
            break
        except ValueError:
            pass
        pass
    if dsID == 0 :
        print "Coudn't determine the dataset ID from dataset name: ", datasetName
        exit(0)
    return dsID



def readSampleListFile(filename) :
    """
    This function reads in the text file that lists all possible input datasets.
    """
    inDSList = []
    # Test if the given filename corresponds to a physical file
    # # CMake should be automatically installing them now such that they are available in $PATH
    # search_path = os.environ["PATH"]
    # fullInFileName = search_file(filename, search_path)
    # if not fullInFileName:
    #     print "Coudn't find input file name '"+filename+"' in $PATH."
    #     print "Please check that it is in PhysicsxAODConfig/scripts and re-run cmake if so."
    #     exit(0)
    fullInFileName = os.getenv("TestArea")
    fullInFileName += "/PhysicsxAODConfig/scripts/"
    fullInFileName += filename
    if not os.path.exists(fullInFileName) :
        print "Coudn't find input file name: ", fullInFileName
        exit(0)
    inFile = open(fullInFileName, 'r')
    for line in inFile:
        # Remove carriage returns and whitespaces
        line = line.rstrip('\n')
        line = line.strip()
        if line: # Skip empty lines
            inDSList.append(line)
            pass
        pass
    if len(inDSList) == 0:
        print "Got zero possible files to run over", fullInFileName
        exit(0)
    # Sort the list in alphabetical order
    inDSList.sort()
    #print "Got inDSList:", inDSList
    return inDSList



if __name__ == '__main__':
    # Start the timing
    startTime = time.time()

    # Get the command line arguments, if given
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option('--userName', action="store", type="string", dest='userName', default="",
                      help="The user name of the current user. If empty string (default), "
                      +"user name will be determined from the shell environment variable USER. "
                      +"Otherwise, the given one will be used.")

    parser.add_option('--destSE', action="store", type="string", dest='DestinationSE', default="IN2P3-CC_PHYS-HIGGS",
                      help='Set the destination storage element where the output dataset will be stored '
                      + '(some options are: IN2P3-CC_PHYS-HIGGS, AGLT2_PHYS-HIGGS, UNI-FREIBURG_PHYS-HIGGS, NIKHEF-ELPROD_PHYS-HIGGS, GOEGRID_PHYS-HIGGS,...)')

    parser.add_option('--inDSTextFile', action="store", type="string", dest='InDSTextFile', default="samplelist_HIGG3D1_mc15c__Common.txt",
                      help='The name of the input text file that lists all possible input datasets to run over')

    parser.add_option('--inDSIDs', action="store", type="string", dest='InDSIDs', default="",
                      help='The dataset ID numbers for the input datasets that we actually want to run over. '
                      +'This should be one string with comma-separated values; where ranges can be given with hypens. '
                      +'An example would be: --inDSIDs="110010,112233,201020-201040,303030". '
                      +'If this option is not provided (meaning the default empty string is used), all samples will be used.')

    parser.add_option('--excludedSite', action="store", type="string", dest='ExcludedSite', default="",
                      help='List the grid sites that you want to exclude (due to known site problems) '
                      +'from the submission. This should be a comma-separated list.')

    parser.add_option('--forceStaged', action="store_true", dest='ForceStaged', default=False,
                      help="If set to true (default=false), will force each site to stage the input data "
                      +"to the worker node and not process it from the storage element directly. "
                      +"It can happen that the brokerage will fail due to a too small scratch disk size. "
                      +"In that case, switch this flag to false.")

    parser.add_option('--nFilesPerJob', action="store", type="int", dest='NFilesPerJob', default=1,
                      help="The number of input files that should be used for one (sub) job.")

    parser.add_option('--nGBPerJob', action="store", type="string", dest='NGBPerJob', default="MAX",
                      help="Use the maximum allowed GBytes of input files to run over per sub-job."
                      +" This will only be used if the above nFilesPerJob is set to 0.")

    parser.add_option('--reuse', action="store_true", dest='Reuse', default=True,
                      help="If set to true, will reuse tar ball and job config from first job for subsequent jobs.")

    parser.add_option('--donotreuse', action="store_false", dest='Reuse',
                      help="If set to true, will not reuse tar ball and job config from first job for subsequent jobs.")

    parser.add_option('--useNewCode', action="store_true", dest='useNewCode', default=False,
                      help="If set to true, will upload new code version and force grid site to use it.")

    parser.add_option('-c', '--athenaOptions', action="store", type="string", dest='athenaOptions', default="",
                      help="Pass athena -c options here.")

    parser.add_option('--donotprocessReco', action="store_false", dest='processReco', default=True,
                      help="Turn OFF the running of the Reco sequence chain"
                      +" and thereby remove the corresponding content from the output.")

    parser.add_option('--processTruth', action="store_true", dest='processTruth', default=False,
                      help="Turn ON the running of the Truth sequence chain"
                      +" and thereby add the corresponding content to the output.")

    parser.add_option('-s', '--doSystematics', action="store_true", dest='doSystematics', default=False,
                      help="If set to true, will change the output dataset name from containing, e.g., 'VN' to 'sysVN'.")

    parser.add_option('--doEffiScaleFactors', action="store_true", dest='doEffiScaleFactors', default=True,
                      help="If false, will NOT run any efficiency or scale-factor calculation")

    parser.add_option('--doMediumOtherLeptons', action="store_true", dest='doMediumOtherLeptons', default=False,
                      help="If set to true, will use medium identification cuts for the pre-selected other leptons, i.e., before overlap-removal.")

    parser.add_option('--doVeryLooseLH', action="store_true", dest='doVeryLooseLH', default=False,
                      help="If set to true, will use VeryLooseLH identification cuts for the pre-selected other electrons, i.e., before overlap-removal.")

    parser.add_option('--doORNoMuNearJetRemoval', action="store_true", dest='doORNoMuNearJetRemoval', default=False,
                      help="Do additionally the overlap removal without removing muons near jets (default: False).")

    parser.add_option('--doORNoMuNearJetRemovalNoBJetPrecedence', action="store_true", dest='doORNoMuNearJetRemovalNoBJetPrecedence', default=False,
                      help="Do additionally the overlap removal without removing muons near jets as well as giving precedence to leptons over b-jets (default: False).")

    parser.add_option('--doPFlowJets', action="store_true", dest='doPFlowJets', default=False,
                      help="Use AntiKt4EMPFlowJets instead of AntiKt4EMTopoJets for the input jets collection")

    parser.add_option('--do2Lep', action="store_true", dest='do2Lep', default=False,
                      help="If set to true, will produce the di-lepton PAODs.")

    parser.add_option('--doVH', action="store_true", dest='doVH', default=False,
                      help="If set to true, will produce the WH and ZH PAODs.")

    parser.add_option('--doWH', action="store_true", dest='doWH', default=False,
                      help="If set to true, will produce the WH PAODs.")

    parser.add_option('--doZH', action="store_true", dest='doZH', default=False,
                      help="If set to true, will produce the ZH PAODs.")

    parser.add_option('--doFakeDiJet', action="store_true", dest='doFakeDiJet', default=False,
                      help="If set to true, will produce the di-jet based fake-lepton PAODs from HIGG3D3.")

    parser.add_option('--doFakeWJets', action="store_true", dest='doFakeWJets', default=False,
                      help="If set to true, will use looser lepton cuts to get the W+jets loose di-lepton sample.")

    parser.add_option('--doFakeZJets', action="store_true", dest='doFakeZJets', default=False,
                      help="If set to true, will use looser other lepton cuts to get the Z+jets loose di-lepton sample.")

    parser.add_option('--writePAOD_2L', action="store_true", dest='writePAOD_2L', default=False,
                      help="If set to true, will write the PAOD_2L output file.")

    parser.add_option('--writePAOD_2LDF', action="store_true", dest='writePAOD_2LDF', default=False,
                      help="If set to true, will write the PAOD_2LDF output file.")

    parser.add_option('--writePAOD_2LJJ', action="store_true", dest='writePAOD_2LJJ', default=False,
                      help="If set to true, will write the PAOD_2LJJ output file.")

    parser.add_option('--writePAOD_2LJJDF', action="store_true", dest='writePAOD_2LJJDF', default=False,
                      help="If set to true, will write the PAOD_2LJJDF output file.")

    parser.add_option('--writePAOD_2LFake', action="store_true", dest='writePAOD_2LFake', default=False,
                      help="If set to true, will write the PAOD_2LFake output file.")

    parser.add_option('--writePAOD_2LZFake', action="store_true", dest='writePAOD_2LZFake', default=False,
                      help="If set to true, will write the PAOD_2LZFake output file.")

    parser.add_option('--writePAOD_2LTopFake', action="store_true", dest='writePAOD_2LTopFake', default=False,
                      help="If set to true, will write the PAOD_2LTopFake output file.")

    parser.add_option('--writePAOD_WH', action="store_true", dest='writePAOD_WH', default=False,
                      help="If set to true, will write the PAOD_WH output file.")

    parser.add_option('--writePAOD_ZH', action="store_true", dest='writePAOD_ZH', default=False,
                      help="If set to true, will write the PAOD_ZH output file.")

    parser.add_option('--nProcs', action="store", type="int", dest='nProcs', default=0,
                      help="Use multiprocessing to submit jobs in parallel. Keep this number rather small,"
                      +"such that your machine isn't going to be blocked! Say < 20 or so?"
                      +" 0 means that no multiprocessing is attempted.")

    parser.add_option('-v', '--version', action="store", type="string", dest='version', default="V18",
                      help="Version number for your production")

    parser.add_option('--middleNameExtra', action="store", type="string", dest='middleNameExtra', default="",
                      help="An additional string to be added to the middle part of the output dataset")

    parser.add_option('--topOptionsPath', action="store", type="string", dest='topOptionsPath', default='PhysicsxAODConfig/HWWAnalysis_topOptions.py',
                      help="Path of your top options file")

    parser.add_option('--outDSType', action="store", type="string", dest='outDSType', default="PAOD",
                      help="String identifying the type of files being produced")

    parser.add_option('--merge', action="store_true", dest='Merge', default=False,
                      help="If set to true, will run the mergeScript at the end to merge the output files")

    parser.add_option('--mergeScript', action="store", type="string", dest='mergeScript', default='PAODGridMerge.py',
                      help="Path of the job options that constitute the merge script")

    parser.add_option('--oneOutDS', action="store_true", dest='oneOutDS', default=False,
                      help="If true, submit everything into one task with one output dataset")

    parser.add_option('--official', action="store_true", dest='official', default=False,
                      help="If true, use higgs group priviliges and store output on higgs group disk space")

    parser.add_option('-p', '--prod', action="store_true", dest='Prod', default=False,
                      help="If set to true, will run real production jobs. "
                      +"This includes using the final output dataset name "
                      +"and storing the output datasets on the specified destination storage element. "
                      +"Otherwise only submit jobs with a 'test' name for the output dataset "
                      +"and NOT asking for a specific detination storage element.")

    parser.add_option('-r', '--run', action="store_true", dest='Run', default=False,
                      help="If set to true, will actually run production jobs. "
                      +"Otherwise only print which job submission commands have been assambled")
    (options, args) = parser.parse_args()

    # Set the right user name
    assert isinstance( options.userName, str )
    if options.userName == "": options.userName = os.getenv("USER")
    print "Using: --userName=%s" % options.userName

    # Check that we got valid options
    assert isinstance( options.DestinationSE, str )
    print "Using: --destSE=%s" % options.DestinationSE

    assert isinstance( options.InDSTextFile, str )
    print "Using: --inDSTextFile=%s" % options.InDSTextFile

    assert isinstance( options.InDSIDs, str )
    print "Using: --inDSIDs=%s" % options.InDSIDs

    assert isinstance( options.ExcludedSite, str )
    print "Using: --excludedSite=%s" % options.ExcludedSite

    assert isinstance( options.ForceStaged, bool )
    print "Using: --forceStaged=%s" % options.ForceStaged

    assert isinstance( options.NFilesPerJob, int )
    print "Using: --nFilesPerJob=%s" % options.NFilesPerJob

    assert isinstance( options.NGBPerJob, str )
    print "Using: --nGBPerJob=%s" % options.NGBPerJob

    assert isinstance( options.Reuse, bool )
    print "Using: --reuse=%s" % options.Reuse

    assert isinstance( options.useNewCode, bool )
    print "Using: --useNewCode=%s" % options.useNewCode

    assert isinstance( options.processReco, bool )
    print "Using: --processReco=%s" % options.processReco

    assert isinstance( options.processTruth, bool )
    print "Using: --processTruth=%s" % options.processTruth

    assert isinstance( options.doSystematics, bool )
    print "Using: --doSystematics=%s" % options.doSystematics

    assert isinstance( options.doEffiScaleFactors, bool )
    print "Using: --doEffiScaleFactors=%s" % options.doEffiScaleFactors

    assert isinstance( options.do2Lep, bool )
    print "Using: --do2Lep=%s" % options.do2Lep

    assert isinstance( options.doVH, bool )
    print "Using: --doVH=%s" % options.doVH

    assert isinstance( options.doWH, bool )
    print "Using: --doWH=%s" % options.doWH

    assert isinstance( options.doZH, bool )
    print "Using: --doZH=%s" % options.doZH

    assert isinstance( options.doFakeDiJet, bool )
    print "Using: --doFakeDiJet=%s" % options.doFakeDiJet

    assert isinstance( options.doFakeWJets, bool )
    print "Using: --doFakeWJets=%s" % options.doFakeWJets

    assert isinstance( options.doFakeZJets, bool )
    print "Using: --doFakeZJets=%s" % options.doFakeZJets

    assert isinstance( options.writePAOD_2L, bool )
    print "Using: --writePAOD_2L=%s" % options.writePAOD_2L

    assert isinstance( options.writePAOD_2LDF, bool )
    print "Using: --writePAOD_2LDF=%s" % options.writePAOD_2LDF

    assert isinstance( options.writePAOD_2LJJ, bool )
    print "Using: --writePAOD_2LJJ=%s" % options.writePAOD_2LJJ

    assert isinstance( options.writePAOD_2LJJDF, bool )
    print "Using: --writePAOD_2LJJDF=%s" % options.writePAOD_2LJJDF

    assert isinstance( options.writePAOD_2LFake, bool )
    print "Using: --writePAOD_2LFake=%s" % options.writePAOD_2LFake

    assert isinstance( options.writePAOD_2LZFake, bool )
    print "Using: --writePAOD_2LZFake=%s" % options.writePAOD_2LZFake

    assert isinstance( options.writePAOD_2LTopFake, bool )
    print "Using: --writePAOD_2LTopFake=%s" % options.writePAOD_2LTopFake

    assert isinstance( options.writePAOD_WH, bool )
    print "Using: --writePAOD_WH=%s" % options.writePAOD_WH

    assert isinstance( options.writePAOD_ZH, bool )
    print "Using: --writePAOD_ZH=%s" % options.writePAOD_ZH

    assert isinstance( options.doMediumOtherLeptons, bool )
    print "Using: --doMediumOtherLeptons=%s" % options.doMediumOtherLeptons

    assert isinstance( options.doVeryLooseLH, bool )
    print "Using: --doVeryLooseLH=%s" % options.doVeryLooseLH

    assert isinstance( options.doORNoMuNearJetRemoval, bool )
    print "Using: --doORNoMuNearJetRemoval=%s" % options.doORNoMuNearJetRemoval

    assert isinstance( options.doORNoMuNearJetRemovalNoBJetPrecedence, bool )
    print "Using: --doORNoMuNearJetRemovalNoBJetPrecedence=%s" % options.doORNoMuNearJetRemovalNoBJetPrecedence

    assert isinstance( options.doPFlowJets, bool )
    print "Using: --doPFlowJets=%s" % options.doPFlowJets

    assert isinstance( options.athenaOptions, str )
    if not options.processReco:                        options.athenaOptions += "processReco=False;"
    if options.processTruth:                           options.athenaOptions += "processTruth=True;"
    if not options.doEffiScaleFactors:                 options.athenaOptions += "doEffiScaleFactors=False;"
    if not options.doSystematics:                      options.athenaOptions += "doEffiSystematics=False;doP4Systematics=False;"
    if options.doFakeDiJet:                            options.athenaOptions += "doFakeDiJet=True;"
    elif options.doFakeWJets:                          options.athenaOptions += "doFakeWJets=True;"
    elif options.doFakeZJets:                          options.athenaOptions += "doFakeZJets=True;"
    if options.do2Lep:                                 options.athenaOptions += "do2Lep=True;"
    if options.doVH:                                   options.athenaOptions += "do3Lep=True;do4Lep=True;"
    if options.doWH:                                   options.athenaOptions += "do3Lep=True;"
    if options.doZH:                                   options.athenaOptions += "do4Lep=True;"
    if options.doMediumOtherLeptons:                   options.athenaOptions += "doMediumOtherLeptons=True;"
    elif options.doVeryLooseLH:                        options.athenaOptions += "doVeryLooseLH=True;"
    if options.doORNoMuNearJetRemoval:                 options.athenaOptions += "doORNoMuNearJetRemoval=True;"
    if options.doORNoMuNearJetRemovalNoBJetPrecedence: options.athenaOptions += "doORNoMuNearJetRemovalNoBJetPrecedence=True;"
    if options.doPFlowJets:                            options.athenaOptions += "doPFlowJets=True;"
    if options.writePAOD_2L:                           options.athenaOptions += "writePAOD_2L=True;"
    if options.writePAOD_2LDF:                         options.athenaOptions += "writePAOD_2LDF=True;"
    if options.writePAOD_2LJJ:                         options.athenaOptions += "writePAOD_2LJJ=True;"
    if options.writePAOD_2LJJDF:                       options.athenaOptions += "writePAOD_2LJJDF=True;"
    if options.writePAOD_2LFake:                       options.athenaOptions += "writePAOD_2LFake=True;"
    if options.writePAOD_2LZFake:                      options.athenaOptions += "writePAOD_2LZFake=True;"
    if options.writePAOD_2LTopFake:                    options.athenaOptions += "writePAOD_2LTopFake=True;"
    if options.writePAOD_WH:                           options.athenaOptions += "writePAOD_WH=True;"
    if options.writePAOD_ZH:                           options.athenaOptions += "writePAOD_ZH=True;"
    print "Using: --athenaOptions=%s" % options.athenaOptions

    assert isinstance( options.nProcs, int )
    print "Using: --nProcs=%s" % options.nProcs

    assert isinstance( options.outDSType, str )
    if options.processTruth and not options.processReco: options.outDSType = "Truth" + options.outDSType
    if options.processTruth and options.processReco: options.outDSType = "TruthReco" + options.outDSType
    if not options.processTruth and not options.processReco:
        print "Oops, scheduled to process neither Reco or Truth - you should at least process something!"
        exit(0)
    if options.do2Lep and not options.doVH: options.outDSType += "_2L"
    elif options.doVH and not options.do2Lep: options.outDSType += "_VH"
    elif options.doWH: options.outDSType += "_WH"
    elif options.doZH: options.outDSType += "_ZH"
    print "Using: --outDSType=%s" % options.outDSType

    assert isinstance( options.version, str )
    print "Using: --version=%s" % options.version

    assert isinstance( options.middleNameExtra, str )
    print "Using: --middleNameExtra=%s" % options.middleNameExtra

    assert isinstance( options.topOptionsPath, str )
    print "Using: --topOptionsPath=%s" % options.topOptionsPath

    assert isinstance( options.Merge, bool )
    print "Using: --merge=%s" % options.Merge

    assert isinstance( options.mergeScript, str )
    print "Using: --mergeScript=%s" % options.mergeScript

    assert isinstance( options.oneOutDS, bool )
    print "Using: --oneOutDS=%s" % options.oneOutDS

    assert isinstance( options.official, bool )
    print "Using: --official=%s" % options.official

    assert isinstance( options.Prod, bool )
    print "Using: --prod=%s" % options.Prod

    assert isinstance( options.Run, bool )
    print "Using: --run=%s" % options.Run

    # Now, actually run the submit job function
    nJobsSubmitted = SubmitJobs(options,startTime)

    # End the timing and print out the resulting total time
    endTime = time.time()
    print "\n\nsubmitGridJobs.py: Total time spend for submitting all %i jobs: %12.6f s\n" % ( nJobsSubmitted, (endTime - startTime)*1.0 )

    pass
