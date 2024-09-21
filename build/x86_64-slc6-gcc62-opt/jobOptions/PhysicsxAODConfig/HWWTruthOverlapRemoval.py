# ====================================================================
# Here we perform the Overlap Removal on the sorted electron. muon, and jet view
# container. Also, afterwards the leading lepton view container are generated.
# For now, we chose the logic of generating one view container for every systematic
# variation, even if this systematic is not related to the object type. This makes
# using the OverlapRemovalTool pretty straight forward but a LOT of "redundant" view
# containers and shallow copy containers (the latter we may actually be able to reduce).
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWTruthOverlapRemoval.py")


# ====================================================================
# Get the OverlapRemovalTool
# ====================================================================
# ToolSvc += CfgMgr.OverlapRemovalTool( "HWWTruthOverlapRemovalTool", InputLabel = "" )


# ====================================================================
# --------------------------------------------------------------------
# =======      THIS IS FOR THE FINALLY SELECTED OBJECTS!       =======
# --------------------------------------------------------------------
# ====================================================================

# ====================================================================
# Let's do the Overlap Removal. In the end we have the sorted view containers,
# selected according to the "overlaps" tag from the OverlapRemovalTool.
# ====================================================================
# Build all container lists in one go with the systematics tracker
tmpInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthMuons.preORAllPtSortCont,['','electronNOSUFFIX','muon','jetNOSUFFIX']),
                                            (hWWCommon.TruthElectrons.preORAllPtSortCont,['','electron','muonNOSUFFIX','jetNOSUFFIX']),
                                            (hWWCommon.TruthJets.preORAllPtSortCont,['','electronNOSUFFIX','muonNOSUFFIX','jet']),
                                            (hWWCommon.TruthMuons.finalAllPtSortCont,['','electron','muon','jet']),
                                            (hWWCommon.TruthElectrons.finalAllPtSortCont,['','electron','muon','jet']),
                                            (hWWCommon.TruthJets.finalAllPtSortCont,['','electron','muon','jet'])
                                            ] )

for inMuonContName, inElectronContName, inJetContName,   \
    outMuonContName, outElectronContName, outJetContName \
    in zip(*tmpInOut) :

    systSuffixName = ""
    if inMuonContName.__contains__("___"):       systSuffixName = inMuonContName.split("___")[1]
    elif inElectronContName.__contains__("___"): systSuffixName = inElectronContName.split("___")[1]
    elif inJetContName.__contains__("___"):      systSuffixName = inJetContName.split("___")[1]
    algNameSuffix = systSuffixName.replace("_","")
    algName = "HWWTruthOverlapRemovalAlg"+algNameSuffix

    hWW_msg.debug("Building overlap removal algorithm with name %s:" % algName)
    hWW_msg.debug("    inMuonContName      = %s" % inMuonContName)
    hWW_msg.debug("    inElectronContName  = %s" % inElectronContName)
    hWW_msg.debug("    inJetContName       = %s" % inJetContName)
    hWW_msg.debug("    outMuonContName     = %s" % outMuonContName)
    hWW_msg.debug("    outElectronContName = %s" % outElectronContName)
    hWW_msg.debug("    outJetContName      = %s" % outJetContName)

    hWWTruthCommonSeq += CfgMgr.HWW__TruthOverlapRemovalAlg( algName,
                                                             #OutputLevel        = DEBUG,
                                                             SelectedElectrons  = inElectronContName,
                                                             SelectedMuons      = inMuonContName,
                                                             SelectedJets       = inJetContName,
                                                             ORElectrons        = outElectronContName,
                                                             ORMuons            = outMuonContName,
                                                             ORJets             = outJetContName
                                                             )

    pass






# ====================================================================
# --------------------------------------------------------------------
# ======= THIS IS FOR THE CALIBRATED AND PRE-SELECTED OBJECTS! =======
# --------------------------------------------------------------------
# ====================================================================

# ====================================================================
# Let's do the Overlap Removal. In the end we have the sorted view containers,
# selected according to the "overlaps" tag from the OverlapRemovalTool.
#
# ====================================================================
# First, we only remove overlaps between electrons and muons:
# ====================================================================
# Build all container lists in one go with the systematics tracker
tmpInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthMuons.calibPreSelCont,['','electronNOSUFFIX','muon','jetNOSUFFIX']),
                                            (hWWCommon.TruthElectrons.calibPreSelCont,['','electron','muonNOSUFFIX','jetNOSUFFIX']),
                                            (hWWCommon.TruthJets.calibPreSelCont,['','electronNOSUFFIX','muonNOSUFFIX','jet']),
                                            (hWWCommon.TruthMuons.calibPreSelORCont,['','electron','muon','jet']),
                                            (hWWCommon.TruthElectrons.calibPreSelORCont,['','electron','muon','jet'])
                                            ] )

for inMuonContName, inElectronContName, inJetContName, outMuonContName, outElectronContName in zip(*tmpInOut) :

    systSuffixName = ""
    if inMuonContName.__contains__("___"):       systSuffixName = inMuonContName.split("___")[1]
    elif inElectronContName.__contains__("___"): systSuffixName = inElectronContName.split("___")[1]
    elif inJetContName.__contains__("___"):      systSuffixName = inJetContName.split("___")[1]
    algNameSuffix = systSuffixName.replace("_","")
    algName = "HWWCalibPreSelLeptonTruthOverlapRemovalAlg"+algNameSuffix

    hWW_msg.debug("Building overlap removal algorithm with name %s:" % algName)
    hWW_msg.debug("    inMuonContName      = %s" % inMuonContName)
    hWW_msg.debug("    inElectronContName  = %s" % inElectronContName)
    hWW_msg.debug("    outMuonContName     = %s" % outMuonContName)
    hWW_msg.debug("    outElectronContName = %s" % outElectronContName)

    hWWTruthCommonSeq += CfgMgr.HWW__TruthOverlapRemovalAlg( algName,
                                                             #OutputLevel        = DEBUG,
                                                             SelectedElectrons  = inElectronContName,
                                                             SelectedMuons      = inMuonContName,
                                                             ORElectrons        = outElectronContName,
                                                             ORMuons            = outMuonContName
                                                             )

    pass



# ====================================================================
# Second, we only remove overlaps between the final leptons and the pre-selected jets.
# The resulting lepton containers will be discarded.
# ====================================================================
# Build all container lists in one go with the systematics tracker
tmpInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthMuons.preORAllPtSortCont,['','electronNOSUFFIX','muon','jetNOSUFFIX']),
                                            (hWWCommon.TruthElectrons.preORAllPtSortCont,['','electron','muonNOSUFFIX','jetNOSUFFIX']),
                                            (hWWCommon.TruthJets.calibPreSelCont,['','electronNOSUFFIX','muonNOSUFFIX','jet']),
                                            ("TmpMuonsORFinal",['','electron','muon','jet']),
                                            ("TmpElectronsORFinal",['','electron','muon','jet']),
                                            (hWWCommon.TruthJets.calibPreSelORCont,['','electron','muon','jet'])
                                            ] )

for inMuonContName, inElectronContName, inJetContName,   \
    outMuonContName, outElectronContName, outJetContName \
    in zip(*tmpInOut) :

    systSuffixName = ""
    if inMuonContName.__contains__("___"):       systSuffixName = inMuonContName.split("___")[1]
    elif inElectronContName.__contains__("___"): systSuffixName = inElectronContName.split("___")[1]
    elif inJetContName.__contains__("___"):      systSuffixName = inJetContName.split("___")[1]
    algNameSuffix = systSuffixName.replace("_","")
    algName = "HWWCalibPreSelJetTruthOverlapRemovalAlg"+algNameSuffix

    hWW_msg.debug("Building overlap removal algorithm with name %s:" % algName)
    hWW_msg.debug("    inMuonContName      = %s" % inMuonContName)
    hWW_msg.debug("    inElectronContName  = %s" % inElectronContName)
    hWW_msg.debug("    inJetContName       = %s" % inJetContName)
    hWW_msg.debug("    outMuonContName     = %s" % outMuonContName)
    hWW_msg.debug("    outElectronContName = %s" % outElectronContName)
    hWW_msg.debug("    outJetContName      = %s" % outJetContName)

    hWWTruthCommonSeq += CfgMgr.HWW__TruthOverlapRemovalAlg( algName,
                                                             #OutputLevel        = DEBUG,
                                                             SelectedElectrons  = inElectronContName,
                                                             SelectedMuons      = inMuonContName,
                                                             SelectedJets       = inJetContName,
                                                             ORElectrons        = outElectronContName,
                                                             ORMuons            = outMuonContName,
                                                             ORJets             = outJetContName
                                                             )

    pass
