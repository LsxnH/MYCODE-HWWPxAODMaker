
# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("HWWlnulnuxAODConfig/HWWlnulnuEventCandidateBuilding.py")


# ====================================================================
# Create a sub-sequence that will always run through all algorithms
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWEventCandSeq = AthSequencer( "HWWEventCandSeq", OutputLevel = WARNING, StopOverride = True )
hWWCommonSeq += hWWEventCandSeq

from PhysicsxAODConfig.HWWCommonHelpers import buildContainerNames


# ====================================================================
# Build the electron-electron event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWSysTracker.containers( [ (hWWCommon.Electrons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.MET.finalCont,['','electron','muon','jet','met']),
                                          (hWWCommon.Electrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Muons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWlnulnu.Event.eeEvent,['','electron','muon','jet','met'])
                                          ] )

eeEventExistsString = ""
for inElectronContName, inJetContName, inMETContName, \
    inOtherElectronContName, inOtherMuonContName, inOtherJetContName,         \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWElElFullEventBuilderAlg"+algNameSuffix

    # Replace the MET to the nominal one, if we are on a TrackMET-only systematic
    if any( sysSuffix in inMETContName for sysSuffix in hWWCommon.MET.p4JetTrkSysts ):
        inMETContName = hWWCommon.MET.finalCont
        pass

    hWWlnulnu_msg.debug("Creating H->ee event building algorithm with name %s:" % algName)
    hWWlnulnu_msg.debug("    inElectronContName      = %s" % inElectronContName)
    hWWlnulnu_msg.debug("    inJetContName           = %s" % inJetContName)
    hWWlnulnu_msg.debug("    inMETContName           = %s" % inMETContName)
    hWWlnulnu_msg.debug("    inOtherElectronContName = %s" % inOtherElectronContName)
    hWWlnulnu_msg.debug("    inOtherMuonContName     = %s" % inOtherMuonContName)
    hWWlnulnu_msg.debug("    inOtherJetContName      = %s" % inOtherJetContName)
    hWWlnulnu_msg.debug("    outEventName            = %s" % outEventName)

    # Build also the final 'event' candidates
    hWWEventCandSeq += CfgMgr.HWW__FullEventBuilderAlg( algName,
                                                        #OutputLevel               = VERBOSE,
                                                        Lepton1Container          = inElectronContName,
                                                        CutLeadingLeptonPtMin     = hWWCommon.Electrons.cutLeadPtMin,
                                                        Lepton2Container          = inElectronContName,
                                                        JetContainer              = inJetContName,
                                                        MissingETContainer        = inMETContName,
                                                        MissingETObject           = hWWCommon.MET.inObject,
                                                        OtherElectronContainer    = inOtherElectronContName,
                                                        OtherMuonContainer        = inOtherMuonContName,
                                                        OtherJetContainer         = inOtherJetContName,
                                                        EventContainer            = outEventName,
                                                        WriteSplitOutputContainer = True
                                                        )

    # Add this algorithm to the list for event selection
    eeEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWEventCandSeq += CfgMgr.CutAlg("HWWElElFullEventExistsAlg", Cut = eeEventExistsString.rstrip(" || ") )
hWWlnulnu.Global.acceptAlgList.append("HWWElElFullEventExistsAlg")





# ====================================================================
# Build the muon-muon event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWSysTracker.containers( [ (hWWCommon.Muons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.MET.finalCont,['','electron','muon','jet','met']),
                                          (hWWCommon.Electrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Muons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWlnulnu.Event.mmEvent,['','electron','muon','jet','met'])
                                          ] )

mmEventExistsString = ""
for inMuonContName, inJetContName, inMETContName, \
    inOtherElectronContName, inOtherMuonContName, inOtherJetContName, \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWMuMuFullEventBuilderAlg"+algNameSuffix

    # Replace the MET to the nominal one, if we are on a TrackMET-only systematic
    if any( sysSuffix in inMETContName for sysSuffix in hWWCommon.MET.p4JetTrkSysts ):
        inMETContName = hWWCommon.MET.finalCont
        pass

    hWWlnulnu_msg.debug("Creating H->mumu event building algorithm with name %s:" % algName)
    hWWlnulnu_msg.debug("    inMuonContName          = %s" % inMuonContName)
    hWWlnulnu_msg.debug("    inJetContName           = %s" % inJetContName)
    hWWlnulnu_msg.debug("    inMETContName           = %s" % inMETContName)
    hWWlnulnu_msg.debug("    inOtherElectronContName = %s" % inOtherElectronContName)
    hWWlnulnu_msg.debug("    inOtherMuonContName     = %s" % inOtherMuonContName)
    hWWlnulnu_msg.debug("    inOtherJetContName      = %s" % inOtherJetContName)
    hWWlnulnu_msg.debug("    outEventName            = %s" % outEventName)

    # Build also the final 'event' candidates
    hWWEventCandSeq += CfgMgr.HWW__FullEventBuilderAlg( algName,
                                                        #OutputLevel               = VERBOSE,
                                                        Lepton1Container          = inMuonContName,
                                                        CutLeadingLeptonPtMin     = hWWCommon.Muons.cutLeadPtMin,
                                                        Lepton2Container          = inMuonContName,
                                                        JetContainer              = inJetContName,
                                                        MissingETContainer        = inMETContName,
                                                        MissingETObject           = hWWCommon.MET.inObject,
                                                        OtherElectronContainer    = inOtherElectronContName,
                                                        OtherMuonContainer        = inOtherMuonContName,
                                                        OtherJetContainer         = inOtherJetContName,
                                                        EventContainer            = outEventName,
                                                        WriteSplitOutputContainer = True
                                                        )

    # Add this algorithm to the list for event selection
    mmEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWEventCandSeq += CfgMgr.CutAlg("HWWMuMuFullEventExistsAlg", Cut = mmEventExistsString.rstrip(" || ") )
hWWlnulnu.Global.acceptAlgList.append("HWWMuMuFullEventExistsAlg")







# ====================================================================
# Build the electron-muon event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWSysTracker.containers( [ (hWWCommon.Electrons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Muons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.MET.finalCont,['','electron','muon','jet','met']),
                                          (hWWCommon.Electrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Muons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWlnulnu.Event.emEvent,['','electron','muon','jet','met'])
                                          ] )

emEventExistsString = ""
for inElectronContName, inMuonContName, inJetContName, inMETContName, \
    inOtherElectronContName, inOtherMuonContName, inOtherJetContName, \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWElMuFullEventBuilderAlg"+algNameSuffix

    # Replace the MET to the nominal one, if we are on a TrackMET-only systematic
    if any( sysSuffix in inMETContName for sysSuffix in hWWCommon.MET.p4JetTrkSysts ):
        inMETContName = hWWCommon.MET.finalCont
        pass

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
    hWWEventCandSeq += CfgMgr.HWW__FullEventBuilderAlg( algName,
                                                        #OutputLevel               = VERBOSE,
                                                        Lepton1Container          = inElectronContName,
                                                        CutLeadingLeptonPtMin     = hWWCommon.Electrons.cutLeadPtMin,
                                                        Lepton2Container          = inMuonContName,
                                                        JetContainer              = inJetContName,
                                                        MissingETContainer        = inMETContName,
                                                        MissingETObject           = hWWCommon.MET.inObject,
                                                        OtherElectronContainer    = inOtherElectronContName,
                                                        OtherMuonContainer        = inOtherMuonContName,
                                                        OtherJetContainer         = inOtherJetContName,
                                                        EventContainer            = outEventName,
                                                        WriteSplitOutputContainer = True
                                                        )

    # Add this algorithm to the list for event selection
    emEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWEventCandSeq += CfgMgr.CutAlg("HWWElMuFullEventExistsAlg", Cut = emEventExistsString.rstrip(" || ") )
hWWlnulnu.Global.acceptAlgList.append("HWWElMuFullEventExistsAlg")





# ====================================================================
# Build the muon-electron event candidates
# ====================================================================

# need to change the input container to take into account the sys
# Get the names of all needed containers
tmpEvtInOut = HWWSysTracker.containers( [ (hWWCommon.Muons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Electrons.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.MET.finalCont,['','electron','muon','jet','met']),
                                          (hWWCommon.Electrons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Muons.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWCommon.Jets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
                                          (hWWlnulnu.Event.meEvent,['','electron','muon','jet','met'])
                                          ] )

meEventExistsString = ""
for inLeadMuonContName, inElectronContName, inJetContName, inMETContName, \
    inOtherElectronContName, inOtherMuonContName, inOtherJetContName,     \
    outEventName in zip(*tmpEvtInOut):

    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = outEventName.replace("_","")
    algName = "HWWMuElFullEventBuilderAlg"+algNameSuffix

    # Replace the MET to the nominal one, if we are on a TrackMET-only systematic
    if any( sysSuffix in inMETContName for sysSuffix in hWWCommon.MET.p4JetTrkSysts ):
        inMETContName = hWWCommon.MET.finalCont
        pass

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
    hWWEventCandSeq += CfgMgr.HWW__FullEventBuilderAlg( algName,
                                                        #OutputLevel               = VERBOSE,
                                                        Lepton1Container          = inLeadMuonContName,
                                                        CutLeadingLeptonPtMin     = hWWCommon.Muons.cutLeadPtMin,
                                                        Lepton2Container          = inElectronContName,
                                                        JetContainer              = inJetContName,
                                                        MissingETContainer        = inMETContName,
                                                        MissingETObject           = hWWCommon.MET.inObject,
                                                        OtherElectronContainer    = inOtherElectronContName,
                                                        OtherMuonContainer        = inOtherMuonContName,
                                                        OtherJetContainer         = inOtherJetContName,
                                                        EventContainer            = outEventName,
                                                        WriteSplitOutputContainer = True
                                                        )

    # Add this algorithm to the list for event selection
    meEventExistsString += " count(%s.pt > -100.0*GeV) >= 1 || " % outEventName
    pass
# Schedule an event selection algorithm that says passEvent if at least one higgs cancidate was found.
# TODO: should we change this to exactly one higgs candidate being found?
hWWEventCandSeq += CfgMgr.CutAlg("HWWMuElFullEventExistsAlg", Cut = meEventExistsString.rstrip(" || ") )
hWWlnulnu.Global.acceptAlgList.append("HWWMuElFullEventExistsAlg")
