#!/usr/bin/env python

# ==============================================================================
# File: submitSuperMerge.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: This file is a python executable that is meant for submitting
# an additional mergin job on existing grid datasets, i.e., produce superMerge
# datasets.
# ==============================================================================


import user  # look for .pythonrc.py for user init
import os,sys



inDSList = ["group.phys-higgs.data15_13TeV.HWW.merge.PAOD_2L.V18.1",
            "group.phys-higgs.data16_13TeV.HWW.merge.PAOD_2L.V18.1",
            "group.phys-higgs.mc16_13TeV.HWW_mc16a_HWWSignal.merge.PAOD_2L.V18.1",
            "group.phys-higgs.mc16_13TeV.HWW_mc16a_CommonOtherBkg.merge.PAOD_2L.V18.1",
            "group.phys-higgs.mc16_13TeV.HWW_mc16a_TopBkg.merge.PAOD_2L.V18.1",
            "group.phys-higgs.mc16_13TeV.HWW_mc16a_SherpaDYBkg.merge.PAOD_2L.V18.1.1",

            "group.phys-higgs.data15_13TeV.HWW.merge.PAOD_VH.V18.1",
            # "group.phys-higgs.data16_13TeV.HWW.merge.PAOD_VH.V18.1",
            "group.phys-higgs.mc16_13TeV.HWW_mc16a_HWWSignal.merge.PAOD_VH.V18.1",
            "group.phys-higgs.mc16_13TeV.HWW_mc16a_CommonOtherBkg.merge.PAOD_VH.V18.1",
            "group.phys-higgs.mc16_13TeV.HWW_mc16a_TopBkg.merge.PAOD_VH.V18.1",
            "group.phys-higgs.mc16_13TeV.HWW_mc16a_SherpaDYBkg.merge.PAOD_VH.V18.1",
            ]


inStreamNames = {'PAOD_2L': ['PAOD_2LDF'],
                 'PAOD_VH': ['PAOD_WH', 'PAOD_ZH'],
                 }

for inDS in inDSList:
    for key in inStreamNames:
        if key not in inDS:
            continue
        for inStreamName in inStreamNames[key]:
            job = 'pathena  -c "OUTSTREAMNAME=\''
            job += inStreamName+'\';"'
            job += ' PhysicsxAODConfig/PAODMerge.py  --dbRelease LATEST '
            job += ' --official --voms=atlas:/atlas/phys-higgs/Role=production  --destSE IN2P3-CC_PHYS-HIGGS '
            fullInDSName = inDS+"_"+inStreamName
            job += ' --inDS ' + fullInDSName
            outDSName = fullInDSName.replace(".merge.",".superMerge.")
            job += ' --outDS ' + outDSName
            job += ' --nGBPerJob=5 '
            # job += ' --site DESY-HH '
            if inDS.__contains__(".mc1"): job += ' --addNthFieldOfInFileToLFN=3,4 '

            # Now, submit the actual job
            print "Going to run this job:"
            print job
            os.system(job)
            pass
        pass
    pass
