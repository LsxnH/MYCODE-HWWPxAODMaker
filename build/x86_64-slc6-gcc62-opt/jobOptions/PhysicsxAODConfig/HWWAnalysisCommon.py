
# ====================================================================
# This file schedules all the standardized event pre-selections
# (trigger, GoodRunsList), and also crates the finally calibrated
# objects.
# Here, we also create the needed sub-sequences and we figure out
# over what kind of data/MC we are running.
# This will be the first file that any HWW analysis configuration needs
# to include.
# ====================================================================


# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWAnalysisCommon.py")


# Import the module that allows to use named units, e.g. GeV
from AthenaCommon.SystemOfUnits import *

# Import the steering flags for this analysis
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon


# ====================================================================
# Check if we have Monte Carlo or real data, based on the input file meta-data
# ====================================================================
if af.fileinfos.has_key("evt_type"):
    eventTypeList = af.fileinfos["evt_type"]
    if eventTypeList.__contains__("IS_SIMULATION") :
        hWW_msg.info( "Detected that the input file is a simulated dataset" )
        hWWCommon.Global.inputIsSimulation = True
        pass
    pass


AtlasRelease = af.fileinfos["metadata"]["/TagInfo"]["AtlasRelease"]
hWW_msg.info( "AtlasRelease of input file: %s" % AtlasRelease )

# ====================================================================
# Check if we have a DxAOD or xAOD, based on the input file meta-data
# ====================================================================
if AtlasRelease.__contains__("AthDerivation"):
    hWWCommon.Global.inputIsDAOD = True
    hWW_msg.info( "Input file is a DxAOD")
    pass


# ====================================================================
# Check what input file type we actually have
# ====================================================================
hWWCommon.Global.inputStreamName = af.fileinfos["stream_names"][0]
hWW_msg.info( "Input stream name found: %s" % hWWCommon.Global.inputStreamName )


# ====================================================================
# Check which release the input file was produced with
# ====================================================================
if AtlasRelease.__contains__("-20.1."):
    hWWCommon.Global.inputRelease = "20.1"
    pass
elif AtlasRelease.__contains__("-20.7."):
    hWWCommon.Global.inputRelease = "20.7"
    pass
elif AtlasRelease.__contains__("-21.2."):
    hWWCommon.Global.inputRelease = "21.2"
    pass

if hWWCommon.Global.inputRelease:
    hWW_msg.info( "Input file was processed with release %s" % hWWCommon.Global.inputRelease )
else:
    hWW_msg.warning( "Couldn't determine which numbered release was used to generate the input" )


# ====================================================================
# Get beam energy from AthFile (set default to bigger than 4 TeV)
# ====================================================================
if af.fileinfos.has_key("beam_energy"):
    hWWCommon.Global.beamEnergy = af.fileinfos["beam_energy"][0]
    hWW_msg.info( "Beam energy from input metadata: %f", hWWCommon.Global.beamEnergy )
    pass
else:
    hWW_msg.warning( "No beam energy found in input metadata, use default value of %s TeV (to avoid crashes, no pileup reweighting will be applied)" % hWWCommon.Global.beamEnergy/TeV )
    pass


# ====================================================================
# Allowing for input from the user,
# determine if we are running reco processing, truth processing, or both
# each will be attached independently to the topSequence
# ====================================================================
hWWCommon.Global.processReco  = vars().get('processReco',  hWWCommon.Global.processReco)
hWWCommon.Global.processTruth = vars().get('processTruth', hWWCommon.Global.processTruth)
hWW_msg.info( "The user requested to use hWWCommon.Global.processReco = %s" % hWWCommon.Global.processReco )
hWW_msg.info( "The user requested to use hWWCommon.Global.processTruth = %s" % hWWCommon.Global.processTruth )
if hWWCommon.Global.processReco:
    hWW_msg.info( "The Reco sequence chain will be added to the topSequence" )
if hWWCommon.Global.processTruth:
    hWW_msg.info( "The Truth sequence chain will be added to the topSequence" )


# ====================================================================
# Break up the AuxContainers into individual AuxDyn variables for selected containers
# ====================================================================
# TODO: probably keep this in for both truth/reco running
if hWWCommon.Global.breakUpAuxContainers :
    if hWWCommon.Jets.writeTrackJets: hWWCommon.Global.auxContsToBreakUp.append("AntiKt4PV0TrackJetsAux.")
    topSequence += CfgMgr.xAODMaker__AuxStoreWrapper( "HWWAuxStoreWrapperAlg", OutputLevel = INFO )
    topSequence.HWWAuxStoreWrapperAlg.SGKeys = hWWCommon.Global.auxContsToBreakUp
    pass


if hWWCommon.Global.processReco:
    include("PhysicsxAODConfig/HWWAnalysisCommonReco.py")


if hWWCommon.Global.processTruth:
    include("PhysicsxAODConfig/HWWAnalysisCommonTruth.py")
