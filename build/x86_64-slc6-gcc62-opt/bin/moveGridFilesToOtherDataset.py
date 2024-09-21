#!/usr/bin/env python

# ==============================================================================
# File: moveGridFilesToOtherDataset.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: This script moves files from one grid dataset to another.
# ==============================================================================

import user  # look for .pythonrc.py for user init
import os,sys
import subprocess



inStreamNameList = [#"PAOD_ZH", "PAOD_WH",
                    #"PAOD_2LDF",
                    #"PAOD_2LJJDF",
                    "PAOD_2LJJ",
                    #"PAOD_2L"
                    ]


#datasets = ["group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_Part01",
#            "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01",
#            "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_Part01",
#            "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01"
#    ]
datasets = ["group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_FakeWJets_Part01",
            "group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_FakeWJets_Part01"]

sourceTargetList = [ {"source":"HWWSignal", "target":"CommonBkg", "dsids":[343362,343478,343479,343480,343481,343482,343637,343852,343853,343854,343982,343983,343984,343985,343986]},
                     {"source":"CommonBkg", "target":"HWWSignal", "dsids":[341462,342282,342283,342284,342285,342299]} ]

#sourceTargetList = [ {"source":"HWWSignal", "target":"CommonBkg", "dsids":[343478]},
#                     {"source":"CommonBkg", "target":"HWWSignal", "dsids":[342299]} ]




rucioBaseCmdList   = "rucio list-files --csv "
rucioBaseCmdAttach = "rucio attach "
rucioBaseCmdDetach = "rucio detach "


def getDatasetsFromContainer(contName):
    rucioCmd = "rucio ls --short --filter type=DATASET " + contName + "\*"
    output = subprocess.check_output(rucioCmd, shell=True)
    outputList = output.split("\n")
    return outputList


def datasetExists(dsName):
    rucioCmd = "rucio ls " + dsName + " &> /dev/null" # Also avoid printing the result of the rucio command
    retVal =  subprocess.call(rucioCmd, shell=True)
    if retVal == 0: return True
    return False


# Keep a list of new datasets that we created and print it at the end
targetDSList = []


for inDS in datasets:
    for streamName in inStreamNameList:
        for sourceTarget in sourceTargetList:
            sourceStr = sourceTarget["source"]
            if not inDS.__contains__(sourceStr): continue
            targetStr = sourceTarget["target"]
            dsidList  = sourceTarget["dsids"]
            sourceDSCont = inDS+"_"+streamName
            targetDSCont = sourceDSCont.replace(sourceStr,targetStr)

            # Create a new target dataset
            targetDS = targetDSCont + ".move01"
            targetExists = datasetExists(targetDS)
            #print "Target exists: %s" % targetExists
            if not targetExists:
                targetDSList.append(targetDS)
                # print "TargetDS: ", targetDS
                rucioCreateDS = "rucio add-dataset " + targetDS
                print rucioCreateDS
                subprocess.check_output(rucioCreateDS, shell=True)

                # Attach this new dataset to the target container
                rucioAttachDStoCont = "rucio attach " + targetDSCont + " " + targetDS
                print rucioAttachDStoCont
                subprocess.check_output(rucioAttachDStoCont, shell=True)
                pass


            # Now, iterate over the source datasets that we get from the source dataset container
            sourceDSList = getDatasetsFromContainer(sourceDSCont)
            for sourceDS in sourceDSList:
                if len(sourceDS) < 20: continue
                #print "SourceDS: ", sourceDS
                
                # Now, get the list of files in the source dataset
                rucioListFileCmd = rucioBaseCmdList + sourceDS

                #print "Going ask rucio for the list of files within a dataset:"
                #print rucioListFileCmd
                output = subprocess.check_output(rucioListFileCmd, shell=True)
                
                # build the full attach and detachcommand
                attachCmd = rucioBaseCmdAttach + targetDS + " "
                detachCmd = rucioBaseCmdDetach + sourceDS + " "

                # Find all files to move
                outputList = output.split("\n")
                nFilesAdded = 0
                for outStr in outputList:
                    if any( "."+str(dsid)+"." in outStr for dsid in dsidList):
                        fileToMove = outStr.split(",")[0]
                        attachCmd += fileToMove + " "
                        detachCmd += fileToMove + " "
                        nFilesAdded += 1
                        pass
                    pass
                if nFilesAdded == 0: continue
                print
                print
                print "Running rucio attach for DS: "+targetDS
                #print attachCmd
                subprocess.check_output(attachCmd, shell=True)
            
                print
                print
                print "Running rucio detach for DS: "+sourceDS
                #print detachCmd
                subprocess.check_output(detachCmd, shell=True)

                pass
            pass
        pass
    pass


print
print
print "You still need to close the following datasets by running the following commands:"
for ds in targetDSList:
    print "rucio close " + ds
    pass


"""
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_2LDF.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_ZH.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_WH.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_ZH.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_WH.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_2LDF.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_ZH.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_WH.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_2LDF.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_ZH.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_WH.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_2LDF.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_2LJJDF.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_2LJJ.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_2L.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_2LJJDF.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_2LJJ.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_2L.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_2LJJDF.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_2LJJ.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_Part01_PAOD_2L.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_2LJJDF.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_2LJJ.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.sysV13_rel20p7_Part01_PAOD_2L.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_CommonBkg_NoEffiSF.merge.PAOD.V13_rel20p7_FakeWJets_Part01_PAOD_2LJJ.move01
rucio close group.phys-higgs:group.phys-higgs.mc15_13TeV.HWW_BJesNoRelPtOR_HWWSignal_NoEffiSF.merge.PAOD.V13_rel20p7_FakeWJets_Part01_PAOD_2LJJ.move01


"""



# % diff samplelist_HIGG3D1_mc15c__HWWSignal.txt backup/samplelist_HIGG3D1_mc15c__HWWSignal.txt
# 34,40d33
# < mc15_13TeV.341462.PowhegPythia8EvtGen_CT10_AZNLO_ZH125J_MINLO_qqWWlvqq_VpT.merge.DAOD_HIGG3D1.e4435_a766_a821_r7676_p2666
# < mc15_13TeV.342282.PowhegPythia8EvtGen_CT10_AZNLOCTEQ6L1_ggH125_inc.merge.DAOD_HIGG3D1.e4246_s2608_s2183_r7772_r7676_p2666
# < mc15_13TeV.342282.PowhegPythia8EvtGen_CT10_AZNLOCTEQ6L1_ggH125_inc.merge.DAOD_HIGG3D1.e4850_a766_a821_r7676_p2666
# < mc15_13TeV.342283.PowhegPythia8EvtGen_CT10_AZNLOCTEQ6L1_VBFH125_inc.merge.DAOD_HIGG3D1.e4246_s2726_r7772_r7676_p2666
# < mc15_13TeV.342284.Pythia8EvtGen_A14NNPDF23LO_WH125_inc.merge.DAOD_HIGG3D1.e4246_s2608_s2183_r7772_r7676_p2666
# < mc15_13TeV.342285.Pythia8EvtGen_A14NNPDF23LO_ZH125_inc.merge.DAOD_HIGG3D1.e4246_s2608_s2183_r7772_r7676_p2666
# < mc15_13TeV.342299.aMcAtNloHerwigppEvtGen_UEEE5_CTEQ6L1_CT10ME_ttH125_inc.merge.DAOD_HIGG3D1.e4346_s2608_s2183_a821_r7676_p2666
# 51a45,46
# > mc15_13TeV.343362.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_dil_highMjj.merge.DAOD_HIGG3D1.e4661_a766_a821_r7676_p2666
# > mc15_13TeV.343362.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_dil_highMjj.merge.DAOD_HIGG3D1.e4661_s2726_r7772_r7676_p2666
# 58a54,62
# > mc15_13TeV.343478.Sherpa_CT10_lllvSFMinus.merge.DAOD_HIGG3D1.e4703_a766_a821_r7676_p2666
# > mc15_13TeV.343479.Sherpa_CT10_lllvOFMinus.merge.DAOD_HIGG3D1.e4703_a766_a821_r7676_p2666
# > mc15_13TeV.343480.Sherpa_CT10_lllvSFPlus.merge.DAOD_HIGG3D1.e4703_a766_a821_r7676_p2666
# > mc15_13TeV.343481.Sherpa_CT10_lllvOFPlus.merge.DAOD_HIGG3D1.e4703_a766_a821_r7676_p2666
# > mc15_13TeV.343482.PowhegPythia8EvtGen_CT10nloME_AZNLOCTEQ6L1_WWlvlv_highMjj.merge.DAOD_HIGG3D1.e4701_s2726_r7772_r7676_p2666
# > mc15_13TeV.343637.PowhegPythiaEvtGen_P2012_ttbar_hdamp172p5_threelepton.merge.DAOD_HIGG3D1.e4948_s2726_r7772_r7676_p2666
# > mc15_13TeV.343852.MadGraphPythia8EvtGen_A14NNPDF23LO_ttbar_Np0.merge.DAOD_HIGG3D1.e4849_a766_a818_r7676_p2666
# > mc15_13TeV.343853.MadGraphPythia8EvtGen_A14NNPDF23LO_ttbar_Np1.merge.DAOD_HIGG3D1.e4849_a766_a818_r7676_p2666
# > mc15_13TeV.343854.MadGraphPythia8EvtGen_A14NNPDF23LO_ttbar_Np2.merge.DAOD_HIGG3D1.e4849_a766_a818_r7676_p2666
# 59a64,68
# > mc15_13TeV.343982.MadGraphPythia8EvtGen_A14NNPDF23_Zmumu_Np0_mVBFfilt.merge.DAOD_HIGG3D1.e4967_s2726_r7772_r7676_p2666
# > mc15_13TeV.343983.MadGraphPythia8EvtGen_A14NNPDF23_Zmumu_Np1_mVBFfilt.merge.DAOD_HIGG3D1.e4967_s2726_r7772_r7676_p2666
# > mc15_13TeV.343984.MadGraphPythia8EvtGen_A14NNPDF23_Zmumu_Np2_mVBFfilt.merge.DAOD_HIGG3D1.e4967_s2726_r7772_r7676_p2666
# > mc15_13TeV.343985.MadGraphPythia8EvtGen_A14NNPDF23_Zmumu_Np3_mVBFfilt.merge.DAOD_HIGG3D1.e4967_s2726_r7772_r7676_p2666
# > mc15_13TeV.343986.MadGraphPythia8EvtGen_A14NNPDF23_Zmumu_Np4_mVBFfilt.merge.DAOD_HIGG3D1.e4967_s2726_r7772_r7676_p2666
