#Wed Jan 30 20:55:59 2019"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from AthenaCommon.Configurable import *

class HWW__FakeLeptonEventBuilderAlg( ConfigurableAlgorithm ) :
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
    'LeptonContainer' : '', # str
    'FakableLeptonContainer' : '', # str
    'OtherLeptonContainer' : '', # str
    'JetContainer' : '', # str
    'EventContainer' : '', # str
    'WriteSplitOutputContainer' : True, # bool
    'MissingETContainer' : '', # str
    'MissingETObject' : '', # str
  }
  _propertyDocDct = { 
    'MissingETObject' : """ Name of the input missingET object """,
    'MissingETContainer' : """ Name of the input missingET container """,
    'WriteSplitOutputContainer' : """ Decide if we want to write a fully-split AuxContainer such that we can remove any variables """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'LeptonContainer' : """ Name of the input fully identified lepton container """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'Cardinality' : """ How many clones to create """,
    'EventContainer' : """ Name of the output event container """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'FakableLeptonContainer' : """ Name of the input fakable lepton container """,
    'OtherLeptonContainer' : """ Name of the input container for other leptons """,
    'JetContainer' : """ Name of the input jet container """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__FakeLeptonEventBuilderAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'HWWFakeFactorxAOD'
  def getType( self ):
      return 'HWW::FakeLeptonEventBuilderAlg'
  pass # class HWW__FakeLeptonEventBuilderAlg
