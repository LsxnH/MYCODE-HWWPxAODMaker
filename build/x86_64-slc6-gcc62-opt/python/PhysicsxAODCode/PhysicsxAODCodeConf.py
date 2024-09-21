#Wed Jan 30 20:57:46 2019"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from AthenaCommon.Configurable import *

class HWW__BtagScaleFactorAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'ContainersFinderTool' : PublicToolHandle('HWW::ContainersFinderTool/ContainersFinderTool'), # GaudiHandle
    'DecorateAllCopies' : True, # bool
    'Separator' : '___', # str
    'TaggerName' : 'MV2c10', # str
    'OperatingPoint' : 0.17580000, # float
    'BTaggingEfficiencyTool' : PrivateToolHandle('BTaggingEfficiencyTool/BTaggingEfficiencyTool'), # GaudiHandle
    'BTaggingSelectionTool' : PrivateToolHandle('BTaggingEfficiencyTool/BTaggingSelectionTool'), # GaudiHandle
    'EfficiencySystematicVariations' : [  ], # list
    'EfficiencyScaleFactorVarName' : 'effiSF', # str
    'MinJetPt' : 0.0000000, # float
    'AbortOnUncheckedCorrectionCode' : False, # bool
  }
  _propertyDocDct = { 
    'AbortOnUncheckedCorrectionCode' : """ Abort on an unchecked CP::CorrectionCode """,
    'EfficiencyScaleFactorVarName' : """ The name of the efficiency scale-factor variable that will be added to the jet """,
    'BTaggingSelectionTool' : """ The ToolHandle for the b-tagging selection tool """,
    'BTaggingEfficiencyTool' : """ The ToolHandle for the b-tagging efficiency scale factor tool """,
    'OperatingPoint' : """ The cut value on the b-tagging discriminant """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'TaggerName' : """ The name of the tagger that we want to use (default='MV2c20') """,
    'InputContainer' : """ Input container name """,
    'EfficiencySystematicVariations' : """ The names of all systematic variations to be applied """,
    'Cardinality' : """ How many clones to create """,
    'ContainersFinderTool' : """ The tool that tries to find all input containers, including their systematic variations """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'MinJetPt' : """ The cut value on the minimum jet pt """,
    'DecorateAllCopies' : """ If true, will decorate all copies of the input container """,
    'Separator' : """ The string seperator between the output container name and the sytematic variation (default='___') """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__BtagScaleFactorAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::BtagScaleFactorAlg'
  pass # class HWW__BtagScaleFactorAlg

class HWW__ContainersFinderTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'NominalSuffix' : '', # str
    'Separator' : '___', # str
  }
  _propertyDocDct = { 
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Separator' : """ The string seperator between the variable/container name and its sytematic variation (default='___') """,
    'NominalSuffix' : """ The suffix for the nominal name (default='') """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__ContainersFinderTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::ContainersFinderTool'
  pass # class HWW__ContainersFinderTool

class HWW__ElectronCalibrationSmearingAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'OutputContainer' : '', # str
    'Separator' : '___', # str
    'EgammaCalibrationTool' : PrivateToolHandle('CP::IEgammaCalibrationAndSmearingTool'), # GaudiHandle
    'MomentumSystematicVariations' : [  ], # list
    'EGammeIsolationCorrectionTool' : PrivateToolHandle('CP::IsolationCorrectionTool/IsolationCorrectionTool'), # GaudiHandle
  }
  _propertyDocDct = { 
    'EGammeIsolationCorrectionTool' : """ The EGamma isolation correction tool """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'InputContainer' : """ Input container name """,
    'Cardinality' : """ How many clones to create """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'MomentumSystematicVariations' : """ The names of all systematic variations to be applied """,
    'EgammaCalibrationTool' : """ The ToolHandle for the electron four-momentum correction tool """,
    'OutputContainer' : """ The name of the output container with the deep copy of input objects """,
    'Separator' : """ The string seperator between the output container name and the sytematic variation (default='___') """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__ElectronCalibrationSmearingAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::ElectronCalibrationSmearingAlg'
  pass # class HWW__ElectronCalibrationSmearingAlg

class HWW__ElectronDecorationAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'SelectionToolList' : PublicToolHandleArray([]), # GaudiHandleArray
    'SelectionToolDecoList' : [  ], # list
    'SelectionWithVertexToolList' : PublicToolHandleArray([]), # GaudiHandleArray
    'SelectionWithVertexToolDecoList' : [  ], # list
    'IsolationToolList' : PublicToolHandleArray([]), # GaudiHandleArray
    'IsolationToolDecoList' : [  ], # list
    'TransferValueSources' : [  ], # list
    'TransferValueTargets' : [  ], # list
    'DoImpactParameter' : False, # bool
    'PrimaryVertexContainer' : 'PrimaryVertices', # str
    'DoAmbiguity' : False, # bool
    'EGammeAmbiguityTool' : PrivateToolHandle('EGammaAmbiguityTool/EGammaAmbiguityTool'), # GaudiHandle
    'EGammeAmbiguityToolTight' : PrivateToolHandle('EGammaAmbiguityTool/EGammaAmbiguityTool'), # GaudiHandle
    'DoChargeIDTagging' : False, # bool
    'ElectronChargeIDSelectorTool' : PrivateToolHandle('AsgElectronChargeIDSelectorTool/AsgElectronChargeIDSelectorTool'), # GaudiHandle
    'DoTruthInformation' : False, # bool
    'DecorateAllCopies' : False, # bool
  }
  _propertyDocDct = { 
    'DoTruthInformation' : """ If true, will decorate charge and pt to ele """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'SelectionToolList' : """ List of Electron ID selection tool instances """,
    'DoImpactParameter' : """ If true, will calculate and store the z0sinTheta, d0, and d0Err """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'SelectionWithVertexToolList' : """ List of selection-with-vertex tool instances """,
    'Cardinality' : """ How many clones to create """,
    'SelectionWithVertexToolDecoList' : """ List of decoration names for each selection-with-vertex tools """,
    'DecorateAllCopies' : """ If true, will decorate all copies of the input container """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'IsolationToolDecoList' : """ List of electron isolation result names """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsolationToolList' : """ List of CP tool to calculate the lepton isolation """,
    'TransferValueSources' : """ Transfer variables from the input (given here) to the output """,
    'TransferValueTargets' : """ Transfer variables from the input to the output (given here) """,
    'PrimaryVertexContainer' : """ The input primary vertex container name """,
    'EGammeAmbiguityToolTight' : """ The egamma ambiguity tool (tight) """,
    'DoAmbiguity' : """ If true, will calculate and store the result of the egamma ambiguity tool """,
    'SelectionToolDecoList' : """ List of electron decoration names """,
    'DoChargeIDTagging' : """ If true, will calculate and store the result of the electron Charge ID selector """,
    'ElectronChargeIDSelectorTool' : """ The electron charge ID selector tool """,
    'InputContainer' : """ Input container name """,
    'EGammeAmbiguityTool' : """ The egamma ambiguity tool """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__ElectronDecorationAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::ElectronDecorationAlg'
  pass # class HWW__ElectronDecorationAlg

class HWW__ElectronScaleFactorAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'ContainersFinderTool' : PublicToolHandle('HWW::ContainersFinderTool/ContainersFinderTool'), # GaudiHandle
    'DecorateAllCopies' : True, # bool
    'Separator' : '___', # str
    'ElectronEfficiencyScaleFactorTools' : PrivateToolHandleArray([]), # GaudiHandleArray
    'EfficiencyScaleFactorVarNames' : [  ], # list
    'EfficiencySystematicVariations' : [  ], # list
    'RunAlsoOnData' : False, # bool
  }
  _propertyDocDct = { 
    'RunAlsoOnData' : """ Boolean variable to define if the algorithm should also run on data or not (default: not) """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'InputContainer' : """ Input container name """,
    'EfficiencySystematicVariations' : """ The names of all systematic variations to be applied """,
    'ElectronEfficiencyScaleFactorTools' : """ The ToolHandle for the electron efficiency scale factor tool """,
    'Cardinality' : """ How many clones to create """,
    'EfficiencyScaleFactorVarNames' : """ The name of the efficiency scale-factor variable that will be added to the electron """,
    'ContainersFinderTool' : """ The tool that tries to find all input containers, including their systematic variations """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'DecorateAllCopies' : """ If true, will decorate all copies of the input container """,
    'Separator' : """ The string seperator between the output container name and the sytematic variation (default='___') """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__ElectronScaleFactorAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::ElectronScaleFactorAlg'
  pass # class HWW__ElectronScaleFactorAlg

class HWW__ElectronSelectionTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'CutObjectQualityMask' : 0, # int
    'RequireIsElectronAuthor' : False, # bool
    'CutPtMin' : -99999.000, # float
    'CutAbsEtaMax' : 1.7976931e+308, # float
    'CutAbsEtaCrackMin' : -1000.0000, # float
    'CutAbsEtaCrackMax' : -1000.0000, # float
    'CutIDList' : [  ], # list
    'CutIDPtMinList' : [  ], # list
    'CutZ0SinThetaMax' : 3.40282e+38, # float
    'CutD0SignificanceMax' : 3.40282e+38, # float
    'CaloIsoList' : [  ], # list
    'CaloIsoRelativeMaxCutList' : [  ], # list
    'CaloIsoMaxCutList' : [  ], # list
    'CutCaloIsoPtMinList' : [  ], # list
    'TrackIsoList' : [  ], # list
    'TrackIsoRelativeMaxCutList' : [  ], # list
    'TrackIsoMaxCutList' : [  ], # list
    'CutTrackIsoPtMinList' : [  ], # list
  }
  _propertyDocDct = { 
    'CutTrackIsoPtMinList' : """ The minimum pt cuts for the track isolation list """,
    'CaloIsoMaxCutList' : """ The absolute calorimetric isolation maximum cut list """,
    'CutCaloIsoPtMinList' : """ The minimum pt cuts for the calorimetric isolation list """,
    'CutD0SignificanceMax' : """ The electron d0 maximum cut value """,
    'CaloIsoRelativeMaxCutList' : """ The relativ calorimetric isolation maximum cut list """,
    'CutIDPtMinList' : """ The electron.pt minimum cuts for the identification selection; must be ordered from lowest to highest """,
    'TrackIsoList' : """ The track isolation types list """,
    'CutAbsEtaMax' : """ The |electron.cluster().eta()| maximum cut value """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'CutZ0SinThetaMax' : """ The electron z0 maximum cut value """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'CutIDList' : """ The electron identification selection list """,
    'CutObjectQualityMask' : """ The electron object quality cut mask """,
    'RequireIsElectronAuthor' : """ The electron author cut """,
    'TrackIsoMaxCutList' : """ The absolute track isolation maximum cut list """,
    'CutPtMin' : """ The electron.pt() minimum cut value """,
    'TrackIsoRelativeMaxCutList' : """ The relativ track isolation maximum cut list """,
    'CaloIsoList' : """ The calorimetric isolation types list """,
    'CutAbsEtaCrackMin' : """ The |electron.cluster().eta()| minimum cut value for the calo crack """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'CutAbsEtaCrackMax' : """ The |electron.cluster().eta()| maximum cut value for the calo crack """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__ElectronSelectionTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::ElectronSelectionTool'
  pass # class HWW__ElectronSelectionTool

class HWW__EventInfoDecorationAlg( ConfigurableAlgorithm ) :
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
    'EventInfo' : 'EventInfo', # str
    'PrimaryVertexContainer' : 'PrimaryVertices', # str
    'PrimVtxIdxVarName' : 'primVtxIdx', # str
    'NPrimVtxVarName' : 'nPrimVtx', # str
    'NPrimVtxTwoTrackVarName' : 'nPrimVtxTwoTrk', # str
    'NPrimVtxThreeTrackVarName' : 'nPrimVtxThreeTrk', # str
    'NPrimVtxFourTrackVarName' : 'nPrimVtxFourTrk', # str
  }
  _propertyDocDct = { 
    'NPrimVtxFourTrackVarName' : """ Variable name for the resuling variable that holds the number of vertices with four or more tracks """,
    'NPrimVtxThreeTrackVarName' : """ Variable name for the resuling variable that holds the number of vertices with three or more tracks """,
    'NPrimVtxTwoTrackVarName' : """ Variable name for the resuling variable that holds the number of vertices with two or more tracks """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'Cardinality' : """ How many clones to create """,
    'PrimaryVertexContainer' : """ The input primary vertex container name """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EventInfo' : """ Input container name """,
    'PrimVtxIdxVarName' : """ Variable name for the resuling variable that holds the index of the found primary vertex """,
    'NPrimVtxVarName' : """ Variable name for the resuling variable that holds the number of vertices """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__EventInfoDecorationAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::EventInfoDecorationAlg'
  pass # class HWW__EventInfoDecorationAlg

class HWW__EventSelectionAlg( ConfigurableAlgorithm ) :
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
    'InputContainerList' : [  ], # list
    'MinNOtherLeptons' : 0, # int
    'MinNJets' : 0, # int
    'MinNBJets' : 0, # int
    'TaggerName' : 'MV2c10', # str
    'BTagOperatingPoint' : 0.17580000, # float
    'HasIdentifiedFakeMuon' : False, # bool
    'HasIdentifiedOtherMuon' : False, # bool
  }
  _propertyDocDct = { 
    'BTagOperatingPoint' : """ The cut value on the b-tagging discriminant """,
    'TaggerName' : """ The name of the tagger that we want to use (default='MV2c20') """,
    'MinNBJets' : """ The minimum number of b-tagged jets required """,
    'MinNJets' : """ The minimum number of jets required """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'HasIdentifiedOtherMuon' : """ Ask for an identified other muon """,
    'Cardinality' : """ How many clones to create """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'CutFlowSvc' : """ handle to the ICutFlowSvc instance this filtering algorithm will use for building the flow of cuts. """,
    'InputContainerList' : """ Input container name list """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'FilterDescription' : """ describe to the cutflowsvc what this filter does. """,
    'HasIdentifiedFakeMuon' : """ Ask for an identified fake muon """,
    'MinNOtherLeptons' : """ The minimum number of other leptons required """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__EventSelectionAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::EventSelectionAlg'
  pass # class HWW__EventSelectionAlg

class HWW__FatJetDecorationAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'BosonTaggerWorkingPoint' : 'medium', # str
    'BosonTaggerAlgorithm' : 'smooth', # str
    'WBosonTaggerConfig' : '', # str
    'ZBosonTaggerConfig' : '', # str
    'DecorateAllCopies' : False, # bool
  }
  _propertyDocDct = { 
    'DecorateAllCopies' : """ If true, will decorate all copies of the input container """,
    'ZBosonTaggerConfig' : """ The config file of the Z-boson taggers """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'InputContainer' : """ Input container name """,
    'Cardinality' : """ How many clones to create """,
    'BosonTaggerWorkingPoint' : """ The working point of the boson taggers """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'WBosonTaggerConfig' : """ The config file of the W-boson taggers """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'BosonTaggerAlgorithm' : """ The algorithm of the boson taggers """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__FatJetDecorationAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::FatJetDecorationAlg'
  pass # class HWW__FatJetDecorationAlg

class HWW__FullEventBuilderAlg( ConfigurableAlgorithm ) :
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
    'Lepton1Container' : '', # str
    'Lepton2Container' : '', # str
    'JetContainer' : '', # str
    'MissingETContainer' : '', # str
    'MissingETObject' : '', # str
    'OtherElectronContainer' : '', # str
    'OtherMuonContainer' : '', # str
    'OtherJetContainer' : '', # str
    'EventContainer' : '', # str
    'WriteSplitOutputContainer' : True, # bool
    'CutLeadingLeptonPtMin' : 0.0000000, # float
  }
  _propertyDocDct = { 
    'CutLeadingLeptonPtMin' : """ Name of the leading-lepton pt cut """,
    'WriteSplitOutputContainer' : """ Decide if we want to write a fully-split AuxContainer such that we can remove any variables """,
    'MissingETObject' : """ Name of the input missingET object """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'OtherJetContainer' : """ Name of the input container for other jets, i.e., the ones for the sub-threshold jets """,
    'MissingETContainer' : """ Name of the input missingET container """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'OtherMuonContainer' : """ Name of the input container for other muons, i.e., the ones for the third lepton veto """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'Cardinality' : """ How many clones to create """,
    'EventContainer' : """ Name of the output event container """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'OtherElectronContainer' : """ Name of the input container for other electrons, i.e., the ones for the third lepton veto """,
    'Lepton2Container' : """ Name of the input lepton 2 container """,
    'Lepton1Container' : """ Name of the input lepton 1 container """,
    'JetContainer' : """ Name of the input jet container """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__FullEventBuilderAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::FullEventBuilderAlg'
  pass # class HWW__FullEventBuilderAlg

class HWW__GoodRunsListSelectionAlg( ConfigurableAlgorithm ) :
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
    'GoodRunsListVec' : [  ], # list
  }
  _propertyDocDct = { 
    'FilterDescription' : """ describe to the cutflowsvc what this filter does. """,
    'CutFlowSvc' : """ handle to the ICutFlowSvc instance this filtering algorithm will use for building the flow of cuts. """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'GoodRunsListVec' : """ The list of GoodRunsList names """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__GoodRunsListSelectionAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::GoodRunsListSelectionAlg'
  pass # class HWW__GoodRunsListSelectionAlg

class HWW__JetCalibrationSmearingAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'OutputContainer' : '', # str
    'JetCalibrationTool' : PrivateToolHandle(''), # GaudiHandle
    'DoBJESLabeling' : True, # bool
    'JetUncertaintyTool' : PublicToolHandle(''), # GaudiHandle
    'JetSystematicsUncertaintyTool' : PublicToolHandle(''), # GaudiHandle
    'JetSystematicVariations' : [  ], # list
    'MCType' : 'MC16', # str
    'JetSystematicsNameSuffix' : '', # str
    'Separator' : '___', # str
    'DoFatJetHack' : False, # bool
  }
  _propertyDocDct = { 
    'Separator' : """ The string seperator between the output container name and the sytematic variation (default='___') """,
    'JetSystematicsNameSuffix' : """ The suffix for the systematic variation name as used in the output container name; to be added before the '__1up/down' part """,
    'MCType' : """ The name of the MC, either 'MC16' (default) or 'AFII' """,
    'JetSystematicsUncertaintyTool' : """ The ToolHandle for the jet uncertainties tool for systematics """,
    'DoFatJetHack' : """ Enable a hack for using the fat-jet """,
    'JetUncertaintyTool' : """ The ToolHandle for the jet uncertainties tool """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'InputContainer' : """ Input container name """,
    'Cardinality' : """ How many clones to create """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'OutputContainer' : """ The name of the output container with the shallow copy of input objects """,
    'DoBJESLabeling' : """ Enable using the truth b-jet labeling to get flavor-dependent JES uncertainties (default: true) """,
    'JetSystematicVariations' : """ The names of all systematic variations to be applied to the JES/JER """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'JetCalibrationTool' : """ The ToolHandle for the jet calibration tool """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__JetCalibrationSmearingAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::JetCalibrationSmearingAlg'
  pass # class HWW__JetCalibrationSmearingAlg

class HWW__JetDecorationAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'PrimaryVertexContainer' : 'PrimaryVertices', # str
    'TruthEventContainer' : '', # str
    'JetSelectionToolList' : PublicToolHandleArray([]), # GaudiHandleArray
    'JetDecorationList' : [  ], # list
    'SelectionWithVertexToolList' : PublicToolHandleArray([]), # GaudiHandleArray
    'SelectionWithVertexToolDecoList' : [  ], # list
    'JVTUpdateTool' : PublicToolHandle('JetVertexTaggerTool/JetVertexTaggerTool'), # GaudiHandle
    'UpdateJVT' : False, # bool
    'UpdateJVTName' : 'calibJvt', # str
    'ForwardJvtTool' : PublicToolHandle('JetForwardJvtTool/JetForwardJvtTool'), # GaudiHandle
    'ForwardJvtTightTool' : PublicToolHandle('JetForwardJvtTool/JetForwardJvtTightTool'), # GaudiHandle
    'DoForwardJvt' : False, # bool
    'DoJvtPileupTruthLabeling' : True, # bool
    'BTagNameList' : [  ], # list
    'InputTruthContainer' : '', # str
    'TruthMatchName' : 'hardScatterTruthMatchDeltaR', # str
    'TruthJetPtName' : 'hardScatterTruthJetPt', # str
    'TruthJetMinPt' : 10000.000, # float
    'TruthMatchMaxDeltaR' : 0.30000000, # float
  }
  _propertyDocDct = { 
    'TruthJetPtName' : """ Variable name for the resulting truth-jet pt """,
    'JetSelectionToolList' : """ List of JetSelectionTool instances """,
    'TruthJetMinPt' : """ The minimum pt threshold for a truth-jet to be considered for matching """,
    'TruthEventContainer' : """ The input TruthEventContainer name """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'PrimaryVertexContainer' : """ The input primary vertex container name """,
    'TruthMatchMaxDeltaR' : """ The maximum deltaR (using rapidity and NOT eta) distance for a successful truth match """,
    'UpdateJVT' : """ Declare if JVT should be updated """,
    'SelectionWithVertexToolDecoList' : """ List of decoration names for each selection-with-vertex tools """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'JetDecorationList' : """ List of jet decoration names """,
    'DoJvtPileupTruthLabeling' : """ Do the jet JVT pileup truth labeling (requires also InputTruthContainer to be set to a valid truth jet container) """,
    'JVTUpdateTool' : """ The CP tool to correct the JVT variable for calibrated jets. No need to set one in the job option as the default instance is OK. """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'ForwardJvtTool' : """ The tool handle for the forwardJVT and the truth pileup labeling """,
    'UpdateJVTName' : """ Variable name for the updated JVT """,
    'InputContainer' : """ Input container name """,
    'ForwardJvtTightTool' : """ The tool handle for the tight forwardJVT labeling """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'SelectionWithVertexToolList' : """ List of selection-with-vertex tool instances """,
    'DoForwardJvt' : """ Declare if forwardJVT should be calculated """,
    'TruthMatchName' : """ Variable name for the resulting truth match """,
    'BTagNameList' : """ List of b-tagger names """,
    'InputTruthContainer' : """ Input jet truth container name for truth matching """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__JetDecorationAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::JetDecorationAlg'
  pass # class HWW__JetDecorationAlg

class HWW__JetEventCleaningAlg( ConfigurableAlgorithm ) :
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
    'Eventcleanflag' : 'DFCommonJets_eventClean_LooseBad', # str
  }
  _propertyDocDct = { 
    'FilterDescription' : """ describe to the cutflowsvc what this filter does. """,
    'Eventcleanflag' : """ Eventcleaning flag """,
    'CutFlowSvc' : """ handle to the ICutFlowSvc instance this filtering algorithm will use for building the flow of cuts. """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__JetEventCleaningAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::JetEventCleaningAlg'
  pass # class HWW__JetEventCleaningAlg

class HWW__JetJVTScaleFactorAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'InputAllCalibORJets' : '', # str
    'ContainersFinderTool' : PublicToolHandle('HWW::ContainersFinderTool/ContainersFinderTool'), # GaudiHandle
    'JetJvtEfficiencyTool' : PrivateToolHandle('CP::JetJvtEfficiency/JetJvtEfficiencyTool'), # GaudiHandle
    'EfficiencySystematicVariations' : [  ], # list
    'EfficiencyScaleFactorVarName' : '', # str
    'Separator' : '___', # str
    'PassJVTVarName' : '', # str
    'AbortOnUncheckedCorrectionCode' : False, # bool
    'DecorateAllCopies' : True, # bool
    'DecorateJets' : True, # bool
    'DecorateEvent' : True, # bool
  }
  _propertyDocDct = { 
    'DecorateJets' : """ If true, will decorate each individual jet """,
    'DecorateAllCopies' : """ If true, will decorate all copies of the input container """,
    'Separator' : """ The string seperator between the variable/container name and its sytematic variation (default='___') """,
    'AbortOnUncheckedCorrectionCode' : """ Abort on an unchecked CP::CorrectionCode """,
    'EfficiencyScaleFactorVarName' : """ The name of the efficiency scale-factor variable that will be added to the jet """,
    'PassJVTVarName' : """ The name of the variable for passing the JVT selection """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'InputAllCalibORJets' : """ The input jet container name for the calibrated, overlap-removed jets """,
    'DecorateEvent' : """ If true, will decorate the event with the combined scale-factor and uncertainty """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'InputContainer' : """ Input container name """,
    'EfficiencySystematicVariations' : """ The names of all systematic variations to be applied """,
    'Cardinality' : """ How many clones to create """,
    'ContainersFinderTool' : """ The tool that tries to find all input containers, including their systematic variations """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'JetJvtEfficiencyTool' : """ The CP::IJetJvtEfficiency instance """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__JetJVTScaleFactorAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::JetJVTScaleFactorAlg'
  pass # class HWW__JetJVTScaleFactorAlg

class HWW__JetSelectionTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'CutPtMinList' : [  ], # list
    'CutAbsEtaMaxList' : [  ], # list
    'CutCleanList' : [  ], # list
    'CutCleanPtMinList' : [  ], # list
    'UpdateJVTName' : 'calibJvt', # str
    'PassForwardJVTName' : '', # str
    'PassJVTName' : '', # str
    'RequireTruthMatch' : False, # bool
    'BTagWeightName' : '', # str
    'CutBTagWeightMin' : -1.7976931e+308, # float
    'CutBTagWeightMax' : 1.7976931e+308, # float
  }
  _propertyDocDct = { 
    'CutBTagWeightMax' : """ The b-tagging maximum cut value. """,
    'CutBTagWeightMin' : """ The b-tagging minimum cut value. """,
    'BTagWeightName' : """ The b-tagging variable name """,
    'CutPtMinList' : """ The jet.pt() minimum cut values. Must be same lenght as the eta list """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'CutAbsEtaMaxList' : """ The |jet.cluster().eta()| maximum cut value. Must be same lenght as the pt list """,
    'PassForwardJVTName' : """ Name of the variable that stores if a forward jet passes the FJVT selection """,
    'CutCleanList' : """ The JetCleaning selection list """,
    'CutCleanPtMinList' : """ The jet.pt minimum cuts for the JetCleaning selection; must be ordered from lowest to highest """,
    'RequireTruthMatch' : """ Require the jet to be truth-matched """,
    'UpdateJVTName' : """ Variable name for the updated JVT """,
    'PassJVTName' : """ Name of the variable that stores if a jet passes the JVT selection """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__JetSelectionTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::JetSelectionTool'
  pass # class HWW__JetSelectionTool

class HWW__METCalibrationSmearingAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'InputMETMap' : '', # str
    'OutputMETFinalName' : 'Final', # str
    'METSystematicVariations' : [  ], # list
    'METSystematicsTool' : PublicToolHandle('met::METSystematicsTool/met::METSystematicsTool'), # GaudiHandle
    'Separator' : '___', # str
  }
  _propertyDocDct = { 
    'Separator' : """ The string seperator between the output container name and the sytematic variation (default='___') """,
    'METSystematicsTool' : """ The ToolHandle for the MET systematics tool """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'InputContainer' : """ Input container name """,
    'Cardinality' : """ How many clones to create """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'METSystematicVariations' : """ The names of all systematic variations to be applied to the MET """,
    'InputMETMap' : """ The name of the input MET map """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'OutputMETFinalName' : """ The name of the output final missingET object """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__METCalibrationSmearingAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::METCalibrationSmearingAlg'
  pass # class HWW__METCalibrationSmearingAlg

class HWW__METMakerAlg( ConfigurableAlgorithm ) :
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
    'InputMETMap' : '', # str
    'InputMETCore' : '', # str
    'OutputMET' : '', # str
    'OutputTrackMET' : '', # str
    'InputJets' : '', # str
    'InputElectrons' : '', # str
    'InputPhotons' : '', # str
    'InputTaus' : '', # str
    'InputMuons' : '', # str
    'UseJVT' : True, # bool
    'DoMuonJetAssociation' : False, # bool
    'METMakerTool' : PublicToolHandle('met::METMaker/met::METMaker'), # GaudiHandle
    'METSignificanceTool' : PublicToolHandle('met::METSignificance/metSignficance'), # GaudiHandle
  }
  _propertyDocDct = { 
    'METMakerTool' : """ Athena configured tool: the handle for the METMaker tool """,
    'InputMuons' : """ The name of the input muon container """,
    'InputTaus' : """ The name of the input tau container """,
    'InputPhotons' : """ The name of the input photon container """,
    'InputElectrons' : """ The name of the input electron container """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'InputMETCore' : """ The name of the input MET core """,
    'DoMuonJetAssociation' : """ Decide if we want to do the muon-to-jet ghost association (default: false) """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'UseJVT' : """ Decide if the JVT cut should be used or not (default: true) """,
    'Cardinality' : """ How many clones to create """,
    'OutputTrackMET' : """ The name of the newly created output TrackMET container """,
    'METSignificanceTool' : """ Athena configured tool: the handle for the METSignificance tool """,
    'InputMETMap' : """ The name of the input MET map """,
    'InputJets' : """ The name of the input jet container """,
    'OutputMET' : """ The name of the newly created output MET container """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__METMakerAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::METMakerAlg'
  pass # class HWW__METMakerAlg

class HWW__METReducerAlg( ConfigurableAlgorithm ) :
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
    'METContainer' : '', # str
  }
  _propertyDocDct = { 
    'METContainer' : """ The name of the input and output MET container """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__METReducerAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::METReducerAlg'
  pass # class HWW__METReducerAlg

class HWW__MuonCalibrationSmearingAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'Separator' : '___', # str
    'OutputContainer' : '', # str
    'MuonCalibrationTool' : PrivateToolHandle('CP::IMuonCalibrationAndSmearingTool'), # GaudiHandle
    'MomentumSystematicVariations' : [  ], # list
  }
  _propertyDocDct = { 
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'InputContainer' : """ Input container name """,
    'Cardinality' : """ How many clones to create """,
    'MuonCalibrationTool' : """ The ToolHandle for the muon calibration and smearing tool """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Separator' : """ The string seperator between the output container name and the sytematic variation (default='___') """,
    'MomentumSystematicVariations' : """ The names of all systematic variations to be applied """,
    'OutputContainer' : """ The name of the output container with the deep copy of input objects """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__MuonCalibrationSmearingAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::MuonCalibrationSmearingAlg'
  pass # class HWW__MuonCalibrationSmearingAlg

class HWW__MuonDecorationAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'SelectionTool' : PublicToolHandle(''), # GaudiHandle
    'HighPtSelectionTool' : PublicToolHandle(''), # GaudiHandle
    'SelectionWithVertexToolList' : PublicToolHandleArray([]), # GaudiHandleArray
    'SelectionWithVertexToolDecoList' : [  ], # list
    'IsolationToolList' : PublicToolHandleArray([]), # GaudiHandleArray
    'IsolationToolDecoList' : [  ], # list
    'DoDeltaPt' : False, # bool
    'DoImpactParameter' : False, # bool
    'PrimaryVertexContainer' : 'PrimaryVertices', # str
    'DoTruthInformation' : False, # bool
    'DecorateAllCopies' : False, # bool
  }
  _propertyDocDct = { 
    'DoTruthInformation' : """ If true, will attach the results of the MCTruthClassifer to the muon directly """,
    'PrimaryVertexContainer' : """ The input primary vertex container name """,
    'DoImpactParameter' : """ If true, will calculate and store the z0sinTheta, d0, and d0Err """,
    'DoDeltaPt' : """ If true, will calculate and store the relative pt difference between MS and ID """,
    'IsolationToolList' : """ List of CP tool to calculate the lepton isolation """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsolationToolDecoList' : """ List of muon isolation working points """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'SelectionWithVertexToolDecoList' : """ List of decoration names for each selection-with-vertex tools """,
    'InputContainer' : """ Input container name """,
    'SelectionTool' : """ The CP::MuonSelectionTool instance """,
    'Cardinality' : """ How many clones to create """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'SelectionWithVertexToolList' : """ List of selection-with-vertex tool instances """,
    'DecorateAllCopies' : """ If true, will decorate all copies of the input container """,
    'HighPtSelectionTool' : """ The CP::MuonSelectionTool instance configured with the high-pt selection """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__MuonDecorationAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::MuonDecorationAlg'
  pass # class HWW__MuonDecorationAlg

class HWW__MuonScaleFactorAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'ContainersFinderTool' : PublicToolHandle('HWW::ContainersFinderTool/ContainersFinderTool'), # GaudiHandle
    'DecorateAllCopies' : True, # bool
    'Separator' : '___', # str
    'MuonEfficiencyScaleFactorTools' : PrivateToolHandleArray([]), # GaudiHandleArray
    'EfficiencyScaleFactorVarNames' : [  ], # list
    'EfficiencySystematicVariations' : [  ], # list
  }
  _propertyDocDct = { 
    'MuonEfficiencyScaleFactorTools' : """ The ToolHandle for the muon efficiency scale factor tool """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'InputContainer' : """ Input container name """,
    'EfficiencySystematicVariations' : """ The names of all systematic variations to be applied """,
    'Cardinality' : """ How many clones to create """,
    'EfficiencyScaleFactorVarNames' : """ The name of the efficiency scale-factor variable that will be added to the muon """,
    'ContainersFinderTool' : """ The tool that tries to find all input containers, including their systematic variations """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'DecorateAllCopies' : """ If true, will decorate all copies of the input container """,
    'Separator' : """ The string seperator between the output container name and the sytematic variation (default='___') """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__MuonScaleFactorAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::MuonScaleFactorAlg'
  pass # class HWW__MuonScaleFactorAlg

class HWW__MuonSelectionTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'CutPtMin' : -99999.000, # float
    'CutAbsEtaMax' : 1.7976931e+308, # float
    'CutIDList' : [  ], # list
    'CutIDPtMinList' : [  ], # list
    'CutInnerDetectorHits' : False, # bool
    'CutZ0SinThetaMax' : 3.40282e+38, # float
    'CutD0SignificanceMax' : 3.40282e+38, # float
    'CaloIsoList' : [  ], # list
    'CaloIsoRelativeMaxCutList' : [  ], # list
    'CaloIsoMaxCutList' : [  ], # list
    'CutCaloIsoPtMinList' : [  ], # list
    'TrackIsoList' : [  ], # list
    'TrackIsoRelativeMaxCutList' : [  ], # list
    'TrackIsoMaxCutList' : [  ], # list
    'CutTrackIsoPtMinList' : [  ], # list
  }
  _propertyDocDct = { 
    'CutTrackIsoPtMinList' : """ The minimum pt cuts for the track isolation list """,
    'TrackIsoRelativeMaxCutList' : """ The relativ track isolation maximum cut list """,
    'CaloIsoList' : """ The calorimetric isolation types list """,
    'TrackIsoMaxCutList' : """ The absolute track isolation maximum cut list """,
    'CutPtMin' : """ The muon.pt() minimum cut value """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'TrackIsoList' : """ The track isolation types list """,
    'CutAbsEtaMax' : """ The |muon.cluster().eta()| maximum cut value """,
    'CaloIsoMaxCutList' : """ The absolute calorimetric isolation maximum cut list """,
    'CutInnerDetectorHits' : """ The muon inner detector hit cuts """,
    'CaloIsoRelativeMaxCutList' : """ The relativ calorimetric isolation maximum cut list """,
    'CutIDPtMinList' : """ The muon.pt minimum cuts for the identification selection; must be ordered from lowest to highest """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'CutIDList' : """ The muon identification selection list """,
    'CutZ0SinThetaMax' : """ The muon z0 maximum cut value """,
    'CutCaloIsoPtMinList' : """ The minimum pt cuts for the calorimetric isolation list """,
    'CutD0SignificanceMax' : """ The muon d0 maximum cut value """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__MuonSelectionTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::MuonSelectionTool'
  pass # class HWW__MuonSelectionTool

class HWW__MuonTriggerEfficiencyScaleFactorAlg( ConfigurableAlgorithm ) :
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
    'InputContainer' : '', # str
    'ContainersFinderTool' : PublicToolHandle('HWW::ContainersFinderTool/ContainersFinderTool'), # GaudiHandle
    'DecorateAllCopies' : True, # bool
    'Separator' : '___', # str
    'MuonEfficiencyScaleFactorTools2015' : PublicToolHandleArray([]), # GaudiHandleArray
    'MuonEfficiencyScaleFactorTools2016' : PublicToolHandleArray([]), # GaudiHandleArray
    'EfficiencyScaleFactorVarNames' : [  ], # list
    'EfficiencySystematicVariations' : [  ], # list
    'EfficiencyVarNames' : [  ], # list
    'TriggerNames2015' : [  ], # list
    'TriggerNames2016' : [  ], # list
    'GetDataEfficiency' : False, # bool
  }
  _propertyDocDct = { 
    'EfficiencyVarNames' : """ The name of the efficiency variables that will be added to the muon """,
    'MuonEfficiencyScaleFactorTools2016' : """ The ToolHandle for the muon efficiency scale factor tool for 2016 """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'GetDataEfficiency' : """ Set to true, if we want the data efficiency (default: false) """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'TriggerNames2016' : """ The names of the 2016 triggers to be used """,
    'MuonEfficiencyScaleFactorTools2015' : """ The ToolHandle for the muon efficiency scale factor tool for 2015 """,
    'InputContainer' : """ Input container name """,
    'EfficiencySystematicVariations' : """ The names of all systematic variations to be applied """,
    'Cardinality' : """ How many clones to create """,
    'TriggerNames2015' : """ The names of the 2015 triggers to be used """,
    'EfficiencyScaleFactorVarNames' : """ The name of the efficiency scale-factor variable that will be added to the muon """,
    'ContainersFinderTool' : """ The tool that tries to find all input containers, including their systematic variations """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'DecorateAllCopies' : """ If true, will decorate all copies of the input container """,
    'Separator' : """ The string seperator between the output container name and the sytematic variation (default='___') """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__MuonTriggerEfficiencyScaleFactorAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::MuonTriggerEfficiencyScaleFactorAlg'
  pass # class HWW__MuonTriggerEfficiencyScaleFactorAlg

class HWW__OverlapRemovalAlg( ConfigurableAlgorithm ) :
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
    'OverlapRemovalToolList' : PublicToolHandleArray([]), # GaudiHandleArray
    'OverlapRemovalLabels' : [  ], # list
    'WriteElectronOverlaps' : [  ], # list
    'WriteMuonOverlaps' : [  ], # list
    'WriteJetOverlaps' : [  ], # list
    'WriteFatJetOverlaps' : [  ], # list
    'InputElectrons' : '', # str
    'InputMuons' : '', # str
    'InputJets' : '', # str
    'InputFatJets' : '', # str
    'OutputElectrons' : '', # str
    'OutputMuons' : '', # str
    'OutputJets' : '', # str
    'OutputFatJets' : '', # str
    'TaggerName' : 'MV2c10', # str
    'OperatingPoint' : 0.17580000, # float
    'PassBTaggingName' : '', # str
  }
  _propertyDocDct = { 
    'PassBTaggingName' : """ The name of the boolean variable to say pass/fail b-tagging """,
    'OverlapRemovalToolList' : """ The list of OverlapRemovalTools """,
    'OverlapRemovalLabels' : """ The list of label names that the overlap removal tools used to flag overlaps """,
    'InputJets' : """ The name of the input selected jets container """,
    'OutputFatJets' : """ The name of the output overlap-removed jets container """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'WriteFatJetOverlaps' : """ The list of booleans that declare which overlap precedure should be used to write out fat jets. If multiple are given, a logical OR will be used. """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'WriteJetOverlaps' : """ The list of booleans that declare which overlap precedure should be used to write out jets. If multiple are given, a logical OR will be used. """,
    'WriteElectronOverlaps' : """ The list of booleans that declare which overlap precedure should be used to write out electrons. If multiple are given, a logical OR will be used. """,
    'InputElectrons' : """ The name of the input selected electrons container """,
    'OutputJets' : """ The name of the output overlap-removed jets container """,
    'InputMuons' : """ The name of the input selected muons container """,
    'WriteMuonOverlaps' : """ The list of booleans that declare which overlap precedure should be used to write out muons. If multiple are given, a logical OR will be used. """,
    'InputFatJets' : """ The name of the input selected jets container """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'TaggerName' : """ The name of the tagger that we want to use (default='MV2c10') """,
    'OutputElectrons' : """ The name of the output overlap-removed electrons container """,
    'OutputMuons' : """ The name of the output overlap-removed muons container """,
    'OperatingPoint' : """ The cut value on the b-tagging discriminant """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__OverlapRemovalAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::OverlapRemovalAlg'
  pass # class HWW__OverlapRemovalAlg

class HWW__PileupReweightingAlg( ConfigurableAlgorithm ) :
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
    'Tool' : PublicToolHandle('CP::PileupReweightingTool/auto'), # GaudiHandle
    'Input' : '', # str
    'Output' : '', # str
    'ConfigOutputStream' : '', # str
  }
  _propertyDocDct = { 
    'ConfigOutputStream' : """ Specify the stream to output config file to """,
    'Output' : """ Specify an output EventInfo object. If differs from input, will create a clone of EventInfo and decorate that """,
    'Input' : """ Specify a specific EventInfo object """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'Tool' : """ The configured PileupReweightingTool """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__PileupReweightingAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::PileupReweightingAlg'
  pass # class HWW__PileupReweightingAlg

class HWW__PrimaryVertexFilterAlg( ConfigurableAlgorithm ) :
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
    'PrimaryVertexContainer' : 'PrimaryVertices', # str
  }
  _propertyDocDct = { 
    'FilterDescription' : """ describe to the cutflowsvc what this filter does. """,
    'CutFlowSvc' : """ handle to the ICutFlowSvc instance this filtering algorithm will use for building the flow of cuts. """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'PrimaryVertexContainer' : """ The name of the input primary vertex container """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__PrimaryVertexFilterAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::PrimaryVertexFilterAlg'
  pass # class HWW__PrimaryVertexFilterAlg

class HWW__TriggerAlg( ConfigurableAlgorithm ) :
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
    'TrigTool' : PublicToolHandle('HWW::ITriggerTool'), # GaudiHandle
    'Muons' : '', # str
    'Electrons' : '', # str
    'PerformMuonMatch' : False, # bool
    'PerformElectronMatch' : False, # bool
    'PerformDiMuMatch' : False, # bool
    'PerformDiElMatch' : False, # bool
    'PerformElMuMatch' : False, # bool
    'VarPrefix' : 'trigMatch_', # str
  }
  _propertyDocDct = { 
    'PerformElMuMatch' : """ The switch for the electron-muon trigger matching """,
    'PerformDiMuMatch' : """ The switch for the di-muon trigger matching """,
    'PerformElectronMatch' : """ The switch for the electron trigger matching """,
    'PerformDiElMatch' : """ The switch for the di-electron trigger matching """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'Electrons' : """ The name of the input electron collection """,
    'Cardinality' : """ How many clones to create """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'PerformMuonMatch' : """ The switch for the muon trigger matching """,
    'TrigTool' : """ The HWWTriggerTool """,
    'VarPrefix' : """ Prefix used for the decoration variables """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'Muons' : """ The name of the input muon collection """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__TriggerAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::TriggerAlg'
  pass # class HWW__TriggerAlg

class HWW__TriggerTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'VarPrefix' : '', # str
    'MuonMatchList' : [  ], # list
    'ElectronMatchList' : [  ], # list
    'DiMuonMatchList' : [  ], # list
    'DiElectronMatchList' : [  ], # list
    'ElMuMatchList' : [  ], # list
  }
  _propertyDocDct = { 
    'DiElectronMatchList' : """ The list of trigger chains to do di-electron matching on """,
    'DiMuonMatchList' : """ The list of trigger chains to do di-muon matching on """,
    'ElectronMatchList' : """ The list of trigger chains to do electron matching on """,
    'ElMuMatchList' : """ The list of trigger chains to do electron-muon matching on """,
    'MuonMatchList' : """ The list of trigger chains to do muon matching on """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'VarPrefix' : """ The prefix to be used for the trigger matching flags """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__TriggerTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::TriggerTool'
  pass # class HWW__TriggerTool

class HWW__TruthAlg( ConfigurableAlgorithm ) :
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
    'THistSvc' : ServiceHandle('THistSvc/THistSvc'), # GaudiHandle
    'RootStreamName' : '/ANALYSIS', # str
    'RootDirName' : '', # str
    'HistNamePrefix' : '', # str
    'HistNamePostfix' : '', # str
    'HistTitlePrefix' : '', # str
    'HistTitlePostfix' : '', # str
    'TruthInputContainer' : '', # str
    'TruthOutputContainer' : '', # str
    'TruthJetInputContainer' : '', # str
    'TruthWZJetInputContainer' : '', # str
    'TruthMetInputContainer' : '', # str
    'TruthElectronInputContainer' : '', # str
    'TruthMuonInputContainer' : '', # str
    'EventInfoContainer' : '', # str
    'IsSherpa' : False, # bool
    'IsNNLOPS' : False, # bool
    'HiggsWeightTool' : PrivateToolHandle('TruthWeightTools::HiggsWeightTool/HiggsWeightTool'), # GaudiHandle
    'WriteSplitOutputContainer' : True, # bool
  }
  _propertyDocDct = { 
    'WriteSplitOutputContainer' : """ Decide if we want to write a fully-split AuxContainer such that we can remove any variables """,
    'IsNNLOPS' : """ Powheg NNLOPS ggF """,
    'HistNamePrefix' : """ The prefix for the histogram THx name """,
    'RootDirName' : """ Name of the ROOT directory inside the ROOT file where the histograms will go """,
    'HistNamePostfix' : """ The postfix for the histogram THx name """,
    'TruthWZJetInputContainer' : """ Name of the input truth WZ jet container """,
    'HistTitlePrefix' : """ The prefix for the histogram THx title """,
    'TruthMetInputContainer' : """ Name of the input truth MET container """,
    'RootStreamName' : """ Name of the output ROOT stream (file) that the THistSvc uses """,
    'Cardinality' : """ How many clones to create """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'THistSvc' : """ Handle to a THistSvc instance: it will be used to write ROOT objects to ROOT files """,
    'HiggsWeightTool' : """ Tool for handling the NNLOPS ggF weights """,
    'IsSherpa' : """ Sherpa or Powheg """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'TruthInputContainer' : """ Name of the input truth container """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'HistTitlePostfix' : """ The postfix for the histogram THx title """,
    'TruthOutputContainer' : """ Name of the output truth container """,
    'TruthJetInputContainer' : """ Name of the input truth jet container """,
    'EventInfoContainer' : """ Name of the EventInfo container """,
    'TruthElectronInputContainer' : """ Name of the input truth electron container """,
    'TruthMuonInputContainer' : """ Name of the input truth muon container """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__TruthAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::TruthAlg'
  pass # class HWW__TruthAlg

class HWW__TruthElectronSelectionTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'CutPtMin' : -99999.000, # float
    'CutAbsEtaMax' : 1.7976931e+308, # float
    'CutAbsEtaCrackMin' : -1000.0000, # float
    'CutAbsEtaCrackMax' : -1000.0000, # float
  }
  _propertyDocDct = { 
    'CutAbsEtaCrackMax' : """ The |electron.cluster().eta()| maximum cut value for the calo crack """,
    'CutAbsEtaMax' : """ The |electron.cluster().eta()| maximum cut value """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'CutAbsEtaCrackMin' : """ The |electron.cluster().eta()| minimum cut value for the calo crack """,
    'CutPtMin' : """ The electron.pt() minimum cut value """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__TruthElectronSelectionTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::TruthElectronSelectionTool'
  pass # class HWW__TruthElectronSelectionTool

class HWW__TruthJetMETAlg( ConfigurableAlgorithm ) :
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
    'InputJets' : '', # str
    'InputMet' : '', # str
    'OutputJets' : '', # str
    'OutputMet' : '', # str
  }
  _propertyDocDct = { 
    'InputJets' : """ The name of the input jets container """,
    'InputMet' : """ The name of the input met container """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'OutputJets' : """ The name of the output jets container """,
    'Cardinality' : """ How many clones to create """,
    'OutputMet' : """ The name of the output met container """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__TruthJetMETAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::TruthJetMETAlg'
  pass # class HWW__TruthJetMETAlg

class HWW__TruthJetSelectionTool( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ExtraInputs' : [], # list
    'ExtraOutputs' : [], # list
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'CutPtMinList' : [  ], # list
    'CutAbsEtaMaxList' : [  ], # list
  }
  _propertyDocDct = { 
    'CutAbsEtaMaxList' : """ The |jet.cluster().eta()| maximum cut value. Must be same lenght as the pt list """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'CutPtMinList' : """ The jet.pt() minimum cut values. Must be same lenght as the eta list """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__TruthJetSelectionTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::TruthJetSelectionTool'
  pass # class HWW__TruthJetSelectionTool

class HWW__TruthLeptonAlg( ConfigurableAlgorithm ) :
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
    'InputElectrons' : '', # str
    'InputMuons' : '', # str
    'OutputElectrons' : '', # str
    'OutputMuons' : '', # str
  }
  _propertyDocDct = { 
    'OutputMuons' : """ The name of the output muons container """,
    'OutputElectrons' : """ The name of the output electrons container """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'InputElectrons' : """ The name of the input electrons container """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'InputMuons' : """ The name of the input muons container """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__TruthLeptonAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::TruthLeptonAlg'
  pass # class HWW__TruthLeptonAlg

class HWW__TruthOverlapRemovalAlg( ConfigurableAlgorithm ) :
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
    'SelectedElectrons' : '', # str
    'SelectedMuons' : '', # str
    'SelectedJets' : '', # str
    'ORElectrons' : '', # str
    'ORMuons' : '', # str
    'ORJets' : '', # str
    'InputLabel' : 'selectedDecoration which specifies input objects', # str
    'OutputLabel' : 'overlaps', # str
    'OutputPassValue' : False, # bool
    'RequireExpectedPointers' : True, # bool
  }
  _propertyDocDct = { 
    'RequireExpectedPointers' : """ Require non-null container pointers when expected by config """,
    'OutputPassValue' : """ Set the result assigned to objects that pass """,
    'OutputLabel' : """ Decoration given to objects that fail OR """,
    'ORMuons' : """ The name of the output OR muons container """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'ORJets' : """ The name of the output OR jets container """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'Cardinality' : """ How many clones to create """,
    'SelectedElectrons' : """ The name of the input selected electrons container """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'SelectedMuons' : """ The name of the input selected muons container """,
    'SelectedJets' : """ The name of the input selected jets container """,
    'ORElectrons' : """ The name of the output OR electrons container """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__TruthOverlapRemovalAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::TruthOverlapRemovalAlg'
  pass # class HWW__TruthOverlapRemovalAlg

class HWW__UnprescaleDataAlg( ConfigurableAlgorithm ) :
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
    'EventInfoName' : 'EventInfo', # str
    'PileupReweightingTool' : PrivateToolHandle('CP::PileupReweightingTool/UnprescaleDataPRWTool'), # GaudiHandle
    'TriggerExpression' : '', # str
    'LumiCalcFiles' : [  ], # list
  }
  _propertyDocDct = { 
    'PileupReweightingTool' : """ The pileup reweighting tool """,
    'EventInfoName' : """ The input EventInfo name """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'Cardinality' : """ How many clones to create """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'IsClonable' : """ Thread-safe enough for cloning? """,
    'LumiCalcFiles' : """ The list of lumicalc files to pass to the tool """,
    'TriggerExpression' : """ The trigger expression to use for the unweighting of the data """,
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(HWW__UnprescaleDataAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'PhysicsxAODCode'
  def getType( self ):
      return 'HWW::UnprescaleDataAlg'
  pass # class HWW__UnprescaleDataAlg
