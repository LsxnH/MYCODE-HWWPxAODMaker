
# ====================================================================
# TODO: document contents
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWAnalysisCommonTruth.py")

# Build the Truth systematics tracker
# TODO: p4 systematics not considered for Truth atm, but keep functionality in for now
from PhysicsxAODConfig.HWWCommonHelpers import SystematicsTracker
HWWTruthSysTracker = SystematicsTracker( "HWWTruthSystematicsTracker",
                                         jet      = hWWCommon.TruthJets.p4Systs,
                                         electron = hWWCommon.TruthElectrons.p4Systs,
                                         muon     = hWWCommon.TruthMuons.p4Systs,
                                         met      = hWWCommon.TruthMET.p4Systs )
#HWWTruthSysTracker.dump()

# ====================================================================
# Create a subsequence:
# Only when the first algorithm returns isEventAccepted,
# the rest of this sub-sequence is executed
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWTruthCommonPreFilterSeq = AthSequencer("HWWTruthCommonAnalysisPreFilterSeq", OutputLevel = WARNING)
topSequence += hWWTruthCommonPreFilterSeq

# # ====================================================================
# # Decorate the xAOD::EventInfo object with some MCTruth-based quantities
# # ====================================================================
# if hWWCommon.Global.inputIsSimulation:
#     # Sherpa needs some special treatment
#     isFromSherpa = True
#     isNNLOPS = False
#     try:
#         generator = af.fileinfos['metadata']['/TagInfo']['generators']
#         hWW_msg.info("Generator name: " << generator)
#         if "Powheg" in generator or "MadGraph" in generator or "McAtNlo" in generator: isFromSherpa = False
#     except:
#         try:
#             hWW_msg.info("Trying to infer generator type from MC channel number...")
#             mcChannelNumber = af.mc_channel_numbers[0]
#             if mcChannelNumber in [410009]: isFromSherpa = False
#             if mcChannelNumber in range(361700,361899): isFromSherpa = False
#             if mcChannelNumber in range(361100,361110): isFromSherpa = False
#         except:
#             hWW_msg.warning("THIS SAMPLE DOES NOT HAVE METADATA INFO .... asusming SHERPA!!!")
#             pass
#         pass
#     try:
#         mcChannelNumber = af.mc_channel_numbers[0]
#         if mcChannelNumber in [345324]: isNNLOPS = True
#     except:
#         hWW_msg.warning("THIS SAMPLE DOES NOT HAVE METADATA INFO .... asusming no NNLOPS!!!")
#         pass

#     hWWTruthCommonPreFilterSeq += CfgMgr.HWW__TruthAlg("HWWTruthFlaggingAlg",
#                                                        TruthInputContainer      = "TruthEvents",
#                                                        TruthJetInputContainer   = "AntiKt4TruthJets",
#                                                        TruthWZJetInputContainer = "AntiKt4TruthWZJets",
#                                                        TruthMetInputContainer   = "MET_Truth",
#                                                        TruthElectronInputContainer   = "TruthElectrons",
#                                                        TruthMuonInputContainer   = "TruthMuons",
#                                                        IsSherpa                 = isFromSherpa,
#                                                        IsNNLOPS                 = isNNLOPS
#                                                        )

# ====================================================================
# Create a sub-sequence that will always run through all algorithms
# ====================================================================
# TODO: rename this sequence, it's misleading atm
from AthenaCommon.AlgSequence import AthSequencer
hWWTruthCommonCalibSeq = AthSequencer( "HWWTruthCommonCalibSeq", OutputLevel = WARNING, StopOverride = True )
hWWTruthCommonPreFilterSeq += hWWTruthCommonCalibSeq

# ====================================================================
# Do the common object adaptions
# ====================================================================
# TODO: rename this?
include("PhysicsxAODConfig/HWWTruthObjectMod.py")

# ====================================================================
# Create a sub-sequence that will always run through all algorithms
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWTruthCommonSeq = AthSequencer( "HWWTruthCommonSeq", OutputLevel = WARNING, StopOverride = True )
hWWTruthCommonPreFilterSeq += hWWTruthCommonSeq

# ====================================================================
# Create a sub-sequence that will always run through all algorithms.
# This one will be populated with things that need to run BEFORE the
# overlap removal is done, e.g., like lepton pre-selections.
# ====================================================================
from AthenaCommon.AlgSequence import AthSequencer
hWWTruthPreORSeq = AthSequencer( "HWWTruthPreORSeq", OutputLevel = WARNING, StopOverride = True )
hWWTruthCommonSeq += hWWTruthPreORSeq

# ====================================================================
# Do the overlap removal of the containers
# ====================================================================
include("PhysicsxAODConfig/HWWTruthOverlapRemoval.py")

# ====================================================================
# Do the electron selection
# ====================================================================
include("PhysicsxAODConfig/HWWTruthElectronSelection.py")

# ====================================================================
# Do the muon selection
# ====================================================================
include("PhysicsxAODConfig/HWWTruthMuonSelection.py")

# ====================================================================
# Do the jet selection
# ====================================================================
include("PhysicsxAODConfig/HWWTruthJetSelection.py")
