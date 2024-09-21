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
include.block("PhysicsxAODConfig/HWWFatJetCalibration.py")


# ====================================================================
# Create instances of all needed jet tools and add them to the ToolService
# ====================================================================

# Create an instance of the JetCalibrationTool
jetCalibConfigFile = hWWCommon.FatJets.calibConfigFile
jetCalibSeq = hWWCommon.FatJets.calibSequence
# Need to use the insitu calibration for data
if not hWWCommon.Global.inputIsSimulation :
    jetCalibSeq += hWWCommon.FatJets.dataCalibSeqSuffix
    pass
# If the input is AtlFastII, use a different config file
if hWWCommon.Global.inputSimulationType == "AFII" :
    jetCalibConfigFile = hWWCommon.FatJets.calibAFIIConfigFile
    pass
hWW_msg.info( "Using jetCalibConfigFile: %s" % jetCalibConfigFile )

# Determine the jet algorithm from the used jet collection
jetAlg = ""
if hWWCommon.FatJets.inCont.__contains__("AntiKt10LCTopoTrimmedPtFrac5SmallR20"):   jetAlg = "AntiKt10LCTopoTrimmedPtFrac5SmallR20"

# Create an instance of the jet calibration tool
ToolSvc += CfgMgr.JetCalibrationTool( "HWWFatJetCalibTool",
                                      OutputLevel   = WARNING,
                                      JetCollection = jetAlg,
                                      ConfigFile    = jetCalibConfigFile,
                                      CalibSequence = jetCalibSeq,
                                      IsData        = (not hWWCommon.Global.inputIsSimulation)
                                      )


# Create an instance of the JetUncertaintiesTool
simTypeJES = "MC15"
if hWWCommon.Global.inputSimulationType == "AFII": simTypeJES = "AFII"
ToolSvc += CfgMgr.JetUncertaintiesTool( "HWWFatJESUncertaintiesTool",
                                        OutputLevel   = WARNING,
                                        JetDefinition = jetAlg,
                                        MCType        = simTypeJES,
                                        ConfigFile    = hWWCommon.FatJets.jesConfigFile
                                        )



# ====================================================================
# Do the calibration and systematic variations thereof for the large-R jets
# ====================================================================
hWWCommonCalibSeq += CfgMgr.HWW__JetCalibrationSmearingAlg( "HWWFatJetCalibrationSmearingAlg",
                                                            #OutputLevel                   = VERBOSE,
                                                            InputContainer                = hWWCommon.FatJets.inCont,
                                                            OutputContainer               = hWWCommon.FatJets.calibCont,
                                                            JetCalibrationTool            = ToolSvc.HWWFatJetCalibTool,
                                                            JESUncertaintyTool            = ToolSvc.HWWFatJESUncertaintiesTool,
                                                            JESSystematicsUncertaintyTool = ToolSvc.HWWFatJESUncertaintiesTool,
                                                            JESSystematicVariations       = hWWCommon.FatJets.p4Systs,
                                                            DoFatJetHack                  = True
                                                            )

# ====================================================================
# Now, calculate the boson tagger variables and attach them to each large-R jet.
# This has to be applied AFTER calirbation
# ====================================================================
hWWCommonCalibSeq += CfgMgr.HWW__FatJetDecorationAlg( "HWWFatJetDecorationPostCalibAlg",
                                                      #OutputLevel  = VERBOSE,
                                                      DecorateAllCopies       = True,
                                                      InputContainer          = hWWCommon.FatJets.calibCont,
                                                      BosonTaggerWorkingPoint = hWWCommon.FatJets.bosonTaggerWorkingPoint,
                                                      BosonTaggerAlgorithm    = hWWCommon.FatJets.bosonTaggerAlgorithm,
                                                      WBosonTaggerConfig      = hWWCommon.FatJets.WTaggerConfigFile,
                                                      ZBosonTaggerConfig      = hWWCommon.FatJets.ZTaggerConfigFile
                                                      )
