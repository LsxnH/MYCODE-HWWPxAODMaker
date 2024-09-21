# ====================================================================
# In this file, we will create our own sub-sequence that always runs
# through all its algorithms, irespective of the algorithm accepting
# an event or not.
# We will attach all the electron calibration and systematic variation
# algorithms, as well as the electron pre-selection algorithm and
# scale-factor algorithm, and add them to this sequence.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWElectronCalibrationScaleFactor.py")


# ====================================================================
# Create instances of all needed electron tools and add them to the ToolService
# ====================================================================

# import PyCintex
import cppyy
cppyy.loadDictionary('ElectronPhotonSelectorToolsDict')
from ROOT import LikeEnum
from ROOT import egammaPID


# -----------------------------------------
# Likelihood ID
# -----------------------------------------

electronDecorationNames = []
electronSelectionTools  = []

transferValueSources = []
transferValueTargets = []

if hWWCommon.Electrons.calculateLH:

    from ElectronPhotonSelectorTools.ElectronPhotonSelectorToolsConf import AsgElectronLikelihoodTool

    confDir = "ElectronPhotonSelectorTools/offline/mc16_20170828/"

    ToolSvc += AsgElectronLikelihoodTool("HWWElectronLHSelectorTight",
                                         OutputLevel = WARNING,
                                         primaryVertexContainer = "PrimaryVertices",
                                         ConfigFile = confDir + "ElectronLikelihoodTightOfflineConfig2017_Smooth.conf"
                                         )

    ToolSvc += AsgElectronLikelihoodTool("HWWElectronLHSelectorMedium",
                                         OutputLevel = WARNING,
                                         primaryVertexContainer = "PrimaryVertices",
                                         ConfigFile = confDir + "ElectronLikelihoodMediumOfflineConfig2017_Smooth.conf"
                                         )

    ToolSvc += AsgElectronLikelihoodTool("HWWElectronLHSelectorLoose",
                                         OutputLevel = WARNING,
                                         primaryVertexContainer = "PrimaryVertices",
                                         ConfigFile = confDir + "ElectronLikelihoodLooseOfflineConfig2017_Smooth.conf"
                                         )

    ToolSvc += AsgElectronLikelihoodTool("HWWElectronLHSelectorLooseBLayer",
                                         OutputLevel = WARNING,
                                         primaryVertexContainer = "PrimaryVertices",
                                         ConfigFile = confDir + "ElectronLikelihoodLooseOfflineConfig2017_CutBL_Smooth.conf"
                                         )

    ToolSvc += AsgElectronLikelihoodTool("HWWElectronLHSelectorVeryLoose",
                                         OutputLevel = WARNING,
                                         primaryVertexContainer = "PrimaryVertices",
                                         ConfigFile = confDir + "ElectronLikelihoodVeryLooseOfflineConfig2017_Smooth.conf"
                                         )

    # Set electron tool and decorator name list, both must be in the same order
    electronSelectionToolsAndNames  = [ ["isLHTight",       ToolSvc.HWWElectronLHSelectorTight],
                                        ["isLHMedium",      ToolSvc.HWWElectronLHSelectorMedium],
                                        ["isLHLoose",       ToolSvc.HWWElectronLHSelectorLoose],
                                        ["isLHLooseBLayer", ToolSvc.HWWElectronLHSelectorLooseBLayer],
                                        ["isLHVeryLoose",   ToolSvc.HWWElectronLHSelectorVeryLoose] ]
    electronDecorationNames   = [item[0] for item in electronSelectionToolsAndNames]
    electronSelectionTools    = [item[1] for item in electronSelectionToolsAndNames]

else:

    # take the LH values from the input
    transferValueSources = ["DFCommonElectronsLHTight",
                            "DFCommonElectronsLHMedium",
                            "DFCommonElectronsLHLoose",
                            "DFCommonElectronsLHLooseBL",
                            "DFCommonElectronsLHVeryLoose"]
    transferValueTargets = ["isLHTight",
                            "isLHMedium",
                            "isLHLoose",
                            "isLHLooseBLayer",
                            "isLHVeryLoose"]

# -----------------------------------------
# Create an instance of the AsgElectronChargeIDSelectorTool
# -----------------------------------------
from ElectronPhotonSelectorTools.ElectronPhotonSelectorToolsConf import AsgElectronChargeIDSelectorTool
ToolSvc += AsgElectronChargeIDSelectorTool("HWWElectronChargeIDSelectorLoose",
                OutputLevel            = WARNING,
                primaryVertexContainer = "PrimaryVertices",
                TrainingFile           = "ElectronPhotonSelectorTools/ChargeID/ECIDS_20161125for2017Moriond.root"
                )

# -----------------------------------------
# Create instances of the EGammaAmbiguityTool
# -----------------------------------------
from ElectronPhotonSelectorTools.ElectronPhotonSelectorToolsConf import EGammaAmbiguityTool
ToolSvc += EGammaAmbiguityTool("HWWEGammaAmbiguityTool",
                               OutputLevel        = WARNING
                               )
ToolSvc += EGammaAmbiguityTool("HWWEGammaAmbiguityToolTight",
                               OutputLevel        = WARNING,
                               AcceptAmbiguous    = False
                               )


# -----------------------------------------
# Create an instance of the EgammaCalibrationAndSmearingTool
# -----------------------------------------
# Use a different flag if we have an AtlFastII input file
isAFII = 0
if hWWCommon.Global.inputSimulationType == "AFII" : isAFII = 1
ToolSvc += CfgMgr.CP__EgammaCalibrationAndSmearingTool( "HWWElectronCalibSmearTool",
                                                        OutputLevel        = WARNING,
                                                        ESModel            = hWWCommon.Electrons.ESModel,
                                                        decorrelationModel = hWWCommon.Electrons.decorrelationModel,
                                                        useAFII            = isAFII,
                                                        )

# -----------------------------------------
# Create an instance of the egamma IsolationCorrectionTool
# -----------------------------------------
ToolSvc += CfgMgr.CP__IsolationCorrectionTool( "HWWEGammaIsolationCorrectionTool",
                                               OutputLevel = WARNING,
                                               #CorrFile = "IsolationCorrections/v1/isolation_ptcorrections_rel20_2.root",
                                               IsMC     = hWWCommon.Global.inputIsSimulation
                                               )


# -----------------------------------------
# Create the instances of the electron isolation selection tools and configure them
# -----------------------------------------
electronIsoTools = []
for wpName in hWWCommon.Electrons.isoWorkingPointList :
    toolName = "IsoElectronTool"+wpName
    ToolSvc += CfgMgr.CP__IsolationSelectionTool(toolName, ElectronWP=wpName, OutputLevel = WARNING)
    electronIsoTools.append( getattr(ToolSvc,toolName) )
    pass


# ====================================================================
# Decorate the electrons with all needed variables
# ====================================================================
hWWCommonCalibSeq += CfgMgr.HWW__ElectronDecorationAlg( "HWWElectronDecorationAlg",
                                                        #OutputLevel  = DEBUG,
                                                        InputContainer                  = hWWCommon.Electrons.inCont,
                                                        SelectionToolList               = electronSelectionTools,
                                                        SelectionToolDecoList           = electronDecorationNames,
                                                        TransferValueSources            = transferValueSources,
                                                        TransferValueTargets            = transferValueTargets,
                                                        DoImpactParameter               = True,
                                                        DoAmbiguity                     = True,
                                                        EGammeAmbiguityTool             = ToolSvc.HWWEGammaAmbiguityTool,
                                                        EGammeAmbiguityToolTight        = ToolSvc.HWWEGammaAmbiguityToolTight,
                                                        DoChargeIDTagging               = hWWCommon.Electrons.doChargeIDTagging,
                                                        ElectronChargeIDSelectorTool    = ToolSvc.HWWElectronChargeIDSelectorLoose,
                                                        DoTruthInformation              = True
                                                        )

# ====================================================================
# Do the calibration of the electrons, including systematic variations
# ====================================================================
hWWCommonCalibSeq += CfgMgr.HWW__ElectronCalibrationSmearingAlg( "HWWElectronCalibrationSmearingAlg",
                                                                 #OutputLevel                   = VERBOSE,
                                                                 InputContainer                = hWWCommon.Electrons.inCont,
                                                                 OutputContainer               = hWWCommon.Electrons.calibCont,
                                                                 EgammaCalibrationTool         = ToolSvc.HWWElectronCalibSmearTool,
                                                                 MomentumSystematicVariations  = hWWCommon.Electrons.p4Systs,
                                                                 EGammeIsolationCorrectionTool = ToolSvc.HWWEGammaIsolationCorrectionTool
                                                                 )

# The isolation correction, and thus selection, has to be applied after calibration
hWWCommonCalibSeq += CfgMgr.HWW__ElectronDecorationAlg( "HWWElectronDecorationPostCalibAlg",
                                                        #OutputLevel  = DEBUG,
                                                        InputContainer             = hWWCommon.Electrons.calibCont,
                                                        IsolationToolList          = electronIsoTools,
                                                        IsolationToolDecoList      = hWWCommon.Electrons.passIsoVarNameList,
                                                        )
