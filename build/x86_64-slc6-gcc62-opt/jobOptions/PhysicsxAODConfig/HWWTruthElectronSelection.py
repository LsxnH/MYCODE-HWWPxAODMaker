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
include.block("PhysicsxAODConfig/HWWTruthElectronSelection.py")


# ====================================================================
# Create instances of all needed electron tools and add them to the ToolService
# ====================================================================

# Create the instance of the electron pre-selection tool
ToolSvc += CfgMgr.HWW__TruthElectronSelectionTool ( "HWWTruthElectronPreSelectionTool",
                                                    #OutputLevel = DEBUG,
                                                    CutPtMin             = hWWCommon.TruthElectrons.preSelection.cutPtMin,
                                                    CutAbsEtaMax         = hWWCommon.TruthElectrons.preSelection.cutAbsEtaMax
                                                    )

# Create the instance of the electron selection tool for the electron
ToolSvc += CfgMgr.HWW__TruthElectronSelectionTool ( "HWWTruthElectronSelectionTool",
                                                    #OutputLevel = DEBUG,
                                                    CutPtMin                   = hWWCommon.TruthElectrons.cutPtMin,
                                                    CutAbsEtaMax               = hWWCommon.TruthElectrons.cutAbsEtaMax,
                                                    CutAbsEtaCrackMin          = hWWCommon.TruthElectrons.cutAbsEtaCrackMin,
                                                    CutAbsEtaCrackMax          = hWWCommon.TruthElectrons.cutAbsEtaCrackMax
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
tmpInOut = HWWTruthSysTracker.containers( [ (hWWCommon.TruthElectrons.calibCont,['','electron']),
                                            (hWWCommon.TruthElectrons.calibPreSelCont,['','electron']),
                                            (hWWCommon.TruthElectrons.preORAllPtSortCont,['','electron']) ] )

# Create one selection algorithm instance for each pair
for inContName, preSelContName, outContName in zip(*tmpInOut) :
    # One cannot use an algorithm name that contains "__" or "___", thus, remove those
    algNameSuffix = inContName.replace("_","")
    hWW_msg.debug("Building electron selection algorithm with inContName=%s, preSelContName=%s, outContName=%s" % (inContName,preSelContName,outContName))

    # Enable the electron cut-flow bookkeeping only for the nominal objects
    doCutFlow = True
    doTruth = True
    if inContName.__contains__("___"): doCutFlow = False
    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWTruthPreORSeq += CfgMgr.ParticleSelectionAlg( "HWWTruthElectronPreSelectionAlg"+algNameSuffix,
                                                     #OutputLevel             = DEBUG,
                                                     InputContainer          = inContName,
                                                     OutputContainer         = preSelContName,
                                                     #SelectionWithPVToolList = [ ToolSvc.HWWElectronPreSelectionTool ],
                                                     SelectionToolList = [ ToolSvc.HWWTruthElectronPreSelectionTool ],
                                                     DoCutBookkeeping        = doCutFlow,
                                                     CutBookkeeperContainer  = "HWWTruthElectronPreSelectionCutFlow"
                                                     )

    # Do the pre-selection. This needs to be done BEFORE the overlap removal runs.
    hWWTruthPreORSeq += CfgMgr.ParticleSelectionAlg( "HWWTruthElectronSelectionAlg"+algNameSuffix,
                                                     #OutputLevel             = DEBUG,
                                                     InputContainer          = preSelContName,
                                                     OutputContainer         = outContName,
                                                     SelectionToolList = [ ToolSvc.HWWTruthElectronSelectionTool ],
                                                     DoCutBookkeeping        = doCutFlow,
                                                     CutBookkeeperContainer  = "HWWTruthElectronSelectionCutFlow"
                                                     )

    # Do the pt sorting in decending order. This needs to be done BEFORE the overlap removal runs.
    hWWTruthPreORSeq += CfgMgr.ParticleSortingAlg( "HWWTruthElectronSortingAlg"+algNameSuffix,
                                                   #OutputLevel   = VERBOSE,
                                                   InputContainer  = outContName
                                                   )
    pass




# ====================================================================
# Now we select the leading electron view container with the containers
# selected after Overlap Removal
# ====================================================================

# Build all container lists in one go with the systematics tracker
tmpInOutLead = HWWTruthSysTracker.containers( [ (hWWCommon.TruthElectrons.finalAllPtSortCont,['','electron','muon','jet']),
                                                (hWWCommon.TruthElectrons.finalLeadPtSortCont,['','electron','muon','jet']),
                                                ] )

for inElectronContName, outLeadElectronContName in zip(*tmpInOutLead) :

    systSuffixName = ""
    if inElectronContName.__contains__("___"): systSuffixName = inElectronContName.split("___")[1]
    algNameSuffix = systSuffixName.replace("_","")

    hWW_msg.debug("Building sub-leading electron containers after overlap removal algorithm with (input,output):")
    hWW_msg.debug("    inElectronContName=%s, outLeadElectronContName=%s" % (inElectronContName,outLeadElectronContName))
    hWW_msg.debug("    systSuffixName=%s" % (systSuffixName))
    hWW_msg.debug("    algNameSuffix=%s" % (algNameSuffix))

    # Do the final pt selection for the leading electrons
    hWWTruthCommonSeq += CfgMgr.ParticleSelectionAlg( "HWWLeadTruthElectronSelectionAlg"+algNameSuffix,
                                                      #OutputLevel     = VERBOSE,
                                                      InputContainer  = inElectronContName,
                                                      OutputContainer = outLeadElectronContName,
                                                      Selection       = inElectronContName + ".pt > %s" % hWWCommon.TruthElectrons.cutLeadPtMin
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
tmpElectronViewContainersListList = HWWTruthSysTracker.containers( [ (hWWCommon.TruthElectrons.finalLeadPtSortCont,['','electron','muon','jet']),
                                                                     (hWWCommon.TruthElectrons.finalAllPtSortCont,['','electron','muon','jet']),
                                                                     (hWWCommon.TruthElectrons.calibPreSelORCont,['','electron','muon','jet']),
                                                                     ] )
listAllElectronViewContainers = list(itertools.chain.from_iterable(tmpElectronViewContainersListList))
# Build now the final electron container(s)
hWWTruthCommonSeq += CfgMgr.ParticleRemoverAlg( "HWWlnulnuTruthElectronContainerBuilderAlg",
                                                #OutputLevel            = VERBOSE,
                                                Input                  = hWWCommon.TruthElectrons.calibCont,
                                                Output                 = hWWCommon.TruthElectrons.finalCont,
                                                Suffixes               = hWWCommon.TruthElectrons.p4Systs,
                                                SelectedViewContainers = listAllElectronViewContainers
                                                )
