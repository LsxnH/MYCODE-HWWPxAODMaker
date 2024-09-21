# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("HWWlnulnuxAODConfig/HWWlnulnuThinning.py")

# Import the module that allows to use named units, e.g. GeV
from AthenaCommon.SystemOfUnits import *


# ====================================================================
# Do the thinning of the underlying objects (TrackParticles,Truth,CaloClusters,...)
# TODO: Need to figure out how to run these algorithms only for events
# that will be written out
# ====================================================================

# Create a sub-sequence that will always run through all algs, i.e., sub-decay channels
from AthenaCommon.AlgSequence import AthSequencer
hWWThinSeq = AthSequencer( "HWWThinningSeq", OutputLevel = WARNING, StopOverride = True )
hWWCommonPreFilterSeq += hWWThinSeq

# hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWInDetTrackParticleThinnerAlg",
#                                             TrackParticlesToThin = "InDetTrackParticles",
#                                             InputContainerList = [ hWWlnulnu.Muons.finalCont,
#                                                                    hWWlnulnu.Electrons.finalCont],
#                                             ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
#                                             )
# hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWCombinedMuonTrackParticlesThinnerAlg",
#                                             TrackParticlesToThin = "CombinedMuonTrackParticles",
#                                             InputContainerList = [ hWWlnulnu.Muons.finalCont ],
#                                             ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
#                                             )
# hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWExtrapolatedMuonTrackParticlesThinnerAlg",
#                                             TrackParticlesToThin = "ExtrapolatedMuonTrackParticles",
#                                             InputContainerList = [ hWWlnulnu.Muons.finalCont ],
#                                             ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
#                                             )
hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWlnulnuGSFTrackParticlesThinnerAlg",
                                            #OutputLevel = DEBUG,
                                            TrackParticlesToThin       = "GSFTrackParticles",
                                            InputContainerList         = [ hWWCommon.Electrons.finalCont ],
                                            NMaxElectronTrackParticles = 1,
                                            ThinningSvc                = 'ThinningSvc/HWWlnulnuOutStreamThinning'
                                            )
# hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWInDetTrackParticlesForwardThinnerAlg",
#                                             TrackParticlesToThin = "InDetTrackParticlesForward",
#                                             InputContainerList = [ hWWlnulnu.Muons.finalCont,
#                                                                    hWWlnulnu.Electrons.finalCont],
#                                             ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
#                                             )

hWWThinSeq += CfgMgr.ThinCaloClustersAlg( "HWWlnulnuCaloClusterThinnerAlg",
                                          OutputLevel = VERBOSE,
                                          CaloClustersToThin = "egammaClusters",
                                          InputContainerList = [ hWWCommon.Electrons.finalCont ],
                                          ThinningSvc        = 'ThinningSvc/HWWlnulnuOutStreamThinning'
                                          )
