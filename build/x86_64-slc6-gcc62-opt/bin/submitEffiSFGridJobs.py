#!/usr/bin/env python

# ==============================================================================
# File: submitEffiSFGridJobs.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: This file is a python executable that is meant for submitting
# the second step of our grid job PxAOD production chain, i.e., attaching the
# efficiencies and scale-factors to the previously produced PxAODs that don't
# have them (but have all object calibrations and possible systemtic varations
# thereof).
# ==============================================================================


import user  # look for .pythonrc.py for user init
import os,sys



inDSList = [#"group.phys-higgs.data15_13TeV.HWW_NoEffiSF.merge.PAOD.V12_rel20p7_Part01",
            #"group.phys-higgs.data16_13TeV.HWW_NoEffiSF.merge.PAOD.V12_rel20p7_Part01",

            #"group.phys-higgs.mc15_13TeV.HWW_Common_NoEffiSF.merge.PAOD.V12_rel20p7_Part01",
            #"group.phys-higgs.mc15_13TeV.HWW_Common_NoEffiSF.merge.PAOD.sysV12_rel20p7_Part01",
            #"group.phys-higgs.mc15_13TeV.HWW_HWWHighMass_NoEffiSF.merge.PAOD.V12_rel20p7_Part01",
            #"group.phys-higgs.mc15_13TeV.HWW_HWWHighMass_NoEffiSF.merge.PAOD.sysV12_rel20p7_Part01",
            # "group.phys-higgs.mc15_13TeV.HWW_CommonBkg_NoEffiSF.merge.PAOD.V12_rel20p7_FakeWJets_Part01",
            # "group.phys-higgs.mc15_13TeV.HWW_Hmumu_NoEffiSF.merge.PAOD.sysV12_rel20p7_Part01",
            # "group.phys-higgs.mc15_13TeV.HWW_Hmumu_NoEffiSF.merge.PAOD.V12_rel20p7_Part01",

            #"group.phys-higgs.mc15_13TeV.HWW_CommonBkg_NoEffiSF.merge.PAOD.V12_rel20p7_FakeWJets_Part01",

            "group.phys-higgs.mc15_13TeV.HWW_CommonBkg_NoEffiSF.merge.PAOD.V12_rel20p7_FakeZJets_Part01",

            # "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_Part01",
            # "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01",
            # "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_Part01",
            # "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01",
            # "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWHighMass_NoEffiSF.merge.PAOD.V13_rel20p7_Part01",
            # "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWHighMass_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01"
            ]

inStreamNameList = [#"PAOD_ZH", "PAOD_WH",
                    #"PAOD_2LDF",
                    #"PAOD_2LJJDF",
                    #"PAOD_2LJJ",
                    "PAOD_2L",
                    "PAOD_2LFake",
                    "PAOD_2LTopFake",
                    "PAOD_2LZFake",
                    ]

for inDS in inDSList:
    for inStreamName in inStreamNameList:
        job = 'pathena  -c "doOnlyEffiScaleFactors=True;OUTSTREAMNAME=\''
        job += inStreamName+'\';doEffiSystematics='
        if inDS.__contains__(".sys"): job += 'True;"'
        else: job += 'False;"'
        job += ' PhysicsxAODConfig/HWWAnalysis_topOptions.py  --dbRelease LATEST '
        job += ' --official --voms=atlas:/atlas/phys-higgs/Role=production  --destSE IN2P3-CC_PHYS-HIGGS '
        fullInDSName = inDS+"_"+inStreamName
        job += ' --inDS ' + fullInDSName
        outDSName = fullInDSName.replace("_NoEffiSF","_WithEffiSF_AtoI")
        job += ' --outDS ' + outDSName
        job += ' --nGBPerJob=5  --skipScout '
        # job += ' --site DESY-HH '
        if inDS.__contains__(".mc1"): job += ' --addNthFieldOfInFileToLFN=3,4 '

        # Now, submit the actual job
        print "Going to run this job:"
        print job
        os.system(job)
        pass
    pass
