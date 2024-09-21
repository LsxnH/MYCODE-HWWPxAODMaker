
# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("HWWlnulnuxAODConfig/HWWlnulnuTruthEventCandidateBuilding.py")


# ====================================================================
# Create a sub-sequence that will always run through all algorithms
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWTruthEventCandSeq = AthSequencer( "HWWTruthEventCandSeq", OutputLevel = WARNING, StopOverride = True )
hWWTruthCommonSeq += hWWTruthEventCandSeq

from PhysicsxAODConfig.HWWCommonHelpers import buildContainerNames


# ====================================================================
# Build the electron-electron event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthElectrons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthJets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthMET.finalCont,['','electronNOSUFFIX','muonNOSUFFIX','jetNOSUFFIX','met']),
                                               (hWWCommon.TruthElectrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthMuons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthJets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWlnulnu.TruthEvent.eeEvent,['','electron','muon','jet','met'])
                                               ] )

eeTruthEventExistsString = ""
for inElectronContName, inJetContName, inMETContName, \
    inOtherElectronContName, inOtherMuonContName, inOtherJetContName,         \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWElElFullTruthEventBuilderAlg"+algNameSuffix

    hWWlnulnu_msg.debug("Creating H->ee event building algorithm with name %s:" % algName)
    #hWWlnulnu_msg.debug("    inLeadElectronContName  = %s" % inLeadElectronContName)
    hWWlnulnu_msg.debug("    inElectronContName      = %s" % inElectronContName)
    hWWlnulnu_msg.debug("    inJetContName           = %s" % inJetContName)
    hWWlnulnu_msg.debug("    inMETContName           = %s" % inMETContName)
    hWWlnulnu_msg.debug("    inOtherElectronContName = %s" % inOtherElectronContName)
    hWWlnulnu_msg.debug("    inOtherMuonContName     = %s" % inOtherMuonContName)
    hWWlnulnu_msg.debug("    inOtherJetContName      = %s" % inOtherJetContName)
    hWWlnulnu_msg.debug("    outEventName            = %s" % outEventName)

    # Build also the final 'event' candidates
    hWWTruthEventCandSeq += CfgMgr.HWW__FullEventBuilderAlg( algName,
                                                             #OutputLevel               = VERBOSE,
                                                             Lepton1Container          = inElectronContName,
                                                             CutLeadingLeptonPtMin     = hWWCommon.TruthElectrons.cutLeadPtMin,
                                                             Lepton2Container          = inElectronContName,
                                                             JetContainer              = inJetContName,
                                                             MissingETContainer        = inMETContName,
                                                             MissingETObject           = hWWCommon.TruthMET.inObject,
                                                             OtherElectronContainer    = inOtherElectronContName,
                                                             OtherMuonContainer        = inOtherMuonContName,
                                                             OtherJetContainer         = inOtherJetContName,
                                                             EventContainer            = outEventName,
                                                             WriteSplitOutputContainer = True
                                                             )

    # Add this algorithm to the list for event selection
    eeTruthEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWTruthEventCandSeq += CfgMgr.CutAlg("HWWElElFullTruthEventExistsAlg", Cut = eeTruthEventExistsString.rstrip(" || "), TrigDecisionTool = "" )
hWWlnulnu.Global.acceptAlgList.append("HWWElElFullTruthEventExistsAlg")





# ====================================================================
# Build the muon-muon event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthMuons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthJets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthMET.finalCont,['','electronNOSUFFIX','muonNOSUFFIX','jetNOSUFFIX','met']),
                                               (hWWCommon.TruthElectrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthMuons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthJets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWlnulnu.TruthEvent.mmEvent,['','electron','muon','jet','met'])
                                               ] )

mmTruthEventExistsString = ""
for inMuonContName, inJetContName, inMETContName, \
    inOtherElectronContName, inOtherMuonContName, inOtherJetContName, \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWMuMuFullTruthEventBuilderAlg"+algNameSuffix

    hWWlnulnu_msg.debug("Creating H->mumu event building algorithm with name %s:" % algName)
    hWWlnulnu_msg.debug("    inMuonContName          = %s" % inMuonContName)
    hWWlnulnu_msg.debug("    inJetContName           = %s" % inJetContName)
    hWWlnulnu_msg.debug("    inMETContName           = %s" % inMETContName)
    hWWlnulnu_msg.debug("    inOtherElectronContName = %s" % inOtherElectronContName)
    hWWlnulnu_msg.debug("    inOtherMuonContName     = %s" % inOtherMuonContName)
    hWWlnulnu_msg.debug("    inOtherJetContName      = %s" % inOtherJetContName)
    hWWlnulnu_msg.debug("    outEventName            = %s" % outEventName)

    # Build also the final 'event' candidates
    hWWTruthEventCandSeq += CfgMgr.HWW__FullEventBuilderAlg( algName,
                                                             #OutputLevel               = VERBOSE,
                                                             Lepton1Container          = inMuonContName,
                                                             CutLeadingLeptonPtMin     = hWWCommon.TruthMuons.cutLeadPtMin,
                                                             Lepton2Container          = inMuonContName,
                                                             JetContainer              = inJetContName,
                                                             MissingETContainer        = inMETContName,
                                                             MissingETObject           = hWWCommon.TruthMET.inObject,
                                                             OtherElectronContainer    = inOtherElectronContName,
                                                             OtherMuonContainer        = inOtherMuonContName,
                                                             OtherJetContainer         = inOtherJetContName,
                                                             EventContainer            = outEventName,
                                                             WriteSplitOutputContainer = True
                                                             )

    # Add this algorithm to the list for event selection
    mmTruthEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWTruthEventCandSeq += CfgMgr.CutAlg("HWWMuMuFullTruthEventExistsAlg", Cut = mmTruthEventExistsString.rstrip(" || "), TrigDecisionTool = "" )
hWWlnulnu.Global.acceptAlgList.append("HWWMuMuFullTruthEventExistsAlg")







# ====================================================================
# Build the electron-muon event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthElectrons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthMuons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthJets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthMET.finalCont,['','electronNOSUFFIX','muonNOSUFFIX','jetNOSUFFIX','met']),
                                               (hWWCommon.TruthElectrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthMuons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthJets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWlnulnu.TruthEvent.emEvent,['','electron','muon','jet','met'])
                                               ] )

emTruthEventExistsString = ""
for inElectronContName, inMuonContName, inJetContName, inMETContName, \
    inOtherElectronContName, inOtherMuonContName, inOtherJetContName, \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWElMuFullTruthEventBuilderAlg"+algNameSuffix

    hWWlnulnu_msg.debug("Creating H->emu event building algorithm with name %s:" % algName)
    hWWlnulnu_msg.debug("    inElectronContName      = %s" % inElectronContName)
    hWWlnulnu_msg.debug("    inMuonContName          = %s" % inMuonContName)
    hWWlnulnu_msg.debug("    inJetContName           = %s" % inJetContName)
    hWWlnulnu_msg.debug("    inMETContName           = %s" % inMETContName)
    hWWlnulnu_msg.debug("    inOtherElectronContName = %s" % inOtherElectronContName)
    hWWlnulnu_msg.debug("    inOtherMuonContName     = %s" % inOtherMuonContName)
    hWWlnulnu_msg.debug("    inOtherJetContName      = %s" % inOtherJetContName)
    hWWlnulnu_msg.debug("    outEventName            = %s" % outEventName)

    # Build also the final 'event' candidates
    hWWTruthEventCandSeq += CfgMgr.HWW__FullEventBuilderAlg( algName,
                                                             #OutputLevel               = VERBOSE,
                                                             Lepton1Container          = inElectronContName,
                                                             CutLeadingLeptonPtMin     = hWWCommon.TruthElectrons.cutLeadPtMin,
                                                             Lepton2Container          = inMuonContName,
                                                             JetContainer              = inJetContName,
                                                             MissingETContainer        = inMETContName,
                                                             MissingETObject           = hWWCommon.TruthMET.inObject,
                                                             OtherElectronContainer    = inOtherElectronContName,
                                                             OtherMuonContainer        = inOtherMuonContName,
                                                             OtherJetContainer         = inOtherJetContName,
                                                             EventContainer            = outEventName,
                                                             WriteSplitOutputContainer = True
                                                             )

    # Add this algorithm to the list for event selection
    emTruthEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWTruthEventCandSeq += CfgMgr.CutAlg("HWWElMuFullTruthEventExistsAlg", Cut = emTruthEventExistsString.rstrip(" || "), TrigDecisionTool = "" )
hWWlnulnu.Global.acceptAlgList.append("HWWElMuFullTruthEventExistsAlg")





# ====================================================================
# Build the muon-electron event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthMuons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthElectrons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthJets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthMET.finalCont,['','electronNOSUFFIX','muonNOSUFFIX','jetNOSUFFIX','met']),
                                               (hWWCommon.TruthElectrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthMuons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWCommon.TruthJets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                               (hWWlnulnu.TruthEvent.meEvent,['','electron','muon','jet','met'])
                                               ] )

meTruthEventExistsString = ""
for inLeadMuonContName, inElectronContName, inJetContName, inMETContName, \
    inOtherElectronContName, inOtherMuonContName, inOtherJetContName,     \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWMuElFullTruthEventBuilderAlg"+algNameSuffix

    hWWlnulnu_msg.debug("Creating H->mue event building algorithm with name %s:" % algName)
    hWWlnulnu_msg.debug("    inLeadElectronContName  = %s" % inLeadMuonContName)
    hWWlnulnu_msg.debug("    inElectronContName      = %s" % inElectronContName)
    hWWlnulnu_msg.debug("    inJetContName           = %s" % inJetContName)
    hWWlnulnu_msg.debug("    inMETContName           = %s" % inMETContName)
    hWWlnulnu_msg.debug("    inOtherElectronContName = %s" % inOtherElectronContName)
    hWWlnulnu_msg.debug("    inOtherMuonContName     = %s" % inOtherMuonContName)
    hWWlnulnu_msg.debug("    inOtherJetContName      = %s" % inOtherJetContName)
    hWWlnulnu_msg.debug("    outEventName            = %s" % outEventName)

    # Build also the final 'event' candidates
    hWWTruthEventCandSeq += CfgMgr.HWW__FullEventBuilderAlg( algName,
                                                             #OutputLevel               = VERBOSE,
                                                             Lepton1Container          = inLeadMuonContName,
                                                             CutLeadingLeptonPtMin     = hWWCommon.TruthMuons.cutLeadPtMin,
                                                             Lepton2Container          = inElectronContName,
                                                             JetContainer              = inJetContName,
                                                             MissingETContainer        = inMETContName,
                                                             MissingETObject           = hWWCommon.TruthMET.inObject,
                                                             OtherElectronContainer    = inOtherElectronContName,
                                                             OtherMuonContainer        = inOtherMuonContName,
                                                             OtherJetContainer         = inOtherJetContName,
                                                             EventContainer            = outEventName,
                                                             WriteSplitOutputContainer = True
                                                             )

    # Add this algorithm to the list for event selection
    meTruthEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWTruthEventCandSeq += CfgMgr.CutAlg("HWWMuElFullTruthEventExistsAlg", Cut = meTruthEventExistsString.rstrip(" || "), TrigDecisionTool = "" )
hWWlnulnu.Global.acceptAlgList.append("HWWMuElFullTruthEventExistsAlg")
