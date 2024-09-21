#Wed Jan 30 20:56:40 2019"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from AthenaCommon.Configurable import *

class HWW__VHFlatEventBuilderAlg( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCounter' : 0, # int
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : False, # bool
    'IsClonable' : False, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'LeptonsContainer' : '', # str
    'JetContainer' : '', # str
    'MissingETContainer' : '', # str
    'MissingETObject' : '', # str
    'OtherJetContainer' : '', # str
    'EventContainer' : '', # str
    'WriteSplitOutputContainer' : True, # bool
  }
  _propertyDocDct = { 
    'WriteSplitOutputContainer' : """ Decide if we want to write a fully-split AuxContainer such that we can remove any variables """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'OtherJetContainer' : """ Name of the input container for other jets, i.e., the ones for the sub-threshold jets """,
    'MissingETContainer' : """ Name of the input missingET container """,
    'MissingETObject' : """ Name of the input missingET object """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'LeptonsContainer' : """ Name of the input leptons container """,
    'Cardinality' : """ How many clones to create """,
    'EventContainer' : """ Name of the output event container """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'JetContainer' : """ Name of the input jet container """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__VHFlatEventBuilderAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'HWWVHxAOD'
  def getType( self ):
      return 'HWW::VHFlatEventBuilderAlg'
  pass # class HWW__VHFlatEventBuilderAlg

class HWW__VHLepSortingAlg( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCounter' : 0, # int
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'Timeline' : True, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : False, # bool
    'IsClonable' : False, # bool
    'Cardinality' : 1, # int
    'NeededResources' : [  ], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'CutFlowSvc' : ServiceHandle('CutFlowSvc/CutFlowSvc'), # GaudiHandle
    'FilterDescription' : 'N/A', # str
    'nLeptons' : 3, # int
    'InputMuonContainer' : '', # str
    'InputElectronContainer' : '', # str
    'OutputContainer' : '', # str
    'WriteSplitOutputContainer' : True, # bool
    'doTruthPAOD' : False, # bool
  }
  _propertyDocDct = { 
    'doTruthPAOD' : """ Decide if we want to run from Truth """,
    'WriteSplitOutputContainer' : """ Decide if we want to write a fully-split AuxContainer such that we can remove any variables """,
    'OutputContainer' : """ Name of the output leptons container """,
    'InputElectronContainer' : """ Name of the input electron container """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'Cardinality' : """ How many clones to create """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'nLeptons' : """ Number of leptons targeted in the final state (3 or 4) """,
    'CutFlowSvc' : """ handle to the ICutFlowSvc instance this filtering algorithm will use for building the flow of cuts. """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'FilterDescription' : """ describe to the cutflowsvc what this filter does. """,
    'InputMuonContainer' : """ Name of the input muon container """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__VHLepSortingAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'HWWVHxAOD'
  def getType( self ):
      return 'HWW::VHLepSortingAlg'
  pass # class HWW__VHLepSortingAlg
