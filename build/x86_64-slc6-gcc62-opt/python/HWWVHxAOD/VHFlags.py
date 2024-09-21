from AthenaCommon.JobProperties import JobProperty, JobPropertyContainer
from AthenaCommon.JobProperties import jobproperties

# Import the module that allows to use named units, e.g. GeV
from AthenaCommon.SystemOfUnits import *

import PhysicsxAODConfig.HWWCommonAnalysisFlags as hWWCommonFlags
#import PhysicsxAODConfig.HWWTruthCommonAnalysisFlags as flags_common
from   PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon

#=====================================================================
# First define container for the flags
#=====================================================================
class VHFlags(JobPropertyContainer):
    """ The VH->WW->lnulnu analysis flag/job property container."""
jobproperties.add_Container(VHFlags)

#short-cut to get the HiggsWWlnulnuAnalysisFlags container with this one line:
#'from HWWlnulnuxAODConfig.HWWlnulnuAnalysisFlags import hWWlnulnu'
#Note that name has to be different to avoid problems with pickle
vh_flags = jobproperties.VHFlags

class Global(hWWCommonFlags.Global):
    """Global steering for the V(H->WW) analyses"""
    statusOn                   = True
    allowedTypes               = ['bool']
    StoredValue                = True
    DPDMakerScript             = "HWWVHxAOD/VHAnalysisCommon.py"
    StreamName                 = "StreamDAOD_VH"
    FileName                   = "VH_mini_xAOD.pool.root"
    writeMinixAOD              = False
    writeFlatEvent             = True
    writeLeptonTrackParticles  = False
    writeLeptonCaloClusters    = False
    writeJetCaloClusters       = False
    doSkimming                 = True
    acceptAlgList              = [] # This is a default. It will be filled during the job setup
    pass
vh_flags.add_JobProperty(Global)

class Event(hWWCommonFlags.Global):
    """Event steering for the V(H->WW) analyses"""
vh_flags.add_JobProperty(Event)

class Leptons(hWWCommonFlags.Global):
    """Electron definitions for the V(H->WW) analyses"""
vh_flags.add_JobProperty(Leptons)

class Electrons(hWWCommonFlags.Electrons):
    """Electron definitions for the V(H->WW) analyses"""
vh_flags.add_JobProperty(Electrons)

class Muons(hWWCommonFlags.Muons):
    """Muon definitions for the V(H->WW) analyses"""
vh_flags.add_JobProperty(Muons)

class Jets(hWWCommonFlags.Jets):
    """Jet definitions for the V(H->WW) analyses"""
vh_flags.add_JobProperty(Jets)

class MET(hWWCommonFlags.MET):
    """MET definitions for the V(H->WW) analyses"""
vh_flags.add_JobProperty(MET)

class TruthElectrons(hWWCommonFlags.TruthElectrons):
    """TruthElectron definitions for the V(H->WW) analyses"""
vh_flags.add_JobProperty(TruthElectrons)

class TruthMuons(hWWCommonFlags.TruthMuons):
    """TruthMuon definitions for the V(H->WW) analyses"""
vh_flags.add_JobProperty(TruthMuons)

class TruthJets(hWWCommonFlags.TruthJets):
    """TruthJet definitions for the V(H->WW) analyses"""
vh_flags.add_JobProperty(TruthJets)

class TruthMET(hWWCommonFlags.TruthMET):
    """TruthMET definitions for the V(H->WW) analyses"""
vh_flags.add_JobProperty(TruthMET)
