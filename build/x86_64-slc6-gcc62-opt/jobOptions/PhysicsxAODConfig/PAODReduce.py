# =============================================================================
#  Name:        PAODReduce.py
#
#  Author:      Karsten Koeneke
#  Created:     September 2015
#
#  Usage: This script is meant to reduce (and merge) PAODs into one smaller PAOD.
#         It should also correctly merge all available meta data.
#         To run, type:
#              athena PhysicsxAODConfig/PAODReduce.py 2>&1 | tee log.txt
# =============================================================================

# Import the error handling
#svcMgr.CoreDumpSvc.FatalHandler = 438
#import traceback

# To change the print format, leave 40 characters before "INFO",...
MessageSvc.Format = "% F%60W%S%7W%R%T %0W%M"

# for messaging
from AthenaCommon.Logging import logging
paodMsg = logging.getLogger('PAODReduce')
logLevel = vars().get('PAODLogLevel', INFO) # 3=INFO, 2=DEBUG
paodMsg.setLevel(logLevel)


# ==============================================================================
# Load your input file that you want to process.
# Note that the last method gets the highest priority.
# ==============================================================================
from glob import glob
myFileList = ["/afs/cern.ch/user/k/kkoeneke/afsWork/public/DataMC/mc/PAOD_2L/v6/341079/group.phys-higgs.6465928.PAOD_2L._000002.pool.root"]
# envVar = "DataMC"
envVar = "SharedDataMC"
if os.getenv(envVar) and os.path.exists(os.getenv(envVar)) :
    # basePath = os.getenv(envVar)+"/mc/PAOD_2L/v6/341079/"
    basePath = os.getenv(envVar)+"/CERNBoxDang/PAOD_2L/v6/data/"
    if os.path.exists(basePath): myFileList = glob( basePath+"*.root*")
    pass
# For local running
if vars().has_key('INDIR'):
    inDir = vars().get('INDIR')
    if os.path.exists(inDir): myFileList = glob(inDir+"/*.root*")
    else: paodMsg.warning("Provided directory '%s' does not exist. Using input files: %s" % (inDir, myFileList))
    pass
if vars().has_key('INFILELIST'):
    inFileStringList = vars().get('INFILELIST')
    inFileList = inFileStringList.split(',')
    tmpFileList = []
    for inFile in inFileList: tmpFileList.append(inFile)
    # if os.path.exists(inFile): tmpFileList.append(inFile)
    # else: paodMsg.warning("Provided input file '%s' does not exist.... skipping it!" % inFile)
    # pass
    myFileList = tmpFileList
    pass
if vars().has_key('INTEXTFILE'):
    fileName = vars().get('INTEXTFILE')
    tmpFileList = []
    # Test if the file exists
    if not os.path.isfile(fileName): paodMsg.warning("Provided input text file '%s' does not exist...." % fileName)
    # Otherwise, the file exists and we can quickly open it in read-only mode
    else:
        with open(fileName,'r') as fileObject:
            for line in fileObject: tmpFileList.append(line.rstrip('\n'))
            pass
        pass
    myFileList = tmpFileList
    pass
if vars().has_key('INFILE'):
    inFile = vars().get('INFILE')
    if os.path.exists(inFile): myFileList = [inFile]
    else: paodMsg.warning("Provided input file '%s' does not exist. Using input files: %s" % (inFile, myFileList))
    pass


# ==============================================================================
#           ---- NO NEED TO CHANGE ANYTHING BELOW THIS LINE !!! ----
# ==============================================================================

# Set up the Athena file reading and tell it to load the files that you specified above
from AthenaCommon.AthenaCommonFlags import jobproperties as jp
import AthenaPoolCnvSvc.ReadAthenaPool
paodMsg.info("Using %i input files: %s" % (len(myFileList), myFileList))
jp.AthenaCommonFlags.FilesInput = myFileList


# ==============================================================================
# Fetch the AthAlgSeq, i.e., one of the existing master sequences where one should attach all algorithms
# ==============================================================================
topSequence = CfgMgr.AthSequencer("AthAlgSeq", OutputLevel = WARNING)


# ==============================================================================
# Perform some commonly needed tasks
# ==============================================================================
svcMgr.EventSelector.InputCollections = jp.AthenaCommonFlags.FilesInput()
svcMgr.StatusCodeSvc.AbortOnError=True

# Import the reading of in-file metadata
from PyUtils import AthFile
af = AthFile.fopen( svcMgr.EventSelector.InputCollections[0] )
eventDataItems = []
for evtItem in af.fileinfos["eventdata_items"]:
    evtItem0 = evtItem[0]
    if evtItem[0] == None :
        paodMsg.info("Got an unknown type from the input file for the item with name: %s" % evtItem[1])
        evtItem0 = "None"
    eventDataItems.append( evtItem0 + "#" + evtItem[1] )
    pass
# Get also the input stream name
from EventBookkeeperTools.CutFlowHelpers import GetInputStreamNameFromMetaDataItemList
inputStreamName = GetInputStreamNameFromMetaDataItemList( af.fileinfos["metadata_items"] )


# ==============================================================================
# Create the new output stream and copy over all items fron the input file to
# the output file, both event data and meta data
# ==============================================================================

# Build our own list of items that we want to store in the output file
outItemList = []
differentFlavorEventObjectNames = []
for item in eventDataItems:
    #if item.__contains__("___"): continue
    #if item.__contains__("EventIso"): continue
    outItemList.append(item)
    # Find all different flavor event objects
    if ( item.__contains__("EventEM") or item.__contains__("EventME") ) \
       and not item.__contains__("Aux") :
        differentFlavorEventObjectNames.append( item.split("#")[1] )
        pass
    pass

from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
outStreamName = inputStreamName # Use the same name also for the output as we are merging
outFileName   = outStreamName+".reduce.pool.root"
if vars().has_key('OUTFILE'):
    outFileName = vars().get('OUTFILE')
    pass
paodMsg.info("Using output file name: %s" % outFileName)
outStream = MSMgr.NewPoolRootStream( outStreamName, outFileName )
#outStream.GetEventStream().TakeItemsFromInput = True
#outStream.GetMetaDataStream().TakeItemsFromInput = True
outStream.AddItem( outItemList )

# ==============================================================================
# Add an event selection
# ==============================================================================
# topSequence += CfgMgr.CutAlg("HWWReduceEventSelectionAlg",
#                              Cut = "count(EventEM.pt > -100.0*GeV) >= 1 || count(EventME.pt > -100.0*GeV) >= 1" )

from PhysicsxAODConfig.SelectDFEventsAlg import SelectDFEventsAlg
#topSequence += SelectDFEventsAlg("HWWReduceEventSelectionAlg", InputNames = differentFlavorEventObjectNames )
#topSequence += SelectDFEventsAlg("HWWReduceEventSelectionAlg", InputNames = ["EventFakeM"], HasIdentifiedFakeMuon = True )
topSequence += CfgMgr.HWW__EventSelectionAlg("HWWReduceEventSelectionAlg",
                                             InputContainerList     = ["EventMM", "EventEE"],
                                             HasIdentifiedOtherMuon = True )
outStream.AcceptAlgs( ["HWWReduceEventSelectionAlg"] )



# Schedule the meta-data tools/services to correctly propagate the meta-data
# from EventBookkeeperTools.CutFlowHelpers import CreateCutFlowSvc
# CreateCutFlowSvc( svcName="CutFlowSvc", athFile=af, seq=topSequence, addMetaDataToAllOutputFiles=False )
outStream.AddMetaDataItem( ["xAOD::CutBookkeeperContainer#CutBookkeepers",
                            "xAOD::CutBookkeeperAuxContainer#CutBookkeepers*",
                            "xAOD::CutBookkeeperContainer#IncompleteCutBookkeepers",
                            "xAOD::CutBookkeeperAuxContainer#IncompleteCutBookkeepers*"] )
# Also add an instance of the CutFlowSvc for all other CutBookkeeperContainers
for mdItem in af.fileinfos["metadata_items"]:
    if mdItem[0].startswith("xAOD::CutBookkeeperContainer") \
      and not mdItem[1] == "CutBookkeepers" \
      and not mdItem[1] == "IncompleteCutBookkeepers":
        cbkName = mdItem[1]
        paodMsg.info("Creating now a CutFlowSvc instance for CutBookkeeperContainer with name %s" % cbkName)
        cfsName = "CutFlowSvc"+cbkName
        svcMgr += CfgMgr.CutFlowSvc(cfsName,
                                    #OutputLevel              = WARNING,
                                    InputStream              = inputStreamName,
                                    OutputCollName           = cbkName,
                                    OutputIncompleteCollName = "Incomplete"+cbkName
                                    )
        theApp.CreateSvc += [ "CutFlowSvc/"+cfsName ]
        outStream.AddMetaDataItem( ["xAOD::CutBookkeeperContainer#"+cbkName,
                                    "xAOD::CutBookkeeperAuxContainer#"+cbkName+"*"] )
        pass
    pass

# For the correct merging of the trigger meta-data
ToolSvc += CfgMgr.xAODMaker__TriggerMenuMetaDataTool("TriggerMenuMetaDataTool")
svcMgr.MetaDataSvc.MetaDataTools += [ ToolSvc.TriggerMenuMetaDataTool ]
outStream.AddMetaDataItem( ["xAOD::TriggerMenuContainer#*",
                            "xAOD::TriggerMenuAuxContainer#*"] )

# For the correct merging of the luminosity blocks meta-data
# from LumiBlockComps.LumiBlockCompsConf import LumiBlockMetaDataTool
# svcMgr.MetaDataSvc.MetaDataTools += [ "LumiBlockMetaDataTool" ]
ToolSvc += CfgMgr.LumiBlockMetaDataTool("LumiBlockMetaDataTool")
svcMgr.MetaDataSvc.MetaDataTools += [ ToolSvc.LumiBlockMetaDataTool ]
outStream.AddMetaDataItem( ["xAOD::LumiBlockRangeContainer#*",
                            "xAOD::LumiBlockRangeAuxContainer#*"] )

# For the correct handling of the xAOD::EventFormat (required to read file in ROOT)
ToolSvc += CfgMgr.xAODMaker__EventFormatMetaDataTool( "EventFormatMetaDataTool" )
svcMgr.MetaDataSvc.MetaDataTools += [ ToolSvc.EventFormatMetaDataTool ]
# theApp.CreateSvc += [ "xAODMaker::EventFormatSvc" ]
# outStream.AddMetaDataItem(["xAOD::EventFormat#EventFormat"])

# Set up the metadata tool:
# ToolSvc += CfgMgr.xAODMaker__FileMetaDataCreatorTool( "FileMetaDataCreatorTool" )
# svcMgr.MetaDataSvc.MetaDataTools += [ ToolSvc.FileMetaDataCreatorTool ]
outStream.AddMetaDataItem( ["xAOD::FileMetaData#FileMetaData",
                            "xAOD::FileMetaDataAuxInfo#FileMetaDataAux."] )

# Add some more meta data
outStream.AddMetaDataItem( ["IOVMetaDataContainer#*"] )


# ==============================================================================
# Set the number of events that you want to process (-1 means all events) or skip.
# Shown is a handy way how you can use command-line options.
# If EVTMAX is not given on the command line, the default -1 (process all events) is used.
# If SKIPEVT is not given on the command line, the default 0 (start from the beginning) is used.
# This works for any command line option that you may need; it is a python feature.
# ==============================================================================
svcMgr.EventSelector.SkipEvents = vars().get('SKIPEVT', 0)
theApp.EvtMax = vars().get('EVTMAX', -1)


# Suppress warnings from unknown objects (i.e., non-xAOD objects) in the input file
#svcMgr.PoolSvc.OutputLevel=ERROR

# Change the event printout interval, if you want to
evtPrintoutInterval = vars().get('EVTPRINT', 500)
svcMgr += CfgMgr.AthenaEventLoopMgr( EventPrintoutInterval=evtPrintoutInterval )


# ==============================================================================
# Remove the long printouts of ItemListSvc at the end of the job
# ==============================================================================
# svcMgr.ItemListSvc.OutputLevel = WARNING


# ==============================================================================
# Add basic code performance monitoring.
# The results will be presented at the end of your job.
# PerfMon profiles what memory was use and how long it took to run.
# Chrono tells you in an ordered table how much time was spend in each algorithm.
# ==============================================================================
from PerfMonComps.PerfMonFlags import jobproperties as pmjp
pmjp.PerfMonFlags.doFastMon = True    # to only enable a lightweight monitoring
if vars().get('doChrono',True):
    theAuditorSvc = svcMgr.AuditorSvc
    theAuditorSvc.Auditors  += [ "ChronoAuditor"]
    svcMgr.ChronoStatSvc.PrintUserTime     = False
    svcMgr.ChronoStatSvc.PrintSystemTime   = False
    svcMgr.ChronoStatSvc.PrintEllapsedTime = False
    svcMgr.ChronoStatSvc.NumberOfSkippedEventsForMemStat = 1
    theApp.AuditAlgorithms = True
pass
