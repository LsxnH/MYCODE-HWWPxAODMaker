# ====================================================================
# In this file, we will create our own sub-sequence that always runs
# through all its algorithms, irespective of the algorithm accepting
# an event or not.
# We will attach all the jet calibration and systematic variation
# algorithms, as well as the jet pre-selection algorithm and
# scale-factor algorithm, and add them to this sequence.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWJetCalibrationScaleFactor.py")

# Import the module that allows to use named units, e.g. GeV
from AthenaCommon.SystemOfUnits import *

# ====================================================================
# Create instances of all needed jet tools and add them to the ToolService
# ====================================================================

# Determine the ConfigFile for calibration
jetCalibConfigFile = hWWCommon.Jets.calibConfigFile
# If the input is AtlFastII, use a different config file
if hWWCommon.Global.inputSimulationType == "AFII" :
    jetCalibConfigFile = hWWCommon.Jets.calibAFIIConfigFile
    pass
hWW_msg.info( "Using jetCalibConfigFile: %s" % jetCalibConfigFile )

# Determine the calibration sequence to use
jetCalibSeq = hWWCommon.Jets.calibSequence
# Need to use the insitu calibration for data
if not hWWCommon.Global.inputIsSimulation :
    jetCalibSeq += hWWCommon.Jets.dataCalibSeqSuffix
    pass
# Need to use an mc suffix for FullSim
elif hWWCommon.Global.inputSimulationType == "FullSim" :
    jetCalibSeq += hWWCommon.Jets.mcCalibSeqSuffix
    pass

# Determine the jet algorithm from the used jet collection
jetAlg = ""
jetContName = hWWCommon.Jets.inCont
if jetContName.__contains__("AntiKt4EMTopo"):    jetAlg = "AntiKt4EMTopo"
elif jetContName.__contains__("AntiKt6EMTopo"):  jetAlg = "AntiKt6EMTopo"
elif jetContName.__contains__("AntiKt4LCTopo"):  jetAlg = "AntiKt4LCTopo"
elif jetContName.__contains__("AntiKt6LCTopo"):  jetAlg = "AntiKt4LCTopo"
elif jetContName.__contains__("AntiKt4EMPFlow"): jetAlg = "AntiKt4EMPFlow"
else:
    hWW_msg.warning("Couldn't determine the jet algorithm for the input jet container with name: %s" % jetContName )
    pass


# Create an instance of the jet calibration tool
ToolSvc += CfgMgr.JetCalibrationTool( "HWWJetCalibTool",
                                      OutputLevel   = WARNING,
                                      JetCollection = jetAlg,
                                      ConfigFile    = jetCalibConfigFile,
                                      CalibSequence = jetCalibSeq,
                                      CalibArea     = hWWCommon.Jets.CalibArea,
                                      IsData        = (not hWWCommon.Global.inputIsSimulation)
                                      )


# Create the needed instances of the JetUncertaintiesTool
simType = "MC16"
if hWWCommon.Global.inputSimulationType == "AFII": simType = "AFII"
ToolSvc += CfgMgr.JetUncertaintiesTool( "HWWJetUncertaintiesTool",
                                        OutputLevel   = WARNING,
                                        JetDefinition = jetAlg,
                                        MCType        = simType,
                                        ConfigFile    = hWWCommon.Jets.jesjerConfigFile,
                                        CalibArea     = hWWCommon.Jets.jesjerCalibArea,
                                        IsData        = (not hWWCommon.Global.inputIsSimulation)
                                        )




# ====================================================================
# Decorate the jets with all needed variables
# ====================================================================
hWWCommonCalibSeq += CfgMgr.HWW__JetDecorationAlg( "HWWJetDecorationAlg",
                                                   #OutputLevel              = VERBOSE,
                                                   InputContainer           = hWWCommon.Jets.inCont,
                                                   InputTruthContainer      = hWWCommon.Jets.truthCont,
                                                   TruthEventContainer      = "TruthEvents",
                                                   DoJvtPileupTruthLabeling = True
                                                   )



# ====================================================================
# Do the calibration of the jets, including systematic variations
# ====================================================================
hWWCommonCalibSeq += CfgMgr.HWW__JetCalibrationSmearingAlg( "HWWJetCalibrationSmearingMainAlg",
                                                            #OutputLevel                   = VERBOSE,
                                                            InputContainer                = hWWCommon.Jets.inCont,
                                                            OutputContainer               = hWWCommon.Jets.calibCont,
                                                            MCType                        = simType,
                                                            JetCalibrationTool            = ToolSvc.HWWJetCalibTool,
                                                            JetUncertaintyTool            = ToolSvc.HWWJetUncertaintiesTool,
                                                            JetSystematicsUncertaintyTool = ToolSvc.HWWJetUncertaintiesTool,
                                                            JetSystematicVariations       = hWWCommon.Jets.p4Systs
                                                            )



# ====================================================================
# Decorate the calibrated jets with all needed variables
# ====================================================================
# Create two instances of the ForwardJVTTool,
# one for the normal operating point and one for the tight operating point.
ToolSvc += CfgMgr.JetForwardJvtTool("HWWJetForwardJvtTool",
                                    OutputLevel   = WARNING,
                                    CentralMaxPt  = 60.0*GeV,
                                    JvtMomentName = hWWCommon.Jets.updateJVTName
                                    )
ToolSvc += CfgMgr.JetForwardJvtTool("HWWJetForwardJvtTightTool",
                                    OutputLevel   = WARNING,
                                    CentralMaxPt  = 60.0*GeV,
                                    JvtMomentName = hWWCommon.Jets.updateJVTName,
                                    OutputDec     = "passFJVTTight",
                                    UseTightOP    = True
                                    )
ToolSvc += CfgMgr.JetVertexTaggerTool("HWWJetVertexTaggerTool",
                                      OutputLevel = WARNING,
                                      JVFCorrName = "Jvt" #"JvtJvfcorr", "JvtRpt"
                                      )

hWWCommonCalibSeq += CfgMgr.HWW__JetDecorationAlg( "HWWCalibratedJetDecorationAlg",
                                                   #OutputLevel          = VERBOSE,
                                                   InputContainer       = hWWCommon.Jets.calibCont,
                                                   UpdateJVTName        = hWWCommon.Jets.updateJVTName,
                                                   UpdateJVT            = True,
                                                   JVTUpdateTool        = ToolSvc.HWWJetVertexTaggerTool,
                                                   ForwardJvtTool       = ToolSvc.HWWJetForwardJvtTool,
                                                   ForwardJvtTightTool  = ToolSvc.HWWJetForwardJvtTightTool,
                                                   DoForwardJvt         = True
                                                   )



# ====================================================================
# Handle the JVT, its efficiency and associated uncertainties
# Actually, here, we only calculate the passJVT variable.
# The efficiency scale-factors and their uncertainties are calculated
# in the file HWWEfficiencyScaleFactor.py
# ====================================================================

# Create an instance of the JetJvtEfficiencyTool for the central JVT, if we don't already have it
if not hasattr(ToolSvc,"HWWJetJvtEfficiencyTool"):
    ToolSvc += CfgMgr.CP__JetJvtEfficiency("HWWJetJvtEfficiencyTool",
                                        OutputLevel      = WARNING,
                                        SFFile           = hWWCommon.Jets.jvtConfigFile,
                                        JetJvtMomentName = hWWCommon.Jets.updateJVTName
                                        )
    pass



# Schedule the algorithm to flag the jets with the passJVT flag
hWWCommonCalibSeq += CfgMgr.HWW__JetJVTScaleFactorAlg("HWWJetJVTPassAlg",
                                InputContainer       = hWWCommon.Jets.calibCont,
                                JetJvtEfficiencyTool = ToolSvc.HWWJetJvtEfficiencyTool,
                                PassJVTVarName       = hWWCommon.Jets.passJVTVarName,
                                DecorateEvent        = False
                                )



# ====================================================================
# Also work with track jets, if requested
# ====================================================================
if hWWCommon.Jets.writeTrackJets :
    # ====================================================================
    # Decorate the jets with all needed variables
    # ====================================================================
    hWWCommonCalibSeq += CfgMgr.HWW__JetDecorationAlg( "HWWTrackJetDecorationAlg",
                                                       InputContainer       = hWWCommon.Jets.inTrackJetsCont,
                                                       BTagNameList         = ["MV2c10"]
                                                       )
    pass
