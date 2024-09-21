#!/usr/bin/env python

# ==============================================================================
# File: submitBatchJobs.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: Script to submit athena batch jobs. You need to check all log files with:
# grep 'leaving with code' group.phys-higgs.* | grep -v '"successful run"'
# to see if there were failures.
# ==============================================================================


import user  # look for .pythonrc.py for user init
import os,sys
import time
from glob import glob
import subprocess
from optparse import OptionParser
import shutil
import subprocess




#===================================
# The main function... everything starts here
#===================================
def submitBatchJobs(options,startTime):
    """
    Here, we will actually go over all input files that we find in options.inDir
    and submit one batch job for each.
    """
    nJobsSubmitted = 0
    # Get the list of input files
    myFileList = glob( options.inDir+"*pool.root.txt")
    nTotal = len(myFileList)
    print "Found %i potential jobs to submit (modulo the given restrict list)..." % nTotal
    for inTextFile in myFileList:
        # Restrict the submission to only a subset, if requested
        #print "Now on: %s" % inTextFile
        if options.restrictList:
            # Test if the current inTextFile contains a sub-string in the restrictList
            if not any(testStr in inTextFile for testStr in options.restrictList): continue
            pass
        options.inTextFile  = inTextFile
        # options.jobName     = "j"+((inTextFile.rstrip(".pool.root.txt").split("/")[-1]).split('.', 2)[-1])
        options.jobName     = buildJobName(inTextFile)
        options.outFileName = buildOutFileName(inTextFile)

        # Actually create the run script and submit the job to the batch system
        runScript(options, nJobsSubmitted, nTotal)
        nJobsSubmitted += 1
        pass

    return nJobsSubmitted



def buildJobName(inTextFile):
    """ Build the name of the batch job."""
    return "j"+((inTextFile.rstrip(".pool.root.txt").split("/")[-1]).split('.', 2)[-1])



def buildOutFileName(inTextFile):
    """ Build the name of the output root file from the input text file."""
    return ((inTextFile.split("/")[-1]).replace(".merge.", ".superMerge.")).split(".txt")[0]



def runCmd(exe):
    """Running a shell command and returning the output"""
    p = subprocess.Popen(exe, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return p.communicate()[0]


def checkOutput(options):
    """
    Try to check the output log files and the presence of the output root file
    """
    # Get the list of input text files that were used to list the input files to run over
    myFileList = glob( options.inDir+"*pool.root.txt")
    nJobsToCheck = len(myFileList)
    print "Found %i input text files to check..." % nJobsToCheck

    # Create the folder where the root and log files of the broken jobs will be moved to
    if not os.path.exists(options.brokenDir): os.makedirs(options.brokenDir)

    completedJobs     = []
    runningJobs       = []
    missingOutputJobs = [] # If no log file or ROOT file exists, assume the job is still running
    brokenJobs        = []
    undetectedJobs    = []

    # Get the list of running/queing/pending jobs from the batch system
    batchJobCmd = ""
    if options.site == "NAF":
        #batchJobCmd = "qstat -xml | tr '\n' ' ' | sed 's#<job_list[^>]*>#\n#g' | sed 's#<[^>]*>##g' | grep ' ' | column -t"
        batchJobCmd = "qstat -xml"
        pass
    batchJobs = ""
    if not batchJobCmd == "":
        batchJobs = runCmd(batchJobCmd)
        #print "Jobs in batch system:\n%s" % batchJobs
        pass

    for inTextFile in myFileList:
        outFileName  = buildOutFileName(inTextFile)
        batchJobName = buildJobName(inTextFile)


        # Check the log file
        logFileReturnCode = passLogFileCheck(outFileName)
        # Check the ROOT file
        rootFileReturnCode = passRootFileCheck(outFileName)

        # Make a decision
        if batchJobs.__contains__(batchJobName):
            # The job is still running
            #print "Found running job with name %s" % batchJobName
            runningJobs.append(inTextFile)
            pass
        elif logFileReturnCode == 0 and rootFileReturnCode == 0:
            # All is ok and job is done
            completedJobs.append(inTextFile)
            pass
        elif logFileReturnCode == 1 and rootFileReturnCode == 1:
            # Neither the log file nor the root file exist
            missingOutputJobs.append(inTextFile)
            pass
        elif logFileReturnCode == 2:
            # Athena didn't complete successfully
            brokenJobs.append(inTextFile)
            # Move the log files and root file to the broken directory
            if logFileReturnCode != 1:
                stdOutFileName = outFileName.replace(".pool.root",".stdout.log")
                if options.moveFiles: shutil.move(options.outDirLogs + stdOutFileName, options.brokenDir + stdOutFileName)
                pass
            stdErrFileName = outFileName.replace(".pool.root",".stderr.log")
            if os.path.exists(options.outDirLogs+stdErrFileName):
                if options.moveFiles: shutil.move(options.outDirLogs + stdErrFileName, options.brokenDir + stdErrFileName)
                pass
            if rootFileReturnCode != 1:
                if options.moveFiles: shutil.move(options.outDir + outFileName, options.brokenDir + outFileName)
                pass
            pass
        else:
            # Something strange happend
            undetectedJobs.append(inTextFile)
            # Move also the ROOT files and log files to the broken folder, if requested
            if options.moveUnknownFiles:
                stdOutFileName = outFileName.replace(".pool.root",".stdout.log")
                if os.path.exists(options.outDirLogs+stdOutFileName):
                    shutil.move(options.outDirLogs + stdOutFileName, options.brokenDir + stdOutFileName)
                    pass
                stdErrFileName = outFileName.replace(".pool.root",".stderr.log")
                if os.path.exists(options.outDirLogs+stdErrFileName):
                    shutil.move(options.outDirLogs + stdErrFileName, options.brokenDir + stdErrFileName)
                    pass
                if os.path.exists(options.outDir + outFileName):
                    shutil.move(options.outDir + outFileName, options.brokenDir + outFileName)
                    pass
                pass
            pass
        pass
    # Build the main part of the resubmit command
    resubmitCommandBase = "submitBatchJobs.py --userName %s --site %s --testArea %s " \
                      % (options.userName, options.site, options.testArea)
    if options.jobOptions: resubmitCommandBase += " --jobOptions %s " % options.jobOptions
    if options.jobName:    resubmitCommandBase += " --jobName %s " % options.jobName
    if options.inTextFile: resubmitCommandBase += " --inTextFile %s " % options.inTextFile
    resubmitCommandBase += " --inDir %s --outDir %s --outDirLogs %s " \
                      % (options.inDir, options.outDir, options.outDirLogs)
    resubmitCommandBase += " --restrict "

    # Now, print the summary
    print "Completed %i of %i jobs." % (len(completedJobs),nJobsToCheck)
    print "%i of %i jobs are still in the batch system." % (len(runningJobs),nJobsToCheck)
    if len(missingOutputJobs):
        print "The following %i jobs have no output file or log file. They might not yet be completed:" % len(missingOutputJobs)
        resubmitNoOutputCommand = ""
        missingOutputJobs.sort()
        for jobName in missingOutputJobs:
            print "    %s" % printName(jobName)
            resubmitNoOutputCommand += ((jobName.split("/"))[-1])+","
            pass
        resubmitNoOutputFullCommand = resubmitCommandBase + resubmitNoOutputCommand.rstrip(",")
        print "You can resubmit the jobs with no existing output with this command:\n%s\n" % resubmitNoOutputFullCommand
        pass

    print "The following %i jobs are of unknown state:" % len(undetectedJobs)
    resubmitUnknownCommand = ""
    undetectedJobs.sort()
    for jobName in undetectedJobs:
        print "    %s" % printName(jobName)
        resubmitUnknownCommand += ((jobName.split("/"))[-1])+","
        pass
    resubmitUnknownFullCommand = resubmitCommandBase + resubmitUnknownCommand.rstrip(",")
    if len(undetectedJobs): print "You can resubmit the jobs of unknown state with this command:\n%s\n" % resubmitUnknownFullCommand

    print "The following %i jobs seem to be broken and need to be resubmitted:" % len(brokenJobs)
    resubmitBrokenCommand = ""
    brokenJobs.sort()
    for jobName in brokenJobs:
        print "    %s" % printName(jobName)
        resubmitBrokenCommand += ((jobName.split("/"))[-1])+","
        pass
    resubmitBrokenFullCommand = resubmitCommandBase + resubmitBrokenCommand.rstrip(",")
    if len(brokenJobs): print "You can resubmit the broken jobs with this command:\n%s\n" % resubmitBrokenFullCommand

    return nJobsToCheck



def printName(jobName):
    dirName = (jobName.split("/"))[-2]
    dirName += "/"
    dirName += (jobName.split("/"))[-1]
    return dirName


def passLogFileCheck(outFileName):
    """
    Check the log file if athena finished sucessfully.
    Return codes: 0=OK, 1= log file doesn't exist, 2= athena didn't run sucessfully.
    """
    stdoutFileName = outFileName.replace(".pool.root",".stdout.log")
    if not os.path.exists(options.outDirLogs+stdoutFileName): return 1
    statinfo = os.stat(options.outDirLogs+stdoutFileName)
    if statinfo.st_size == 0:
        #print "Got empty log file with name %s" % (options.outDirLogs+stdoutFileName)
        return 2
    with open(options.outDirLogs+stdoutFileName,'r') as fileObject:
        last_line = fileObject.readlines()[-1]
        if not last_line.__contains__('INFO leaving with code 0: "successful run"'): return 2
        pass
    return 0



def passRootFileCheck(outFileName):
    """
    Check the output ROOT file.
    Return codes: 0=OK, 1= ROOT file doesn't exist.
    """
    if not os.path.exists(options.outDir+outFileName): return 1
    return 0



def runScript(options, nJobsSubmitted, nTotal):
    """
    Here, we build the script that will run on the batch worker node
    """
    # Open a new file that will be executed on the workernode
    fileName = None
    if options.mode == 'merge':    fileName = options.inTextFile.replace(".pool.root.txt",".merge.sh")
    elif options.mode == 'reduce': fileName = options.inTextFile.replace(".pool.root.txt",".reduce.sh")
    with open(fileName,'w') as fileObject:
        # fileObject.write("#!/usr/bin/env zsh\n")
        # fileObject.write("#!/bin/bash\n")
        fileObject.write("#!/usr/bin/env bash\n")
        if options.site == "SMU":
            fileObject.write("source /grid/software/ATLASLocalRootBase/setup.sh\n")
            pass
        else:
            fileObject.write("export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase\n")
            fileObject.write("source /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/user/atlasLocalSetup.sh\n")
            pass
        fileObject.write("cd %s\n" % options.testArea)
        fileObject.write("asetup\n")
        fileObject.write("mkdir -p %s\n" % options.outDir)
        fileObject.write("cd $TMPDIR\n")
        runCommand = "time athena.py -c \"INTEXTFILE='"+options.inTextFile+"';OUTFILE='"+options.outFileName+"';\" "+options.jobOptions + " 2>&1"
        fileObject.write("%s\n" % runCommand)
        fileObject.write("mv %s %s\n" % (options.outFileName, options.outDir+options.outFileName) )
        pass
    submitCmd = submitCommand(options,fileName)
    # Now, submit the job
    #print "Submitting: %s" % submitCmd
    exitCode = os.system( submitCmd )
    print "Exit code from batch submission of job number %i out of %i total possible ones: %i" % (1+nJobsSubmitted, nTotal, exitCode)
    return




def submitCommand(options,fileName):
    """
    Here, we actually submit one batch job
    """
    if options.site == "NAF":
        return "/usr/sge/bin/lx-amd64/qsub -q long.q -l h_vmem=8G -l h_fsize=24G -l os=sld6 -N " + options.jobName \
                + " -o " + options.outDirLogs + options.outFileName.replace(".pool.root",".stdout.log") \
                + " -e " + options.outDirLogs + options.outFileName.replace(".pool.root",".stderr.log") \
                + " -cwd " + fileName
    elif options.site == "SMU":
        f = open('failedlist.txt')
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(options.outFileName) != -1:
            print('This Job had failed')
            return "sbatch -p serial " \
                + " -o " + options.outDirLogs + options.outFileName.replace(".pool.root",".stdout.log") \
                + " -e " + options.outDirLogs + options.outFileName.replace(".pool.root",".stderr.log") \
                + " " + fileName
        else :
            return "echo 'This Job was already successful'"
        pass
    return "echo 'Could not recognize the site and thus the batch submission command to use...'"




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

    parser.add_option('--site', action="store", type="string", dest='site',
                      default="NAF", help="The name of the site. Based on this, we will choose the batch submission command.")

    parser.add_option('--mode', action="store", type="string", dest='mode', default="merge",
                      help="The running mode. If it is 'merge', the PAODMerge script will be used. If it is 'reduce', the PAODReduce script will be used. Also, the outDir gets the appropriate suffix")

    parser.add_option('--inDir', action="store", type="string", dest='inDir',
                      default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/fileListsToProcess/group.phys-higgs.data15_13TeV.HWW_VeryLooseLH.merge.PAOD_2L.V17b_FakeZJets_PAOD_2LFake/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/fileListsToProcess/group.phys-higgs.data16_13TeV.HWW_VeryLooseLH.merge.PAOD_2L.V17b_FakeZJets_PAOD_2LFake/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/fileListsToProcess/group.phys-higgs.mc15_13TeV.HWW_VeryLooseLH_AlpgenDYBkg.merge.PAOD_2L.V17b_FakeZJets_PAOD_2LFake/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/fileListsToProcess/group.phys-higgs.mc15_13TeV.HWW_VeryLooseLH_CommonOtherBkg.merge.PAOD_2L.V17b_FakeZJets_PAOD_2LFake/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/fileListsToProcess/group.phys-higgs.mc15_13TeV.HWW_VeryLooseLH_HWWSignal.merge.PAOD_2L.V17b_FakeZJets_PAOD_2LFake/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/fileListsToProcess/group.phys-higgs.mc15_13TeV.HWW_VeryLooseLH_MadGraphDYBkg.merge.PAOD_2L.V17b_FakeZJets_PAOD_2LFake/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/fileListsToProcess/group.phys-higgs.mc15_13TeV.HWW_VeryLooseLH_PowhegDYBkg.merge.PAOD_2L.V17b_FakeZJets_PAOD_2LFake/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/fileListsToProcess/group.phys-higgs.mc15_13TeV.HWW_VeryLooseLH_SherpaDYBkg.merge.PAOD_2L.V17b_FakeZJets_PAOD_2LFake/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/fileListsToProcess/group.phys-higgs.mc15_13TeV.HWW_VeryLooseLH_TopBkg.merge.PAOD_2L.V17b_FakeZJets_PAOD_2LFake/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V16/fileListsToProcess/group.phys-higgs.mc15_13TeV.HWW.merge.PAOD.V16_FakeDiJets_PAOD_FakeL/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V16/fileListsToProcess/group.phys-higgs.data16_13TeV.HWW.merge.PAOD.V16_FakeDiJets_PAOD_FakeL/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V16/fileListsToProcess/group.phys-higgs.mc15_13TeV.HWW.merge.PAOD.V16_FakeDiJets_PAOD_FakeL/",
                      help="Define the input directory where the text files are that contain the paths and names of the PADOs to run over")

    parser.add_option('--restrict', action="store", type="string", dest='restrict',
                      default="", help="A comma-separated string of names that should match the jobs, using contains, to only submit")

    parser.add_option('--inTextFile', action="store", type="string", dest='inTextFile',
                      default="", help="The current text file that contains the paths and names of the PADOs to run over")

    parser.add_option('--outDir', action="store", type="string", dest='outDir',
                      default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/merged/",
                      #default="/nfs/dust/atlas/user/kkoeneke/DataMC/PxAOD/V17b/merged/",
                      help="Define the output directory")

    parser.add_option('--outDirLogs', action="store", type="string", dest='outDirLogs',
                      default="", help="Define the directory where the log files will be copied to")

    parser.add_option('--testArea', action="store", type="string", dest='testArea',
                      default = os.getenv("TestArea"),
                      help="The athena TestArea where asetup was run")

    parser.add_option('--jobOptions', action="store", type="string", dest='jobOptions',
                      #default='PhysicsxAODConfig/PAODMerge.py',
                      #default='PhysicsxAODConfig/PAODMerge.py',
                      help="The actual job options to use")

    parser.add_option('--jobName', action="store", type="string", dest='jobName',
                      default='', help="The name of each job that will  be submitted")

    parser.add_option('--checkOutput', action="store_true", dest='checkOutput', default=False,
                      help="Check the output files that are present and check the corresponding log files.")

    parser.add_option('--moveFiles', action="store_true", dest='moveFiles', default=False,
                      help="Move the ROOT and log files of broken jobs to the brokenDir (default=False).")

    parser.add_option('--moveUnknownFiles', action="store_true", dest='moveUnknownFiles', default=False,
                      help="Move the ROOT and log files of jobs with some unknown problem to the brokenDir (default=False).")

    parser.add_option('--brokenDir', action="store", type="string", dest='brokenDir',
                      default='', help="The name of a directory where the root files and logs of broken jobs get moved to")


    # Actually parse all options
    (options, args) = parser.parse_args()

    # Check that we got valid options

    # Set the right user name
    assert isinstance( options.userName, str )
    if options.userName == "": options.userName = os.getenv("USER")
    print "Using: --userName=%s" % options.userName

    assert isinstance( options.site, str )
    print "Using: --site=%s" % options.site

    assert isinstance( options.mode, str )
    print "Using: --mode=%s" % options.mode

    assert isinstance( options.inDir, str )
    if len(options.inDir) and not options.inDir.endswith("/"): options.inDir += "/"
    print "Using: --inDir=%s" % options.inDir

    assert isinstance( options.restrict, str )
    print "Using: --restrict=%s" % options.restrict
    options.restrictList = []
    if options.restrict: options.restrictList = options.restrict.split(",")
    print "Using: --restrictList=%s" % options.restrictList

    assert isinstance( options.inTextFile, str )
    # print "Using: --inTextFile=%s" % options.inTextFile

    assert isinstance( options.outDir, str )
    if len(options.outDir) and not options.outDir.endswith("/"): options.outDir += "/"
    inDirLast = options.inDir.split("/")[-2]
    inDirLastSuperMerge = inDirLast.replace(".merge.", ".superMerge.")
    inDirLastReduce     = inDirLast.replace(".merge.", ".reduce.")
    if not ( options.outDir.__contains__(inDirLast) or options.outDir.__contains__(inDirLastSuperMerge) or options.outDir.__contains__(inDirLastReduce) ):
        if options.mode == 'merge':    options.outDir += "merged/"
        elif options.mode == 'reduce': options.outDir += "reduced/"
        options.outDir += inDirLast + "/"
        pass
    if options.mode == 'merge':    options.outDir = options.outDir.replace(".merge.", ".superMerge.")
    elif options.mode == 'reduce': options.outDir = options.outDir.replace(".merge.", ".reduce.")
    if not os.path.exists(options.outDir): os.makedirs(options.outDir)
    print "Using: --outDir=%s" % options.outDir

    assert isinstance( options.outDirLogs, str )
    if options.outDirLogs == "": options.outDirLogs = options.outDir.rstrip("/") + "_logs/"
    if not os.path.exists(options.outDirLogs): os.makedirs(options.outDirLogs)
    print "Using: --outDirLogs=%s" % options.outDirLogs

    assert isinstance( options.brokenDir, str )
    if options.brokenDir == "": options.brokenDir = options.outDir+"../broken/"
    print "Using: --brokenDir=%s" % options.brokenDir

    assert isinstance( options.testArea, str )
    print "Using: --testArea=%s" % options.testArea

    if options.mode == "merge" and not options.jobOptions :
        options.jobOptions = "PhysicsxAODConfig/PAODMerge.py"
        pass
    elif options.mode == "reduce" and not options.jobOptions :
        options.jobOptions = "PhysicsxAODConfig/PAODReduce.py"
        pass
    print "Using: --jobOptions=%s" % options.jobOptions
    assert isinstance( options.jobOptions, str )

    assert isinstance( options.checkOutput, bool )
    print "Using: --checkOutput=%s" % options.checkOutput

    assert isinstance( options.moveFiles, bool )
    print "Using: --moveFiles=%s" % options.moveFiles

    assert isinstance( options.moveUnknownFiles, bool )
    print "Using: --moveUnknownFiles=%s" % options.moveUnknownFiles

    nJobsSubmitted = 0
    nameOfJob = "submitting"
    # Decide what to run
    if options.checkOutput:
        nameOfJob = "checking"
        nJobsSubmitted = checkOutput(options)
        pass
    else:
        # Now, actually run the submit job function
        nJobsSubmitted = submitBatchJobs(options,startTime)
        pass

    # End the timing and print out the resulting total time
    endTime = time.time()
    print "\n\nsubmitBatchJobs.py: Total time spend for %s all %i jobs: %12.6f s\n" % (nameOfJob, nJobsSubmitted, (endTime - startTime)*1.0 )

    pass
