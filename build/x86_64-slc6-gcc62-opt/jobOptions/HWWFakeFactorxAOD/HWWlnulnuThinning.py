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
hWWCommonPreSeq += hWWThinSeq

hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWInDetTrackParticleThinnerAlg",
                                            TrackParticlesToThin = "InDetTrackParticles",
                                            InputContainerList = [ hWWlnulnu.Muons.finalCont,
                                                                   hWWlnulnu.Electrons.finalCont],
                                            ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
                                            )
hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWCombinedMuonTrackParticlesThinnerAlg",
                                            TrackParticlesToThin = "CombinedMuonTrackParticles",
                                            InputContainerList = [ hWWlnulnu.Muons.finalCont ],
                                            ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
                                            )
hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWExtrapolatedMuonTrackParticlesThinnerAlg",
                                            TrackParticlesToThin = "ExtrapolatedMuonTrackParticles",
                                            InputContainerList = [ hWWlnulnu.Muons.finalCont ],
                                            ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
                                            )
hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWGSFTrackParticlesThinnerAlg",
                                            TrackParticlesToThin = "GSFTrackParticles",
                                            InputContainerList = [ hWWlnulnu.Electrons.finalCont ],
                                            ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
                                            )
hWWThinSeq += CfgMgr.ThinTrackParticlesAlg( "HWWInDetTrackParticlesForwardThinnerAlg",
                                            TrackParticlesToThin = "InDetTrackParticlesForward",
                                            InputContainerList = [ hWWlnulnu.Muons.finalCont,
                                                                   hWWlnulnu.Electrons.finalCont],
                                            ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
                                            )

# hWWThinSeq += CfgMgr.ThinCaloClustersAlg( "MyCaloClusterThinnerAlg",
#                                                    #OutputLevel = VERBOSE,
#                                                    CaloClustersToThin = "CaloCalTopoCluster",
#                                                    InputContainerList = ["Muons"],
#                                                    ThinningSvc = 'ThinningSvc/HWWlnulnuOutStreamThinning'
#                                                    )



# ====================================================================
# THINNING: We must create an instance of the ThinningSvc for this output stream.
# Thinning service name must match the one passed to the thinning tools
# ====================================================================
from AthenaServices.Configurables import ThinningSvc, createThinningSvc
augStream = MSMgr.GetStream( hWWlnulnu.Global.StreamName )
evtStream = augStream.GetEventStream()
svcMgr += createThinningSvc( svcName="HWWlnulnuOutStreamThinning", outStreams=[evtStream] )
