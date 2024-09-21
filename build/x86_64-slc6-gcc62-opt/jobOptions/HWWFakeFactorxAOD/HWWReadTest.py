# import os
#myxAOD = os.getenv("TestArea")+"/HiggsWWlnulnu/run/HWWMinixAOD.pool.root"
myxAOD = os.getenv("DataMC")+"/mc/xAOD/mc14_8TeV.117050.PowhegPythia_P2011C_ttbar.merge.AOD.e1727_s1933_s1911_r5591_r5625_tid01507244_00/AOD.01507244._011715.pool.root.1"
import AthenaPoolCnvSvc.ReadAthenaPool
svcMgr.EventSelector.InputCollections = [ myxAOD ]
theApp.EvtMax = 100

ServiceMgr.StatusCodeSvc.AbortOnError = False

algseq = CfgMgr.AthSequencer("AthAlgSeq")
#algseq += CfgMgr.HWWMuonTestAlg("MuTestViewNoSC", OutputLevel=VERBOSE, InputContainer="HWWCalibMuonsViewNoSC")
#algseq += CfgMgr.HWWMuonTestAlg("MuTestView", OutputLevel=VERBOSE, InputContainer="HWWCalibMuonsView")

algseq += CfgMgr.ParticleSelectionAlg( "TestPartSelAlg",
                                       InputContainer  = "Muons",
                                       OutputContainer = "SelectedMuons",
                                       Selection       = "Muons.pt>15.0*GeV"
                                       )

algseq += CfgMgr.xAODMaker__AuxStoreWrapper( "HWWAuxStoreWrapperAlg",
                                             OutputLevel=INFO,
                                             SGKeys = ["MuonsAux.","SelectedMuonsAux."
                                                       ]
                                             )

# Create a new mini-xAOD output stream object
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
TestOutStream = MSMgr.NewPoolRootStream( "TestOutStream", "TestOutFile.pool.root" )
TestOutStream.AddItem( "xAOD::MuonContainer_v1#Muons" )
# TestOutStream.AddItem( "xAOD::MuonAuxContainer_v1#MuonsAux." )
TestOutStream.AddItem( "xAOD::AuxContainerBase#MuonsAux." )
TestOutStream.AddItem( "xAOD::MuonContainer_v1#SelectedMuons" )
# TestOutStream.AddItem( "xAOD::MuonAuxContainer_v1#SelectedMuonsAux." )
TestOutStream.AddItem( "xAOD::AuxContainerBase#SelectedMuonsAux." )
TestOutStream.AddItem( "xAOD::AuxContainerBase#*" )
