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
include.block("PhysicsxAODConfig/HWWTruthJetSelection.py")


# ====================================================================
# Create instances of all needed jet tools and add them to the ToolService
# ====================================================================

# Create the instance of the jet pre-selection tool
ToolSvc += CfgMgr.HWW__TruthJetSelectionTool( "HWWTruthJetPreSelectionTool",
                                              #OutputLevel       = DEBUG,
                                              CutPtMinList      = hWWCommon.TruthJets.preSelection.cutPtMinList,
                                              CutAbsEtaMaxList  = hWWCommon.TruthJets.preSelection.cutAbsEtaMaxList
                                              )


# Create the instance of the jet selection tool
ToolSvc += CfgMgr.HWW__TruthJetSelectionTool( "HWWTruthJetSelectionTool",
                                              #OutputLevel       = DEBUG,
                                              CutPtMinList      = hWWCommon.TruthJets.cutPtMinList,
                                              CutAbsEtaMaxList  = hWWCommon.TruthJets.cutAbsEtaMaxList
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
tmpInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthJets.calibCont,['','jet']),
                                            (hWWCommon.TruthJets.calibPreSelCont,['','jet']),
                                            (hWWCommon.TruthJets.preORAllPtSortCont,['','jet']) ] )

# Create one selection algorithm instance for each pair
for inContName, preSelContName, outContName in zip(*tmpInOut) :
    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = inContName.replace("_","")
    hWW_msg.debug("Building jet selection algorithm with inContName=%s, preSelContName=%s, outContName=%s" % (inContName,preSelContName,outContName))

    # Enable the jet cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    if inContName.__contains__("___"): doCutFlow = False
    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWTruthPreORSeq += CfgMgr.ParticleSelectionAlg( "HWWTruthJetPreSelectionAlg"+algNameSuffix,
                                                     #OutputLevel             = DEBUG,
                                                     InputContainer          = inContName,
                                                     OutputContainer         = preSelContName,
                                                     SelectionToolList = [ ToolSvc.HWWTruthJetPreSelectionTool ],
                                                     DoCutBookkeeping        = doCutFlow,
                                                     CutBookkeeperContainer  = "HWWTruthJetPreSelectionCutFlow"
                                                     )

    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWTruthPreORSeq += CfgMgr.ParticleSelectionAlg( "HWWTruthJetSelectionAlg"+algNameSuffix,
                                                     #OutputLevel             = DEBUG,
                                                     InputContainer          = preSelContName,
                                                     OutputContainer         = outContName,
                                                     SelectionToolList = [ ToolSvc.HWWTruthJetSelectionTool ],
                                                     DoCutBookkeeping        = doCutFlow,
                                                     CutBookkeeperContainer  = "HWWTruthJetSelectionCutFlow"
                                                     )

    # Do the pt sorting in decending order. This needs to be done BEFORE the overlap removal runs.
    hWWTruthPreORSeq += CfgMgr.ParticleSortingAlg( "HWWTruthJetSortingAlg"+algNameSuffix,
                                                   # OutputLevel   = VERBOSE,
                                                   InputContainer  = outContName
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
tmpJetViewContainersListList = HWWTruthSysTracker.containers( [ (hWWCommon.TruthJets.finalAllPtSortCont,['','electron','muon','jet']),
                                                                (hWWCommon.TruthJets.calibPreSelORCont,['','electron','muon','jet']),
                                                                ] )
listAllJetViewContainers = list(itertools.chain.from_iterable(tmpJetViewContainersListList))
# Build now the final jet container(s)
hWWTruthCommonSeq += CfgMgr.ParticleRemoverAlg( "HWWlnulnuTruthJetContainerBuilderAlg",
                                                #OutputLevel            = VERBOSE,
                                                Input                  = hWWCommon.TruthJets.calibCont,
                                                Output                 = hWWCommon.TruthJets.finalCont,
                                                Suffixes               = hWWCommon.TruthJets.p4Systs,
                                                SelectedViewContainers = listAllJetViewContainers
                                                )
