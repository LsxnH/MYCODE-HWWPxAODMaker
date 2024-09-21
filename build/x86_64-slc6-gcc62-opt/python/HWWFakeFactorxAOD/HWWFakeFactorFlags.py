##=============================================================================
## Name:        HWWFakeFactorFlags.py
##
## Author:      Olivier Arnaez
## Created:     October 2015
##
## Description: Here, all neccessary job flags for the Higgs->WW->lnulnu
##              fake factor analysis are defined.
##=============================================================================

__doc__ = """Here, all neccessary job flags for the Higgs->WW->lnulnu fake factor analysis are defined."""
__version__ = "0.0.1"
__author__  = "Olivier Arnaez <olivier.arnaez@cern.ch>"

from AthenaCommon.JobProperties import JobProperty, JobPropertyContainer
from AthenaCommon.JobProperties import jobproperties

# Import the module that allows to use named units, e.g. GeV
from AthenaCommon.SystemOfUnits import *

# Import the common steering flags for this analysis
import PhysicsxAODConfig.HWWCommonAnalysisFlags as hWWCommonFlags
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon


#=====================================================================
# First define container for the flags
#=====================================================================
class HWWFakeFactorFlags(JobPropertyContainer):
    """ The Higgs->WW->lnulnu fake factor analysis flag/job property container."""
jobproperties.add_Container(HWWFakeFactorFlags)

#short-cut to get the HiggsWWFakeFactorFlags container with this one line:
#'from HWWFakeFactorxAOD.HWWFakeFactorFlags import hWWFakes'
#Note that name has to be different to avoid problems with pickle
hWWFakes = jobproperties.HWWFakeFactorFlags



#=====================================================================
# Now define each flag and add it to the container
#=====================================================================

class Global(hWWCommonFlags.Global):
    """
    Global steering for the H->WW->lnulnu lepton-fake factor analysis.
    The common parts are directly taken from PhysicsxAODConfig/python/HWWCommonFlags.py.
    """
    statusOn                   = True
    allowedTypes               = ['bool']
    StoredValue                = True
    DPDMakerScript             = "HWWFakeFactorxAOD/HWWFakeFactorAnalysisCommon.py"
    StreamName                 = "PAOD_FakeL"
    FileName                   = "PAOD_FakeL.pool.root"
    writeMinixAOD              = True
    doSkimming                 = True
    acceptAlgList              = [] # This is a default. It will be filled during the job setup
    pass
hWWFakes.add_JobProperty(Global)


class Trigger(JobProperty):
    """Common trigger definitions for all the H->WW analyzes"""
    statusOn                = True
    allowedTypes            = ['bool']
    StoredValue             = True
    # Updated Trigger lists to match HIGG3D3 /Edvin 2016-06-30
    fakesElectronTriggerList = ['HLT_e17_lhloose_L1EM15', 'HLT_e17_loose_L1EM15', 'HLT_e60_medium', 'HLT_e60_lhmedium', 'HLT_e24_lhmedium_L1EM18VH', 'HLT_e24_lhmedium_L1EM20VH', 'HLT_e5_etcut', 'HLT_e10_etcut_L1EM7', 'HLT_e13_etcut_trkcut_L1EM10', 'HLT_e15_etcut_L1EM7', 'HLT_e18_etcut_trkcut_L1EM15', 'HLT_e20_etcut_L1EM12', 'HLT_e25_etcut_L1EM15', 'HLT_e30_etcut_L1EM15', 'HLT_e40_etcut_L1EM15', 'HLT_e50_etcut_L1EM15', 'HLT_e60_etcut', 'HLT_e5_lhvloose', 'HLT_e5_lhvloose_nod0', 'HLT_e10_lhvloose_L1EM7', 'HLT_e12_lhvloose_L1EM10VH', 'HLT_e12_lhvloose_nod0_L1EM10VH', 'HLT_e15_lhvloose_L1EM7', 'HLT_e15_lhvloose_L1EM13VH', 'HLT_e15_lhvloose_nod0_L1EM13VH', 'HLT_e17_lhvloose', 'HLT_e17_lhvloose_nod0', 'HLT_e20_lhvloose_L1EM12', 'HLT_e20_lhvloose', 'HLT_e20_lhvloose_nod0', 'HLT_e24_lhvloose_nod0_L1EM18VH', 'HLT_e24_lhvloose_nod0_L1EM20VH', 'HLT_e24_lhmedium_L1EM20VHI', 'HLT_e24_lhmedium_nod0_ivarloose', 'HLT_e60_lhmedium_nod0', 'HLT_e120_lhloose_nod0', 'HLT_e250_etcut', 'HLT_e100_etcut', 'HLT_e100_lhvloose', 'HLT_e100_lhvloose_nod0', 'HLT_e10_lhvloose_nod0_L1EM7', 'HLT_e120_etcut', 'HLT_e120_lhloose', 'HLT_e120_lhvloose', 'HLT_e120_lhvloose_nod0', 'HLT_e12_lhloose', 'HLT_e12_lhloose_cutd0dphideta_L1EM10VH', 'HLT_e12_lhloose_L1EM10VH', 'HLT_e12_lhloose_nod0', 'HLT_e12_lhloose_nod0_L1EM10VH', 'HLT_e12_lhloose_nodeta_L1EM10VH', 'HLT_e12_lhloose_nodphires_L1EM10VH', 'HLT_e12_lhmedium', 'HLT_e12_lhmedium_nod0', 'HLT_e12_loose', 'HLT_e12_loose_L1EM10VH', 'HLT_e12_medium', 'HLT_e12_vloose_L1EM10VH', 'HLT_e13_etcut_trkcut_L1EM12', 'HLT_e140_etcut', 'HLT_e140_lhloose', 'HLT_e140_lhloose_L1EM24VHI', 'HLT_e140_lhloose_nod0', 'HLT_e140_lhloose_nod0_L1EM24VHI', 'HLT_e140_lhvloose', 'HLT_e140_lhvloose_nod0', 'HLT_e14_etcut', 'HLT_e14_lhtight', 'HLT_e14_lhtight_nod0', 'HLT_e14_tight', 'HLT_e15_lhloose_cutd0dphideta_L1EM13VH', 'HLT_e15_lhloose_L1EM13VH', 'HLT_e15_lhloose_nod0_L1EM13VH', 'HLT_e15_lhtight_iloose_L1EM13VH', 'HLT_e15_lhvloose_nod0_L1EM7', 'HLT_e15_loose_L1EM13VH', 'HLT_e15_vloose_L1EM13VH', 'HLT_e17_lhloose', 'HLT_e17_lhloose_cutd0dphideta', 'HLT_e17_lhloose_cutd0dphideta_L1EM15', 'HLT_e17_lhloose_nod0', 'HLT_e17_lhloose_nod0_L1EM15', 'HLT_e17_lhloose_nodeta_L1EM15', 'HLT_e17_lhloose_nodphires_L1EM15', 'HLT_e17_lhmedium', 'HLT_e17_lhmedium_iloose', 'HLT_e17_lhmedium_iloose_L1EM15HI', 'HLT_e17_lhmedium_ivarloose_L1EM15HI', 'HLT_e17_lhmedium_L1EM15HI', 'HLT_e17_lhmedium_nod0', 'HLT_e17_lhmedium_nod0_iloose', 'HLT_e17_lhmedium_nod0_iloose_L1EM15HI', 'HLT_e17_lhmedium_nod0_ivarloose_L1EM15HI', 'HLT_e17_lhmedium_nod0_L1EM15HI', 'HLT_e17_loose', 'HLT_e17_medium', 'HLT_e17_medium_iloose', 'HLT_e17_medium_iloose_L1EM15HI', 'HLT_e17_medium_ivarloose_L1EM15HI', 'HLT_e17_medium_L1EM15HI', 'HLT_e17_vloose', 'HLT_e200_etcut', 'HLT_e20_lhmedium', 'HLT_e20_lhmedium_nod0', 'HLT_e20_lhvloose_nod0_L1EM12', 'HLT_e20_medium', 'HLT_e20_vloose', 'HLT_e24_lhmedium_iloose', 'HLT_e24_lhmedium_ivarloose', 'HLT_e24_lhmedium_L1EM15VH', 'HLT_e24_lhmedium_nod0_iloose', 'HLT_e24_lhmedium_nod0_L1EM15VH', 'HLT_e24_lhmedium_nod0_L1EM18VH', 'HLT_e24_lhmedium_nod0_L1EM20VH', 'HLT_e24_lhmedium_nod0_L1EM20VHI', 'HLT_e24_lhtight_iloose', 'HLT_e24_lhtight_ivarloose', 'HLT_e24_lhtight_L1EM20VH', 'HLT_e24_lhtight_nod0_iloose', 'HLT_e24_lhtight_nod0_ivarloose', 'HLT_e24_lhtight_nod0_L1EM20VH', 'HLT_e24_lhvloose_L1EM18VH', 'HLT_e24_lhvloose_L1EM20VH', 'HLT_e24_loose_L1EM20VHI', 'HLT_e24_medium_iloose_L1EM20VH', 'HLT_e24_medium_L1EM15VH', 'HLT_e24_medium_L1EM20VHI', 'HLT_e24_tight_L1EM20VHI', 'HLT_e24_vloose_L1EM18VH', 'HLT_e24_vloose_L1EM20VH', 'HLT_e25_lhvloose_L1EM15', 'HLT_e25_lhvloose_nod0_L1EM15', 'HLT_e26_lhmedium_L1EM22VHI', 'HLT_e26_lhmedium_nod0_L1EM22VHI', 'HLT_e26_lhtight_cutd0dphideta_ivarloose', 'HLT_e26_lhtight_iloose', 'HLT_e26_lhtight_ivarloose', 'HLT_e26_lhtight_nod0', 'HLT_e26_lhtight_nod0_iloose', 'HLT_e26_lhtight_nod0_ivarloose', 'HLT_e26_lhtight_smooth_iloose', 'HLT_e26_lhtight_smooth_ivarloose', 'HLT_e26_lhvloose_L1EM20VH', 'HLT_e26_lhvloose_nod0_L1EM20VH', 'HLT_e26_medium_L1EM22VHI', 'HLT_e26_vloose_L1EM20VH', 'HLT_e28_lhtight_iloose', 'HLT_e28_lhtight_ivarloose', 'HLT_e28_lhtight_nod0_iloose', 'HLT_e28_lhtight_nod0_ivarloose', 'HLT_e28_lhtight_nod0_ivarloose_L1EM22VHI', 'HLT_e28_lhtight_nod0_L1EM22VHI', 'HLT_e28_lhtight_smooth_iloose', 'HLT_e28_lhtight_smooth_ivarloose', 'HLT_e28_tight_iloose', 'HLT_e300_etcut', 'HLT_e30_lhvloose_L1EM15', 'HLT_e30_lhvloose_nod0_L1EM15', 'HLT_e40_lhvloose', 'HLT_e40_lhvloose_L1EM15', 'HLT_e40_lhvloose_nod0', 'HLT_e40_lhvloose_nod0_L1EM15', 'HLT_e40_vloose', 'HLT_e4_etcut', 'HLT_e50_lhvloose_L1EM15', 'HLT_e50_lhvloose_nod0_L1EM15', 'HLT_e5_lhloose', 'HLT_e5_lhloose_nod0', 'HLT_e5_lhtight', 'HLT_e5_lhtight_nod0', 'HLT_e5_loose', 'HLT_e5_tight', 'HLT_e60_lhloose', 'HLT_e60_lhloose_nod0', 'HLT_e60_lhmedium_L1EM24VHI', 'HLT_e60_lhmedium_nod0_L1EM24VHI', 'HLT_e60_lhvloose', 'HLT_e60_lhvloose_nod0', 'HLT_e60_loose', 'HLT_e60_medium_L1EM24VHI', 'HLT_e60_vloose', 'HLT_e70_etcut', 'HLT_e70_lhloose', 'HLT_e70_lhloose_nod0', 'HLT_e70_lhvloose', 'HLT_e70_lhvloose_nod0', 'HLT_e70_loose', 'HLT_e7_lhmedium', 'HLT_e7_lhmedium_nod0', 'HLT_e7_medium', 'HLT_e80_etcut', 'HLT_e80_lhvloose', 'HLT_e80_lhvloose_nod0', 'HLT_e9_etcut', 'HLT_e9_lhloose', 'HLT_e9_lhloose_nod0', 'HLT_e9_lhmedium', 'HLT_e9_lhmedium_nod0', 'HLT_e9_lhtight', 'HLT_e9_lhtight_nod0', 'HLT_e9_loose', 'HLT_e9_medium', 'HLT_e9_tight']
    fakesMuonTriggerList = ['HLT_mu24_L1MU15', 'HLT_mu4', 'HLT_mu6', 'HLT_mu10', 'HLT_mu14', 'HLT_mu18', 'HLT_mu20_L1MU15', 'HLT_mu24', 'HLT_mu40', 'HLT_mu20_iloose_L1MU15', 'HLT_mu50', 'HLT_mu20_ivarloose_L1MU15', 'HLT_mu0_perf', 'HLT_mu14_iloose', 'HLT_mu14_ivarloose', 'HLT_mu20', 'HLT_mu20_imedium_L1MU10', 'HLT_mu20_ivarmedium_L1MU10', 'HLT_mu22', 'HLT_mu24_iloose', 'HLT_mu24_iloose_L1MU15', 'HLT_mu24_imedium', 'HLT_mu24_ivarloose', 'HLT_mu24_ivarloose_L1MU15', 'HLT_mu24_ivarmedium', 'HLT_mu26', 'HLT_mu26_imedium', 'HLT_mu26_ivarmedium', 'HLT_mu28_imedium', 'HLT_mu28_ivarmedium']
    fakesPhotonTriggerList = ['HLT_g10_etcut', 'HLT_g10_loose', 'HLT_g15_loose_L1EM7', 'HLT_g20_loose_L1EM12', 'HLT_g20_loose_L1EM15', 'HLT_g20_etcut_L1EM12', 'HLT_g25_loose_L1EM15', 'HLT_g35_loose_L1EM15', 'HLT_g40_loose_L1EM15', 'HLT_g45_loose_L1EM15', 'HLT_g50_loose_L1EM15']
    fakesDiTriggerList  = ['HLT_g35_loose_L1EM15_g25_loose_L1EM15', 'HLT_e20_lhmedium_g35_loose', 'HLT_2e12_loose_L12EM10VH', 'HLT_2e12_lhloose_L12EM10VH', 'HLT_2e15_vloose_L12EM13VH', 'HLT_2g20_loose_g15_loose', 'HLT_2mu10', 'HLT_2e12_lhvloose_nod0_L12EM10VH', 'HLT_2e12_lhloose_mu10', 'HLT_2e12_lhloose_nod0_mu10', 'HLT_2e12_lhmedium_mu10', 'HLT_2e12_lhmedium_nod0_mu10', 'HLT_2e12_lhvloose_L12EM10VH', 'HLT_2e12_loose_mu10', 'HLT_2e12_medium_mu10', 'HLT_2e15_lhvloose_L12EM13VH', 'HLT_2e15_lhvloose_nod0_L12EM13VH', 'HLT_2e17_lhloose', 'HLT_2e17_lhloose_L12EM15', 'HLT_2e17_lhloose_nod0_L12EM15', 'HLT_2e17_lhvloose', 'HLT_2e17_lhvloose_nod0', 'HLT_2e17_loose_L12EM15', 'HLT_2mu14', 'HLT_2mu15', 'HLT_2mu4', 'HLT_2mu6', 'HLT_e12_lhloose_2mu10', 'HLT_e12_lhloose_nod0_2mu10', 'HLT_e12_lhmedium_2mu10', 'HLT_e12_lhmedium_nod0_2mu10', 'HLT_e12_loose_2mu10', 'HLT_e12_medium_2mu10', 'HLT_e17_lhloose_2e9_lhloose', 'HLT_e17_lhloose_mu14', 'HLT_e17_lhloose_nod0_2e9_lhloose_nod0', 'HLT_e17_lhloose_nod0_mu14', 'HLT_e17_lhmedium_2e9_lhmedium', 'HLT_e17_lhmedium_nod0_2e9_lhmedium_nod0', 'HLT_e17_loose_mu14', 'HLT_e20_lhmedium_nod0_g35_loose', 'HLT_e20_medium_g35_loose', 'HLT_e24_lhmedium_L1EM15VH_g25_medium', 'HLT_e24_lhmedium_L1EM20VHI_mu8noL1', 'HLT_e24_lhmedium_nod0_L1EM15VH_g25_medium', 'HLT_e24_lhmedium_nod0_L1EM20VHI_mu8noL1', 'HLT_e24_medium_L1EM15VH_g25_medium', 'HLT_e24_medium_L1EM20VHI_mu8noL1', 'HLT_e26_lhmedium_L1EM22VHI_mu8noL1', 'HLT_e26_lhmedium_nod0_L1EM22VHI_mu8noL1', 'HLT_e26_medium_L1EM22VHI_mu8noL1', 'HLT_e5_lhtight_e4_etcut', 'HLT_e5_lhtight_nod0_e4_etcut', 'HLT_e5_tight_e4_etcut', 'HLT_e7_lhmedium_mu24', 'HLT_e7_lhmedium_nod0_mu24', 'HLT_e7_medium_mu24', 'HLT_mu20_2mu4noL1', 'HLT_mu20_mu8noL1', 'HLT_mu22_2mu4noL1', 'HLT_mu22_mu8noL1', 'HLT_mu24_2mu4noL1', 'HLT_mu24_mu8noL1', 'HLT_mu26_mu8noL1']

    #fakesElectronTriggerList = ['HLT_e17_lhloose_L1EM15', 'HLT_e17_loose_L1EM15', 'HLT_e60_medium', 'HLT_e60_lhmedium', 'HLT_e24_lhmedium_L1EM18VH', 'HLT_e24_lhmedium_L1EM20VH', 'HLT_e5_etcut', 'HLT_e10_etcut_L1EM7', 'HLT_e13_etcut_trkcut_L1EM10', 'HLT_e15_etcut_L1EM7', 'HLT_e18_etcut_trkcut_L1EM15', 'HLT_e20_etcut_L1EM12', 'HLT_e25_etcut_L1EM15', 'HLT_e30_etcut_L1EM15', 'HLT_e40_etcut_L1EM15', 'HLT_e50_etcut_L1EM15', 'HLT_e60_etcut', 'HLT_e5_lhvloose', 'HLT_e5_lhvloose_nod0', 'HLT_e10_lhvloose_L1EM7', 'HLT_e12_lhvloose_L1EM10VH', 'HLT_e12_lhvloose_nod0_L1EM10VH', 'HLT_e15_lhvloose_L1EM7', 'HLT_e15_lhvloose_L1EM13VH', 'HLT_e15_lhvloose_nod0_L1EM13VH', 'HLT_e17_lhvloose', 'HLT_e17_lhvloose_nod0', 'HLT_e20_lhvloose_L1EM12', 'HLT_e20_lhvloose', 'HLT_e20_lhvloose_nod0', 'HLT_e24_lhvloose_nod0_L1EM18VH', 'HLT_e24_lhvloose_nod0_L1EM20VH']
    #fakesPhotonTriggerList = ['HLT_g10_etcut', 'HLT_g10_loose', 'HLT_g15_loose_L1EM7', 'HLT_g20_loose_L1EM12', 'HLT_g20_loose_L1EM15', 'HLT_g20_etcut_L1EM12', 'HLT_g25_loose_L1EM15', 'HLT_g35_loose_L1EM15', 'HLT_g40_loose_L1EM15', 'HLT_g45_loose_L1EM15', 'HLT_g50_loose_L1EM15']
    #fakesMuonTriggerList = ['HLT_mu24_L1MU15', 'HLT_mu4', 'HLT_mu6', 'HLT_mu10', 'HLT_mu14', 'HLT_mu18', 'HLT_mu20_L1MU15', 'HLT_mu24', 'HLT_mu40', 'HLT_mu20_iloose_L1MU15']
    #fakesDiTriggerList = ['HLT_g35_loose_L1EM15_g25_loose_L1EM15', 'HLT_e20_lhmedium_g35_loose', 'HLT_2e12_loose_L12EM10VH', 'HLT_2e12_lhloose_L12EM10VH', 'HLT_2e15_vloose_L12EM13VH', 'HLT_2g20_loose_g15_loose']

    #fakesElectronTriggerList = [ "HLT_e17_lhloose_L1EM15", "HLT_e17_loose_L1EM15", "HLT_e60_medium", "HLT_e60_lhmedium", "HLT_e24_lhmedium_L1EM18VH" ]
    #fakesPhotonTriggerList = [ "HLT_g10_etcut", "HLT_g10_loose", "HLT_g15_loose_L1EM7", "HLT_g20_loose_L1EM12", "HLT_g20_loose_L1EM15", "HLT_g20_etcut_L1EM12", "HLT_g25_loose_L1EM15", "HLT_g35_loose_L1EM15", "HLT_g40_loose_L1EM15", "HLT_g45_loose_L1EM15", "HLT_g50_loose_L1EM15"]
    #fakesMuonTriggerList     = [ "HLT_mu24_L1MU15" ]
    #fakesDiTriggerList = [ "HLT_g35_loose_L1EM15_g25_loose_L1EM15", "HLT_e20_lhmedium_g35_loose", "HLT_2e12_loose_L12EM10VH", "HLT_2e12_lhloose_L12EM10VH", "HLT_2e15_vloose_L12EM13VH", "HLT_2g20_loose_g15_loose"]

    allFakableLeptonsTriggerList = fakesElectronTriggerList + fakesPhotonTriggerList + fakesMuonTriggerList + fakesDiTriggerList
    pass
hWWFakes.add_JobProperty(Trigger)


class Event(JobProperty):
    """
    Event steering for the Fake Factor analysis.
    """
    statusOn          = True
    allowedTypes      = ['bool']
    StoredValue       = True
    eFakeEvent        = "EventFakeE"
    mFakeEvent        = "EventFakeM"
    pass
hWWFakes.add_JobProperty(Event)
