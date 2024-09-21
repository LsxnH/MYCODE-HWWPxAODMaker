# ====================================================================
# In this file, we will create our own sub-sequence that always runs
# through all its algorithms, irespective of the algorithm accepting
# an event or not.
# We will attach all the electron selection algorithms, including
# the creation of the final electron selection for the leading and sub-leading.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWElectronSelection.py")


# ====================================================================
# Create instances of all needed electron tools and add them to the ToolService
# ====================================================================

# Create the instance of the electron pre-selection tool
ToolSvc += CfgMgr.HWW__ElectronSelectionTool ( "HWWElectronPreSelectionTool",
                                               #OutputLevel = DEBUG,
                                               CutObjectQualityMask = hWWCommon.Electrons.preSelection.cutObjectQualityMask,
                                               CutPtMin             = hWWCommon.Electrons.preSelection.cutPtMin,
                                               CutAbsEtaMax         = hWWCommon.Electrons.preSelection.cutAbsEtaMax,
                                               CutIDList            = hWWCommon.Electrons.preSelection.cutIDList,
                                               CutIDPtMinList       = hWWCommon.Electrons.preSelection.cutIDPtMinList,
                                               CutD0SignificanceMax = hWWCommon.Electrons.preSelection.cutD0SignificanceMax,
                                               CutZ0SinThetaMax     = hWWCommon.Electrons.preSelection.cutZ0SinThetaMax
                                               )

# Create the instance of the electron selection tool for the electron
ToolSvc += CfgMgr.HWW__ElectronSelectionTool ( "HWWElectronSelectionTool",
                                               OutputLevel = INFO,
                                               CutObjectQualityMask       = hWWCommon.Electrons.cutObjectQualityMask,
                                               CutPtMin                   = hWWCommon.Electrons.cutPtMin,
                                               CutAbsEtaMax               = hWWCommon.Electrons.cutAbsEtaMax,
                                               CutAbsEtaCrackMin          = hWWCommon.Electrons.cutAbsEtaCrackMin,
                                               CutAbsEtaCrackMax          = hWWCommon.Electrons.cutAbsEtaCrackMax,
                                               CutIDList                  = hWWCommon.Electrons.cutIDList,
                                               CutIDPtMinList             = hWWCommon.Electrons.cutIDPtMinList,
                                               CutD0SignificanceMax       = hWWCommon.Electrons.cutD0SignificanceMax,
                                               CutZ0SinThetaMax           = hWWCommon.Electrons.cutZ0SinThetaMax
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
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.Electrons.calibCont,['','electron']),
                                       (hWWCommon.Electrons.calibPreSelCont,['','electron']) ] )

# Create one selection algorithm instance for each pair
for inContName, preSelContName in zip(*tmpInOut) :
    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = inContName.replace("_","")
    hWW_msg.debug("Building electron selection algorithm with inContName=%s, preSelContName=%s" % (inContName,preSelContName))

    # Enable the electron cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    if inContName.__contains__("___"): doCutFlow = False
    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWPreORSeq += CfgMgr.ParticleSelectionAlg("HWWElectronPreSelectionAlg"+algNameSuffix,
                                               OutputLevel             = INFO,
                                               InputContainer          = inContName,
                                               OutputContainer         = preSelContName,
                                               SelectionWithPVToolList = [ ToolSvc.HWWElectronPreSelectionTool ],
                                               DoCutBookkeeping        = doCutFlow,
                                               CutBookkeeperContainer  = "HWWElectronPreSelectionCutFlow"
                                               )

    # Do the pt sorting in decending order. This needs to be done BEFORE the overlap removal runs.
    hWWPreORSeq += CfgMgr.ParticleSortingAlg( "HWWElectronSortingAlg"+algNameSuffix,
                                              #OutputLevel   = VERBOSE,
                                              InputContainer  = preSelContName
                                              )
    pass




# ====================================================================
# Now we select the final electron view containers with the containers
# selected after Overlap Removal
# ====================================================================

# Build all container lists in one go with the systematics tracker
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.Electrons.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                       (hWWCommon.Electrons.finalAllPtSortCont,['','electron','muon','jet','fatjet'])
                                       ] )

for calibPreSelORCont, outElectronContName in zip(*tmpInOut) :
    algNameSuffix = calibPreSelORCont.replace("_","")
    hWW_msg.debug("Building final-selected electron containers after overlap removal algorithm with:")
    hWW_msg.debug("    calibPreSelORCont   = %s" % (calibPreSelORCont))
    hWW_msg.debug("    outElectronContName = %s" % (outElectronContName))
    hWW_msg.debug("    algNameSuffix       = %s" % (algNameSuffix))

    # Enable the electron cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    if calibPreSelORCont.__contains__("___"): doCutFlow = False
    # Do the final selection. This is done AFTER overlap removal
    hWWCommonSeq += CfgMgr.ParticleSelectionAlg("HWWElectronSelectionAlg"+algNameSuffix,
                                                #OutputLevel             = VERBOSE,
                                                InputContainer          = calibPreSelORCont,
                                                OutputContainer         = outElectronContName,
                                                SelectionWithPVToolList = [ ToolSvc.HWWElectronSelectionTool ],
                                                DoCutBookkeeping        = doCutFlow,
                                                CutBookkeeperContainer  = "HWWElectronSelectionCutFlow"
                                                )
    pass



# =============================================================================
# Build the final particle containers.
# Note that also the view containers that have the selected particles will be
# re-mapped to point to the final particle containers (or their shallow copies)
# and not any more to the original calibrated containers (or their shallow copies).
# =============================================================================

import itertools

# Make one long list all all electron view containers that point to selected muons
tmpElectronViewContainersListList = HWWSysTracker.containers( [ (hWWCommon.Electrons.finalAllPtSortCont,['','electron','muon','jet','fatjet']),
                                                                (hWWCommon.Electrons.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                                                ] )
listAllElectronViewContainers = list(itertools.chain.from_iterable(tmpElectronViewContainersListList))
# Build now the final electron container(s)
hWWCommonSeq += CfgMgr.ParticleRemoverAlg("HWWElectronContainerBuilderAlg",
                                          #OutputLevel            = VERBOSE,
                                          Input                  = hWWCommon.Electrons.calibCont,
                                          Output                 = hWWCommon.Electrons.finalCont,
                                          Suffixes               = hWWCommon.Electrons.p4Systs,
                                          SelectedViewContainers = listAllElectronViewContainers
                                          )
