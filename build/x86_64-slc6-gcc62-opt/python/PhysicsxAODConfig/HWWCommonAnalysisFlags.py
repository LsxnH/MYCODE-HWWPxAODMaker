##=============================================================================
## Name:        HWWCommonAnalysisFlags.py
##
## Author:      Karsten Koeneke
## Created:     August 2014
##
## Description: Here, all neccessary job flags that are commonly needed for
##              all Higgs->WW analyses are defined.
##=============================================================================

__doc__ = """Here, all neccessary job flags for the common aspects of all the Higgs->WW analyses are defined."""
__version__ = "0.0.1"
__author__  = "Karsten Koeneke <karsten.koeneke@cern.ch>"

from AthenaCommon.JobProperties import JobProperty, JobPropertyContainer
from AthenaCommon.JobProperties import jobproperties

# Import the module that allows to use named units, e.g. GeV
from AthenaCommon.SystemOfUnits import *

# Import the common helper functions
from PhysicsxAODConfig.HWWCommonHelpers import buildContainerNames

# Import ROOT
import PyUtils.RootUtils as ru
ROOT = ru.import_root()

# Import PyCintex to get enums from dictionaries for electron/muon isolation
import cppyy
cppyy.loadDictionary('xAODPrimitivesDict')
IsoEnums = ROOT.xAOD.Iso

# Get muon quality enums
cppyy.loadDictionary('xAODMuonDict')
MuonQualityEnums = ROOT.xAOD.Muon_v1



# Get the egamma enums
# cppyy.loadDictionary('xAODEgammaDict')
# EGammaEnums = ROOT.xAOD.



#=====================================================================
# First define container for the flags
#=====================================================================
class HWWCommonAnalysisFlags(JobPropertyContainer):
    """ The Higgs->WW common analysis flag/job property container."""
jobproperties.add_Container(HWWCommonAnalysisFlags)

#short-cut to get the HiggsWWCommonAnalysisFlags container with this one line:
#'from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon'
#Note that name has to be different to avoid problems with pickle
hWWCommon = jobproperties.HWWCommonAnalysisFlags

#=====================================================================
# Now define each flag and add it to the container
#=====================================================================

class Global(JobProperty):
    """Steer the common aspects of the H->WW analyses"""

    processReco            = True
    processTruth           = False
    statusOn               = True
    allowedTypes           = ['bool']
    StoredValue            = True
    logLevel               = 3 # 3=INFO, 2=DEBUG
    do1Lep                 = False
    do2Lep                 = False
    do3Lep                 = False
    do4Lep                 = False
    doFakeLep              = False
    doFakeWJets            = False
    doFakeZJets            = False
    doMediumOtherLeptons   = False
    doVeryLooseLH          = False
    doORNoMuNearJetRemoval = False
    doORNoMuNearJetRemovalNoBJetPrecedence = False
    doEventPreSelection    = True
    doTruthFlagging        = True
    doCalibrations         = True
    doSelections           = True
    doOverlapRemoval       = True
    doCandidateBuilding    = True
    doEffiScaleFactors     = True
    doOnlyEffiScaleFactors = False
    doFilterEffiSFSeq      = True
    doThinning             = True
    inputIsSimulation      = False # This is a default. It will be determined from the input automatically
    inputSimulationType    = "" # This is a default. It will be determined from the input automatically: "FullSim" or "AFII"
    mcSubCampaign          = "" # This is a default. It will be determined from the input automatically: "mc16a", "mc16d", or "mc16e"
    inputIsDAOD            = False # This is a default. It will be determined from the input automatically
    inputStreamName        = ""
    inputRelease           = "" # This is a default. It will be determined from the input automatically: e.g. "20.1", "20.7", "21.2"
    beamEnergy             = 6.5*TeV
    bunchSpacing           = 25 #[ns] The default. If input is 50ns, this will be changed automatically
    doGRLSelection         = True
    grlFileList            = [ "GoodRunsLists/data15_13TeV/20170619/data15_13TeV.periodAllYear_DetStatus-v89-pro21-02_Unknown_PHYS_StandardGRL_All_Good_25ns.xml",
                               "GoodRunsLists/data16_13TeV/20180129/data16_13TeV.periodAllYear_DetStatus-v89-pro21-01_DQDefects-00-02-04_PHYS_StandardGRL_All_Good_25ns.xml",
                               "GoodRunsLists/data17_13TeV/20180619/data17_13TeV.periodAllYear_DetStatus-v99-pro22-01_Unknown_PHYS_StandardGRL_All_Good_25ns_Triggerno17e33prim.xml"
                             ]
    doPileupReweighting    = True

    PRWConfigFilesFSmc16a  = [ "PhysicsxAODConfig/HWW_merged_prw_config_mc16a_FS_v1.root" ]
    LumiCalcFilesData1516  = [ "GoodRunsLists/data15_13TeV/20170619/PHYS_StandardGRL_All_Good_25ns_276262-284484_OflLumi-13TeV-008.root",
                               "GoodRunsLists/data16_13TeV/20180129/PHYS_StandardGRL_All_Good_25ns_297730-311481_OflLumi-13TeV-009.root" ]

    PRWConfigFilesFSmc16d  = [ "PhysicsxAODConfig/HWW_merged_prw_config_mc16d_FS_v1.root" ]
    PRWActualMuData17      = [ "GoodRunsLists/data17_13TeV/20180619/physics_25ns_Triggerno17e33prim.actualMu.OflLumi-13TeV-010.root" ]
    LumiCalcFilesData17    = [ "GoodRunsLists/data17_13TeV/20180619/physics_25ns_Triggerno17e33prim.lumicalc.OflLumi-13TeV-010.root" ]

    doP4Systematics            = True
    doEffiSystematics          = True
    doTriggerSelection         = True
    doTriggerMatching          = True
    requireAlgList             = [] # This will contain the algorithm instance names that everyone needs to add to their requireAlgs output stream
    breakUpAuxContainers       = False
    # auxContsToBreakUp          = [ "EventInfoAux.", "AntiKt4PV0TrackJetsAux." ]
    auxContsToBreakUp          = [  ]
    writeLeptonTrackParticles  = False
    writeLeptonCaloClusters    = False
    writeJetCaloClusters       = False
    writeTruthParticles        = False
    pass
hWWCommon.add_JobProperty(Global)





class Trigger(JobProperty):
    """Common trigger definitions for all the H->WW analyses"""
    statusOn                     = True
    allowedTypes                 = ['bool']
    StoredValue                  = True
    triggerMatchPrefix           = "trigMatch_"
    triggerPassPrefix            = "pass_"
    ## Extended list of trigger chains ##
    
    electronTriggerList          = [ "HLT_e24_lhmedium_L1EM20VH",             # 2015
                                     "HLT_e24_lhmedium_L1EM18VH",
                                     "HLT_e60_lhmedium",
                                     "HLT_e120_lhloose",
                                     "HLT_e24_lhtight_nod0_ivarloose",        # 2016
                                     "HLT_e26_lhtight_nod0_ivarloose",
                                     "HLT_e17_lhloose",                        # Legs from the electron-muon triggers 2015
                                     "HLT_e7_lhmedium",
                                     "HLT_e17_lhloose_nod0",                   # Legs from the electron-muon triggers 2016
                                     "HLT_e7_lhmedium_nod0",
                                     "HLT_e60_lhmedium_nod0",                  # 2016 + 2017
                                     "HLT_e140_lhloose_nod0",
                                     "HLT_e28_lhtight_nod0_ivarloose",         # 2017
                                     "HLT_e300_etcut"
                                   ]
    diElectronTriggerList        = [ "HLT_2e12_lhloose_L12EM10VH",             # 2015
                                     "HLT_2e17_lhvloose_nod0",                 # 2016 + 2017
                                     "HLT_2e17_lhvloose_nod0_L12EM15VHI*",     # 2017
                                     
                                   ]
    multiElectronTriggerList     = [ "HLT_e17_lhloose_2e9_lhloose",            # 2015
                                     "HLT_e17_lhloose_nod0_2e9_lhloose_nod0",  # 2016
                                     "HLT_e24_lhvloose_nod0_2e12_lhvloose_nod0_L1EM20VH_3EM10VH" # 2017
                                   ]
    
    muonTriggerList              = [ "HLT_mu20_iloose_L1MU15",                 # 2015
                                     "HLT_mu50",
                                     "HLT_mu24_ivarmedium",                    # 2016
                                     "HLT_mu26_imedium",
                                     "HLT_mu24_imedium", 
                                    # "HLT_mu14",                              # Legs from the electron-muon triggers    remove the R20.7 only trigger. 
                                    # "HLT_mu24",
                                     "HLT_mu26_ivarmedium",                    # 2016 + 2017
                                     "HLT_mu50",                               # 2017
                                     "HLT_mu60_0eta105_msonly",
                                     "HLT_mu50_0eta105_msonly"                 #New R21 muon trigger
                                     "HLT_mu26_ivarmedium_OR_HLT_mu50"

                                   ] 
    muonTriggerSFFullList        = [ ["HLT_mu20_iloose_L1MU15_OR_HLT_mu50","HLT_mu24_ivarmedium_OR_HLT_mu50"],
                                     ["HLT_mu20_iloose_L1MU15_OR_HLT_mu50","HLT_mu26_ivarmedium_OR_HLT_mu50"],
                                    # ["HLT_mu10","HLT_mu10"],                 #remove the R20.7 only trigger.
                                    # ["HLT_mu18", "HLT_mu22"],
                                    # ["HLT_mu8noL1", "HLT_mu8noL1"],
                                    # ["HLT_mu14","HLT_mu14"],
                                    # ["HLT_mu24","HLT_mu24"]
                                                                     ]  # The first one of the pair is always for data2015, the second one for data2016
    diMuonTriggerList            = [  "HLT_mu18_mu8noL1",                       # 2015
                                      "HLT_2mu10",
                                      "HLT_mu20_mu8noL1",                       # 2016
                                      "HLT_mu22_mu8noL1",                       # 2016 + 2017
                                      "HLT_2mu14",                              # 2017
                                      "HLT_mu22_mu8noL1_calotag_0eta010"
                                   ]
    multiMuonTriggerList         = [ "HLT_3mu6",
                                     "HLT_3mu6_msonly",
                                     "HLT_mu20_2mu4noL1",
                                     "HLT_3mu4",
                                     "HLT_2mu14",                              #New R21 multi-muon triggers
                                     "HLT_mu22_mu8noL1"
                                   ]
    
    muonTriggerSFReducedList     = [ "HLT_mu20_iloose_L1MU15_OR_HLT_mu50" ]
    
    ## Additional electron-muon trigger chains
    electronMuonTriggerList      = [ "HLT_e17_lhloose_mu14",                   # 2015
                                     "HLT_e7_lhmedium_mu24",
                                     "HLT_e17_lhloose_nod0_mu14",              # 2016 + 2017
                                     "HLT_e7_lhmedium_nod0_mu24",
                                     "HLT_e26_lhmedium_nod0_mu8noL1",          # 2017
                                   ] 
    multiElectronMuonTriggerList = [ "HLT_2e12_lhloose_mu10",                  # 2015
                                     "HLT_e12_lhloose_2mu10",
                                     "HLT_2e12_lhloose_nod0_mu10",             # 2016 + 2017
                                     "HLT_e12_lhloose_nod0_2mu10",
                                   ]
    
    singleLeptonTriggerList      = trigList = muonTriggerList + electronTriggerList
    diLeptonTriggerList          = diMuonTriggerList + diElectronTriggerList + electronMuonTriggerList
    multiLeptonTriggerList       = multiMuonTriggerList + multiElectronTriggerList + multiElectronMuonTriggerList
    allLeptonTriggerList         = singleLeptonTriggerList + diLeptonTriggerList + multiLeptonTriggerList
    metTriggerList               = [ "HLT_xe70" ]
    allTriggerList               = allLeptonTriggerList + metTriggerList
    pass
hWWCommon.add_JobProperty(Trigger)





class Electrons(JobProperty):
    """Definitions for the common electrons of all the H->WW analyses"""
    statusOn            = True
    allowedTypes        = ['bool']
    StoredValue         = True
    calculateLH         = False # input already has correct LH values now
    doChargeIDTagging   = False # input already has required quantities now
    inCont              = "Electrons"
    calibCont           = "HWWCalibElectrons"
    calibPreSelCont     = "HWWCalibPreSelElectrons"
    calibPreSelORCont   = "HWWCalibPreSelORElectrons"
    finalCont           = "HWWElectrons"
    finalAllPtSortCont  = "FinalAllPtSort"+finalCont
    def finalContList(self) :
        """ The names of the final electron containers. This is a list because every
        4-vector systematic variation is stored in its own container. Thus, we
        are building the list of all these containers using a helper function."""
        return buildContainerNames(baseName=self.finalCont, systList=hWWCommon.Electrons.p4Systs)

    ESModel                 = "es2017_R21_v1"

    decorrelationModel      = "1NP_v1"
    p4Systs                 = ["EG_RESOLUTION_ALL__1down", "EG_RESOLUTION_ALL__1up",
                               "EG_SCALE_AF2__1down",      "EG_SCALE_AF2__1up",
                               "EG_SCALE_ALL__1down",      "EG_SCALE_ALL__1up"]

    # decorrelationModel      = "FULL_v1"
    # p4Systs                 = ["EG_RESOLUTION_MATERIALCALO__1down",       "EG_RESOLUTION_MATERIALCALO__1up",
    #                            "EG_RESOLUTION_MATERIALCRYO__1down",       "EG_RESOLUTION_MATERIALCRYO__1up",
    #                            "EG_RESOLUTION_MATERIALGAP__1down",        "EG_RESOLUTION_MATERIALGAP__1up",
    #                            "EG_RESOLUTION_MATERIALIBL__1down",        "EG_RESOLUTION_MATERIALIBL__1up",
    #                            "EG_RESOLUTION_MATERIALID__1down",         "EG_RESOLUTION_MATERIALID__1up",
    #                            "EG_RESOLUTION_MATERIALPP0__1down",        "EG_RESOLUTION_MATERIALPP0__1up",
    #                            "EG_RESOLUTION_PILEUP__1down",             "EG_RESOLUTION_PILEUP__1up",
    #                            "EG_RESOLUTION_SAMPLINGTERM__1down",       "EG_RESOLUTION_SAMPLINGTERM__1up",
    #                            "EG_RESOLUTION_ZSMEARING__1down",          "EG_RESOLUTION_ZSMEARING__1up",
    #                            "EG_SCALE_AF2__1down",                     "EG_SCALE_AF2__1up",
    #                            "EG_SCALE_E4SCINTILLATOR__ETABIN0__1down", "EG_SCALE_E4SCINTILLATOR__ETABIN0__1up",
    #                            "EG_SCALE_E4SCINTILLATOR__ETABIN1__1down", "EG_SCALE_E4SCINTILLATOR__ETABIN1__1up",
    #                            "EG_SCALE_E4SCINTILLATOR__ETABIN2__1down", "EG_SCALE_E4SCINTILLATOR__ETABIN2__1up",
    #                            "EG_SCALE_G4__1down",                      "EG_SCALE_G4__1up",
    #                            "EG_SCALE_L1GAIN__1down",                  "EG_SCALE_L1GAIN__1up",
    #                            "EG_SCALE_L2GAIN__1down",                  "EG_SCALE_L2GAIN__1up",
    #                            "EG_SCALE_LARCALIB__ETABIN0__1down",       "EG_SCALE_LARCALIB__ETABIN0__1up",
    #                            "EG_SCALE_LARCALIB__ETABIN1__1down",       "EG_SCALE_LARCALIB__ETABIN1__1up",
    #                            "EG_SCALE_LARELECCALIB__1down",            "EG_SCALE_LARELECCALIB__1up",
    #                            "EG_SCALE_LARELECUNCONV__ETABIN0__1down",  "EG_SCALE_LARELECUNCONV__ETABIN0__1up",
    #                            "EG_SCALE_LARELECUNCONV__ETABIN1__1down",  "EG_SCALE_LARELECUNCONV__ETABIN1__1up",
    #                            "EG_SCALE_LARUNCONVCALIB__ETABIN0__1down", "EG_SCALE_LARUNCONVCALIB__ETABIN0__1up",
    #                            "EG_SCALE_LARUNCONVCALIB__ETABIN1__1down", "EG_SCALE_LARUNCONVCALIB__ETABIN1__1up",
    #                            "EG_SCALE_MATCALO__ETABIN0__1down",        "EG_SCALE_MATCALO__ETABIN0__1up",
    #                            "EG_SCALE_MATCALO__ETABIN10__1down",       "EG_SCALE_MATCALO__ETABIN10__1up",
    #                            "EG_SCALE_MATCALO__ETABIN11__1down",       "EG_SCALE_MATCALO__ETABIN11__1up",
    #                            "EG_SCALE_MATCALO__ETABIN1__1down",        "EG_SCALE_MATCALO__ETABIN1__1up",
    #                            "EG_SCALE_MATCALO__ETABIN2__1down",        "EG_SCALE_MATCALO__ETABIN2__1up",
    #                            "EG_SCALE_MATCALO__ETABIN3__1down",        "EG_SCALE_MATCALO__ETABIN3__1up",
    #                            "EG_SCALE_MATCALO__ETABIN4__1down",        "EG_SCALE_MATCALO__ETABIN4__1up",
    #                            "EG_SCALE_MATCALO__ETABIN5__1down",        "EG_SCALE_MATCALO__ETABIN5__1up",
    #                            "EG_SCALE_MATCALO__ETABIN6__1down",        "EG_SCALE_MATCALO__ETABIN6__1up",
    #                            "EG_SCALE_MATCALO__ETABIN7__1down",        "EG_SCALE_MATCALO__ETABIN7__1up",
    #                            "EG_SCALE_MATCALO__ETABIN8__1down",        "EG_SCALE_MATCALO__ETABIN8__1up",
    #                            "EG_SCALE_MATCALO__ETABIN9__1down",        "EG_SCALE_MATCALO__ETABIN9__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN0__1down",        "EG_SCALE_MATCRYO__ETABIN0__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN10__1down",       "EG_SCALE_MATCRYO__ETABIN10__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN11__1down",       "EG_SCALE_MATCRYO__ETABIN11__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN1__1down",        "EG_SCALE_MATCRYO__ETABIN1__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN2__1down",        "EG_SCALE_MATCRYO__ETABIN2__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN3__1down",        "EG_SCALE_MATCRYO__ETABIN3__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN4__1down",        "EG_SCALE_MATCRYO__ETABIN4__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN5__1down",        "EG_SCALE_MATCRYO__ETABIN5__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN6__1down",        "EG_SCALE_MATCRYO__ETABIN6__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN7__1down",        "EG_SCALE_MATCRYO__ETABIN7__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN8__1down",        "EG_SCALE_MATCRYO__ETABIN8__1up",
    #                            "EG_SCALE_MATCRYO__ETABIN9__1down",        "EG_SCALE_MATCRYO__ETABIN9__1up",
    #                            "EG_SCALE_MATID__ETABIN0__1down",          "EG_SCALE_MATID__ETABIN0__1up",
    #                            "EG_SCALE_MATID__ETABIN1__1down",          "EG_SCALE_MATID__ETABIN1__1up",
    #                            "EG_SCALE_MATID__ETABIN2__1down",          "EG_SCALE_MATID__ETABIN2__1up",
    #                            "EG_SCALE_MATID__ETABIN3__1down",          "EG_SCALE_MATID__ETABIN3__1up",
    #                            "EG_SCALE_MATPP0__ETABIN0__1down",         "EG_SCALE_MATPP0__ETABIN0__1up",
    #                            "EG_SCALE_MATPP0__ETABIN1__1down",         "EG_SCALE_MATPP0__ETABIN1__1up",
    #                            "EG_SCALE_PEDESTAL__1down",                "EG_SCALE_PEDESTAL__1up",
    #                            "EG_SCALE_PS_BARREL_B12__1down",           "EG_SCALE_PS_BARREL_B12__1up",
    #                            "EG_SCALE_PS__ETABIN0__1down",             "EG_SCALE_PS__ETABIN0__1up",
    #                            "EG_SCALE_PS__ETABIN1__1down",             "EG_SCALE_PS__ETABIN1__1up",
    #                            "EG_SCALE_PS__ETABIN2__1down",             "EG_SCALE_PS__ETABIN2__1up",
    #                            "EG_SCALE_PS__ETABIN3__1down",             "EG_SCALE_PS__ETABIN3__1up",
    #                            "EG_SCALE_PS__ETABIN4__1down",             "EG_SCALE_PS__ETABIN4__1up",
    #                            "EG_SCALE_PS__ETABIN5__1down",             "EG_SCALE_PS__ETABIN5__1up",
    #                            "EG_SCALE_PS__ETABIN6__1down",             "EG_SCALE_PS__ETABIN6__1up",
    #                            "EG_SCALE_PS__ETABIN7__1down",             "EG_SCALE_PS__ETABIN7__1up",
    #                            "EG_SCALE_PS__ETABIN8__1down",             "EG_SCALE_PS__ETABIN8__1up",
    #                            "EG_SCALE_S12__ETABIN0__1down",            "EG_SCALE_S12__ETABIN0__1up",
    #                            "EG_SCALE_S12__ETABIN1__1down",            "EG_SCALE_S12__ETABIN1__1up",
    #                            "EG_SCALE_S12__ETABIN2__1down",            "EG_SCALE_S12__ETABIN2__1up",
    #                            "EG_SCALE_S12__ETABIN3__1down",            "EG_SCALE_S12__ETABIN3__1up",
    #                            "EG_SCALE_S12__ETABIN4__1down",            "EG_SCALE_S12__ETABIN4__1up",
    #                            "EG_SCALE_TOPOCLUSTER_THRES__1down",       "EG_SCALE_TOPOCLUSTER_THRES__1up",
    #                            "EG_SCALE_WTOTS1__1down",                  "EG_SCALE_WTOTS1__1up",
    #                            "EG_SCALE_ZEESTAT__1down",                 "EG_SCALE_ZEESTAT__1up",
    #                            "EG_SCALE_ZEESYST__1down",                 "EG_SCALE_ZEESYST__1up"]

    # The file path prefix for all scale-factor configuration files
    correctionFilePathPrefix   = "ElectronEfficiencyCorrection/2015_2016/rel20.7/Moriond_February2017_v1/"
    correctionFilePathPrefixV2 = "ElectronEfficiencyCorrection/2015_2016/rel20.7/Moriond_February2017_v2/"

    correctionFilePathPrefix_Moriond2018_V1    = "ElectronEfficiencyCorrection/2015_2017/rel21.2/Moriond_February2018_v1/"
    correctionFilePathPrefix_Moriond2018_V2    = "ElectronEfficiencyCorrection/2015_2017/rel21.2/Moriond_February2018_v2/"
    correctionFilePathPrefix_Consolidation2018 = "ElectronEfficiencyCorrection/2015_2017/rel21.2/Consolidation_September2018_v1/"

    # Identification scale-factors
    effiVarName             = "effiSF"
    effiVarNameList         = [ effiVarName+"LooseAndBLayerLH", effiVarName+"MediumLH", effiVarName+"TightLH" ]
    effiCorrectionFiles     = [correctionFilePathPrefix_Moriond2018_V1+"offline/efficiencySF.offline.LooseAndBLayerLLH_d0z0_v13.root",
                               correctionFilePathPrefix_Moriond2018_V1+"offline/efficiencySF.offline.MediumLLH_d0z0_v13.root",
                               correctionFilePathPrefix_Moriond2018_V1+"offline/efficiencySF.offline.TightLLH_d0z0_v13.root" ]
    effiIDCorrelationModel  = "SIMPLIFIED"
    effiSysts               = ["EL_EFF_ID_CorrUncertaintyNP0__1down", "EL_EFF_ID_CorrUncertaintyNP0__1up",
                               "EL_EFF_ID_CorrUncertaintyNP1__1down", "EL_EFF_ID_CorrUncertaintyNP1__1up",
                               "EL_EFF_ID_CorrUncertaintyNP2__1down", "EL_EFF_ID_CorrUncertaintyNP2__1up",
                               "EL_EFF_ID_CorrUncertaintyNP3__1down", "EL_EFF_ID_CorrUncertaintyNP3__1up",
                               "EL_EFF_ID_CorrUncertaintyNP4__1down", "EL_EFF_ID_CorrUncertaintyNP4__1up",
                               "EL_EFF_ID_CorrUncertaintyNP5__1down", "EL_EFF_ID_CorrUncertaintyNP5__1up",
                               "EL_EFF_ID_CorrUncertaintyNP6__1down", "EL_EFF_ID_CorrUncertaintyNP6__1up",
                               "EL_EFF_ID_CorrUncertaintyNP7__1down", "EL_EFF_ID_CorrUncertaintyNP7__1up",
                               "EL_EFF_ID_CorrUncertaintyNP8__1down", "EL_EFF_ID_CorrUncertaintyNP8__1up",
                               "EL_EFF_ID_CorrUncertaintyNP9__1down", "EL_EFF_ID_CorrUncertaintyNP9__1up",
                               "EL_EFF_ID_CorrUncertaintyNP10__1down", "EL_EFF_ID_CorrUncertaintyNP10__1up",
                               "EL_EFF_ID_CorrUncertaintyNP11__1down", "EL_EFF_ID_CorrUncertaintyNP11__1up",
                               "EL_EFF_ID_CorrUncertaintyNP12__1down", "EL_EFF_ID_CorrUncertaintyNP12__1up",
                               "EL_EFF_ID_CorrUncertaintyNP13__1down", "EL_EFF_ID_CorrUncertaintyNP13__1up",
                               "EL_EFF_ID_CorrUncertaintyNP14__1down", "EL_EFF_ID_CorrUncertaintyNP14__1up",
                               "EL_EFF_ID_CorrUncertaintyNP15__1down", "EL_EFF_ID_CorrUncertaintyNP15__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP0__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP0__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP1__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP1__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP2__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP2__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP3__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP3__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP4__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP4__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP5__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP5__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP6__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP6__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP7__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP7__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP8__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP8__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP9__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP9__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP10__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP10__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP11__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP11__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP12__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP12__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP13__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP13__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP14__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP14__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP15__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP15__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP16__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP16__1up",
                               "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP17__1down", "EL_EFF_ID_SIMPLIFIED_UncorrUncertaintyNP17__1up"]

    # Reconstruction scale-factors
    effiRecoVarNameList         = [effiVarName+"RecoTrk"]
    effiRecoCorrectionFiles     = [correctionFilePathPrefix_Moriond2018_V2+"offline/efficiencySF.offline.RecoTrk.root"]
    effiRecoCorrelationModel    = "TOTAL"
    effiRecoSysts               = ["EL_EFF_Reco_TOTAL_1NPCOR_PLUS_UNCOR__1down", "EL_EFF_Reco_TOTAL_1NPCOR_PLUS_UNCOR__1up"]

    # Trigger scale-factors
    effiSFTrigVarNameList       = [effiVarName+"Trig_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0_wrtOffline_MediumLHIsoGradient",
                                   effiVarName+"Trig_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0_wrtOffline_TightLHIsoGradient",
                                   effiVarName+"Trig_e17_lhloose_2016_e17_lhloose_nod0_wrtOffline_MediumLHIsoGradient",
                                   effiVarName+"Trig_e17_lhloose_2016_e17_lhloose_nod0_wrtOffline_TightLHIsoGradient",
                                   effiVarName+"Trig_e7_lhmedium_2016_e7_lhmedium_nod0_wrtOffline_MediumLHIsoGradient",
                                   effiVarName+"Trig_e7_lhmedium_2016_e7_lhmedium_nod0_wrtOffline_TightLHIsoGradient",
                                   effiVarName+"Trig_singleEl_preICHEP_wrtOffline_MediumLHIsoGradient",
                                   effiVarName+"Trig_singleEl_preICHEP_wrtOffline_TightLHIsoGradient",
                                   effiVarName+"Trig_singleEl_postICHEP_wrtOffline_MediumLHIsoGradient",
                                   effiVarName+"Trig_singleEl_postICHEP_wrtOffline_TightLHIsoGradient",
                                   effiVarName+"Trig_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0_wrtOffline_TightLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_e17_lhloose_2016_e17_lhloose_nod0_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_e17_lhloose_2016_e17_lhloose_nod0_wrtOffline_TightLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_e7_lhmedium_2016_e7_lhmedium_nod0_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_e7_lhmedium_2016_e7_lhmedium_nod0_wrtOffline_TightLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_singleEl_preICHEP_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_singleEl_preICHEP_wrtOffline_TightLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_singleEl_postICHEP_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_singleEl_postICHEP_wrtOffline_TightLHIsoFixedCutTightTrackOnly",
                                   effiVarName+"Trig_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0_wrtOffline_TightLHIsoLoose",
                                   effiVarName+"Trig_e17_lhloose_2016_e17_lhloose_nod0_wrtOffline_TightLHIsoLoose",
                                   effiVarName+"Trig_e7_lhmedium_2016_e7_lhmedium_nod0_wrtOffline_TightLHIsoLoose",
                                   effiVarName+"Trig_singleEl_preICHEP_wrtOffline_TightLHIsoLoose",
                                   effiVarName+"Trig_singleEl_postICHEP_wrtOffline_TightLHIsoLoose"]
    effiSFTrigCorrectionFiles   = [correctionFilePathPrefix+"trigger/efficiencySF.DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e17_lhloose_2016_e17_lhloose_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e17_lhloose_2016_e17_lhloose_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e7_lhmedium_2016_e7_lhmedium_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e7_lhmedium_2016_e7_lhmedium_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e24_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e24_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e17_lhloose_2016_e17_lhloose_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e17_lhloose_2016_e17_lhloose_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e7_lhmedium_2016_e7_lhmedium_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e7_lhmedium_2016_e7_lhmedium_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e24_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e24_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0.TightLLH_d0z0_v11_isolLoose.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e17_lhloose_2016_e17_lhloose_nod0.TightLLH_d0z0_v11_isolLoose.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.MULTI_L_2015_e7_lhmedium_2016_e7_lhmedium_nod0.TightLLH_d0z0_v11_isolLoose.root",
                                   "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e24_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolLoose.root",
                                   correctionFilePathPrefix+"trigger/efficiencySF.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolLoose.root"]
    effiSFTrigCorrelationModel  = "TOTAL"
    effiSFTrigSysts             = ["EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR__1down", "EL_EFF_Trigger_TOTAL_1NPCOR_PLUS_UNCOR__1up"]

    # Trigger efficiencies
    effiTrigVarNameList         = ["effiTrig_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0_wrtOffline_MediumLHIsoGradient",
                                   "effiTrig_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0_wrtOffline_TightLHIsoGradient",
                                   "effiTrig_e17_lhloose_2016_e17_lhloose_nod0_wrtOffline_MediumLHIsoGradient",
                                   "effiTrig_e17_lhloose_2016_e17_lhloose_nod0_wrtOffline_TightLHIsoGradient",
                                   "effiTrig_e7_lhmedium_2016_e7_lhmedium_nod0_wrtOffline_MediumLHIsoGradient",
                                   "effiTrig_e7_lhmedium_2016_e7_lhmedium_nod0_wrtOffline_TightLHIsoGradient",
                                   "effiTrig_singleEl_preICHEP_wrtOffline_MediumLHIsoGradient",
                                   "effiTrig_singleEl_preICHEP_wrtOffline_TightLHIsoGradient",
                                   "effiTrig_singleEl_postICHEP_wrtOffline_MediumLHIsoGradient",
                                   "effiTrig_singleEl_postICHEP_wrtOffline_TightLHIsoGradient",
                                   "effiTrig_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   "effiTrig_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0_wrtOffline_TightLHIsoFixedCutTightTrackOnly",
                                   "effiTrig_e17_lhloose_2016_e17_lhloose_nod0_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   "effiTrig_e17_lhloose_2016_e17_lhloose_nod0_wrtOffline_TightLHIsoFixedCutTightTrackOnly",
                                   "effiTrig_e7_lhmedium_2016_e7_lhmedium_nod0_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   "effiTrig_e7_lhmedium_2016_e7_lhmedium_nod0_wrtOffline_TightLHIsoFixedCutTightTrackOnly",
                                   "effiTrig_singleEl_preICHEP_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   "effiTrig_singleEl_preICHEP_wrtOffline_TightLHIsoFixedCutTightTrackOnly",
                                   "effiTrig_singleEl_postICHEP_wrtOffline_MediumLHIsoFixedCutTightTrackOnly",
                                   "effiTrig_singleEl_postICHEP_wrtOffline_TightLHIsoFixedCutTightTrackOnly"]
    effiTrigCorrectionFiles     = [correctionFilePathPrefix+"trigger/efficiency.DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiency.DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiency.MULTI_L_2015_e17_lhloose_2016_e17_lhloose_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiency.MULTI_L_2015_e17_lhloose_2016_e17_lhloose_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiency.MULTI_L_2015_e7_lhmedium_2016_e7_lhmedium_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiency.MULTI_L_2015_e7_lhmedium_2016_e7_lhmedium_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/trigger/efficiency.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e24_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/trigger/efficiency.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e24_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiency.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.MediumLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiency.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolGradient.root",
                                   correctionFilePathPrefix+"trigger/efficiency.DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiency.DI_E_2015_e12_lhloose_L1EM10VH_2016_e17_lhvloose_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiency.MULTI_L_2015_e17_lhloose_2016_e17_lhloose_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiency.MULTI_L_2015_e17_lhloose_2016_e17_lhloose_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiency.MULTI_L_2015_e7_lhmedium_2016_e7_lhmedium_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiency.MULTI_L_2015_e7_lhmedium_2016_e7_lhmedium_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/trigger/efficiency.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e24_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   "ElectronEfficiencyCorrection/2015_2016/rel20.7/ICHEP_June2016_v3/trigger/efficiency.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e24_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiency.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.MediumLLH_d0z0_v11_isolFixedCutTightTrackOnly.root",
                                   correctionFilePathPrefix+"trigger/efficiency.SINGLE_E_2015_e24_lhmedium_L1EM20VH_OR_e60_lhmedium_OR_e120_lhloose_2016_e26_lhtight_nod0_ivarloose_OR_e60_lhmedium_nod0_OR_e140_lhloose_nod0.TightLLH_d0z0_v11_isolFixedCutTightTrackOnly.root"]

    effiTrigCorrelationModel    = "TOTAL"
    effiTrigSysts               = ["EL_EFF_TriggerEff_TOTAL_1NPCOR_PLUS_UNCOR__1down", "EL_EFF_TriggerEff_TOTAL_1NPCOR_PLUS_UNCOR__1up"]

    # Isolation scale-factors
    effiIsoVarNameList     = [effiVarName+"IsoFCLoose_wrtLooseAndBLayerLH",
                              effiVarName+"IsoFCLoose_wrtMediumLH",
                              effiVarName+"IsoFCLoose_wrtTightLH",
                              effiVarName+"IsoFCTight_wrtLooseAndBLayerLH",
                              effiVarName+"IsoFCTight_wrtMediumLH",
                              effiVarName+"IsoFCTight_wrtTightLH",
                              effiVarName+"IsoFCHighPtCaloOnly_wrtLooseAndBLayerLH",
                              effiVarName+"IsoFCHighPtCaloOnly_wrtMediumLH",
                              effiVarName+"IsoFCHighPtCaloOnly_wrtTightLH",
                              effiVarName+"IsoGradient_wrtLooseAndBLayerLH",
                              effiVarName+"IsoGradient_wrtMediumLH",
                              effiVarName+"IsoGradient_wrtTightLH",
                              effiVarName+"IsoLoosePrompt_wrtTightLH",
                              effiVarName+"IsoLoosePromptCFTMedium_wrtTightLH"]
    effiIsoCorrectionFiles = [correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.LooseAndBLayerLLH_d0z0_v13_FCLoose.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.MediumLLH_d0z0_v13_FCLoose.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.TightLLH_d0z0_v13_FCLoose.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.LooseAndBLayerLLH_d0z0_v13_FCTight.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.MediumLLH_d0z0_v13_FCTight.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.TightLLH_d0z0_v13_FCTight.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.LooseAndBLayerLLH_d0z0_v13_FCHighPtCaloOnly.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.MediumLLH_d0z0_v13_FCHighPtCaloOnly.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.TightLLH_d0z0_v13_FCHighPtCaloOnly.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.LooseAndBLayerLLH_d0z0_v13_Gradient.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.MediumLLH_d0z0_v13_Gradient.root",
                              correctionFilePathPrefix_Consolidation2018+"isolation/efficiencySF.Isolation.TightLLH_d0z0_v13_Gradient.root",
                              "PhysicsxAODConfig/efficiencySF.Isolation.TightLLH_d0z0_v11_isolLoose_PromptLeptonIso.root",
                              "PhysicsxAODConfig/efficiencySF.Isolation.TightLLH_d0z0_v11_isolLoose_PromptLeptonIsoAndCFTMedium.root"]

    effiIsoCorrelationModel= "TOTAL"
    effiIsoSysts           = ["EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR__1down", "EL_EFF_Iso_TOTAL_1NPCOR_PLUS_UNCOR__1up"]


    # Isolation working points to use for lepton flagging
    isoWorkingPointList  = ["FCLoose", "FCTight", "FCHighPtCaloOnly", "Gradient", # SF available, configured above
                            "FixedCutPflowTight", "FixedCutPflowLoose",
                            "FCLoose_FixedRad", "FCTight_FixedRad", "FCTightTrackOnly_FixedRad",
                            "Gradient_exp", "FixedCutTrackCone40", "FCTightTrackOnly_new"]
    passIsoVarNameList   = [ "passIso"+wpName for wpName in isoWorkingPointList ]

    # Now come the pre-selection cuts (used for overlap removal, MET-making, and going into "otherElectrons")
    class preSelection(object):
        #cutObjectQualityMask           = xAOD::BADCLUSELECTRON
        cutObjectQualityMask           = 1
        cutPtMin                       = 10.0*GeV
        cutAbsEtaMax                   = 2.47
        #cutAbsEtaCrackMin              = 1.37
        #cutAbsEtaCrackMax              = 1.52
        cutIDList                      = [ "isLHLoose" ] #mgeisen: this is for Xchecking with r20.7, set to isLHVeryLoose when XCheck is done!
        cutIDPtMinList                 = [ 0.0*GeV ]
        cutIDListMedium                = [ "isLHMedium" ]    # For testing. Only used if command-line option doMediumOtherLeptons=True is set
        cutIDListVeryLoose             = [ "isLHVeryLoose" ] # Only used if command-line option doVeryLooseLH=True is set
        removeSelfOverlap              = True
        cutZ0SinThetaMax               = 0.5
        cutD0SignificanceMax           = 5.0
        fakeWJets_cutZ0SinThetaMax     = 0.5 # KEEP THEM AT NOMINAL, NO IMPROVEMENT EXPECTED. For W+jets or Z+jets fakes, used if hWWCommon.Global.doFakeWJets=True OR doFakeZJets=True
        fakeWJets_cutD0SignificanceMax = 5.0 # KEEP THEM AT NOMINAL, NO IMPROVEMENT EXPECTED. For W+jets or Z+jets fakes, used if hWWCommon.Global.doFakeWJets=True OR doFakeZJets=True
        #fakeWJets_cutZ0SinThetaMax     = 1.5  # For W+jets or Z+jets fakes, used if hWWCommon.Global.doFakeWJets=True OR doFakeZJets=True
        #fakeWJets_cutD0SignificanceMax = 15.0 # For W+jets or Z+jets fakes, used if hWWCommon.Global.doFakeWJets=True OR doFakeZJets=True
        pass

    # The following cuts are NOT used in the pre-selection
    cutObjectQualityMask           = 1
    cutPtMin                       = 10.0*GeV
    cutLeadPtMin                   = 22.0*GeV
    cutAbsEtaMax                   = 2.47
    cutAbsEtaCrackMin              = 1.37
    cutAbsEtaCrackMax              = 1.52
    cutIDList                      = [ "isLHMedium" ] #mgeisen: this is for Xchecking with r20.7, set to isLHVeryLoose when XCheck is done!
    fakeWJets_cutIDList            = [ "isLHLoose" ]     # For W+jets fakes, used if hWWCommon.Global.doFakeWJets=True
    fakeWJets_cutIDListVeryLoose   = [ "isLHVeryLoose" ] # For W+jets fakes, used if hWWCommon.Global.doFakeWJets=True AND doVeryLooseLH=True are set
    cutIDPtMinList                 = [ 0.0*GeV ]
    cutZ0SinThetaMax               = 0.5
    cutD0SignificanceMax           = 5.0
    fakeWJets_cutZ0SinThetaMax     = 0.5 # KEEP THEM AT NOMINAL, NO IMPROVEMENT EXPECTED. For W+jets or Z+jets fakes, used if hWWCommon.Global.doFakeWJets=True OR doFakeZJets=True
    fakeWJets_cutD0SignificanceMax = 5.0 # KEEP THEM AT NOMINAL, NO IMPROVEMENT EXPECTED. For W+jets or Z+jets fakes, used if hWWCommon.Global.doFakeWJets=True OR doFakeZJets=True
    #fakeWJets_cutZ0SinThetaMax     = 1.5  # For W+jets fakes, used if hWWCommon.Global.doFakeWJets=True
    #fakeWJets_cutD0SignificanceMax = 15.0 # For W+jets fakes, used if hWWCommon.Global.doFakeWJets=True
    removeSelfOverlap              = True
    pass
hWWCommon.add_JobProperty(Electrons)





class Muons(JobProperty):
    """Definitions for the common muons of all the H->WW analyses"""
    statusOn            = True
    allowedTypes        = ['bool']
    StoredValue         = True
    inCont              = "Muons"
    calibCont           = "HWWCalibMuons"
    calibPreSelCont     = "HWWCalibPreSelMuons"
    calibPreSelORCont   = "HWWCalibPreSelORMuons"
    finalCont           = "HWWMuons"
    finalAllPtSortCont  = "FinalAllPtSort"+finalCont
    def finalContList(self) :
        """ The names of the final muon containers. This is a list because every
        4-vector systematic variation is stored in its own container. Thus, we
        are building the list of all these containers using a helper function."""
        return buildContainerNames(baseName=self.finalCont, systList=hWWCommon.Muons.p4Systs)

    p4Systs              = [ "MUON_ID__1down",    "MUON_ID__1up",
                             "MUON_MS__1down",    "MUON_MS__1up",
                             "MUON_SCALE__1down", "MUON_SCALE__1up",
                             "MUON_SAGITTA_RHO__1down", "MUON_SAGITTA_RHO__1up",
                             "MUON_SAGITTA_RESBIAS__1down", "MUON_SAGITTA_RESBIAS__1up"]

    # Reconstruction scale-factors
    effiVarName          = "effiSF"
    effiVarNameList      = [] # Will be filled automatically
    effiSysts            = ["MUON_EFF_RECO_STAT__1down", "MUON_EFF_RECO_STAT__1up",
                            "MUON_EFF_RECO_SYS__1down", "MUON_EFF_RECO_SYS__1up",
                            "MUON_EFF_RECO_STAT_LOWPT__1down", "MUON_EFF_RECO_STAT_LOWPT__1up",
                            "MUON_EFF_RECO_SYS_LOWPT__1down", "MUON_EFF_RECO_SYS_LOWPT__1up"]         

    # Track-to-vertex-association scale-factors
    effiTTVAVarNameList   = ["effiSFTTVA"]
    effiTTVASysts         = ["MUON_EFF_TTVA_STAT__1down", "MUON_EFF_TTVA_STAT__1up",
                             "MUON_EFF_TTVA_SYS__1down", "MUON_EFF_TTVA_SYS__1up"]

    # Isolation scale-factors
    effiIsoVarNameList   = [] # Will be filled automatically
    effiIsoSysts         = ["MUON_EFF_ISO_STAT__1down", "MUON_EFF_ISO_STAT__1up",
                            "MUON_EFF_ISO_SYS__1down", "MUON_EFF_ISO_SYS__1up"]

    # Trigger efficiencies/SF
    effiTrigVarNameList   = [] # Will be filled in job option
    effiTrigSFVarNameList = [] # Will be filled in job option
    effiTrigSysts         = ["MUON_EFF_TrigStatUncertainty__1down", "MUON_EFF_TrigStatUncertainty__1up",
                             "MUON_EFF_TrigSystUncertainty__1down", "MUON_EFF_TrigSystUncertainty__1up"]

    # Isolation working points to use for lepton flagging
    isoWorkingPointList  = ["FCTightTrackOnly_FixedRad", "FCLoose_FixedRad", "FCTight_FixedRad", "FixedCutPflowTight", "FixedCutPflowLoose",
                            "FixedCutHighPtTrackOnly", "FCTightTrackOnly", "FCLoose", "FCTight",
                            "FixedCutHighMuTight", "FixedCutHighMuLoose", "FixedCutHighMuTrackOnly"]
    passIsoVarNameList   = [ "passIso"+wpName for wpName in isoWorkingPointList ]

    # Now come the pre-selection cuts (used for overlap removal, MET-making, and going into "otherMuons")
    class preSelection(object):
        cutPtMin                       = 10.0*GeV
        cutAbsEtaMax                   = 2.7
        cutIDList                      = [ MuonQualityEnums.Loose ]
        cutIDListMedium                = [ MuonQualityEnums.Medium ] # For testing. Only used if command-line option doMediumOtherLeptons=True is set
        cutIDPtMinList                 = [ 0.0*GeV ]
        cutInnerDetectorHits           = True
        cutZ0SinThetaMax               = 0.5
        cutD0SignificanceMax           = 3.0
        fakeWJets_cutZ0SinThetaMax     = 1.5  # For W+jets or Z+jets fakes, used if hWWCommon.Global.doFakeWJets=True OR doFakeZJets=True
        fakeWJets_cutD0SignificanceMax = 15.0 # For W+jets or Z+jets fakes, used if hWWCommon.Global.doFakeWJets=True OR doFakeZJets=True
        pass

    # The following cuts are the final cuts, used on top of the pre-selection
    cutInnerDetectorHits           = True
    cutPtMin                       = 10.0*GeV
    cutLeadPtMin                   = 22.0*GeV
    cutAbsEtaMax                   = 2.5
    cutIDList                      = [ MuonQualityEnums.Medium,4 ]
    cutIDPtMinList                 = [ 0.0*GeV, 0.0*GeV ]
    cutZ0SinThetaMax               = 0.5
    cutD0SignificanceMax           = 3.0
    fakeWJets_cutZ0SinThetaMax     = 1.5  # For W+jets fakes, used if hWWCommon.Global.doFakeWJets=True
    fakeWJets_cutD0SignificanceMax = 15.0 # For W+jets fakes, used if hWWCommon.Global.doFakeWJets=True
    pass
hWWCommon.add_JobProperty(Muons)





class Jets(JobProperty):
    """Definitions for the common jets of all the H->WW analyses"""
    statusOn              = True
    allowedTypes          = ['bool']
    StoredValue           = True
    truthCont             = "AntiKt4TruthJets"
    inTrackJetsCont       = "AntiKt4PV0TrackJets"
    writeTrackJets        = False 
    writeAntiKt2TrackJets = False
    writeJetConstituents  = True
    doPFlowJets           = False
    inCont                = "" # Will be determined on-the-fly
    inContEMTopo          = "AntiKt4EMTopoJets"
    inContEMPFlow         = "AntiKt4EMPFlowJets"
    calibCont             = "HWWCalibJets"
    calibPreSelCont       = "HWWCalibPreSelJets"
    calibPreSelORCont     = "HWWCalibPreSelORJets"
    finalCont             = "HWWJets"
    finalAllPtSortCont    = "FinalAllPtSort"+finalCont
    def finalContList(self) :
        """ The names of the final jet containers. This is a list because every
        4-vector systematic variation is stored in its own container. Thus, we
        are building the list of all these containers using a helper function."""
        return buildContainerNames(baseName=self.finalCont, systList=hWWCommon.Jets.p4Systs)

    # Jet calibration
    calibConfigFile        = "" # Will be determined on-the-fly
    calibConfigFileEMTopo  = "JES_data2017_2016_2015_Consolidated_EMTopo_2018_Rel21.config"
    calibConfigFileEMPFlow = "JES_data2017_2016_2015_Consolidated_PFlow_2018_Rel21.config"

    calibAFIIConfigFile        = "" # Will be determined on-the-fly
    calibAFIIConfigFileEMTopo  = "JES_MC16Recommendation_AFII_EMTopo_April2018_rel21.config"
    calibAFIIConfigFileEMPFlow = "JES_MC16Recommendation_AFII_PFlow_April2018_rel21.config"

    calibSequence       = "JetArea_Residual_EtaJES_GSC"
    dataCalibSeqSuffix  = "_Insitu"
    mcCalibSeqSuffix    = "_Smear"
    CalibArea           = "00-04-82"

    # Jet uncertainties
    jesjerConfigFile    = "rel21/Fall2018/R4_CategoryReduction_SimpleJER.config"
    jesjerCalibArea     = "CalibArea-06"

    jesSysts            = ["JET_BJES_Response__1up",                         "JET_BJES_Response__1down",
                           "JET_EffectiveNP_Detector1__1up",                 "JET_EffectiveNP_Detector1__1down",
                           "JET_EffectiveNP_Detector2__1up",                 "JET_EffectiveNP_Detector2__1down",
                           "JET_EffectiveNP_Mixed1__1up",                    "JET_EffectiveNP_Mixed1__1down",
                           "JET_EffectiveNP_Mixed2__1up",                    "JET_EffectiveNP_Mixed2__1down",
                           "JET_EffectiveNP_Mixed3__1up",                    "JET_EffectiveNP_Mixed3__1down",
                           "JET_EffectiveNP_Modelling1__1up",                "JET_EffectiveNP_Modelling1__1down",
                           "JET_EffectiveNP_Modelling2__1up",                "JET_EffectiveNP_Modelling2__1down",
                           "JET_EffectiveNP_Modelling3__1up",                "JET_EffectiveNP_Modelling3__1down",
                           "JET_EffectiveNP_Modelling4__1up",                "JET_EffectiveNP_Modelling4__1down",
                           "JET_EffectiveNP_Statistical1__1up",              "JET_EffectiveNP_Statistical1__1down",
                           "JET_EffectiveNP_Statistical2__1up",              "JET_EffectiveNP_Statistical2__1down",
                           "JET_EffectiveNP_Statistical3__1up",              "JET_EffectiveNP_Statistical3__1down",
                           "JET_EffectiveNP_Statistical4__1up",              "JET_EffectiveNP_Statistical4__1down",
                           "JET_EffectiveNP_Statistical5__1up",              "JET_EffectiveNP_Statistical5__1down",
                           "JET_EffectiveNP_Statistical6__1up",              "JET_EffectiveNP_Statistical6__1down",
                           "JET_EtaIntercalibration_Modelling__1up",         "JET_EtaIntercalibration_Modelling__1down",
                           "JET_EtaIntercalibration_NonClosure_highE__1up",  "JET_EtaIntercalibration_NonClosure_highE__1down",
                           "JET_EtaIntercalibration_NonClosure_negEta__1up", "JET_EtaIntercalibration_NonClosure_negEta__1down",
                           "JET_EtaIntercalibration_NonClosure_posEta__1up", "JET_EtaIntercalibration_NonClosure_posEta__1down",
                           "JET_EtaIntercalibration_TotalStat__1up",         "JET_EtaIntercalibration_TotalStat__1down",
                           "JET_Flavor_Composition__1up",                    "JET_Flavor_Composition__1down",
                           "JET_Flavor_Response__1up",                       "JET_Flavor_Response__1down",
                           "JET_Pileup_OffsetMu__1up",                       "JET_Pileup_OffsetMu__1down",
                           "JET_Pileup_OffsetNPV__1up",                      "JET_Pileup_OffsetNPV__1down",
                           "JET_Pileup_PtTerm__1up",                         "JET_Pileup_PtTerm__1down",
                           "JET_Pileup_RhoTopology__1up",                    "JET_Pileup_RhoTopology__1down",
                           "JET_PunchThrough_MC16__1up",                     "JET_PunchThrough_MC16__1down",
                           "JET_SingleParticle_HighPt__1up",                 "JET_SingleParticle_HighPt__1down" ]

    jerSysts            = [ "JET_JER_DataVsMC__1up",                         "JET_JER_DataVsMC__1down",
                            "JET_JER_EffectiveNP_1__1up",                    "JET_JER_EffectiveNP_1__1down",
                            "JET_JER_EffectiveNP_2__1up",                    "JET_JER_EffectiveNP_2__1down",
                            "JET_JER_EffectiveNP_3__1up",                    "JET_JER_EffectiveNP_3__1down",
                            "JET_JER_EffectiveNP_4__1up",                    "JET_JER_EffectiveNP_4__1down",
                            "JET_JER_EffectiveNP_5__1up",                    "JET_JER_EffectiveNP_5__1down",
                            "JET_JER_EffectiveNP_6__1up",                    "JET_JER_EffectiveNP_6__1down",
                            "JET_JER_EffectiveNP_7restTerm__1up",            "JET_JER_EffectiveNP_7restTerm__1down",
                            ]

    ## This will be filled automatically with the sum of all JES and JER systematics
    p4Systs             = [ ]

    # JVT stuff
    updateJVTName         = "calibJvt"
    passJVTVarName        = "passJVT"
    effiJVTVarName        = "effiSFJVT"
    effiForwardJVTVarName = "effiSFForwardJVT"

    jvtConfigFile         = "" # Will be determined on-the-fly
    jvtConfigFileEMTopo   = "JetJvtEfficiency/Moriond2018/JvtSFFile_EMTopoJets.root"
    jvtConfigFileEMPFlow  = "JetJvtEfficiency/Moriond2018/JvtSFFile_EMPFlow.root"

    forwardJvtConfigFile  = "JetJvtEfficiency/Moriond2018/fJvtSFFile.root"
    effiJVTSysts          = ["JET_JvtEfficiency__1down", "JET_JvtEfficiency__1up"]
    effiForwardJVTSysts   = ["JET_fJvtEfficiency__1down", "JET_fJvtEfficiency__1up"]

    # b-tagging stuff
    effiVarName          = "effiSF"
    effiSysts            = ["FT_EFF_Eigen_B_0__1down", "FT_EFF_Eigen_B_0__1up",
                            "FT_EFF_Eigen_B_1__1down", "FT_EFF_Eigen_B_1__1up",
                            "FT_EFF_Eigen_B_2__1down", "FT_EFF_Eigen_B_2__1up",
                            "FT_EFF_Eigen_C_0__1down", "FT_EFF_Eigen_C_0__1up",
                            "FT_EFF_Eigen_C_1__1down", "FT_EFF_Eigen_C_1__1up",
                            "FT_EFF_Eigen_C_2__1down", "FT_EFF_Eigen_C_2__1up",
                            "FT_EFF_Eigen_Light_0__1down", "FT_EFF_Eigen_Light_0__1up",
                            "FT_EFF_Eigen_Light_1__1down", "FT_EFF_Eigen_Light_1__1up",
                            "FT_EFF_Eigen_Light_2__1down", "FT_EFF_Eigen_Light_2__1up",
                            "FT_EFF_Eigen_Light_3__1down", "FT_EFF_Eigen_Light_3__1up",
                            "FT_EFF_extrapolation__1down", "FT_EFF_extrapolation__1up",
                            "FT_EFF_extrapolation_from_charm__1down", "FT_EFF_extrapolation_from_charm__1up"]
    systematicsStrategy   = "SFEigen"
    systematicsReduction  = "Medium"
    bTagName              = "MV2c10" #
    bTagWP                = "FixedCutBEff_85" # 85% WP
    bTagWPNumber          = 0.11   # 85% WP for MV2c10
    bTagWPTrackJets       = "FixedCutBEff_77" # 77% WP for AntiKt4PV0TrackJets
    bTagWPTrackJetsNumber = 0.38 # 77% WP for AntiKt4PV0TrackJets
    # bTagWPTrackJetsNumber = -0.0168 # 85% WP for AntiKt4PV0TrackJets
    CDIFile               = "xAODBTaggingEfficiency/13TeV/2017-21-13TeV-MC16-CDI-2018-10-19_v1.root"
    bJetLabel             = "isBJet85"


    # Now come the pre-selection cuts (used for overlap removal, MET-making, and going into "otherJets")
    class preSelection(object):
        cutPtMinList          = [ 20.0*GeV ]
        cutAbsEtaMaxList      = [ 4.5 ]
        # passForwardJVTVarName = "" # empty string would be no selection
        passForwardJVTVarName = "passFJVT" # empty string would be no selection
        pass

    # And now the final selection
    cutPtMinList         = [ 25.0*GeV, 25.0*GeV ]
    cutAbsEtaMaxList     = [ 2.4,      4.5 ]
    cutCleaningMinPt     = 20.0*GeV
    cutCleaningMaxPt     = 60.0*GeV
    cutCleaningMaxAbsEta = 2.4
    pass
hWWCommon.add_JobProperty(Jets)





class FatJets(JobProperty):
    """Definitions for the large-R jets of all the H->WW analyses"""
    statusOn            = True
    allowedTypes        = ['bool']
    StoredValue         = True
    inCont              = "AntiKt10LCTopoTrimmedPtFrac5SmallR20Jets"
    # inCont              = "AntiKt10LCTopoJets"
    calibCont           = "HWWCalibFatJets"
    calibPreSelCont     = "HWWCalibPreSelFatJets"
    calibPreSelORCont   = "HWWCalibPreSelORFatJets"
    finalCont           = "HWWFatJets"
    finalAllPtSortCont  = "FinalAllPtSort"+finalCont

    calibConfigFile     = "JES_MC16recommendation_FatJet_JMS_TA_29Nov2017.config"
    calibAFIIConfigFile = "JES_MC16recommendation_FatJet_JMS_TA_29Nov2017.config" # No AF2 file available yet!
    calibSequence       = "EtaJES_JMS"
    dataCalibSeqSuffix  = ""
    jesConfigFile       = "JES_MC16Recommendation_28Nov2017.config"
    p4Systs             = ['JET_WZ_CrossCalib_D2__1up','JET_WZ_CrossCalib_D2__1down',
                           'JET_WZ_CrossCalib_mass__1up','JET_WZ_CrossCalib_mass__1down',
                           'JET_WZ_CrossCalib_pT__1up','JET_WZ_CrossCalib_pT__1down',
                           'JET_WZ_Run1_D2__1up','JET_WZ_Run1_D2__1down',
                           'JET_WZ_Run1_mass__1up','JET_WZ_Run1_mass__1down',
                           'JET_WZ_Run1_pT__1up','JET_WZ_Run1_pT__1down']

    bosonTaggerWorkingPoint = "medium"
    bosonTaggerAlgorithm    = "smooth"
    WTaggerConfigFile       = "JetSubStructureUtils/data/config_13TeV_Wtagging_MC15_Prerecommendations_20150809.dat"
    ZTaggerConfigFile       = "JetSubStructureUtils/data/config_13TeV_Ztagging_MC15_Prerecommendations_20150809.dat"

    # Now come the pre-selection cuts
    class preSelection(object):
        cutPtMinList      = [ 200.0*GeV ]
        cutAbsEtaMaxList  = [ 2.0 ]
        pass

    # And now the final selection
    cutPtMinList      = [ 200.0*GeV ]
    cutAbsEtaMaxList  = [ 2.0 ]
    pass
hWWCommon.add_JobProperty(FatJets) #mgeisen





class MET(JobProperty):
    """Definitions for the missing ET of the H->WW-> analysis"""
    statusOn       = True
    allowedTypes   = ['bool']
    StoredValue    = True
    # inMap and inCore must currently be set to EMTopo for MET to properly
    # be written out when making FakeDijet PAODs. The reason is that HIGG3D3
    # doesn't have LCTopo jets and the check for that happens before checking
    # what jets are to be used. TODO: fix this.
    inMap          = "METAssoc_AntiKt4EMTopo" # Only a default, gets changed according to the jet type
    inCore         = "MET_Core_AntiKt4EMTopo" # Only a default, gets changed according to the jet type
    inObject       = "FinalTrk"
    calibCont      = "HWWCalibMET"
    finalCont      = "HWWMET"
    finalTrackCont = "HWWTrackMET"

    configSoftTrkFile = "TrackSoftTerms.config"
    configJetTrkFile  = "JetTrackSyst.config"

    p4TSTSysts     = ["MET_SoftTrk_ResoPara", "MET_SoftTrk_ResoPerp", "MET_SoftTrk_ScaleDown", "MET_SoftTrk_ScaleUp"]
    p4CSTSysts     = []#"MET_SoftCalo_Reso", "MET_SoftCalo_ScaleDown", "MET_SoftCalo_ScaleUp", "MET_SoftTrk_ResoCorr"]
    p4JetTrkSysts  = [ "MET_JetTrk_ScaleDown", "MET_JetTrk_ScaleUp" ]
    p4Systs        = [ ]
    effiVarName    = "effiSF"
    effiSysts      = [ ]
    cutMETMin      = 0.0*GeV
    pass
hWWCommon.add_JobProperty(MET)





class TruthElectrons(JobProperty):
    """Definitions for the common truth electrons of all the H->WW analyses"""
    statusOn            = True
    allowedTypes        = ['bool']
    StoredValue         = True
    inCont              = "TruthElectrons"
    calibCont           = "HWWTruthCalibElectrons"
    calibPreSelCont     = "HWWTruthCalibPreSelElectrons"
    calibPreSelORCont   = "HWWTruthCalibPreSelORElectrons"
    finalCont           = "HWWTruthElectrons"
    preORAllPtSortCont  = "PreORAllPtSort"+finalCont
    finalLeadPtSortCont = "FinalLeadPtSort"+finalCont
    finalAllPtSortCont  = "FinalAllPtSort"+finalCont
    def finalContList(self) :
        """ The names of the final electron containers. This is a list because every
        4-vector systematic variation is stored in its own container. Thus, we
        are building the list of all these containers using a helper function."""
        return buildContainerNames(baseName=self.finalCont, systList=hWWCommon.Electrons.p4Systs)

    # p4Systs                 = ["EG_RESOLUTION_ALL__1down","EG_RESOLUTION_ALL__1up",
    #                            "EG_SCALE_ALL__1down","EG_SCALE_ALL__1up"]
    p4Systs = []

    # Isolation working points to use for lepton flagging
    isoWorkingPointList  = ["LooseTrackOnly", "Loose", "Tight", "GradientLoose", "Gradient",
                            "FixedCutTight", "FixedCutTightTrackOnly", "FixedCutLoose" ]
    passIsoVarNameList   = [ "passIso"+wpName for wpName in isoWorkingPointList ]

    # Now come the pre-selection cuts
    class preSelection(object):
        #cutObjectQualityMask       = xAOD::BADCLUSELECTRON
        cutObjectQualityMask       = 1
        cutPtMin                   = 10.0*GeV
        cutAbsEtaMax               = 2.47
        #cutAbsEtaCrackMin          = 1.37
        #cutAbsEtaCrackMax          = 1.52
        cutIDList                  = [ ]
        cutIDPtMinList             = [ 0.0*GeV ]
        removeSelfOverlap          = True
        cutZ0SinThetaMax           = 0.5
        cutD0SignificanceMax       = 5.0
        pass

    # The following cuts are NOT used in the pre-selection
    cutObjectQualityMask       = 1
    cutPtMin                   = 15.0*GeV
    cutLeadPtMin               = 22.0*GeV
    cutAbsEtaMax               = 2.47
    cutAbsEtaCrackMin          = 1.37
    cutAbsEtaCrackMax          = 1.52
    # cutIDList                  = [ "isLHTight", "isLHMedium" ]
    # cutIDPtMinList             = [ 10.0*GeV, 25.0*GeV ]
    cutIDList                  = [  ]
    cutIDPtMinList             = [ 0.0*GeV]
    cutZ0SinThetaMax           = 0.5
    cutD0SignificanceMax       = 5.0
    removeSelfOverlap          = True
    pass
hWWCommon.add_JobProperty(TruthElectrons)





class TruthMuons(JobProperty):
    """Definitions for the common muons of all the H->WW analyses"""
    statusOn            = True
    allowedTypes        = ['bool']
    StoredValue         = True
    inCont              = "TruthMuons"
    calibCont           = "HWWTruthCalibMuons"
    calibPreSelCont     = "HWWTruthCalibPreSelMuons"
    calibPreSelORCont   = "HWWTruthCalibPreSelORMuons"
    finalCont           = "HWWTruthMuons"
    preORAllPtSortCont  = "PreORAllPtSort"+finalCont
    finalLeadPtSortCont = "FinalLeadPtSort"+finalCont
    finalAllPtSortCont  = "FinalAllPtSort"+finalCont
    def finalContList(self) :
        """ The names of the final muon containers. This is a list because every
        4-vector systematic variation is stored in its own container. Thus, we
        are building the list of all these containers using a helper function."""
        return buildContainerNames(baseName=self.finalCont, systList=hWWCommon.Muons.p4Systs)

    # p4Systs              = [ "MUONS_ID__1down", "MUONS_ID__1up",
    #                          "MUONS_MS__1down", "MUONS_MS__1up",
    #                          "MUONS_SCALE__1down", "MUONS_SCALE__1up" ]
    p4Systs = []

    # Isolation working points to use for lepton flagging
    isoWorkingPointList  = ["LooseTrackOnly", "Loose", "Tight", "GradientLoose",
                            "Gradient", "FixedCutTightTrackOnly", "FixedCutLoose" ]
    passIsoVarNameList   = [ "passIso"+wpName for wpName in isoWorkingPointList ]
    effiTrigVarNameList  = []
    effiTrigSFToolList   = []
    effiTrigSysts        = []

    # Now come the pre-selection cuts
    class preSelection(object):
        cutPtMin             = 10.0*GeV
        cutAbsEtaMax         = 2.7
        cutIDList            = [ ]
        cutIDPtMinList       = [ 0.0*GeV ]
        cutInnerDetectorHits = False
        cutZ0SinThetaMax     = 0.5
        cutD0SignificanceMax = 3.0
        pass

    # The following cuts are NOT used in the pre-selection
    cutInnerDetectorHits = True
    cutPtMin             = 15.0*GeV
    cutLeadPtMin         = 22.0*GeV
    cutAbsEtaMax         = 2.5
    cutIDList            = [ ]
    cutIDPtMinList       = [ 0.0*GeV ]
    cutZ0SinThetaMax     = 0.5
    cutD0SignificanceMax = 3.0
    pass
hWWCommon.add_JobProperty(TruthMuons)





class TruthJets(JobProperty):
    """Definitions for the common jets of all the H->WW analyses"""
    statusOn            = True
    allowedTypes        = ['bool']
    StoredValue         = True
    truthCont           = "AntiKt4TruthJets"
    inTrackJetsCont     = "AntiKt4PV0TrackJets"
    writeTrackJets      = False
    # inCont              = "AntiKt4LCTopoJets"
    inCont              = "AntiKt4TruthJets"
    calibCont           = "HWWTruthCalibJets"
    calibPreSelCont     = "HWWTruthCalibPreSelJets"
    calibPreSelORCont   = "HWWTruthCalibPreSelORJets"
    finalCont           = "HWWTruthJets"
    preORAllPtSortCont  = "PreORAllPtSort"+finalCont
    finalAllPtSortCont  = "FinalAllPtSort"+finalCont
    def finalContList(self) :
        """ The names of the final jet containers. This is a list because every
        4-vector systematic variation is stored in its own container. Thus, we
        are building the list of all these containers using a helper function."""
        return buildContainerNames(baseName=self.finalCont, systList=hWWCommon.Jets.p4Systs)

    # jesSysts            = [ 'JET_GroupedNP_1__1up', 'JET_GroupedNP_1__1down',
    #                         'JET_GroupedNP_2__1up', 'JET_GroupedNP_2__1down',
    #                         'JET_GroupedNP_3__1up', 'JET_GroupedNP_3__1down' ]
    # jerSysts            = [ "JET_JER_SINGLE_NP__1up" ]
    # p4Systs             = [ ] ## VD: this will be filled with the sum of jes and jer for application that are transparent to the difference
    p4Systs = []

    updateJVTName       = "calibJvt"

    # Now come the pre-selection cuts
    class preSelection(object):
        cutPtMinList      = [ 20.0*GeV ]
        cutAbsEtaMaxList  = [ 4.5 ]
        cutCleanList      = [ ]
        cutCleanPtMinList = [ 0.0*GeV ]
        #requireTruthMatch = False
        cutJVT            = 0.64
        cutJVTMaxPt       = 50.0*GeV
        cutJVTMaxAbsEta   = 2.4
        pass

    # And now the final selection
    cutPtMinList      = [ 25.0*GeV, 30.0*GeV ]
    cutAbsEtaMaxList  = [ 2.4,      4.5 ]
    cutCleanList      = [  ]
    cutCleanPtMinList = [ 0.0*GeV ]
    cutJVT            = 0.64
    cutJVTMaxPt       = 50.0*GeV
    cutJVTMaxAbsEta   = 2.4

    pass
hWWCommon.add_JobProperty(TruthJets)





class TruthMET(JobProperty):
    """Definitions for the missing ET of the H->WW-> analysis"""
    statusOn       = True
    allowedTypes   = ['bool']
    StoredValue    = True
    inMap          = "MET_Truth" # Only a default, gets changed according to the jet type
    inCore         = "MET_Truth" # Only a default, gets changed according to the jet type
    inCont         = "MET_Truth"
    inObject       = "NonInt"
    calibCont      = "HWWTruthMET"
    #finalCont      = "HWWTruthMET"
    finalCont      = "MET_Truth"
    #finalTrackCont = "HWWTrackMET"
    p4Systs        = [ #"MET_JetTrk_ScaleDown", "MET_JetTrk_ScaleUp",
                       #"MET_SoftCalo_Reso"   , "MET_SoftCalo_ScaleDown", "MET_SoftCalo_ScaleUp" , # Not recommendet: "MET_SoftTrk_ResoCorr" ,
                       #"MET_SoftTrk_ResoPara", "MET_SoftTrk_ResoPerp"  , "MET_SoftTrk_ScaleDown", "MET_SoftTrk_ScaleUp"
                      ]
    effiVarName    = "effiSF"
    effiSysts      = [ ]
    cutMETMin      = 0.0*GeV
    pass
hWWCommon.add_JobProperty(TruthMET)
