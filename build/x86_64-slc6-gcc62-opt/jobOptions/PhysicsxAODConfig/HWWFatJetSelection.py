# ====================================================================
# In this file, we will create our own sub-sequence that always runs
# through all its algorithms, irespective of the algorithm accepting
# an event or not.
# We will attach all the jet selection algorithms,  including
# the creation of the final large-R jet selection.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWFatJetSelection.py")


# ====================================================================
# Create instances of all needed large-R jet tools and add them to the ToolService
# ====================================================================

# Create the instance of the large-R jet pre-selection tool
ToolSvc += CfgMgr.HWW__JetSelectionTool( "HWWFatJetPreSelectionTool",
                                         OutputLevel       = INFO,
                                         CutPtMinList      = hWWCommon.FatJets.preSelection.cutPtMinList,
                                         CutAbsEtaMaxList  = hWWCommon.FatJets.preSelection.cutAbsEtaMaxList,
                                         )


# Create the instance of the large-R jet selection tool
ToolSvc += CfgMgr.HWW__JetSelectionTool( "HWWFatJetSelectionTool",
                                         OutputLevel       = INFO,
                                         CutPtMinList      = hWWCommon.FatJets.cutPtMinList,
                                         CutAbsEtaMaxList  = hWWCommon.FatJets.cutAbsEtaMaxList,
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
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.FatJets.calibCont,['','fatjet']),
                                       (hWWCommon.FatJets.calibPreSelCont,['','fatjet']) ] )

# Create one selection algorithm instance for each pair
for inContName, preSelContName in zip(*tmpInOut) :
    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = inContName.replace("_","")
    hWW_msg.debug("Building large-R jet selection algorithm with:")
    hWW_msg.debug("    inContName     = %s" % (inContName))
    hWW_msg.debug("    preSelContName = %s" % (preSelContName))
    hWW_msg.debug("    algNameSuffix  = %s" % (algNameSuffix))

    # Enable the jet cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    if inContName.__contains__("___"): doCutFlow = False
    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWPreORSeq += CfgMgr.ParticleSelectionAlg("HWWFatJetPreSelectionAlg"+algNameSuffix,
                                               OutputLevel             = INFO,
                                               InputContainer          = inContName,
                                               OutputContainer         = preSelContName,
                                               SelectionWithPVToolList = [ ToolSvc.HWWFatJetPreSelectionTool ],
                                               DoCutBookkeeping        = doCutFlow,
                                               CutBookkeeperContainer  = "HWWFatJetPreSelectionCutFlow"
                                               )
    # Do the pt sorting in decending order. This needs to be done BEFORE the overlap removal runs.
    hWWPreORSeq += CfgMgr.ParticleSortingAlg( "HWWFatJetSortingAlg"+algNameSuffix,
                                              # OutputLevel   = VERBOSE,
                                              InputContainer  = preSelContName
                                              )
    pass





# ====================================================================
# Now we select the final large-R jet view containers with the containers
# selected after Overlap Removal
# ====================================================================

# Build all container lists in one go with the systematics tracker
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.FatJets.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                       (hWWCommon.FatJets.finalAllPtSortCont,['','electron','muon','jet','fatjet'])
                                       ] )

for calibPreSelORCont, outJetContName in zip(*tmpInOut) :
    algNameSuffix = calibPreSelORCont.replace("_","")
    hWW_msg.debug("Building final-selected large-R jet containers after overlap removal algorithm with:")
    hWW_msg.debug("    calibPreSelORCont = %s" % (calibPreSelORCont))
    hWW_msg.debug("    outJetContName    = %s" % (outJetContName))
    hWW_msg.debug("    algNameSuffix     = %s" % (algNameSuffix))

    # Enable the jet cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    if calibPreSelORCont.__contains__("___"): doCutFlow = False
    # Do the final selection. This needs to be done AFTER the overlap removal runs.
    hWWCommonSeq += CfgMgr.ParticleSelectionAlg("HWWFatJetSelectionAlg"+algNameSuffix,
                                                OutputLevel             = INFO,
                                                InputContainer          = calibPreSelORCont,
                                                OutputContainer         = outJetContName,
                                                SelectionWithPVToolList = [ ToolSvc.HWWFatJetSelectionTool ],
                                                DoCutBookkeeping        = doCutFlow,
                                                CutBookkeeperContainer  = "HWWFatJetSelectionCutFlow"
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
tmpJetViewContainersListList = HWWSysTracker.containers( [ (hWWCommon.FatJets.finalAllPtSortCont,['','electron','muon','jet','fatjet']),
                                                           (hWWCommon.FatJets.calibPreSelORCont,['','electron','muon','jet','fatjet']),
                                                           ] )
listAllJetViewContainers = list(itertools.chain.from_iterable(tmpJetViewContainersListList))
# Build now the final jet container(s)
hWWCommonSeq += CfgMgr.ParticleRemoverAlg("HWWFatJetContainerBuilderAlg",
                                          #OutputLevel            = VERBOSE,
                                          Input                  = hWWCommon.FatJets.calibCont,
                                          Output                 = hWWCommon.FatJets.finalCont,
                                          Suffixes               = hWWCommon.FatJets.p4Systs,
                                          SelectedViewContainers = listAllJetViewContainers
                                          )
