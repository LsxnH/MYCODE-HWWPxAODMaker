# ====================================================================
# block that this file is included twice
# ====================================================================
#in this case cannot do it since it is in a loop!
#include.block("HWWVHxAOD/VHTruthCandidateBuilding.py")

# ====================================================================
# Create a sub-sequence that will always run through all algorithms
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWTruthVHCandSeq = AthSequencer( vh_flags.Global.truthPrefix+"CandSeq", StopOverride = True )
hWWTruthCommonSeq += hWWTruthVHCandSeq

from PhysicsxAODConfig.HWWCommonHelpers import buildContainerNames

sortingContainers = HWWTruthSysTracker.containers( [
    (vh_flags.TruthElectrons.finalAllPtSortCont,['','electron','muon','jet']),
    (vh_flags.TruthMuons.finalAllPtSortCont,['','electron','muon','jet']),
    (vh_flags.TruthLeptons.cont,['','electron','muon','jet']),
 ] )

lepSortingAlgNames = HWWTruthSysTracker.containers( [
        (vh_flags.Global.truthPrefix+'LepSortingAlg',['','electron','muon','jet'])
        ] )[0]
lepSortingAlgNames = [algName.replace('_','') for algName in lepSortingAlgNames]
for algName in lepSortingAlgNames: vh_flags.Global.acceptAlgList.append(algName)
# flatEventBuilderAlgNames = [algName.replace('LepSorting','FlatEventBuilder') for algName in lepSortingAlgNames]

for algName, elecInContName, muonInContName, outContName in zip(lepSortingAlgNames, *sortingContainers):
    # Some debug printout
    hWWVH_msg.debug("Working with LeptSortingAlg name: %s" % algName)
    hWWVH_msg.debug(" truth   electron input container:     %s" % elecInContName)
    hWWVH_msg.debug("    muon input container:         %s" % muonInContName)
    hWWVH_msg.debug("    ouput container:              %s" % outContName)
    hWWVH_msg.debug("    nLeptons       :              %s" % nLeptons)

    hWWTruthVHCandSeq += CfgMgr.HWW__VHLepSortingAlg(
            algName,
            #OutputLevel               = VERBOSE,
            nLeptons                  = nLeptons,
            InputElectronContainer    = elecInContName,
            InputMuonContainer        = muonInContName,
            OutputContainer           = outContName,
            WriteSplitOutputContainer = not vh_flags.Global.writeFlatEvent,
            doTruthPAOD               = True
            )

if vh_flags.Global.writeFlatEvent:
    flatEventContainers = HWWTruthSysTracker.containers( [
        (vh_flags.TruthLeptons.cont,['','electron','muon','jet','metNOSUFFIX']),
        (vh_flags.TruthJets.finalAllPtSortCont,['','electron','muon','jet','metNOSUFFIX']),
        (vh_flags.TruthMET.finalCont,['','electron','muon','jet','met']),
        (vh_flags.TruthJets.calibPreSelORCont,['','electron','muon','jet','metNOSUFFIX']),
        (vh_flags.TruthEvent.cont,['','electron','muon','jet','met']),
     ] )

    for lepInContName, jetInContName, METInContName, inOtherJetContName, outContName, \
        in zip(*flatEventContainers):

        # Build the name of the current algorithm instance
        algNameSuffix = outContName.replace("_","")
        algName = vh_flags.Global.truthPrefix+'FlatEventBuilder' + algNameSuffix

        # Some debug printout
        hWWVH_msg.debug("Working with EventBuilderAlg name: %s" % algName)
        hWWVH_msg.debug("    lepton input container:        %s" % lepInContName)
        hWWVH_msg.debug("    jet input container:           %s" % jetInContName)
        hWWVH_msg.debug("    MET input container:           %s" % METInContName)
        hWWVH_msg.debug("    MET input object:              %s" % hWWCommon.TruthMET.inObject)
        hWWVH_msg.debug("    other jet input container:     %s" % inOtherJetContName)
        hWWVH_msg.debug("    output container:              %s" % outContName)

        hWWTruthVHCandSeq += CfgMgr.HWW__VHFlatEventBuilderAlg(
                algName,
                #OutputLevel = VERBOSE,
                LeptonsContainer          = lepInContName,
                JetContainer              = jetInContName,
                MissingETContainer        = METInContName,
                MissingETObject           = hWWCommon.TruthMET.inObject,
                OtherJetContainer         = inOtherJetContName,
                EventContainer            = outContName,
                WriteSplitOutputContainer = True
                )
