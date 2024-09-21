# ====================================================================
# In this file, we will create our own sub-sequence that always runs
# through all its algorithms, irespective of the algorithm accepting
# an event or not.
# We will attach all the jet selection algorithms,  including
# the creation of the final jet selection.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWJetSelection.py")


# ====================================================================
# Create instances of all needed jet tools and add them to the ToolService
# ====================================================================

# Create the instance of the jet pre-selection tool
ToolSvc += CfgMgr.HWW__JetSelectionTool( "HWWJetPreSelectionTool",
                                         OutputLevel        = INFO,
                                         CutPtMinList       = hWWCommon.Jets.preSelection.cutPtMinList,
                                         CutAbsEtaMaxList   = hWWCommon.Jets.preSelection.cutAbsEtaMaxList,
                                         UpdateJVTName      = hWWCommon.Jets.updateJVTName,
                                         PassJVTName        = hWWCommon.Jets.passJVTVarName,
                                         PassForwardJVTName = hWWCommon.Jets.preSelection.passForwardJVTVarName
                                         )


# Create the instance of the jet selection tool
ToolSvc += CfgMgr.HWW__JetSelectionTool( "HWWJetSelectionTool",
                                         OutputLevel       = INFO,
                                         CutPtMinList      = hWWCommon.Jets.cutPtMinList,
                                         CutAbsEtaMaxList  = hWWCommon.Jets.cutAbsEtaMaxList
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
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.Jets.calibCont,['','jet']),
                                       (hWWCommon.Jets.calibPreSelCont,['','jet']) ] )

# Create one selection algorithm instance for each pair
for inContName, preSelContName in zip(*tmpInOut) :
    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = inContName.replace("_","")
    hWW_msg.debug("Building jet selection algorithm with:")
    hWW_msg.debug("    inContName     = %s" % (inContName))
    hWW_msg.debug("    preSelContName = %s" % (preSelContName))
    hWW_msg.debug("    algNameSuffix  = %s" % (algNameSuffix))

    # Enable the jet cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    if inContName.__contains__("___"): doCutFlow = False
    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWPreORSeq += CfgMgr.ParticleSelectionAlg("HWWJetPreSelectionAlg"+algNameSuffix,
                                               #OutputLevel             = VERBOSE,
                                               InputContainer          = inContName,
                                               OutputContainer         = preSelContName,
                                               SelectionWithPVToolList = [ ToolSvc.HWWJetPreSelectionTool ],
                                               DoCutBookkeeping        = doCutFlow,
                                               CutBookkeeperContainer  = "HWWJetPreSelectionCutFlow"
                                               )
    # Do the pt sorting in decending order. This needs to be done BEFORE the overlap removal runs.
    hWWPreORSeq += CfgMgr.ParticleSortingAlg( "HWWJetSortingAlg"+algNameSuffix,
                                              # OutputLevel   = VERBOSE,
                                              InputContainer  = preSelContName
                                              )
    pass





# ====================================================================
# Now we select the final jet view containers with the containers
# selected after Overlap Removal
# ====================================================================

# Build all container lists in one go with the systematics tracker
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.Jets.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                       (hWWCommon.Jets.finalAllPtSortCont,['','electron','muon','jet','fatjet'])
                                       ] )

for calibPreSelORCont, outJetContName in zip(*tmpInOut) :
    algNameSuffix = calibPreSelORCont.replace("_","")
    hWW_msg.debug("Building final-selected jet containers after overlap removal algorithm with:")
    hWW_msg.debug("    calibPreSelORCont = %s" % (calibPreSelORCont))
    hWW_msg.debug("    outJetContName    = %s" % (outJetContName))
    hWW_msg.debug("    algNameSuffix     = %s" % (algNameSuffix))

    # Do the final selection. This needs to be done AFTER the overlap removal runs.
    hWWCommonSeq += CfgMgr.ParticleSelectionAlg("HWWJetSelectionAlg"+algNameSuffix,
                                                OutputLevel             = INFO,
                                                InputContainer          = calibPreSelORCont,
                                                OutputContainer         = outJetContName,
                                                SelectionWithPVToolList = [ ToolSvc.HWWJetSelectionTool ],
                                                DoCutBookkeeping        = doCutFlow,
                                                CutBookkeeperContainer  = "HWWJetSelectionCutFlow"
                                                )
pass



# =============================================================================
# Build the final particle containers.
# Note that also the view containers that have the selected particles will be
# re-mapped to point to the final particle containers (or their shallow copies)
# and not any more to the original calibrated containers (or their shallow copies).
# =============================================================================

import itertools

# Make one long list all all jet view containers that point to selected jets
tmpJetViewContainersListList = HWWSysTracker.containers( [ (hWWCommon.Jets.finalAllPtSortCont,['','electron','muon','jet','fatjet']),
                                                           (hWWCommon.Jets.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                                           ] )
listAllJetViewContainers = list(itertools.chain.from_iterable(tmpJetViewContainersListList))
hWW_msg.debug("List of all jet view containers: %s" % (listAllJetViewContainers))
# Build now the final jet container(s)
hWWCommonSeq += CfgMgr.ParticleRemoverAlg("HWWJetContainerBuilderAlg",
                                          #OutputLevel            = VERBOSE,
                                          Input                  = hWWCommon.Jets.calibCont,
                                          Output                 = hWWCommon.Jets.finalCont,
                                          Suffixes               = hWWCommon.Jets.p4Systs,
                                          SelectedViewContainers = listAllJetViewContainers
                                          )
