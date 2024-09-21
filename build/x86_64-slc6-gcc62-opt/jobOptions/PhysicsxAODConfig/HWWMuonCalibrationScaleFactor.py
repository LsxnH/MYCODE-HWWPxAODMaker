# ====================================================================
# In this file, we will create our own sub-sequence that always runs
# through all its algorithms, irespective of the algorithm accepting
# an event or not.
# We will attach all the muon calibration and systematic variation
# algorithms, as well as the muon pre-selection algorithm and
# scale-factor algorithm, and add them to this sequence.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWMuonCalibrationScaleFactor.py")


# ====================================================================
# Create instances of all needed muon tools and add them to the ToolService
# ====================================================================
# Create an instance of the MuonCalibrationPeriodTool and configure it
# this is a wrapper tool around MuonCalibrationAndSmearingTool (although inheriting from the same interface),
# internally configuring separate instances for each of the mc16 subcampaigns
ToolSvc += CfgMgr.CP__MuonCalibrationPeriodTool( "HWWMuonCalibSmearTool", OutputLevel = WARNING )

# Muon selection tool (CP::MuonSelectionTool)
ToolSvc += CfgMgr.CP__MuonSelectionTool("HWWCPMuonSelectionTool", OutputLevel = ERROR)
ToolSvc += CfgMgr.CP__MuonSelectionTool("HWWCPHighPtMuonSelectionTool", MuQuality = 4, OutputLevel = ERROR)


# -----------------------------------------------------------------------------
# Create the muon isolation tools
# -----------------------------------------------------------------------------
muonIsoTools = []
for wpName in hWWCommon.Muons.isoWorkingPointList :
    toolName = "IsoMuonTool"+wpName
    ToolSvc += CfgMgr.CP__IsolationSelectionTool(toolName, MuonWP=wpName, OutputLevel = WARNING)
    muonIsoTools.append( getattr(ToolSvc,toolName) )
    pass


# ====================================================================
# Decorate the muons with all needed variables
# ====================================================================
# doMuonTruthClassifierTransfer = False
# if hWWCommon.Global.inputRelease == "20.1": doMuonTruthClassifierTransfer = True
hWWCommonCalibSeq += CfgMgr.HWW__MuonDecorationAlg( "HWWMuonDecorationAlg",
                                                    #OutputLevel  = VERBOSE,
                                                    InputContainer                  = hWWCommon.Muons.inCont,
                                                    DoDeltaPt                       = True,
                                                    DoImpactParameter               = True,
                                                    DoTruthInformation              = True
                                                    )



# ====================================================================
# Do the calibration of the muons, including systematic variations
# ====================================================================
# Create the algorithm that will apply the calibrations/smearings provided by
# the tool and write out the new container(s)
hWWCommonCalibSeq += CfgMgr.HWW__MuonCalibrationSmearingAlg( "HWWMuonCalibrationSmearingAlg",
                                                             #OutputLevel                  = VERBOSE,
                                                             MuonCalibrationTool          = ToolSvc.HWWMuonCalibSmearTool,
                                                             InputContainer               = hWWCommon.Muons.inCont,
                                                             OutputContainer              = hWWCommon.Muons.calibCont,
                                                             MomentumSystematicVariations = hWWCommon.Muons.p4Systs
                                                             )

# Now, the MuonSelectionTool has to be applied AFTER calibration
# (do it individually for each systematically varied four-momentum muon)
hWWCommonCalibSeq += CfgMgr.HWW__MuonDecorationAlg( "HWWMuonDecorationPostCalibAlg",
                                                    #OutputLevel  = VERBOSE,
                                                    DecorateAllCopies   = True,
                                                    InputContainer      = hWWCommon.Muons.calibCont,
                                                    SelectionTool       = ToolSvc.HWWCPMuonSelectionTool,
                                                    HighPtSelectionTool = ToolSvc.HWWCPHighPtMuonSelectionTool
                                                    )

# Now, the isolation tools have to be applied AFTER calibration
# (ONLY for the nominal muons)
hWWCommonCalibSeq += CfgMgr.HWW__MuonDecorationAlg( "HWWMuonDecorationPostCalibNominalOnlyAlg",
                                                    #OutputLevel  = VERBOSE,
                                                    DecorateAllCopies     = False,
                                                    InputContainer        = hWWCommon.Muons.calibCont,
                                                    IsolationToolList     = muonIsoTools,
                                                    IsolationToolDecoList = hWWCommon.Muons.passIsoVarNameList
                                                    )
