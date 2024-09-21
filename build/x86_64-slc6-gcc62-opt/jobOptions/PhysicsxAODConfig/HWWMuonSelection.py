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
include.block("PhysicsxAODConfig/HWWMuonSelection.py")


# ====================================================================
# Create instances of all needed muon tools and add them to the ToolService
# ====================================================================

# Create the instance of the muon selection tool
ToolSvc += CfgMgr.HWW__MuonSelectionTool( "HWWMuonPreSelectionTool",
                                          #OutputLevel          = DEBUG,
                                          CutPtMin             = hWWCommon.Muons.preSelection.cutPtMin,
                                          CutAbsEtaMax         = hWWCommon.Muons.preSelection.cutAbsEtaMax,
                                          CutIDList            = hWWCommon.Muons.preSelection.cutIDList,
                                          CutIDPtMinList       = hWWCommon.Muons.preSelection.cutIDPtMinList,
                                          CutInnerDetectorHits = hWWCommon.Muons.preSelection.cutInnerDetectorHits,
                                          CutD0SignificanceMax = hWWCommon.Muons.preSelection.cutD0SignificanceMax,
                                          CutZ0SinThetaMax     = hWWCommon.Muons.preSelection.cutZ0SinThetaMax
                                          )

# Create the instance of the muon selection tool
ToolSvc += CfgMgr.HWW__MuonSelectionTool( "HWWMuonSelectionTool",
                                          OutputLevel                = INFO,
                                          CutPtMin                   = hWWCommon.Muons.cutPtMin,
                                          CutAbsEtaMax               = hWWCommon.Muons.cutAbsEtaMax,
                                          CutIDList                  = hWWCommon.Muons.cutIDList,
                                          CutIDPtMinList             = hWWCommon.Muons.cutIDPtMinList,
                                          CutInnerDetectorHits       = hWWCommon.Muons.cutInnerDetectorHits,
                                          CutD0SignificanceMax       = hWWCommon.Muons.cutD0SignificanceMax,
                                          CutZ0SinThetaMax           = hWWCommon.Muons.cutZ0SinThetaMax
                                          )



# ====================================================================
# Build all containers with the pre-selection applied. These containers
# will be in SG::VIEW_ELEMENTS mode, i.e., only bare pointers to the
# selected objects. This is much faster compared to a deep copy and,
# contrary to a shallow copy container, allows for selection and sorting.
# These view containers will NOT be written out. Their only purpose is
# as input to the overlap removal and susequent composite particle building.
# ====================================================================


# Get the names of all input and output containers
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.Muons.calibCont,['','muon']),
                                       (hWWCommon.Muons.calibPreSelCont,['','muon']) ] )

# Create one selection algorithm instance for each pair
for inContName, preSelContName in zip(*tmpInOut) :
    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = inContName.replace("_","")
    hWW_msg.debug("Building muon selection algorithm with inContName=%s, preSelContName=%s" % (inContName,preSelContName))

    # Enable the muon cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    if inContName.__contains__("___"): doCutFlow = False
    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWPreORSeq += CfgMgr.ParticleSelectionAlg("HWWMuonPreSelectionAlg"+algNameSuffix,
                                               OutputLevel             = INFO,
                                               InputContainer          = inContName,
                                               OutputContainer         = preSelContName,
                                               SelectionWithPVToolList = [ ToolSvc.HWWMuonPreSelectionTool ],
                                               DoCutBookkeeping        = doCutFlow,
                                               CutBookkeeperContainer  = "HWWMuonPreSelectionCutFlow"
                                               )

    # Do the pt sorting in decending order. This needs to be done BEFORE the overlap removal runs.
    hWWPreORSeq += CfgMgr.ParticleSortingAlg( "HWWMuonSortingAlg"+algNameSuffix,
                                              #OutputLevel   = VERBOSE,
                                              InputContainer  = preSelContName
                                              )
    pass



# ====================================================================
# Now we select the final muon view container with the containers
# selected after Overlap Removal
# ====================================================================

# Build all container lists in one go with the systematics tracker
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.Muons.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                       (hWWCommon.Muons.finalAllPtSortCont,['','electron','muon','jet','fatjet']) ] )

for calibPreSelORCont, outMuonContName in zip(*tmpInOut) :
    algNameSuffix = calibPreSelORCont.replace("_","")
    hWW_msg.debug("Building final muon containers after overlap removal algorithm with:")
    hWW_msg.debug("    calibPreSelORCont = %s" % (calibPreSelORCont))
    hWW_msg.debug("    outMuonContName   = %s" % (outMuonContName))
    hWW_msg.debug("    algNameSuffix     = %s" % (algNameSuffix))

    # Enable the muon cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    if calibPreSelORCont.__contains__("___"): doCutFlow = False
    # Do the final selection. This needs to be done AFTER the overlap removal runs.
    hWWCommonSeq += CfgMgr.ParticleSelectionAlg("HWWMuonSelectionAlg"+algNameSuffix,
                                                OutputLevel             = INFO,
                                                InputContainer          = calibPreSelORCont,
                                                OutputContainer         = outMuonContName,
                                                SelectionWithPVToolList = [ ToolSvc.HWWMuonSelectionTool ],
                                                DoCutBookkeeping        = doCutFlow,
                                                CutBookkeeperContainer  = "HWWMuonSelectionCutFlow"
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
tmpMuonViewContainersListList = HWWSysTracker.containers( [ (hWWCommon.Muons.finalAllPtSortCont,['','electron','muon','jet','fatjet']),
                                                            (hWWCommon.Muons.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                                            ] )
listAllMuonViewContainers = list(itertools.chain.from_iterable(tmpMuonViewContainersListList))
# Build now the final muon container(s)
hWWCommonSeq += CfgMgr.ParticleRemoverAlg("HWWMuonContainerBuilderAlg",
                                          #OutputLevel            = VERBOSE,
                                          Input                  = hWWCommon.Muons.calibCont,
                                          Output                 = hWWCommon.Muons.finalCont,
                                          Suffixes               = hWWCommon.Muons.p4Systs,
                                          SelectedViewContainers = listAllMuonViewContainers
                                          )
