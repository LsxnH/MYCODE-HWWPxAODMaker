export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
source $ATLAS_LOCAL_ROOT_BASE/user/atlasLocalSetup.sh
pushd /home/hengli/testarea/HWWPxAODMaker/build/
asetup --restore
source */setup.sh
popd
athena -c "INTEXTFILE='input.txt';EVTMAX=-1;doEffiSystematics=False;doP4Systematics=False;do3Lep=True;writePAOD_WH=True;" /home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/PhysicsxAODConfig/share/HWWAnalysis_topOptions.py

