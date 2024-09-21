# ====================================================================
# block that this file is included twice
# ====================================================================
# include.block("HWWVHxAOD/VHCandidateBuilding.py")

# ====================================================================
# Create a sub-sequence that will always run through all algorithms
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWVHCandSeq = AthSequencer( vh_flags.Global.prefix+"CandSeq", StopOverride = True )
hWWCommonSeq += hWWVHCandSeq

from PhysicsxAODConfig.HWWCommonHelpers import buildContainerNames

sortingContainers = HWWSysTracker.containers( [
    (vh_flags.Electrons.finalAllPtSortCont,['','electron','muon','jet']),
    (vh_flags.Muons.finalAllPtSortCont,['','electron','muon','jet']),
    (vh_flags.Leptons.cont,['','electron','muon','jet']),
 ] )

lepSortingAlgNames = HWWSysTracker.containers( [
        (vh_flags.Global.prefix+'LepSortingAlg',['','electron','muon','jet'])
        ] )[0]
lepSortingAlgNames = [algName.replace('_','') for algName in lepSortingAlgNames]
for algName in lepSortingAlgNames: vh_flags.Global.acceptAlgList.append(algName)
# flatEventBuilderAlgNames = [algName.replace('LepSorting','FlatEventBuilder') for algName in lepSortingAlgNames]

for algName, elecInContName, muonInContName, outContName in zip(lepSortingAlgNames, *sortingContainers):
    # Some debug printout
    hWWVH_msg.debug("Working with LeptSortingAlg name: %s" % algName)
    hWWVH_msg.debug("    electron input container:     %s" % elecInContName)
    hWWVH_msg.debug("    muon input container:         %s" % muonInContName)
    hWWVH_msg.debug("    ouput container:              %s" % outContName)

    hWWVHCandSeq += CfgMgr.HWW__VHLepSortingAlg(
            algName,
            # OutputLevel               = DEBUG,
            nLeptons                  = nLeptons,
            InputElectronContainer    = elecInContName,
            InputMuonContainer        = muonInContName,
            OutputContainer           = outContName,
            WriteSplitOutputContainer = not vh_flags.Global.writeFlatEvent,
            )

if vh_flags.Global.writeFlatEvent:
    flatEventContainers = HWWSysTracker.containers( [
        (vh_flags.Leptons.cont,['','electron','muon','jet','metNOSUFFIX']),
        (vh_flags.Jets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
        (vh_flags.MET.finalCont,['','electron','muon','jet','met']),
        (vh_flags.Jets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
        (vh_flags.Event.cont,['','electron','muon','jet','met']),
     ] )

    for lepInContName, jetInContName, METInContName, inOtherJetContName, outContName, \
        in zip(*flatEventContainers):

        # Build the name of the current algorithm instance
        algNameSuffix = outContName.replace("_","")
        algName = vh_flags.Global.prefix+'FlatEventBuilder' + algNameSuffix

        # Replace the MET to the nominal one, if we are on a TrackMET-only systematic
        if any( sysSuffix in METInContName for sysSuffix in hWWCommon.MET.p4JetTrkSysts ):
            METInContName = hWWCommon.MET.finalCont
            pass

        # Some debug printout
        hWWVH_msg.debug("Working with EventBuilderAlg name: %s" % algName)
        hWWVH_msg.debug("    lepton input container:        %s" % lepInContName)
        hWWVH_msg.debug("    jet input container:           %s" % jetInContName)
        hWWVH_msg.debug("    MET input container:           %s" % METInContName)
        hWWVH_msg.debug("    MET input object:              %s" % hWWCommon.MET.inObject)
        hWWVH_msg.debug("    other jet input container:     %s" % inOtherJetContName)
        hWWVH_msg.debug("    output container:              %s" % outContName)

        hWWVHCandSeq += CfgMgr.HWW__VHFlatEventBuilderAlg(
                algName,
                # OutputLevel = VERBOSE,
                LeptonsContainer          = lepInContName,
                JetContainer              = jetInContName,
                MissingETContainer        = METInContName,
                MissingETObject           = hWWCommon.MET.inObject,
                OtherJetContainer         = inOtherJetContName,
                EventContainer            = outContName,
                WriteSplitOutputContainer = True
                )

# # ====================================================================
# # Create the muon trigger scale factor algs
# # ====================================================================
# # Do the trigger efficiencies and scale-factors only for MC
# if hWWCommon.Global.inputIsSimulation :
#     # Get all the systematic suffixes
#     allSystematicSuffixes = HWWSysTracker.systematics( ['electron','muon','jet','met'] )
#     hWWVH_msg.debug("Using these systematics suffixes for muon trigger scale factor building: %s" % allSystematicSuffixes)
#
#     # Add the muon trigger scale factor calculation algorithm for the di-muon event
#     hWWVHCandSeq += CfgMgr.HWW__MuonTriggerScaleFactorAlg("HWW"+vh_flags.Global.prefix+"EventMuonTriggerScaleFactorAlg",
#                                                              MaxNPartsToUse = nLeptons,
#                                                              InputContainer = vh_flags.Event.cont,
#                                                              TriggerNames   = hWWCommon.Trigger.muonTriggerSFReducedList,
#                                                              ContainerVariationSuffixes     = allSystematicSuffixes,
#                                                              MuonEfficiencyScaleFactorTools = hWWCommon.Muons.effiTrigSFToolList,
#                                                              EfficiencyScaleFactorVarNames  = hWWCommon.Muons.effiTrigSFVarNameList,
#                                                              EfficiencySystematicVariations = hWWCommon.Muons.effiTrigSysts
#                                                              )
#     pass
