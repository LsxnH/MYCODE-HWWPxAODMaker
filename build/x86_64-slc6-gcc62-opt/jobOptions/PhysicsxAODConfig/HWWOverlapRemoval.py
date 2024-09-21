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
include.block("PhysicsxAODConfig/HWWOverlapRemoval.py")


# Print a status message
hWW_msg.info("Running overlap removal")



# Import the steering flags for this analysis
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon


# ====================================================================
# Get the OverlapRemovalTool
# ====================================================================
# Configure the final, full overlap removal tool using the helper module.
from AssociationUtils.config import recommended_tools
HWWORTool = recommended_tools("HWWOverlapRemovalTool",
                              #OutputLevel = VERBOSE,
                              #inputLabel  = "",
                              #RequireExpectedPointers = False,
                              bJetLabel  = hWWCommon.Jets.bJetLabel,
                              doEleEleOR = hWWCommon.Electrons.removeSelfOverlap,
                              doTaus     = False,
                              doPhotons  = False )
if hWWCommon.FatJets():
    hWW_msg.debug("Adding overlap removal specific for large-R jets")
    ToolSvc += CfgMgr.ORUtils__DeltaROverlapTool("HWWDeltaRFatJetOverlapTool",
                                                 #OutputLevel = VERBOSE,
                                                 DR = 1.0)
    HWWORTool.EleFatJetORT = ToolSvc.HWWDeltaRFatJetOverlapTool
    #HWWORTool.JetFatJetORT = ToolSvc.HWWDeltaRFatJetOverlapTool
    pass
# For trying to get back our small fake-muon rate
HWWORTool.MuJetORT.MuJetPtRatio    = 1e20
HWWORTool.MuJetORT.MuJetTrkPtRatio = 1e20
ToolSvc += HWWORTool




# -----------------------------------------------------------------------------
# Schedule the right set of overlap removals, depending on the provided flags
# -----------------------------------------------------------------------------

# Default setup

writeJetOverlaps       = [True]
overlapRemovalToolList = [ToolSvc.HWWOverlapRemovalTool]
overlapRemovalLabels   = ["overlaps"]

# Do additionally the one without removing muons near jets
if hWWCommon.Global.doORNoMuNearJetRemoval :
    # This instance of the overlap removal is not removing muons near jets
    HWWORToolNoMuNearJetRemoval = recommended_tools("HWWOverlapRemovalToolNoMuNearJetRemoval",
                                  #OutputLevel = VERBOSE,
                                  #inputLabel  = "",
                                  #RequireExpectedPointers = False,
                                  OutputLabel = "overlapsNoMuNearJetRemoval",
                                  bJetLabel   = hWWCommon.Jets.bJetLabel,
                                  doEleEleOR  = hWWCommon.Electrons.removeSelfOverlap,
                                  doTaus      = False,
                                  doPhotons   = False )
    # For trying to get back our small fake-muon rate
    HWWORToolNoMuNearJetRemoval.MuJetORT.MuJetPtRatio    = 1e20
    HWWORToolNoMuNearJetRemoval.MuJetORT.MuJetTrkPtRatio = 1e20
    HWWORToolNoMuNearJetRemoval.MuJetORT.OuterDR         = 0.0 # Don't remove muons near jets
    ToolSvc += HWWORToolNoMuNearJetRemoval
    # Now, extend the appropriate configuration lists
    writeJetOverlaps.append(False)
    overlapRemovalToolList.append(ToolSvc.HWWOverlapRemovalToolNoMuNearJetRemoval)
    overlapRemovalLabels.append("overlapsNoMuNearJetRemoval")
    pass

# Do additionally the one without removing muons near jets as well as giving
# precedence to leptons over b-jets
if hWWCommon.Global.doORNoMuNearJetRemovalNoBJetPrecedence :
    # This instance of the overlap removal is not removing muons near jets
    # and is not giving precedence to b-jets over leptons
    HWWORToolNoMuNearJetRemovalNoBJetPrecedence = recommended_tools("HWWOverlapRemovalToolNoMuNearJetRemovalNoBJetPrecedence",
                                  #OutputLevel = VERBOSE,
                                  #inputLabel  = "",
                                  #RequireExpectedPointers = False,
                                  #bJetLabel  = hWWCommon.Jets.bJetLabel,
                                  OutputLabel = "overlapsNoMuNearJetRemovalNoBJetPrecedence",
                                  doEleEleOR  = hWWCommon.Electrons.removeSelfOverlap,
                                  doTaus      = False,
                                  doPhotons   = False )
    # For trying to get back our small fake-muon rate
    HWWORToolNoMuNearJetRemovalNoBJetPrecedence.MuJetORT.MuJetPtRatio    = 1e20
    HWWORToolNoMuNearJetRemovalNoBJetPrecedence.MuJetORT.MuJetTrkPtRatio = 1e20
    HWWORToolNoMuNearJetRemovalNoBJetPrecedence.MuJetORT.OuterDR         = 0.0 # Don't remove muons near jets
    ToolSvc += HWWORToolNoMuNearJetRemovalNoBJetPrecedence

    # Now, extend the appropriate configuration lists
    writeJetOverlaps.append(False)
    overlapRemovalToolList.append(ToolSvc.HWWOverlapRemovalToolNoMuNearJetRemovalNoBJetPrecedence)
    overlapRemovalLabels.append("overlapsNoMuNearJetRemovalNoBJetPrecedence")
    pass






# ====================================================================
# --------------------------------------------------------------------
# =======        THIS IS FOR THE PRE-SELECTED OBJECTS!         =======
# --------------------------------------------------------------------
# ====================================================================

# ====================================================================
# Let's do the Overlap Removal. In the end we have the sorted view containers,
# selected according to the "overlaps" tag from the OverlapRemovalTool.
# ====================================================================
# Build all container lists in one go with the systematics tracker
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.Muons.calibPreSelCont,['','electronNOSUFFIX','muon','jetNOSUFFIX','fatjetNOSUFFIX']),
                                       (hWWCommon.Electrons.calibPreSelCont,['','electron','muonNOSUFFIX','jetNOSUFFIX','fatjetNOSUFFIX']),
                                       (hWWCommon.Jets.calibPreSelCont,['','electronNOSUFFIX','muonNOSUFFIX','jet','fatjetNOSUFFIX']),
                                       (hWWCommon.FatJets.calibPreSelCont,['','electronNOSUFFIX','muonNOSUFFIX','jetNOSUFFIX','fatjet']),
                                       (hWWCommon.Muons.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                       (hWWCommon.Electrons.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                       (hWWCommon.Jets.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                       (hWWCommon.FatJets.calibPreSelORCont,['','electron','muon','jet','fatjet'])
                                       ] )

for inMuonContName, inElectronContName, inJetContName, inFatJetContName,    \
    outMuonContName, outElectronContName, outJetContName, outFatJetContName \
    in zip(*tmpInOut) :

    systSuffixName = ""
    if inMuonContName.__contains__("___"):       systSuffixName = inMuonContName.split("___")[1]
    elif inElectronContName.__contains__("___"): systSuffixName = inElectronContName.split("___")[1]
    elif inJetContName.__contains__("___"):      systSuffixName = inJetContName.split("___")[1]
    elif inFatJetContName.__contains__("___"):   systSuffixName = inFatJetContName.split("___")[1]
    algNameSuffix = systSuffixName.replace("_","")
    algName = "HWWOverlapRemovalAlg"+algNameSuffix

    hWW_msg.debug("Building overlap removal algorithm with name %s:" % algName)
    hWW_msg.debug("    inMuonContName      = %s" % inMuonContName)
    hWW_msg.debug("    inElectronContName  = %s" % inElectronContName)
    hWW_msg.debug("    inJetContName       = %s" % inJetContName)
    hWW_msg.debug("    inFatJetContName    = %s" % inFatJetContName)
    hWW_msg.debug("    outMuonContName     = %s" % outMuonContName)
    hWW_msg.debug("    outElectronContName = %s" % outElectronContName)
    hWW_msg.debug("    outJetContName      = %s" % outJetContName)
    hWW_msg.debug("    outFatJetContName   = %s" % outFatJetContName)

    overlapRemovalAlg = CfgMgr.HWW__OverlapRemovalAlg( algName,
                                                       #OutputLevel            = VERBOSE,
                                                       OverlapRemovalToolList = overlapRemovalToolList,
                                                       OverlapRemovalLabels   = overlapRemovalLabels,
                                                       WriteJetOverlaps       = writeJetOverlaps,
                                                       InputElectrons         = inElectronContName,
                                                       InputMuons             = inMuonContName,
                                                       InputJets              = inJetContName,
                                                       TaggerName             = hWWCommon.Jets.bTagName,
                                                       OperatingPoint         = hWWCommon.Jets.bTagWPNumber,
                                                       PassBTaggingName       = hWWCommon.Jets.bJetLabel,
                                                       OutputElectrons        = outElectronContName,
                                                       OutputMuons            = outMuonContName,
                                                       OutputJets             = outJetContName
                                                       )
    if hWWCommon.FatJets():
        hWW_msg.debug("Adding large-R jets to overlap removal alg with name = %s" % algName)
        overlapRemovalAlg.InputFatJets  = inFatJetContName
        overlapRemovalAlg.OutputFatJets = outFatJetContName
        pass
    hWWCommonSeq += overlapRemovalAlg
    pass


# ====================================================================
# Add the already created post overlap removal sequence here to the hWWCommonSeq
# ====================================================================
hWWCommonSeq += hWWPostORSeq
