##=============================================================================
## Name:        HWWlnulnuAnalysisFlags.py
##
## Author:      Karsten Koeneke
## Created:     August 2014
##
## Description: Here, all neccessary job flags for the Higgs->WW->lnulnu analysis
##              are defined.
##=============================================================================

__doc__ = """Here, all neccessary job flags for the Higgs->WW->lnulnu analysis are defined."""
__version__ = "0.0.1"
__author__  = "Karsten Koeneke <karsten.koeneke@cern.ch>"

from AthenaCommon.JobProperties import JobProperty, JobPropertyContainer
from AthenaCommon.JobProperties import jobproperties

# Import the module that allows to use named units, e.g. GeV
from AthenaCommon.SystemOfUnits import *

# Import the common steering flags for this analysis
#from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon
import PhysicsxAODConfig.HWWCommonAnalysisFlags as hWWCommonFlags
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon


#=====================================================================
# First define container for the flags
#=====================================================================
class HWWlnulnuAnalysisFlags(JobPropertyContainer):
    """ The Higgs->WW->lnulnu analysis flag/job property container."""
jobproperties.add_Container(HWWlnulnuAnalysisFlags)

#short-cut to get the HiggsWWlnulnuAnalysisFlags container with this one line:
#'from HWWlnulnuxAODConfig.HWWlnulnuAnalysisFlags import hWWlnulnu'
#Note that name has to be different to avoid problems with pickle
hWWlnulnu = jobproperties.HWWlnulnuAnalysisFlags



#=====================================================================
# Now define each flag and add it to the container
#=====================================================================

class Global(hWWCommonFlags.Global):
    """
    Global steering for the H->WW->lnulnu analysis.
    The common parts are directly taken from PhysicsxAODConfig/python/HWWCommonFlags.py.
    """
    statusOn                   = True
    allowedTypes               = ['bool']
    StoredValue                = True
    DPDMakerScript             = "HWWlnulnuxAODConfig/HWWlnulnuAnalysisCommon.py"
    writeMinixAOD              = False
    StreamName                 = "PAOD_2L"
    FileName                   = "PAOD_2L.pool.root"
    writeDifferentFlavorPxAOD  = False
    DFStreamName               = "PAOD_2LDF"
    DFFileName                 = "PAOD_2LDF.pool.root"
    writeDiJetPxAOD            = False
    DiJetStreamName            = "PAOD_2LJJ"
    DiJetFileName              = "PAOD_2LJJ.pool.root"
    writeDiJetDFPxAOD          = False
    DiJetDFStreamName          = "PAOD_2LJJDF"
    DiJetDFFileName            = "PAOD_2LJJDF.pool.root"
    write2LFakePxAOD           = False
    FakesStreamName           = "PAOD_2LFake"
    FakesFileName             = "PAOD_2LFake.pool.root"
    writeZFakePxAOD            = False
    ZFakesStreamName           = "PAOD_2LZFake"
    ZFakesFileName             = "PAOD_2LZFake.pool.root"
    writeTopFakePxAOD          = False
    TopFakesStreamName         = "PAOD_2LTopFake"
    TopFakesFileName           = "PAOD_2LTopFake.pool.root"
    doSkimming                 = True
    acceptAlgList              = [] # This is a default. It will be filled during the job setup
    pass
hWWlnulnu.add_JobProperty(Global)


class Event(JobProperty):
    """
    Event steering for the H->WW->lnulnu analysis.
    """
    statusOn          = True
    allowedTypes      = ['bool']
    StoredValue       = True
    eeEvent           = "EventEE"
    mmEvent           = "EventMM"
    emEvent           = "EventEM"
    meEvent           = "EventME"
    pass
hWWlnulnu.add_JobProperty(Event)


class TruthEvent(JobProperty):
    """
    TruthEvent steering for the H->WW->lnulnu analysis
    """
    statusOn          = True
    allowedTypes      = ['bool']
    StoredValue       = True
    eeEvent           = "EventTruthEE"
    mmEvent           = "EventTruthMM"
    emEvent           = "EventTruthEM"
    meEvent           = "EventTruthME"
    pass
hWWlnulnu.add_JobProperty(TruthEvent)
