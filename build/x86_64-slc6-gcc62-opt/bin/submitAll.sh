# We are testing out the use of the (--doFakeWJets + --doVeryLooseLH) loosened lepton ID for use as a baseline, so these arguments will appear for now in all submissions

###
### data15/16 + mc16a
###

# Nominal 2-lepton output
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data15.txt                --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=10 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data16.txt               --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__TopBkg.txt         --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run

# Nominal PFlow 2-lepton output
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data15.txt                --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=10 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data16.txt               --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__TopBkg.txt         --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run

# Systematics 2-lepton output
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__TopBkg.txt         --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run

# Nominal VH output
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data15.txt                --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=10 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data16.txt               --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__TopBkg.txt         --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run

# Nominal PFlow VH output
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data15.txt                --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=10 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data16.txt               --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__TopBkg.txt         --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run

# Systematics VH output
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__TopBkg.txt         --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.0 --run

# Systematics ggF/VBF noskim TruthReco
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --processTruth --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16a__HWWSignalNoSkim.txt      --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.0 --run



###
### data17 + mc16d
###

# Nominal 2-lepton output
# submitGridJobs.py --nFilesPerJob=10 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data17.txt               --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__TopBkg.txt         --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run

# Nominal PFlow 2-lepton output
# submitGridJobs.py --nFilesPerJob=10 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data17.txt               --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__TopBkg.txt         --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run

# Systematics 2-lepton output
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__TopBkg.txt         --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --do2Lep --writePAOD_2L --writePAOD_2LDF --version=V19.1 --run

# Nominal VH output
# submitGridJobs.py --nFilesPerJob=10 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data17.txt               --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__TopBkg.txt         --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run

# Nominal PFlow VH output
# submitGridJobs.py --nFilesPerJob=10 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_data17.txt               --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__TopBkg.txt         --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=5 --official --prod --merge --doPFlowJets --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run

# Systematics VH output
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWHighMass.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__HWWSignal.txt      --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__CommonOtherBkg.txt --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__TopBkg.txt         --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__SherpaDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__PowhegDYBkg.txt    --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
# submitGridJobs.py --nFilesPerJob=1 --official --prod --merge --doSystematics --forceStaged --useNewCode --oneOutDS --inDSTextFile submitList_HIGG3D1_mc16d__MadGraphDYBkg.txt  --doVeryLooseLH --doFakeWJets --doVH   --writePAOD_WH --writePAOD_ZH   --version=V19.1 --run
