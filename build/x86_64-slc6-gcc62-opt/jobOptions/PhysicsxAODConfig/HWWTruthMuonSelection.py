# ====================================================================
# In this file, we will create our own sub-sequence that always runs
# through all its algorithms, irespective of the algorithm accepting
# an event or not.
# We will attach all the muon selection algorithms, including
# the creation of the final muon selection for the leading and sub-leading.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWTruthMuonSelection.py")


# ====================================================================
# Create instances of all needed muon tools and add them to the ToolService
# ====================================================================

# Create the instance of the muon selection tool
ToolSvc += CfgMgr.HWW__TruthElectronSelectionTool( "HWWTruthMuonPreSelectionTool",
                                                   #OutputLevel          = VERBOSE,
                                                   CutPtMin             = hWWCommon.TruthMuons.preSelection.cutPtMin,
                                                   CutAbsEtaMax         = hWWCommon.TruthMuons.preSelection.cutAbsEtaMax
                                                   )

# Create the instance of the muon selection tool
ToolSvc += CfgMgr.HWW__TruthElectronSelectionTool( "HWWTruthMuonSelectionTool",
                                                   #OutputLevel                = DEBUG,
                                                   CutPtMin                   = hWWCommon.TruthMuons.cutPtMin,
                                                   CutAbsEtaMax               = hWWCommon.TruthMuons.cutAbsEtaMax
                                                   )



# ====================================================================
# Build all containers with the final selection applied. These containers
# will be in SG::VIEW_ELEMENTS mode, i.e., only bare pointers to the
# selected objects. This is much faster compared to a deep copy and,
# contrary to a shallow copy container, allows for selection and sorting.
# These view containers will NOT be written out. Their only purpose is
# as input to the overlap removal and susequent composite particle building.
# ====================================================================


# Get the names of all input and output containers
tmpInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthMuons.calibCont,['','muon']),
                                            (hWWCommon.TruthMuons.calibPreSelCont,['','muon']),
                                            (hWWCommon.TruthMuons.preORAllPtSortCont,['','muon']) ] )

# Create one selection algorithm instance for each pair
for inContName, preSelContName, outContName in zip(*tmpInOut) :
    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = inContName.replace("_","")
    hWW_msg.debug("Building muon selection algorithm with inContName=%s, preSelContName=%s, outContName=%s" % (inContName,preSelContName,outContName))

    # Enable the muon cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    if inContName.__contains__("___"): doCutFlow = False
    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWTruthPreORSeq += CfgMgr.ParticleSelectionAlg( "HWWTruthMuonPreSelectionAlg"+algNameSuffix,
                                                     #OutputLevel             = DEBUG,
                                                     InputContainer          = inContName,
                                                     OutputContainer         = preSelContName,
                                                     SelectionToolList = [ ToolSvc.HWWTruthMuonPreSelectionTool ],
                                                     DoCutBookkeeping        = doCutFlow,
                                                     CutBookkeeperContainer  = "HWWTruthMuonPreSelectionCutFlow"
                                                     )

    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWTruthPreORSeq += CfgMgr.ParticleSelectionAlg( "HWWTruthMuonSelectionAlg"+algNameSuffix,
                                                     #OutputLevel             = DEBUG,
                                                     InputContainer          = preSelContName,
                                                     OutputContainer         = outContName,
                                                     SelectionToolList = [ ToolSvc.HWWTruthMuonSelectionTool ],
                                                     DoCutBookkeeping        = doCutFlow,
                                                     CutBookkeeperContainer  = "HWWTruthMuonSelectionCutFlow"
                                                     )

    # Do the pt sorting in decending order. This needs to be done BEFORE the overlap removal runs.
    hWWTruthPreORSeq += CfgMgr.ParticleSortingAlg( "HWWTruthMuonSortingAlg"+algNameSuffix,
                                                   #OutputLevel   = VERBOSE,
                                                   InputContainer  = outContName
                                                   )
    pass



# ====================================================================
# Now we select the leading muon view container with the containers
# selected after Overlap Removal
# ====================================================================

# Build all container lists in one go with the systematics tracker
tmpInOutLead = HWWTruthSysTracker.containers( [ (hWWCommon.TruthMuons.finalAllPtSortCont,['','electron','muon','jet']),
                                                (hWWCommon.TruthMuons.finalLeadPtSortCont,['','electron','muon','jet']) ] )

for inMuonContName, outLeadMuonContName in zip(*tmpInOutLead) :

    systSuffixName = ""
    if inMuonContName.__contains__("___"): systSuffixName = inMuonContName.split("___")[1]
    algNameSuffix = systSuffixName.replace("_","")

    hWW_msg.debug("Building sub-leading muon containers after overlap removal algorithm with (input,output):")
    hWW_msg.debug("    inMuonContName=%s, outLeadMuonContName=%s" % (inMuonContName,outLeadMuonContName))
    hWW_msg.debug("    systSuffixName=%s" % (systSuffixName))
    hWW_msg.debug("    algNameSuffix=%s" % (algNameSuffix))

    # Do the final pt selection for the leading muons
    hWWTruthCommonSeq += CfgMgr.ParticleSelectionAlg( "HWWLeadTruthMuonSelectionAlg"+algNameSuffix,
                                                      #OutputLevel     = VERBOSE,
                                                      InputContainer  = inMuonContName,
                                                      OutputContainer = outLeadMuonContName,
                                                      Selection       = inMuonContName + ".pt > %s" % hWWCommon.TruthMuons.cutLeadPtMin
                                                      )
    pass

# =============================================================================
# Build the final particle containers.
# Note that also the view containers that have the selected particles will be
# re-mapped to point to the final particle containers (or their shallow copies)
# and not any more to the original calibrated containers (or their shallow copies).
# =============================================================================

import itertools

# Make one long list all all muon view containers that point to selected muons
tmpMuonViewContainersListList = HWWTruthSysTracker.containers( [ (hWWCommon.TruthMuons.finalLeadPtSortCont,['','electron','muon','jet']),
                                                                 (hWWCommon.TruthMuons.finalAllPtSortCont,['','electron','muon','jet']),
                                                                 (hWWCommon.TruthMuons.calibPreSelORCont,['','electron','muon','jet']),
                                                                 ] )
listAllMuonViewContainers = list(itertools.chain.from_iterable(tmpMuonViewContainersListList))
# Build now the final muon container(s)
hWWTruthCommonSeq += CfgMgr.ParticleRemoverAlg( "HWWlnulnuTruthMuonContainerBuilderAlg",
                                                #OutputLevel            = VERBOSE,
                                                Input                  = hWWCommon.TruthMuons.calibCont,
                                                Output                 = hWWCommon.TruthMuons.finalCont,
                                                Suffixes               = hWWCommon.TruthMuons.p4Systs,
                                                SelectedViewContainers = listAllMuonViewContainers
                                                )
