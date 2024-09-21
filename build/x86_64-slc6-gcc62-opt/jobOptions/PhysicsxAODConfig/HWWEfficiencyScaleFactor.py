# ====================================================================
# Here, we schedule all efficiency and scale-factor calculations.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWEfficiencyScaleFactor.py")


# Print a status message
hWW_msg.info("Running efficieny and scale-factor calculations")


# =============================================================================
# =============================================================================
# --------------------------------  ELECTRONS  --------------------------------
# =============================================================================
# =============================================================================

# -----------------------------------------------------------------------------
# Create the instances of the electron efficiency scale factor tools and configure them
# -----------------------------------------------------------------------------
dataType = 1 # Full
if hWWCommon.Global.inputIsSimulation :
    if hWWCommon.Global.inputSimulationType == "AFII" : dateType = 3 # Fast
else : dataType = 0 # Data
# Trigger scale-factors
electronTrigScaleFactorTools = []
assert len(hWWCommon.Electrons.effiSFTrigCorrectionFiles) == len(hWWCommon.Electrons.effiSFTrigVarNameList)
for i in xrange(len(hWWCommon.Electrons.effiSFTrigCorrectionFiles)) :
    varName  = hWWCommon.Electrons.effiSFTrigVarNameList[i]
    fileName = hWWCommon.Electrons.effiSFTrigCorrectionFiles[i]
    algName  = ("HWWElectronTrigEffScaleFactorTool"+varName).replace("_","")
    ToolSvc += CfgMgr.AsgElectronEfficiencyCorrectionTool(algName,
                                                          OutputLevel            = WARNING,
                                                          CorrelationModel       = hWWCommon.Electrons.effiSFTrigCorrelationModel,
                                                          CorrectionFileNameList = [fileName],
                                                          ForceDataType          = dataType )
    electronTrigScaleFactorTools.append( getattr(ToolSvc,algName) )
    pass
# Trigger efficiencies
electronTrigEfficiencyTools  = []
assert len(hWWCommon.Electrons.effiTrigCorrectionFiles) == len(hWWCommon.Electrons.effiTrigVarNameList)
for i in xrange(len(hWWCommon.Electrons.effiTrigCorrectionFiles)) :
    varName  = hWWCommon.Electrons.effiTrigVarNameList[i]
    fileName = hWWCommon.Electrons.effiTrigCorrectionFiles[i]
    algName  = ("HWWElectronTrigEfficiencyTool"+varName).replace("_","")
    ToolSvc += CfgMgr.AsgElectronEfficiencyCorrectionTool(algName,
                                                          OutputLevel            = WARNING,
                                                          CorrelationModel       = hWWCommon.Electrons.effiTrigCorrelationModel,
                                                          CorrectionFileNameList = [fileName],
                                                          ForceDataType          = dataType )
    electronTrigEfficiencyTools.append( getattr(ToolSvc,algName) )
    pass

# Reconstruction
assert len(hWWCommon.Electrons.effiRecoCorrectionFiles) == len(hWWCommon.Electrons.effiRecoVarNameList)
electronRecoScaleFactorTools = []
for i in xrange(len(hWWCommon.Electrons.effiRecoCorrectionFiles)) :
    varName  = hWWCommon.Electrons.effiRecoVarNameList[i]
    fileName = hWWCommon.Electrons.effiRecoCorrectionFiles[i]
    algName  = ("HWWElectronRecoEffScaleFactorTool"+varName).replace("_","")
    ToolSvc += CfgMgr.AsgElectronEfficiencyCorrectionTool(algName,
                                                          OutputLevel            = WARNING,
                                                          CorrelationModel       = hWWCommon.Electrons.effiRecoCorrelationModel,
                                                          CorrectionFileNameList = [fileName],
                                                          ForceDataType          = dataType )
    electronRecoScaleFactorTools.append( getattr(ToolSvc,algName) )
    pass
# Identification
assert len(hWWCommon.Electrons.effiCorrectionFiles) == len(hWWCommon.Electrons.effiVarNameList)
electronScaleFactorTools = []
for i in xrange(len(hWWCommon.Electrons.effiCorrectionFiles)) :
    varName  = hWWCommon.Electrons.effiVarNameList[i]
    fileName = hWWCommon.Electrons.effiCorrectionFiles[i]
    algName  = ("HWWElectronIDEffScaleFactorTool"+varName).replace("_","")
    ToolSvc += CfgMgr.AsgElectronEfficiencyCorrectionTool(algName,
                                                          OutputLevel            = WARNING,
                                                          CorrelationModel       = hWWCommon.Electrons.effiIDCorrelationModel,
                                                          CorrectionFileNameList = [fileName],
                                                          ForceDataType          = dataType )
    electronScaleFactorTools.append( getattr(ToolSvc,algName) )
    pass
# Isolation
assert len(hWWCommon.Electrons.effiIsoCorrectionFiles) == len(hWWCommon.Electrons.effiIsoVarNameList)
electronIsoScaleFactorTools = []
for i in xrange(len(hWWCommon.Electrons.effiIsoCorrectionFiles)) :
    varName  = hWWCommon.Electrons.effiIsoVarNameList[i]
    fileName = hWWCommon.Electrons.effiIsoCorrectionFiles[i]
    algName  = ("HWWElectronIsoEffScaleFactorTool"+varName).replace("_","")
    ToolSvc += CfgMgr.AsgElectronEfficiencyCorrectionTool(algName,
                                                          OutputLevel            = WARNING,
                                                          CorrelationModel       = hWWCommon.Electrons.effiIsoCorrelationModel,
                                                          CorrectionFileNameList = [fileName],
                                                          ForceDataType          = dataType )
    electronIsoScaleFactorTools.append( getattr(ToolSvc,algName) )
    pass




# -----------------------------------------------------------------------------
# Apply all the efficiency scale-factors (and their systematic variations)
# to the final electron container (and its p4-systematic variations)
# -----------------------------------------------------------------------------

# Trigger scale-factors
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__ElectronScaleFactorAlg( "HWWElectronTrigEffiScaleFactorAlg",
                                    #OutputLevel                        = DEBUG,
                                    InputContainer                     = hWWCommon.Electrons.finalCont,
                                    ContainersFinderTool               = ToolSvc.HWWContainersFinderTool,
                                    ElectronEfficiencyScaleFactorTools = electronTrigScaleFactorTools,
                                    EfficiencySystematicVariations     = hWWCommon.Electrons.effiSFTrigSysts,
                                    EfficiencyScaleFactorVarNames      = hWWCommon.Electrons.effiSFTrigVarNameList
                                    #RunAlsoOnData                      = True
                                    )

# Trigger efficiencies
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__ElectronScaleFactorAlg( "HWWElectronTrigEfficiencyAlg",
                                    #OutputLevel                        = DEBUG,
                                    InputContainer                     = hWWCommon.Electrons.finalCont,
                                    ContainersFinderTool               = ToolSvc.HWWContainersFinderTool,
                                    ElectronEfficiencyScaleFactorTools = electronTrigEfficiencyTools,
                                    EfficiencySystematicVariations     = hWWCommon.Electrons.effiTrigSysts,
                                    EfficiencyScaleFactorVarNames      = hWWCommon.Electrons.effiTrigVarNameList
                                    #RunAlsoOnData                      = True
                                    )

# Reconstruction
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__ElectronScaleFactorAlg( "HWWElectronRecoEffiScaleFactorAlg",
                                    #OutputLevel                        = DEBUG,
                                    InputContainer                     = hWWCommon.Electrons.finalCont,
                                    ContainersFinderTool               = ToolSvc.HWWContainersFinderTool,
                                    ElectronEfficiencyScaleFactorTools = electronRecoScaleFactorTools,
                                    EfficiencySystematicVariations     = hWWCommon.Electrons.effiRecoSysts,
                                    EfficiencyScaleFactorVarNames      = hWWCommon.Electrons.effiRecoVarNameList,
                                    )

# Identification
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__ElectronScaleFactorAlg( "HWWElectronIDEffiScaleFactorAlg",
                                    #OutputLevel                        = DEBUG,
                                    InputContainer                     = hWWCommon.Electrons.finalCont,
                                    ContainersFinderTool               = ToolSvc.HWWContainersFinderTool,
                                    ElectronEfficiencyScaleFactorTools = electronScaleFactorTools,
                                    EfficiencySystematicVariations     = hWWCommon.Electrons.effiSysts,
                                    EfficiencyScaleFactorVarNames      = hWWCommon.Electrons.effiVarNameList,
                                    )

# Isolation
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__ElectronScaleFactorAlg( "HWWElectronIsoEffiScaleFactorAlg",
                                    #OutputLevel                        = DEBUG,
                                    InputContainer                     = hWWCommon.Electrons.finalCont,
                                    ContainersFinderTool               = ToolSvc.HWWContainersFinderTool,
                                    ElectronEfficiencyScaleFactorTools = electronIsoScaleFactorTools,
                                    EfficiencySystematicVariations     = hWWCommon.Electrons.effiIsoSysts,
                                    EfficiencyScaleFactorVarNames      = hWWCommon.Electrons.effiIsoVarNameList,
                                    )






# =============================================================================
# =============================================================================
# ---------------------------------  MUONS  -----------------------------------
# =============================================================================
# =============================================================================

# -----------------------------------------------------------------------------
# Create the instances of the muon efficiency scale factor tools and configure them
# -----------------------------------------------------------------------------

# Reconstruction and identification scale factors
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonLooseEffScaleFactorTool",  WorkingPoint = "Loose",   OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonMediumEffScaleFactorTool", WorkingPoint = "Medium",  OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonTightEffScaleFactorTool",  WorkingPoint = "Tight",   OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonHighPtEffScaleFactorTool", WorkingPoint = "HighPt",  OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWBadMuonEffScaleFactorTool",    WorkingPoint = "BadMuon", OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonLowPtEffScaleFactorTool",  WorkingPoint = "LowPt",   OutputLevel = WARNING )

muonScaleFactorTools = [ ToolSvc.HWWMuonLooseEffScaleFactorTool,
                         ToolSvc.HWWMuonMediumEffScaleFactorTool,
                         ToolSvc.HWWMuonTightEffScaleFactorTool,
                         ToolSvc.HWWMuonHighPtEffScaleFactorTool,
                         ToolSvc.HWWBadMuonEffScaleFactorTool,
                         ToolSvc.HWWMuonLowPtEffScaleFactorTool]

hWWCommon.Muons.effiVarNameList = [ hWWCommon.Muons.effiVarName+"Loose",
                                    hWWCommon.Muons.effiVarName+"Medium",
                                    hWWCommon.Muons.effiVarName+"Tight",
                                    hWWCommon.Muons.effiVarName+"HighPt",
                                    hWWCommon.Muons.effiVarName+"BadMuon",
                                    hWWCommon.Muons.effiVarName+"LowPt"]

# Track-to-vertex association scale factors
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonTrackToVertexEffScaleFactorTool", WorkingPoint = "TTVA", OutputLevel = WARNING )

# Isolation scale factors
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFCTightTrackOnly_FixedRadEffScaleFactorTool", WorkingPoint = "FCTightTrackOnly_FixedRadIso", OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFCLoose_FixedRadEffScaleFactorTool",          WorkingPoint = "FCLoose_FixedRadIso",          OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFCTight_FixedRadEffScaleFactorTool",          WorkingPoint = "FCTight_FixedRadIso",          OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFixedCutPflowTightEffScaleFactorTool",        WorkingPoint = "FixedCutPflowTightIso",        OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFixedCutPflowLooseEffScaleFactorTool",        WorkingPoint = "FixedCutPflowLooseIso",        OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFixedCutHighPtTrackOnlyEffScaleFactorTool",   WorkingPoint = "FixedCutHighPtTrackOnlyIso",   OutputLevel = WARNING )
# ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFCTightTrackOnlyEffScaleFactorTool",          WorkingPoint = "FCTightTrackOnlyIso",          OutputLevel = WARNING ) # Not yet available
# ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFCLooseEffScaleFactorTool",                   WorkingPoint = "FCLooseIso",                   OutputLevel = WARNING ) # Not yet available
# ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFCTightEffScaleFactorTool",                   WorkingPoint = "FCTightIso",                   OutputLevel = WARNING ) # Not yet available
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFixedCutHighMuTightEffScaleFactorTool",       WorkingPoint = "FixedCutHighMuTightIso",       OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFixedCutHighMuLooseEffScaleFactorTool",       WorkingPoint = "FixedCutHighMuLooseIso",       OutputLevel = WARNING )
ToolSvc += CfgMgr.CP__MuonEfficiencyScaleFactors( "HWWMuonIsoFixedCutHighMuTrackOnlyEffScaleFactorTool",   WorkingPoint = "FixedCutHighMuTrackOnlyIso",   OutputLevel = WARNING )

muonIsoScaleFactorTools = [ ToolSvc.HWWMuonIsoFCTightTrackOnly_FixedRadEffScaleFactorTool,
                            ToolSvc.HWWMuonIsoFCLoose_FixedRadEffScaleFactorTool,
                            ToolSvc.HWWMuonIsoFCTight_FixedRadEffScaleFactorTool,
                            ToolSvc.HWWMuonIsoFixedCutPflowTightEffScaleFactorTool,
                            ToolSvc.HWWMuonIsoFixedCutPflowLooseEffScaleFactorTool,
                            ToolSvc.HWWMuonIsoFixedCutHighPtTrackOnlyEffScaleFactorTool,
                            # ToolSvc.HWWMuonIsoFCTightTrackOnlyEffScaleFactorTool, # Not yet available
                            # ToolSvc.HWWMuonIsoFCLooseEffScaleFactorTool, # Not yet available
                            # ToolSvc.HWWMuonIsoFCTightEffScaleFactorTool, # Not yet available
                            ToolSvc.HWWMuonIsoFixedCutHighMuTightEffScaleFactorTool,
                            ToolSvc.HWWMuonIsoFixedCutHighMuLooseEffScaleFactorTool,
                            ToolSvc.HWWMuonIsoFixedCutHighMuTrackOnlyEffScaleFactorTool ]

hWWCommon.Muons.effiIsoVarNameList = [ hWWCommon.Muons.effiVarName+"IsoFCTightTrackOnly_FixedRad",
                                       hWWCommon.Muons.effiVarName+"IsoFCLoose_FixedRad",
                                       hWWCommon.Muons.effiVarName+"IsoFCTight_FixedRad",
                                       hWWCommon.Muons.effiVarName+"IsoFixedCutPflowTight",
                                       hWWCommon.Muons.effiVarName+"IsoFixedCutPflowLoose",
                                       hWWCommon.Muons.effiVarName+"IsoFixedCutHighPtTrackOnly",
                                       # hWWCommon.Muons.effiVarName+"IsoFCTightTrackOnly", # Not yet available
                                       # hWWCommon.Muons.effiVarName+"IsoFCLoose", # Not yet available
                                       # hWWCommon.Muons.effiVarName+"IsoFCTight", # Not yet available
                                       hWWCommon.Muons.effiVarName+"IsoFixedCutHighMuTight",
                                       hWWCommon.Muons.effiVarName+"IsoFixedCutHighMuLoose",
                                       hWWCommon.Muons.effiVarName+"IsoFixedCutHighMuTrackOnly", ]

# -----------------------------------------------------------------------------
# Create the muon trigger scale factor tools
# -----------------------------------------------------------------------------
# Do the crazy work to get all the needed lists of tools and variable names and trigger names...
prefix = hWWCommon.Muons.effiVarName
muonEffiTrigSFTool2015List  = []
muonEffiTrigSFTool2016List  = []
muonEffiSFTrigVarNameList   = []
muonEffiTrigVarNameList     = []
muonEffiTrigDataVarNameList = []
muonTrig2015NameList        = []
muonTrig2016NameList        = []
offlineMuonIDList           = [ "Medium", "Tight", "HighPt" ]
def getCombinedTrigVarName( trigNamePair ):
    trigName2015 = trigNamePair[0]
    trigName2016 = trigNamePair[1]
    if trigName2015 == trigName2016: return trigName2015.replace("HLT_","")
    trigName = "2015_"+trigName2015+"_2016_"+trigName2016
    return trigName.replace("HLT_","")
i=0
for offlineMuonID in offlineMuonIDList:
    for muTrigNamePair in hWWCommon.Trigger.muonTriggerSFFullList:
        i += 1
        trigVarName = getCombinedTrigVarName(muTrigNamePair)
        muonTrig2015NameList.append(muTrigNamePair[0])
        muonTrig2016NameList.append(muTrigNamePair[1])
        muonEffiSFTrigVarNameList.append(prefix+"Trig_wrt"+offlineMuonID+"_"+trigVarName)
        muonEffiTrigVarNameList.append("effiTrig_wrt"+offlineMuonID+"_"+trigVarName)
        muonEffiTrigDataVarNameList.append("effiTrigData_wrt"+offlineMuonID+"_"+trigVarName)
        Tool2015Name = "HWWMuonTriggerSFTool2015"+offlineMuonID+str(i)
        Tool2016Name = "HWWMuonTriggerSFTool2016"+offlineMuonID+str(i)
        hWW_msg.debug("Configuring muon trigger tools for 2015 with name %s with trigger %s, and for 2016 with name %s for trigger %s; have trigVarName=%s" % (Tool2015Name, muTrigNamePair[0], Tool2016Name, muTrigNamePair[1], trigVarName) )
        muonTrigSF2015Tool = CfgMgr.CP__MuonTriggerScaleFactors(Tool2015Name, MuonQuality=offlineMuonID, OutputLevel = ERROR) #mgeisen: Year="2015", Isolation="", 
        
        ToolSvc += muonTrigSF2015Tool
        muonTrigSF2016Tool = CfgMgr.CP__MuonTriggerScaleFactors(Tool2016Name, MuonQuality=offlineMuonID, OutputLevel = ERROR) #Year="2016", Isolation="",
        
        ToolSvc += muonTrigSF2016Tool
        muonEffiTrigSFTool2015List.append( getattr(ToolSvc,Tool2015Name) )
        muonEffiTrigSFTool2016List.append( getattr(ToolSvc,Tool2016Name) )
        pass
    pass
# add the new names also here, such that they get written out
hWWCommon.Muons.effiTrigSFVarNameList.extend( muonEffiSFTrigVarNameList )
hWWCommon.Muons.effiTrigVarNameList.extend( muonEffiTrigVarNameList )
hWWCommon.Muons.effiTrigVarNameList.extend( muonEffiTrigDataVarNameList )



# -----------------------------------------------------------------------------
# Apply all the efficiency scale-factors (and their systematic variations)
# to the final muon container (and its p4-systematic variations).
# Only calculate all the scale factors and efficiencies for Monte Carlo
# -----------------------------------------------------------------------------

# Trigger efficiencies and scale factors
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__MuonTriggerEfficiencyScaleFactorAlg( "HWWMuonTriggerEfficiencyAlg",
                                    #OutputLevel                        = VERBOSE,
                                    InputContainer                     = hWWCommon.Muons.finalCont,
                                    ContainersFinderTool               = ToolSvc.HWWContainersFinderTool,
                                    MuonEfficiencyScaleFactorTools2015 = muonEffiTrigSFTool2015List,
                                    MuonEfficiencyScaleFactorTools2016 = muonEffiTrigSFTool2016List,
                                    EfficiencyScaleFactorVarNames      = muonEffiSFTrigVarNameList,
                                    EfficiencySystematicVariations     = hWWCommon.Muons.effiTrigSysts,
                                    EfficiencyVarNames                 = muonEffiTrigVarNameList,
                                    TriggerNames2015                   = muonTrig2015NameList,
                                    TriggerNames2016                   = muonTrig2016NameList
                                    )

# Trigger efficiencies for data (it is running on MC events, but giving us the data efficiencies for each MC muon)
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__MuonTriggerEfficiencyScaleFactorAlg( "HWWMuonTriggerDataEfficiencyAlg",
                                    #OutputLevel                        = VERBOSE,
                                    InputContainer                     = hWWCommon.Muons.finalCont,
                                    ContainersFinderTool               = ToolSvc.HWWContainersFinderTool,
                                    MuonEfficiencyScaleFactorTools2015 = muonEffiTrigSFTool2015List,
                                    MuonEfficiencyScaleFactorTools2016 = muonEffiTrigSFTool2016List,
                                    GetDataEfficiency                  = True,
                                    EfficiencyVarNames                 = muonEffiTrigDataVarNameList,
                                    TriggerNames2015                   = muonTrig2015NameList,
                                    TriggerNames2016                   = muonTrig2016NameList
                                    )

# Reconstruction and identification scale factors
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__MuonScaleFactorAlg( "HWWMuonEffiScaleFactorAlg",
                                    #OutputLevel                    = VERBOSE,
                                    InputContainer                 = hWWCommon.Muons.finalCont,
                                    ContainersFinderTool           = ToolSvc.HWWContainersFinderTool,
                                    MuonEfficiencyScaleFactorTools = muonScaleFactorTools,
                                    EfficiencySystematicVariations = hWWCommon.Muons.effiSysts,
                                    EfficiencyScaleFactorVarNames  = hWWCommon.Muons.effiVarNameList
                                    )

# Track-to-vertex association scale factors
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__MuonScaleFactorAlg( "HWWMuonTTVAEffiScaleFactorAlg",
                                    #OutputLevel                    = VERBOSE,
                                    InputContainer                 = hWWCommon.Muons.finalCont,
                                    ContainersFinderTool           = ToolSvc.HWWContainersFinderTool,
                                    MuonEfficiencyScaleFactorTools = [ToolSvc.HWWMuonTrackToVertexEffScaleFactorTool],
                                    EfficiencySystematicVariations = hWWCommon.Muons.effiTTVASysts,
                                    EfficiencyScaleFactorVarNames  = hWWCommon.Muons.effiTTVAVarNameList
                                    )

# Isolation scale factors
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__MuonScaleFactorAlg( "HWWMuonIsoEffiScaleFactorAlg",
                                    #OutputLevel                    = VERBOSE,
                                    InputContainer                 = hWWCommon.Muons.finalCont,
                                    ContainersFinderTool           = ToolSvc.HWWContainersFinderTool,
                                    MuonEfficiencyScaleFactorTools = muonIsoScaleFactorTools,
                                    EfficiencySystematicVariations = hWWCommon.Muons.effiIsoSysts,
                                    EfficiencyScaleFactorVarNames  = hWWCommon.Muons.effiIsoVarNameList
                                    )
#    pass





# =============================================================================
# =============================================================================
# ----------------------------------  JETS  -----------------------------------
# =============================================================================
# =============================================================================

# -----------------------------------------------------------------------------
# Handle the JVT efficiency and associated uncertainties
# -----------------------------------------------------------------------------

# Create an instance of the JetJvtEfficiencyTool, if we don't already have it
if not hasattr(ToolSvc,"HWWJetJvtEfficiencyTool"):
    ToolSvc += CfgMgr.CP__JetJvtEfficiency("HWWJetJvtEfficiencyTool",
                                        OutputLevel      = WARNING,
                                        SFFile           = hWWCommon.Jets.jvtConfigFile,
                                        JetJvtMomentName = hWWCommon.Jets.updateJVTName
                                        )
    pass

# Create an instance of the JetJvtEfficiencyTool for the forwardJVT, if we don't already have it
if not hasattr(ToolSvc,"HWWJetForwardJvtEfficiencyTool"):
    ToolSvc += CfgMgr.CP__JetJvtEfficiency("HWWJetForwardJvtEfficiencyTool",
                                        OutputLevel      = WARNING,
                                        SFFile           = hWWCommon.Jets.forwardJvtConfigFile,
                                        JetJvtMomentName = hWWCommon.Jets.updateJVTName
                                        )
    pass

# Schedule the algorithm for the central JVT
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__JetJVTScaleFactorAlg("HWWJetJVTScaleFactorAlg",
                                    #OutputLevel                    = DEBUG,
                                    InputContainer                 = hWWCommon.Jets.finalCont,
                                    InputAllCalibORJets            = hWWCommon.Jets.calibCont,
                                    JetJvtEfficiencyTool           = ToolSvc.HWWJetJvtEfficiencyTool,
                                    EfficiencyScaleFactorVarName   = hWWCommon.Jets.effiJVTVarName,
                                    EfficiencySystematicVariations = hWWCommon.Jets.effiJVTSysts
                                    )

# Schedule the algorithm for the forward JVT
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__JetJVTScaleFactorAlg("HWWJetForwardJVTScaleFactorAlg",
                                    #OutputLevel                    = DEBUG,
                                    InputContainer                 = hWWCommon.Jets.finalCont,
                                    InputAllCalibORJets            = hWWCommon.Jets.calibCont,
                                    JetJvtEfficiencyTool           = ToolSvc.HWWJetForwardJvtEfficiencyTool,
                                    EfficiencyScaleFactorVarName   = hWWCommon.Jets.effiForwardJVTVarName,
                                    EfficiencySystematicVariations = hWWCommon.Jets.effiForwardJVTSysts,
                                    DecorateJets                   = False
                                    )


# -----------------------------------------------------------------------------
# Apply all the b-tagging efficiency scale-factors (and their systematic variations)
# to the final jet container (and its p4-systematic variations)
# -----------------------------------------------------------------------------

# Only apply btagging SFs on MC
#if hWWCommon.Global.inputIsSimulation :
# Create an instance of the BtaggingSystematics tool, only needed for MC
# Need to figure out which B-tagging efficiencies to use
# Nominal choice is Powheg+Pythia8
ttbarDSID = "410470"
try:
  hWW_msg.info("Trying to infer generator type from MC channel number...")
  mcChannelNumber = af.mc_channel_numbers[0]
  #set Powheg+Pythia6 (also MG+Py6)
  if mcChannelNumber in [410000,410001,410002,410009,410025,410026,410049,410050,410064,410065,429007,410151,410152,410153,410154]: ttbarDSID = "default"
  if mcChannelNumber in range(410011,410020): ttbarDSID = "default"
  if mcChannelNumber in range(410103,410110): ttbarDSID = "default"
  #set Powheg+H++, also for H7 and Madgraph at the moment 
  if mcChannelNumber in [410003,410004,410145,410146,410026,410164]: ttbarDSID = "410004"
  #H7 samples
  if mcChannelNumber in [410525,410527]: ttbarDSID = "410004"
  #Sherpa 2.1.1
  if mcChannelNumber in [410021,410022,410023]: ttbarDSID = "410021"
  #newer Sherpa
  if mcChannelNumber in [410189,410252]: ttbarDSID = "410187"
except:
  hWW_msg.warning("THIS SAMPLE DOES NOT HAVE METADATA INFO .... assuming Powheg+Pythia8 for b-tagging SF")
  pass
pass
hWW_msg.info("Using "+ttbarDSID+" for b-tagging")


ToolSvc += CfgMgr.BTaggingEfficiencyTool("HWWBTaggingEfficiencyTool",
                                    OutputLevel               = WARNING,
                                    TaggerName                = hWWCommon.Jets.bTagName,
                                    OperatingPoint            = hWWCommon.Jets.bTagWP,
                                    JetAuthor                 = hWWCommon.Jets.inCont,
                                    ScaleFactorFileName       = hWWCommon.Jets.CDIFile,
                                    EfficiencyBCalibrations   = str(ttbarDSID),
                                    EfficiencyCCalibrations   = str(ttbarDSID),
                                    EfficiencyTCalibrations   = str(ttbarDSID),
                                    EfficiencyLightCalibrations   = str(ttbarDSID),
                                    SystematicsStrategy       = hWWCommon.Jets.systematicsStrategy,
                                    EigenvectorReductionB     = hWWCommon.Jets.systematicsReduction,
                                    EigenvectorReductionC     = hWWCommon.Jets.systematicsReduction,
                                    EigenvectorReductionLight = hWWCommon.Jets.systematicsReduction
                                    #BTagTool                  = ToolSvc.HWWBTagTool
                                    )
ToolSvc += CfgMgr.BTaggingSelectionTool("HWWBTaggingSelectionTool",
				    TaggerName                    = hWWCommon.Jets.bTagName,
				    OperatingPoint                = hWWCommon.Jets.bTagWP,
				    JetAuthor		      	          = hWWCommon.Jets.inCont,
				    FlvTagCutDefinitionsFileName	= hWWCommon.Jets.CDIFile,
				    )
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__BtagScaleFactorAlg( "HWWBtagScaleFactorAlg",
                                    #OutputLevel                   = VERBOSE,
                                    InputContainer                 = hWWCommon.Jets.finalCont,
                                    ContainersFinderTool           = ToolSvc.HWWContainersFinderTool,
                                    EfficiencySystematicVariations = hWWCommon.Jets.effiSysts,
                                    EfficiencyScaleFactorVarName   = hWWCommon.Jets.effiVarName,
                                    BTaggingEfficiencyTool         = ToolSvc.HWWBTaggingEfficiencyTool,
				    BTaggingSelectionTool	   = ToolSvc.HWWBTaggingSelectionTool,
                                    TaggerName                     = hWWCommon.Jets.bTagName,
                                    OperatingPoint                 = hWWCommon.Jets.bTagWPNumber
                                    )

# Only do the following, if we actually want to write the track jets
if hWWCommon.Jets.writeTrackJets :
    ToolSvc += CfgMgr.BTaggingEfficiencyTool("HWWBTaggingEfficiencyTrackJetTool",
                                        OutputLevel               = WARNING,
                                        TaggerName                = hWWCommon.Jets.bTagName,
                                        OperatingPoint            = hWWCommon.Jets.bTagWPTrackJets,
                                        JetAuthor                 = hWWCommon.Jets.inTrackJetsCont,
                                        ScaleFactorFileName       = hWWCommon.Jets.CDIFile,
                                        SystematicsStrategy       = hWWCommon.Jets.systematicsStrategy,
                                        EigenvectorReductionB     = hWWCommon.Jets.systematicsReduction,
                                        EigenvectorReductionC     = hWWCommon.Jets.systematicsReduction,
                                        EigenvectorReductionLight = hWWCommon.Jets.systematicsReduction
                                        #BTagTool                  = ToolSvc.HWWBTagTool
                                        )
    ToolSvc += CfgMgr.BTaggingSelectionTool("HWWBTaggingSelectionTrackJetTool",
                                    TaggerName                          = hWWCommon.Jets.bTagName,
                                    OperatingPoint                      = hWWCommon.Jets.bTagWPTrackJets,
                                    JetAuthor                           = hWWCommon.Jets.inTrackJetsCont,
                                    FlvTagCutDefinitionsFileName        = hWWCommon.Jets.CDIFile,
                                    )

    hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__BtagScaleFactorAlg( "HWWTrackJetBtagScaleFactorAlg",
                                        #OutputLevel                   = VERBOSE,
                                        InputContainer                 = hWWCommon.Jets.inTrackJetsCont,
                                        MinJetPt                       = 7.0*GeV,
                                        ContainersFinderTool           = ToolSvc.HWWContainersFinderTool,
                                        EfficiencySystematicVariations = hWWCommon.Jets.effiSysts,
                                        EfficiencyScaleFactorVarName   = hWWCommon.Jets.effiVarName,
                                        BTaggingEfficiencyTool         = ToolSvc.HWWBTaggingEfficiencyTrackJetTool,
					BTaggingSelectionTool	       = ToolSvc.HWWBTaggingSelectionTrackJetTool,
                                        TaggerName                     = hWWCommon.Jets.bTagName,
                                        OperatingPoint                 = hWWCommon.Jets.bTagWPTrackJetsNumber
                                        )
    pass
