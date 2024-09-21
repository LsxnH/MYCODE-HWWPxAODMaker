
# ====================================================================
# TODO: document contents
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWAnalysisCommonReco.py")

# ====================================================================
# Determine the flavour of simulation, i.e., Full or AFII
# ====================================================================
# TODO: /Simulation/Parameters might not be available if we are running over TRUTH DAODs
#       Add check on whether it's available and if not, keep inputSimulationType as an empty string
if hWWCommon.Global.inputIsSimulation :
    simType = af.fileinfos['metadata']['/Simulation/Parameters']['SimulationFlavour']
    if simType  == 'default' or simType == 'FullG4':
        hWWCommon.Global.inputSimulationType = "FullSim"
        pass
    elif simType  == 'atlfast' or simType == 'AtlfastII' :
        hWWCommon.Global.inputSimulationType = "AFII"
        pass
    elif type(simType) is str:
        if simType.__contains__('fast'):
            hWWCommon.Global.inputSimulationType = "AFII"
            pass
        else:
            hWW_msg.warning( "Input is simulation, but couldn't figure out of what type: %s" % simType )
        pass
    hWW_msg.info( "Detected that the input file is of simulation type: %s" % hWWCommon.Global.inputSimulationType )
    pass


# ====================================================================
# Check if we have 50ns intra-bunch spacing or 25ns (default)
# ====================================================================
# TODO: /Digitization/Parameters might not be available if we are running over TRUTH DAODs
#       Add check on whether it's available and if not, keep nominal bunchSpacing
if hWWCommon.Global.inputIsSimulation :
    bunchSpace = af.fileinfos['metadata']['/Digitization/Parameters']['intraTrainBunchSpacing']
    if bunchSpace == 50: hWWCommon.Global.bunchSpacing = 50
    pass
else:
    runNumberList = af.fileinfos["run_number"]
    if not runNumberList:
        hWW_msg.warning( "Empty run_number list returned from AthFile - assuming bunch spacing of %i ns" % hWWCommon.Global.bunchSpacing )
    elif runNumberList[0] < 276000:
        hWWCommon.Global.bunchSpacing = 50
    pass
hWW_msg.info( "Using bunch spacing of %i ns" % hWWCommon.Global.bunchSpacing )


# ====================================================================
# Change configuration if input is mc14/dc14, e.g., muon charge needs fixup
# ====================================================================
if af.fileinfos["eventdata_items"].__contains__(('xAOD::MissingETContainer', 'MET_RefFinalFix')):
    hWWCommon.MET.inCont = "MET_RefFinalFix"
    hWW_msg.info( "Using MET_RefFinalFix for the analysis")
    pass


# ====================================================================
# Check if the input file also has the requested track jets.
# If not, turn off the track jets
# ====================================================================
if not af.fileinfos["eventdata_items"].__contains__(('xAOD::JetContainer', hWWCommon.Jets.inTrackJetsCont)):
    hWWCommon.Jets.writeTrackJets = False
    hWW_msg.info( "Couldn't find track jets with name %s in the input container" % hWWCommon.Jets.inTrackJetsCont )
    pass


# ====================================================================
# Check if the input file also has the requested large-R jets.
# If not, turn off the large-R jets
# ====================================================================
if not af.fileinfos["eventdata_items"].__contains__(('xAOD::JetContainer', hWWCommon.FatJets.inCont)):
    hWWCommon.FatJets = False
    hWWCommon.FatJets.p4Systs = []
    hWW_msg.info( "Couldn't find large-R jets with name %s in the input container" % hWWCommon.FatJets.inCont )
    pass


# ====================================================================
# Use VeryLooseLH for electrons. Normally, this is only used for the
# "other" leptons and thus for MET building and overlap removal.
# Only if also doFakeWJets==True is this also used for
# ====================================================================
hWWCommon.Global.doVeryLooseLH = vars().get('doVeryLooseLH', hWWCommon.Global.doVeryLooseLH)
if hWWCommon.Global.doVeryLooseLH:
    hWW_msg.info("The user requested to use VeryLooseLH electron identification: %s" % hWWCommon.Global.doVeryLooseLH)
    hWWCommon.Electrons.preSelection.cutIDList = hWWCommon.Electrons.preSelection.cutIDListVeryLoose
    hWWCommon.Electrons.fakeWJets_cutIDList    = hWWCommon.Electrons.fakeWJets_cutIDListVeryLoose
    pass


# ====================================================================
# Use looser lepton selection, if we want to produce the sample for
# the W+jets fake region.
# ====================================================================
if vars().has_key('doFakeWJets'):
    hWWCommon.Global.doFakeWJets = doFakeWJets
    hWW_msg.info("The user requested to use hWWCommon.Global.doFakeWJets = %s" % hWWCommon.Global.doFakeWJets)
    pass
if hWWCommon.Global.doFakeWJets:
    hWW_msg.info("Using looser lepton selection for W+jets fake-lepton estimates")
    hWWCommon.Electrons.preSelection.cutZ0SinThetaMax     = hWWCommon.Electrons.preSelection.fakeWJets_cutZ0SinThetaMax
    hWWCommon.Electrons.preSelection.cutD0SignificanceMax = hWWCommon.Electrons.preSelection.fakeWJets_cutD0SignificanceMax
    hWWCommon.Electrons.cutIDList                         = hWWCommon.Electrons.fakeWJets_cutIDList
    hWWCommon.Electrons.cutZ0SinThetaMax                  = hWWCommon.Electrons.fakeWJets_cutZ0SinThetaMax
    hWWCommon.Electrons.cutD0SignificanceMax              = hWWCommon.Electrons.fakeWJets_cutD0SignificanceMax
    hWWCommon.Muons.preSelection.cutZ0SinThetaMax         = hWWCommon.Muons.preSelection.fakeWJets_cutZ0SinThetaMax
    hWWCommon.Muons.preSelection.cutD0SignificanceMax     = hWWCommon.Muons.preSelection.fakeWJets_cutD0SignificanceMax
    hWWCommon.Muons.cutZ0SinThetaMax                      = hWWCommon.Muons.fakeWJets_cutZ0SinThetaMax
    hWWCommon.Muons.cutD0SignificanceMax                  = hWWCommon.Muons.fakeWJets_cutD0SignificanceMax
    pass


# ====================================================================
# Use looser lepton selection, but only for the "other" leptons,
# if we want to produce the sample for the Z+jets fake region.
# ====================================================================
# TODO: think about how Truth/Reco configuration should work when we loosen the lepton ID even in the nominal case
if vars().has_key('doFakeZJets'):
    hWWCommon.Global.doFakeZJets = doFakeZJets
    hWW_msg.info("The user requested to use hWWCommon.Global.doFakeZJets = %s" % hWWCommon.Global.doFakeZJets)
    pass
if hWWCommon.Global.doFakeZJets:
    hWW_msg.info("Using looser lepton selection for Z+jets fake-lepton estimates")
    hWWCommon.Electrons.preSelection.cutZ0SinThetaMax     = hWWCommon.Electrons.preSelection.fakeWJets_cutZ0SinThetaMax
    hWWCommon.Electrons.preSelection.cutD0SignificanceMax = hWWCommon.Electrons.preSelection.fakeWJets_cutD0SignificanceMax
    hWWCommon.Muons.preSelection.cutZ0SinThetaMax         = hWWCommon.Muons.preSelection.fakeWJets_cutZ0SinThetaMax
    hWWCommon.Muons.preSelection.cutD0SignificanceMax     = hWWCommon.Muons.preSelection.fakeWJets_cutD0SignificanceMax
    # Also, turn OFF (for now) the VH outputs
    hWWCommon.Global.do3Lep = False
    hWWCommon.Global.do4Lep = False
    pass


# ====================================================================
# Use medium lepton pre-selection cuts for the "other" leptons, i.e.,
# before the overlap removal is done.
# ====================================================================
hWWCommon.Global.doMediumOtherLeptons = vars().get('doMediumOtherLeptons', hWWCommon.Global.doMediumOtherLeptons)
if hWWCommon.Global.doMediumOtherLeptons:
    hWW_msg.info("The user requested to use medium identification for the other leptons, i.e., pre-overlap-removal: %s" % hWWCommon.Global.doMediumOtherLeptons)
    hWWCommon.Electrons.preSelection.cutIDList = hWWCommon.Electrons.preSelection.cutIDListMedium
    hWWCommon.Muons.preSelection.cutIDList     = hWWCommon.Muons.preSelection.cutIDListMedium
    pass


# ====================================================================
# Check if some flags were given regarding the overlap removal
# ====================================================================
hWWCommon.Global.doORNoMuNearJetRemoval = vars().get('doORNoMuNearJetRemoval', hWWCommon.Global.doORNoMuNearJetRemoval)
if hWWCommon.Global.doORNoMuNearJetRemoval:
    hWW_msg.info("The user requested to not remove muons near jets in the overlap removal: %s" % hWWCommon.Global.doORNoMuNearJetRemoval)
    pass
hWWCommon.Global.doORNoMuNearJetRemovalNoBJetPrecedence = vars().get('doORNoMuNearJetRemovalNoBJetPrecedence', hWWCommon.Global.doORNoMuNearJetRemovalNoBJetPrecedence)
if hWWCommon.Global.doORNoMuNearJetRemovalNoBJetPrecedence:
    hWW_msg.info("The user requested to not remove muons near jets in the overlap removal and to give precedence to leptons over b-jets: %s" % hWWCommon.Global.doORNoMuNearJetRemovalNoBJetPrecedence)
    pass


# ====================================================================
# Check if a flag was given for running with PFlow jets
# ====================================================================
hWWCommon.Jets.doPFlowJets = vars().get('doPFlowJets', hWWCommon.Jets.doPFlowJets)
if hWWCommon.Jets.doPFlowJets:
    hWW_msg.info("The user requested to run with EMPFlow jets, setting configuration accordingly")
    hWWCommon.Jets.inCont              = hWWCommon.Jets.inContEMPFlow
    hWWCommon.Jets.calibConfigFile     = hWWCommon.Jets.calibConfigFileEMPFlow
    hWWCommon.Jets.calibAFIIConfigFile = hWWCommon.Jets.calibAFIIConfigFileEMPFlow
    hWWCommon.Jets.jvtConfigFile       = hWWCommon.Jets.jvtConfigFileEMPFlow
else:
    hWW_msg.info("Running with EMTopo jets, setting configuration accordingly")
    hWWCommon.Jets.inCont              = hWWCommon.Jets.inContEMTopo
    hWWCommon.Jets.calibConfigFile     = hWWCommon.Jets.calibConfigFileEMTopo
    hWWCommon.Jets.calibAFIIConfigFile = hWWCommon.Jets.calibAFIIConfigFileEMTopo
    hWWCommon.Jets.jvtConfigFile       = hWWCommon.Jets.jvtConfigFileEMTopo


# ====================================================================
# Get the command line option to turn on/off the efficiency and
# scale-factor calculations
# ====================================================================
hWWCommon.Global.doEffiScaleFactors = vars().get('doEffiScaleFactors', hWWCommon.Global.doEffiScaleFactors)
hWW_msg.info( "Using hWWCommon.Global.doEffiScaleFactors = %s" % hWWCommon.Global.doEffiScaleFactors )


# ====================================================================
# Turn off the four-momentum systematic variations, if requested,
# or if running on data
# ====================================================================
# Try to see if the user specified on the command line which systematics to use
if vars().has_key('doP4Systematics'):
    hWWCommon.Global.doP4Systematics = doP4Systematics
    hWW_msg.info( "The user requested to use hWWCommon.Global.doP4Systematics = %s" % hWWCommon.Global.doP4Systematics )
    pass
if not hWWCommon.Global.inputIsSimulation:
    hWW_msg.info( "Switching OFF four-momentum systematics since we are running on data" )
    hWWCommon.Global.doP4Systematics = False
    pass
if not hWWCommon.Global.doP4Systematics:
    hWW_msg.info( "Switching OFF four-momentum systematics" )
    hWWCommon.Electrons.p4Systs = []
    hWWCommon.Muons.p4Systs     = []
    hWWCommon.Jets.jesSysts     = []
    hWWCommon.Jets.jerSysts     = []
    hWWCommon.FatJets.p4Systs   = []
    hWWCommon.MET.p4TSTSysts    = []
    hWWCommon.MET.p4CSTSysts    = []
    hWWCommon.MET.p4JetTrkSysts = []
    pass
# Adding individual p4 systematics
hWWCommon.Jets.p4Systs = hWWCommon.Jets.jesSysts + hWWCommon.Jets.jerSysts
hWWCommon.MET.p4Systs  = hWWCommon.MET.p4TSTSysts + hWWCommon.MET.p4CSTSysts + hWWCommon.MET.p4JetTrkSysts

# Print what we use
hWW_msg.info("Using %i electron four-momentum systematics" % len(hWWCommon.Electrons.p4Systs) )
hWW_msg.debug("Using electron four-momentum systematics: %s" % hWWCommon.Electrons.p4Systs )
hWW_msg.info("Using %i muon four-momentum systematics" % len(hWWCommon.Muons.p4Systs) )
hWW_msg.debug("Using muon four-momentum systematics: %s" % hWWCommon.Muons.p4Systs )
hWW_msg.info("Using %i jet four-momentum systematics" % len(hWWCommon.Jets.p4Systs) )
hWW_msg.debug("Using jet four-momentum systematics: %s" % hWWCommon.Jets.p4Systs )
hWW_msg.info("Using %i large-R jet four-momentum systematics" % len(hWWCommon.FatJets.p4Systs) )
hWW_msg.debug("Using large-R jet four-momentum systematics: %s" % hWWCommon.FatJets.p4Systs )
hWW_msg.info("Using %i missingET four-momentum systematics" % len(hWWCommon.MET.p4Systs) )
hWW_msg.debug("Using missingET four-momentum systematics: %s" % hWWCommon.MET.p4Systs )

# Build the systematics tracker
from PhysicsxAODConfig.HWWCommonHelpers import SystematicsTracker
HWWSysTracker = SystematicsTracker( "HWWSystematicsTracker",
                                    fatjet   = hWWCommon.FatJets.p4Systs,
                                    jet      = hWWCommon.Jets.p4Systs,
                                    electron = hWWCommon.Electrons.p4Systs,
                                    muon     = hWWCommon.Muons.p4Systs,
                                    met      = hWWCommon.MET.p4Systs )
#HWWSysTracker.dump()


# ====================================================================
# Turn off the scale-factor systematic variations, if requested,
# if running on data, or if EffiScaleFactors not scheduled
# ====================================================================
# Try to see if the user specified on the command line which systematics to use
if vars().has_key('doEffiSystematics'):
    hWWCommon.Global.doEffiSystematics = doEffiSystematics
    hWW_msg.info( "The user requested to use hWWCommon.Global.doEffiSystematics = %s" % hWWCommon.Global.doEffiSystematics )
    pass
if not hWWCommon.Global.inputIsSimulation:
    hWW_msg.info( "Switching OFF efficiency systematics since we are running on data" )
    hWWCommon.Global.doEffiSystematics = False
    pass
elif not hWWCommon.Global.doEffiScaleFactors:
    hWW_msg.info( "Switching OFF efficiency systematics since doEffiScaleFactors=False" )
    hWWCommon.Global.doEffiSystematics = False
    pass
if not hWWCommon.Global.doEffiSystematics :
    hWW_msg.info( "Switching OFF efficiency systematics" )
    hWWCommon.Electrons.effiSysts     = []
    hWWCommon.Electrons.effiRecoSysts = []
    hWWCommon.Electrons.effiSFTrigSysts = []
    hWWCommon.Electrons.effiTrigSysts = []
    hWWCommon.Electrons.effiIsoSysts  = []
    hWWCommon.Muons.effiSysts         = []
    hWWCommon.Muons.effiTTVASysts     = []
    hWWCommon.Muons.effiIsoSysts      = []
    hWWCommon.Muons.effiTrigSysts     = []
    hWWCommon.Jets.effiSysts          = []
    hWWCommon.Jets.effiJVTSysts       = []
    pass
hWW_msg.info("Using %i electron efficiency systematics" % len(hWWCommon.Electrons.effiSysts) )
hWW_msg.info("Using %i electron reconstruction efficiency systematics" % len(hWWCommon.Electrons.effiRecoSysts) )
hWW_msg.info("Using %i electron trigger efficiency scale-factor systematics" % len(hWWCommon.Electrons.effiSFTrigSysts) )
hWW_msg.info("Using %i electron trigger efficiency systematics" % len(hWWCommon.Electrons.effiTrigSysts) )
hWW_msg.info("Using %i electron isolation efficiency systematics" % len(hWWCommon.Electrons.effiIsoSysts) )
hWW_msg.info("Using %i muon efficiency systematics" % len(hWWCommon.Muons.effiSysts) )
hWW_msg.info("Using %i muon isolation efficiency systematics" % len(hWWCommon.Muons.effiIsoSysts) )
hWW_msg.info("Using %i muon trigger efficiency systematics" % len(hWWCommon.Muons.effiTrigSysts) )
hWW_msg.info("Using %i jet b-tag efficiency systematics" % len(hWWCommon.Jets.effiSysts) )
hWW_msg.info("Using %i jet JVT efficiency systematics" % len(hWWCommon.Jets.effiJVTSysts) )


# ====================================================================
# Create the tool that will search for all matching inputput container names.
# This is used downstream by all efficiency and scale-factor algorithms
# to find also all four-vector systematically varied input containers.
# ====================================================================
ToolSvc += CfgMgr.HWW__ContainersFinderTool("HWWContainersFinderTool")#,OutputLevel = VERBOSE)




# ====================================================================
# Create a subsequence:
# Only when the first algorithm returns isEventAccepted,
# the rest of this sub-sequence is executed
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWCommonPreFilterSeq = AthSequencer("HWWCommonAnalysisPreFilterSeq", OutputLevel = WARNING)
topSequence += hWWCommonPreFilterSeq


# ====================================================================
# Schedule the event pre-selection, if requested
# ====================================================================
if hWWCommon.Global.doEventPreSelection:
    include("PhysicsxAODConfig/HWWEventPreSelection.py")
    pass


# ====================================================================
# Determine the mc16 subcampaign
# ====================================================================
if hWWCommon.Global.inputIsSimulation:
    runNumberList = af.fileinfos["run_number"]
    if runNumberList[0] == 284500:
        hWWCommon.Global.mcSubCampaign = "mc16a"
    elif runNumberList[0] == 300000:
        hWWCommon.Global.mcSubCampaign = "mc16d"
    elif runNumberList[0] == 310000:
        hWWCommon.Global.mcSubCampaign = "mc16e"
    else:
        hWW_msg.warning( "Input is simulation, but couldn't figure out of what mc16 subcampaign from runNumber: %s" % runNumberList[0] )

# ====================================================================
# Pileup Reweighting, use only on MC,
# Is stored in EventInfo as "PileupWeight".
# Have to run it, if efficiency tools are running, as they need it
# ====================================================================
if hWWCommon.Global.inputIsSimulation and ( hWWCommon.Global.doEffiScaleFactors or hWWCommon.Global.doPileupReweighting ) :
    hWW_msg.info("Going to run pileup reweighting")

    # Create an instance of the pileup reweighting tool
    ToolSvc += CfgMgr.CP__PileupReweightingTool("PileupReweighting",
                                                OutputLevel = VERBOSE,
                                                )

    # Configure the PRW tool based on the subcampaign and simType
    if hWWCommon.Global.mcSubCampaign == "mc16a" :
        hWW_msg.info("Configuring PRW for mc16a...")
        ToolSvc.PileupReweighting.ConfigFiles     = hWWCommon.Global.PRWConfigFilesFSmc16a
        ToolSvc.PileupReweighting.LumiCalcFiles   = hWWCommon.Global.LumiCalcFilesData1516
        pass
    elif hWWCommon.Global.mcSubCampaign == "mc16d" :
        hWW_msg.info("Configuring PRW for mc16d...")
        ToolSvc.PileupReweighting.ConfigFiles     = hWWCommon.Global.PRWConfigFilesFSmc16d + hWWCommon.Global.PRWActualMuData17
        ToolSvc.PileupReweighting.LumiCalcFiles   = hWWCommon.Global.LumiCalcFilesData17

    # Create the pileup reweighting alg and schedule it
    # hWWCommonPreFilterSeq += CfgMgr.CP__PileupReweightingProvider("PileupReweightingProviderAlg",
    hWWCommonPreFilterSeq += CfgMgr.HWW__PileupReweightingAlg("HWWPileupReweightingAlg",
                                                              #OutputLevel = VERBOSE,
                                                              Tool = ToolSvc.PileupReweighting )
    pass

# ====================================================================
# Add the new PromptLeptonIso_TagWeight to all leptons
# ====================================================================
#import JetTagNonPromptLepton.JetTagNonPromptLeptonConfig as JetTagConfig
#hWWCommonPreFilterSeq += JetTagConfig.GetDecoratePromptLeptonAlgs()


# ====================================================================
# Create a sub-sequence that will always run through all algorithms
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWCommonCalibSeq = AthSequencer( "HWWCommonCalibSeq", OutputLevel = VERBOSE, StopOverride = True )
hWWCommonPreFilterSeq += hWWCommonCalibSeq


# ====================================================================
# Create a sub-sequence that will always run through all algorithms
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWSuperCommonSeq = AthSequencer( "HWWSuperCommonSeq", OutputLevel = WARNING, StopOverride = True )
hWWCommonPreFilterSeq += hWWSuperCommonSeq
hWWCommonSeq = AthSequencer( "HWWCommonSeq", OutputLevel = WARNING, StopOverride = True )
hWWSuperCommonSeq += hWWCommonSeq


# ====================================================================
# Create a sub-sequence that will always run through all algorithms.
# This one will be populated with things that need to run BEFORE the
# overlap removal is done, e.g., like lepton pre-selections.
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWPreORSeq = AthSequencer( "HWWPreORSeq", OutputLevel = WARNING, StopOverride = True )
hWWCommonSeq += hWWPreORSeq


# ====================================================================
# Create a sub-sequence that will always run through all algorithms.
# This one will be populated with things that need to run AFTER the
# overlap removal is done.
# Note that we will only add it to the hWWCommonSeq right after the
# OverlapRemovalAlg has been run.
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWPostORSeq = AthSequencer( "HWWPostORSeq", OutputLevel = WARNING, StopOverride = True )


# ====================================================================
# Create a subsequence:
# Only when the previous algorithm returns isEventAccepted,
# the remainder of this sub-sequence is executed.
# Here, we will schedule the algorithms that only need to run for
# events that are scheduled to be written out (in any output stream).
# These are for example the efficiency scale-factor calculations or
# the MC truth flagging algs.
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWCommonEffiScaleFactorFilterSeq = AthSequencer("HWWCommonEffiScaleFactorFilterSeq", OutputLevel = WARNING)
hWWSuperCommonSeq += hWWCommonEffiScaleFactorFilterSeq
# Schedule the alg that will ask every output stream if the event will be written out.
# If any of them says yes, the rest of the sequence will run, otherwise not.
# We will set the property "OutputStreamNames" later, i.e., when we know which
# output streams actually exist.
if hWWCommon.Global.doFilterEffiSFSeq:
    hWWCommonEffiScaleFactorFilterSeq += CfgMgr.EventDecisionAlg("HWWEventDecisionAlg")
    pass
# Now, add the actual sequence where all the efficiency and scale-factor
# calculation algs will be added to (and other algs that only add stuff to the
# output, but are not needed to determine if an event gets written out or not).
# This sequence will actually run through every of its algs, irrespective of
# the behaviour of the previous alg.
hWWCommonEffiScaleFactorSeq = AthSequencer("HWWCommonEffiScaleFactorSeq", StopOverride = True, OutputLevel = WARNING)
hWWCommonEffiScaleFactorFilterSeq += hWWCommonEffiScaleFactorSeq


# ====================================================================
# Decorate the xAOD::EventInfo object with some MCTruth-based quantities
# ====================================================================
# TODO: Where to put the TruthFlagging in the Truth/Reco combined scenario?
#       Maybe best to add it to it's own post-processing sequence directly to the topSequence in this case?
if hWWCommon.Global.doTruthFlagging and hWWCommon.Global.inputIsSimulation:
    include("PhysicsxAODConfig/HWWTruthFlagging.py")
    pass


# ====================================================================
# Do the common object calibration (including systematics), if requested
# ====================================================================
if hWWCommon.Global.doCalibrations:
    # Do the common electron calibration (including systematics)
    include("PhysicsxAODConfig/HWWElectronCalibrationScaleFactor.py")

    # Do the common muon calibration (including systematics)
    include("PhysicsxAODConfig/HWWMuonCalibrationScaleFactor.py")

    # Do the common jet calibration (including systematics)
    include("PhysicsxAODConfig/HWWJetCalibrationScaleFactor.py")

    # Do the common large-R jet calibration (including systematics)
    if hWWCommon.FatJets(): include("PhysicsxAODConfig/HWWFatJetCalibration.py")
    pass


# ====================================================================
# Do trigger matching on electrons and muons and tag them with the results
# ====================================================================
if hWWCommon.Global.doTriggerMatching :
    include("PhysicsxAODConfig/HWWTriggerMatching.py")
    pass


# ====================================================================
# Do the overlap removal of the containers
# ====================================================================
if hWWCommon.Global.doOverlapRemoval:
    include("PhysicsxAODConfig/HWWOverlapRemoval.py")
    pass


# ====================================================================
# Run the object selections only if requested
# ====================================================================
if hWWCommon.Global.doSelections:
    # Do the electron selection
    include("PhysicsxAODConfig/HWWElectronSelection.py")

    # Do the muon selection
    include("PhysicsxAODConfig/HWWMuonSelection.py")

    # Do the jet selection
    include("PhysicsxAODConfig/HWWJetSelection.py")

    # Do the large-R jet selection
    if hWWCommon.FatJets(): include("PhysicsxAODConfig/HWWFatJetSelection.py")
    pass


# ====================================================================
# Do the common missingET building (including systematics).
# Only attempt this if the input file actually has the required
# missingET items in it (for example, the fake-factor derivations may not).
# ====================================================================
if hWWCommon.Global.doCandidateBuilding:
    if af.fileinfos["eventdata_items"].__contains__(('xAOD::MissingETContainer', hWWCommon.MET.inCore)) \
      and af.fileinfos["eventdata_items"].__contains__(('xAOD::MissingETAssociationMap', hWWCommon.MET.inMap)):
        include("PhysicsxAODConfig/HWWMETBuilding.py")
        pass
    else:
        hWW_msg.info("Couldn't find xAOD::MissingETContainer#%s and/or xAOD::MissingETAssociationMap#%s..." \
          % (hWWCommon.MET.inCore, hWWCommon.MET.inMap) )
        hWW_msg.info("...won't run missingET rebuilding!")
        pass
    pass


# ====================================================================
# Calculate all efficiencies and scale factors, if requested.
# ====================================================================
# TODO: this goes in the reco specific JOs
if hWWCommon.Global.doEffiScaleFactors and hWWCommon.Global.inputIsSimulation:
    include("PhysicsxAODConfig/HWWEfficiencyScaleFactor.py")
    pass


# ====================================================================
# Do the commont thinning (removal of individual objects/particles
# within a container).
# ====================================================================
# TODO: this goes in the reco specific JOs
if hWWCommon.Global.doThinning:
    hWWCommonEffiScaleFactorSeq += CfgMgr.ThinTrackParticlesAlg("HWWGSFTrackParticlesThinnerAlg",
                                                                #OutputLevel = DEBUG,
                                                                TrackParticlesToThin       = "GSFTrackParticles",
                                                                InputContainerList         = [ hWWCommon.Electrons.finalCont ],
                                                                NMaxElectronTrackParticles = 1,
                                                                ThinningSvc                = 'ThinningSvc/HWWCommonThinning'
                                                                )
    hWWCommonEffiScaleFactorSeq += CfgMgr.ThinCaloClustersAlg("HWWlnulnuCaloClusterThinnerAlg",
                                                          #OutputLevel = VERBOSE,
                                                              CaloClustersToThin = "egammaClusters",
                                                              InputContainerList = [ hWWCommon.Electrons.finalCont ],
                                                              ThinningSvc        = 'ThinningSvc/HWWCommonThinning'
                                                              )
    pass
