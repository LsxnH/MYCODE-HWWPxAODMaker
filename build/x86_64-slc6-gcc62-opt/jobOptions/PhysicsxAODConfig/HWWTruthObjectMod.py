# ====================================================================
# Here, we convert TruthParticle leptons from TRUTH1 to TruthParticle we want.
# 
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWTruthObjectMod.py")


# ====================================================================
# Lets do it
# ====================================================================

hWWTruthCommonCalibSeq += CfgMgr.HWW__TruthLeptonAlg( "HWWTruthLeptonAlg",
                                                      #OutputLevel                   = VERBOSE,
                                                      InputElectrons                = hWWCommon.TruthElectrons.inCont,
                                                      InputMuons                    = hWWCommon.TruthMuons.inCont,
                                                      OutputElectrons               = hWWCommon.TruthElectrons.calibCont,
                                                      OutputMuons                   = hWWCommon.TruthMuons.calibCont,
                                                      )

hWWTruthCommonCalibSeq += CfgMgr.HWW__TruthJetMETAlg( "HWWTruthJetMETAlg",
                                                      #OutputLevel                   = VERBOSE,
                                                      InputJets                     = hWWCommon.TruthJets.inCont,
                                                      InputMet                      = hWWCommon.TruthMET.inCont,
                                                      OutputJets                    = hWWCommon.TruthJets.calibCont,
                                                      OutputMet                     = hWWCommon.TruthMET.calibCont,
                                                      )
