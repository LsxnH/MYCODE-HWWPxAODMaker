
# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("HWWFakeFactorxAOD/HWWFakeLeptonEventCandidateBuilding.py")


# ====================================================================
# Create a sub-sequence that will always run through all algorithms
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWFakesEventCandSeq = AthSequencer( "HWWFakesEventCandSeq", OutputLevel = WARNING, StopOverride = True )
hWWCommonSeq += hWWFakesEventCandSeq



# ====================================================================
# Changes to common object and event selection
# ====================================================================

# Configure the trigger preselection for fakes
if hWWCommon.Global.doTriggerSelection :
    # Yes this works, python black magic (aka lists are mutable python objects)
    triggerList = hWWCommonPreFilterSeq.HWWTriggerAlg.TriggerList
    for trigName in hWWFakes.Trigger.allFakableLeptonsTriggerList:
        if trigName in triggerList: continue
        triggerList.append(trigName)
        pass
    # Tell the trigger algorithm to store prescales as well
    hWWCommonPreFilterSeq.HWWTriggerAlg.StorePrescaleInfo = True
    pass

# Decorates leptons with trigger matching information for "fakes" triggers
if hWWCommon.Global.doTriggerMatching :
    eleMatchList = ToolSvc.HWWTriggerMatchingTool.ElectronMatchList
    for trigName in hWWFakes.Trigger.fakesElectronTriggerList:
        if trigName in eleMatchList: continue
        eleMatchList.append(trigName)
        pass
    muMatchList = ToolSvc.HWWTriggerMatchingTool.MuonMatchList
    for trigName in hWWFakes.Trigger.fakesMuonTriggerList:
        if trigName in muMatchList: continue
        muMatchList.append(trigName)
        pass
    pass


# Changing the lepton preselection to match the fakable object definitions
# Electrons
ToolSvc.HWWElectronPreSelectionTool.CutPtMin             = hWWCommon.Electrons.cutPtMin
ToolSvc.HWWElectronPreSelectionTool.CutIDList            = hWWCommon.Electrons.preSelection.cutIDList
ToolSvc.HWWElectronPreSelectionTool.CutIDPtMinList       = hWWCommon.Electrons.preSelection.cutIDPtMinList
ToolSvc.HWWElectronPreSelectionTool.CutZ0SinThetaMax     = hWWCommon.Electrons.preSelection.fakeWJets_cutZ0SinThetaMax
ToolSvc.HWWElectronPreSelectionTool.CutD0SignificanceMax = hWWCommon.Electrons.preSelection.fakeWJets_cutD0SignificanceMax
# Muons
ToolSvc.HWWMuonPreSelectionTool.CutPtMin             = hWWCommon.Muons.preSelection.cutPtMin
ToolSvc.HWWMuonPreSelectionTool.CutD0SignificanceMax = hWWCommon.Muons.preSelection.fakeWJets_cutD0SignificanceMax
ToolSvc.HWWMuonPreSelectionTool.CutZ0SinThetaMax     = hWWCommon.Muons.preSelection.fakeWJets_cutZ0SinThetaMax

# Switch off electron-photon ambiguity evaluation
hWWCommonCalibSeq.HWWElectronDecorationAlg.DoAmbiguity = False



# ====================================================================
# Build the electron fakes event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWSysTracker.containers( [ (hWWCommon.Electrons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.MET.finalCont,['','electronNOSUFFIX','muonNOSUFFIX','jetNOSUFFIX','met']),
                                          (hWWCommon.Electrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Muons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWFakes.Event.eFakeEvent,['','electron','muon','jet','met'])
                                          ] )

eEventExistsString = ""
for inLepContName, inJetContName, inMETContName, \
    inFakableElectronContName, inFakableMuonContName,         \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWFakeElFakeLeptonEventBuilderAlg"+algNameSuffix

    hWWFakes_msg.debug("Creating fake e candidate event building algorithm with name %s:" % algName)
    hWWFakes_msg.debug("    inLepContName             = %s" % inLepContName)
    hWWFakes_msg.debug("    inJetContName             = %s" % inJetContName)
    hWWFakes_msg.debug("    inMETContName             = %s" % inMETContName)
    hWWFakes_msg.debug("    inFakableElectronContName = %s" % inFakableElectronContName)
    hWWFakes_msg.debug("    inOtherLeptonContName     = %s" % inFakableMuonContName)
    hWWFakes_msg.debug("    outEventName              = %s" % outEventName)

    # Build also the final 'event' candidates
    hWWFakesEventCandSeq += CfgMgr.HWW__FakeLeptonEventBuilderAlg( algName,
                                                                   # OutputLevel               = DEBUG,
                                                                   LeptonContainer           = inLepContName,
                                                                   FakableLeptonContainer    = inFakableElectronContName,
                                                                   OtherLeptonContainer      = inFakableMuonContName,
                                                                   JetContainer              = inJetContName,
                                                                   MissingETContainer        = inMETContName,
                                                                   MissingETObject           = hWWCommon.MET.inObject,
                                                                   EventContainer            = outEventName,
                                                                   WriteSplitOutputContainer = True,

                                                                   )

    # Add this algorithm to the list for event selection
    eEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWFakesEventCandSeq += CfgMgr.CutAlg("HWWFakeElFullEventExistsAlg", Cut = eEventExistsString.rstrip(" || ") )
hWWFakes.Global.acceptAlgList.append("HWWFakeElFullEventExistsAlg")


# ====================================================================
# Build the muon fakes event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWSysTracker.containers( [ (hWWCommon.Muons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.MET.finalCont,['','electronNOSUFFIX','muonNOSUFFIX','jetNOSUFFIX','met']),
                                          (hWWCommon.Electrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Muons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWFakes.Event.mFakeEvent,['','electron','muon','jet','met'])
                                          ] )

mEventExistsString = ""
for inLepContName, inJetContName, inMETContName, \
    inFakableElectronContName, inFakableMuonContName, \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWFakeMuFakeLeptonEventBuilderAlg"+algNameSuffix

    hWWFakes_msg.debug("Creating fake mu candidate event building algorithm with name %s:" % algName)
    hWWFakes_msg.debug("    inLepContName             = %s" % inLepContName)
    hWWFakes_msg.debug("    inJetContName             = %s" % inJetContName)
    hWWFakes_msg.debug("    inMETContName             = %s" % inMETContName)
    hWWFakes_msg.debug("    inFakableElectronContName = %s" % inFakableMuonContName)
    hWWFakes_msg.debug("    inOtherLeptonContName     = %s" % inFakableElectronContName)
    hWWFakes_msg.debug("    outEventName              = %s" % outEventName)

    # Build also the final 'event' candidates
    hWWFakesEventCandSeq += CfgMgr.HWW__FakeLeptonEventBuilderAlg( algName,
                                                                   # OutputLevel               = DEBUG,
                                                                   LeptonContainer           = inLepContName,
                                                                   FakableLeptonContainer    = inFakableMuonContName,
                                                                   OtherLeptonContainer      = inFakableElectronContName,
                                                                   JetContainer              = inJetContName,
                                                                   MissingETContainer        = inMETContName,
                                                                   MissingETObject           = hWWCommon.MET.inObject,
                                                                   EventContainer            = outEventName,
                                                                   WriteSplitOutputContainer = True,

                                                                   )

    # Add this algorithm to the list for event selection
    mEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWFakesEventCandSeq += CfgMgr.CutAlg("HWWFakeMuFullEventExistsAlg", Cut = mEventExistsString.rstrip(" || ") )
hWWFakes.Global.acceptAlgList.append("HWWFakeMuFullEventExistsAlg")
