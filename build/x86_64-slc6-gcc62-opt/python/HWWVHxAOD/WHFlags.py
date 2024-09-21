import HWWVHxAOD.VHFlags as flags_vh

class Global(flags_vh.Global):
    """Global steering for the W(H->WW) analyses"""
    StreamName = "PAOD_WH"
    FileName = "PAOD_WH.pool.root"
    #prefix is now used primarily as a suffix
    prefix        = "WH"
    truthPrefix   = "TruthWH"
    acceptAlgList = [] # This is a default. It will be filled during the job setup

class Event(flags_vh.Event):
    """Event steering for the W(H->WW) analyses"""
    cont = 'Event' + Global.prefix

class Leptons(flags_vh.Leptons):
    """Lepton definitions for the W(H->WW) analyses"""
    cont = 'SortedLeptons' + Global.prefix

class Electrons(flags_vh.Electrons):
    """Electron definitions for the W(H->WW) analyses"""

class Muons(flags_vh.Muons):
    """Muon definitions for the W(H->WW) analyses"""

class Jets(flags_vh.Jets):
    """Jet definitions for the W(H->WW) analyses"""

class MET(flags_vh.MET):
    """MET definitions for the W(H->WW) analyses"""

class TruthEvent(flags_vh.Event):
    """Event steering for the W(H->WW) analyses"""
    cont = 'Event' + Global.truthPrefix

class TruthLeptons(flags_vh.Leptons):
    """TruthLepton definitions for the W(H->WW) analyses"""
    cont = 'SortedLeptons' + Global.truthPrefix

class TruthElectrons(flags_vh.TruthElectrons):
    """TruthElectron definitions for the W(H->WW) analyses"""

class TruthMuons(flags_vh.TruthMuons):
    """TruthMuon definitions for the W(H->WW) analyses"""

class TruthJets(flags_vh.TruthJets):
    """TruthJet definitions for the W(H->WW) analyses"""

class TruthMET(flags_vh.TruthMET):
    """TruthMET definitions for the W(H->WW) analyses"""
