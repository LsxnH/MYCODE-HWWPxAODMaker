##=============================================================================
## Name:        CommonPAODContent.py
##
## Author:      Karsten Koeneke
## Created:     August 2014
##
## Description: Here, we define the content that will be written for the
##              PhysicsAOD (PAOD) output file.
##=============================================================================

# Import the steering flags for this analysis
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon


# ====================================================================
# Define the EventInfo variables to be written out
# ====================================================================
def eventInfoVars():
    """ Here, we define which individual variables for the event information get written out.
        We changed this from a positive list, i.e., explicitly list each variable to be written,
        to a negative list, i.e., list the variable that we DON'T want to write."""

    # return "*"
    return "-streamTagDets.-streamTagRobs.-subEventLink.-subEventTime.-subEventType"

    # varList = [ "runNumber", "eventNumber", "lumiBlock", #"timeStamp", "timeStampNSOffset", "bcid",
    #             #"streamTagNames", "streamTagTypes",
    #             "eventTypeBitmask", # Contains 'IS_SIMULATION' and such
    #             "primVtxIdx",
    #             "nPrimVtx", "nPrimVtxTwoTrk", "nPrimVtxThreeTrk", "nPrimVtxFourTrk",
    #             "actualInteractionsPerCrossing", "averageInteractionsPerCrossing" ]
    # if hWWCommon.Global.inputIsSimulation:
    #     varList.extend( [ "RandomRunNumber", "RandomLumiBlockNumber",
    #                       "PileupWeight", "PileupWeight___PRW_DATASF__1up", "PileupWeight___PRW_DATASF__1down",
    #                       "PRWHash", "corrected_averageInteractionsPerCrossing", "corrected_averageInteractionsPerCrossing",
    #                       "mcChannelNumber", "mcEventNumber", "mcEventWeights",
    #                       #"weight_*",
    #                       "weight_CT10_0", "weight_MMHT2014nlo68cl_0", "weight_NNPDF30_nlo_as_0118_0", "weight_PDF4LHC15_nlo_30_0",
    #                       "truth_WWtype",
    #                       "truthHiggsPt", "truthHiggsY", "truthHiggsPhi", "truthHiggsM",
    #                       "truth_nTruthLep", "truth_isZZ", "truth_mvv",
    #                       "truth_mW0W1", "truth_hasFSRPhoton", "truth_hasFSRPhotonDR01",
    #                       "truth_VBFMjj", "truth_VVMass", "truth_nJet", "truth_nWZJet", "truth_ttbarpt", "truth_toppt", "truth_nOutgoingPartons"] )
    #     # Higgs simplified template cross-section variables
    #     varList.extend( [ "HTXS_Higgs_decay_eta","HTXS_Higgs_decay_m","HTXS_Higgs_decay_phi","HTXS_Higgs_decay_pt",
    #                       "HTXS_Higgs_eta","HTXS_Higgs_m","HTXS_Higgs_phi","HTXS_Higgs_pt",
    #                       "HTXS_V_decay_eta","HTXS_V_decay_m","HTXS_V_decay_phi","HTXS_V_decay_pt",
    #                       "HTXS_V_eta","HTXS_V_m","HTXS_V_phi","HTXS_V_pt",
    #                       "HTXS_V_jets25_eta","HTXS_V_jets25_m","HTXS_V_jets25_phi","HTXS_V_jets25_pt",
    #                       "HTXS_V_jets30_eta","HTXS_V_jets30_m","HTXS_V_jets30_phi","HTXS_V_jets30_pt",
    #                       "HTXS_Njets_pTjet25","HTXS_Njets_pTjet30","HTXS_errorCode","HTXS_prodMode",
    #                       "HTXS_Stage0_Category","HTXS_Stage1_Category_pTjet25","HTXS_Stage1_Category_pTjet30" ] )
    #     # JVT per-event scale factors and systematics
    #
    #     EfficiencyScaleFactorVarName   = hWWCommon.Jets.effiJVTVarName,
    #     EfficiencySystematicVariations = hWWCommon.Jets.effiJVTSysts
    #
    #     # JVT scale factors
    #     jvtVarList = [ hWWCommon.Jets.effiJVTVarName, hWWCommon.Jets.effiJVTVarName+"C25F25", hWWCommon.Jets.effiJVTVarName+"C25F30",
    #                    hWWCommon.Jets.effiForwardJVTVarName, hWWCommon.Jets.effiForwardJVTVarName+"C25F25", hWWCommon.Jets.effiForwardJVTVarName+"C25F30" ]
    #     for effiVarName in hWWCommon.Jets.effiJVTSysts :
    #         jvtVarList.extend( [hWWCommon.Jets.effiJVTVarName+"___"+sysName       for sysName in hWWCommon.Jets.effiJVTSysts] )
    #         jvtVarList.extend( [hWWCommon.Jets.effiJVTVarName+"C25F25___"+sysName for sysName in hWWCommon.Jets.effiJVTSysts] )
    #         jvtVarList.extend( [hWWCommon.Jets.effiJVTVarName+"C25F30___"+sysName for sysName in hWWCommon.Jets.effiJVTSysts] )
    #         jvtVarList.extend( [hWWCommon.Jets.effiForwardJVTVarName+"___"+sysName       for sysName in hWWCommon.Jets.effiJVTSysts] )
    #         jvtVarList.extend( [hWWCommon.Jets.effiForwardJVTVarName+"C25F25___"+sysName for sysName in hWWCommon.Jets.effiJVTSysts] )
    #         jvtVarList.extend( [hWWCommon.Jets.effiForwardJVTVarName+"C25F30___"+sysName for sysName in hWWCommon.Jets.effiJVTSysts] )
    #         pass
    #     varList.extend( jvtVarList )
    #     pass
    # for trigName in hWWCommon.Trigger.allTriggerList :
    #     varList.append( hWWCommon.Trigger.triggerPassPrefix + trigName )
    #     pass
    # varNames = ""
    # for varName in varList:
    #     varNames += ("."+varName)
    #     pass
    #return varNames.lstrip(".")


# ====================================================================
# Define the muon variables to be written out
# ====================================================================
def muonScaleFactorVars():
    """ This function is needed, because we need to dynamically figure out what
    the efficiency scale-factor variable names are (including systematics)."""
    # Also add all the scale factor variables
    varList = [ ]
    # Reconstruction and identification scale factors
    varList.extend( hWWCommon.Muons.effiVarNameList )
    for effiVarName in hWWCommon.Muons.effiVarNameList :
        varList.extend( [effiVarName+"___"+sysName for sysName in hWWCommon.Muons.effiSysts ] )
        pass
    # Track-to-vertex association scale factors
    varList.extend( hWWCommon.Muons.effiTTVAVarNameList )
    for effiVarName in hWWCommon.Muons.effiTTVAVarNameList :
        varList.extend( [effiVarName+"___"+sysName for sysName in hWWCommon.Muons.effiTTVASysts ] )
        pass
    # Isolation scale factors
    varList.extend( hWWCommon.Muons.effiIsoVarNameList )
    for effiIsoVarName in hWWCommon.Muons.effiIsoVarNameList :
        varList.extend( [effiIsoVarName+"___"+sysName for sysName in hWWCommon.Muons.effiIsoSysts ] )
        pass
    # Trigger efficiency scale-factors
    varList.extend( hWWCommon.Muons.effiTrigSFVarNameList )
    for trigEffiSFVarName in hWWCommon.Muons.effiTrigSFVarNameList :
        varList.extend( [trigEffiSFVarName+"___"+sysName for sysName in hWWCommon.Muons.effiTrigSysts ] )
        pass
    # Trigger efficiencies
    varList.extend( hWWCommon.Muons.effiTrigVarNameList )
    # Now, put everything in one long variable name, separated by "."
    varNames = ""
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")

def muonVars():
    """ Here, we define which individual variables for the muons get written out."""
    varList = [ "pt", "eta", "phi", "m", "charge", "muonType", "author",
                #"quality",
                "overlaps",
                "Quality", "PassesIDCuts", "PassesHighPtCuts", "deltaPt", "momentumBalanceSignificance",
                "chargeID","chargeMS","chargeEX","chargeCB", # philip: store the muon charge from different systems
                "InnerDetectorPt", "MuonSpectrometerPt", "IsBadMuon",
                "z0", "z0err", "sinTheta", "d0", "d0sig", # "z0sig", "d0err", "primVtxIsValid",
                "PromptLeptonIso", "PromptLeptonVeto",
                "ptvarcone30", "topoetcone20",
                "ptvarcone30_TightTTVA_pt1000", "ptvarcone30_TightTTVA_pt500",
                "ptcone20_TightTTVA_pt1000", "ptcone20_TightTTVA_pt500",
                "neflowisol20",
                "topoetcone30",
                "topoetcone40",
                "ptvarcone20", "ptvarcone40",
                "ptcone20", "ptcone30", "ptcone40"
                ]

    if hWWCommon.Global.doORNoMuNearJetRemoval:
        varList.append("overlapsNoMuNearJetRemoval")

    if hWWCommon.Global.doORNoMuNearJetRemovalNoBJetPrecedence:
        varList.append("overlapsNoMuNearJetRemovalNoBJetPrecedence")

    if hWWCommon.Global.inputIsSimulation:
        varList.extend( [ "truthType", "truthOrigin" ] )
        varList.extend( [ "hwwTruthType", "hwwTruthOrigin" ] )
        varList.extend( [ "truthPt", "truthEta", "truthPhi", "truthCharge" ] )
        varList.extend( [ "flavourTag" ] )
        pass

    # Add the isolation true/false flag variables
    varList.extend( hWWCommon.Muons.passIsoVarNameList )

    # Add trigger matching variables
    if hWWCommon.Global.doTriggerMatching:
        for trigName in (hWWCommon.Trigger.muonTriggerList+hWWCommon.Trigger.electronMuonTriggerList) :
            varList.append(hWWCommon.Trigger.triggerMatchPrefix+trigName)
            pass
        pass

    varNames = muonScaleFactorVars()
    for varName in varList:
        varNames += ("."+varName)
        pass
    #print "Using muon variable names: ", varNames
    return varNames.lstrip(".")



# ====================================================================
# Define the electron variables to be written out
# ====================================================================
def electronScaleFactorVars():
    """ This function is needed, because we need to dynamically figure out what
    the efficiency scale-factor variable names are (including systematics)."""
    # Also add all the efficiency scale factor variables
    varList = [ ]
    # Reconstruction scale factors
    varList.extend( hWWCommon.Electrons.effiRecoVarNameList )
    for effiVarName in hWWCommon.Electrons.effiRecoVarNameList :
        varList.extend( [effiVarName+"___"+sysName for sysName in hWWCommon.Electrons.effiRecoSysts ] )
        pass
    # Identification scale factors
    varList.extend( hWWCommon.Electrons.effiVarNameList )
    for effiVarName in hWWCommon.Electrons.effiVarNameList :
        varList.extend( [effiVarName+"___"+sysName for sysName in hWWCommon.Electrons.effiSysts ] )
        pass
    # Trigger scale factors
    varList.extend( hWWCommon.Electrons.effiSFTrigVarNameList )
    for effiVarName in hWWCommon.Electrons.effiSFTrigVarNameList :
        varList.extend( [effiVarName+"___"+sysName for sysName in hWWCommon.Electrons.effiSFTrigSysts ] )
        pass
    # Trigger efficiencies
    varList.extend( hWWCommon.Electrons.effiTrigVarNameList )
    for effiVarName in hWWCommon.Electrons.effiTrigVarNameList :
        varList.extend( [effiVarName+"___"+sysName for sysName in hWWCommon.Electrons.effiTrigSysts ] )
        pass
    # Isolation scale factors
    varList.extend( hWWCommon.Electrons.effiIsoVarNameList )
    for effiVarName in hWWCommon.Electrons.effiIsoVarNameList :
        varList.extend( [effiVarName+"___"+sysName for sysName in hWWCommon.Electrons.effiIsoSysts ] )
        pass
    # Now, put everything in one long variable name, separated by "."
    varNames = ""
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")

def electronVars():
    """ Here, we define which individual variables for the electrons get written out."""
    varList = [ "pt", "eta", "phi", "m", "charge",
                "author",
                "overlaps",
                "isLHVeryLoose", "isLHLoose", "isLHLooseBLayer","isLHMedium", "isLHTight",
                "passBLayerRequirement",
                "z0", "z0err", "sinTheta", "d0", "d0sig", # "z0sig", "d0err", "primVtxIsValid",
                "PromptLeptonIso", "PromptLeptonVeto",
                #"chargeIDTag",
                "DFCommonElectronsECIDS", "DFCommonElectronsECIDSResult",
                "ptvarcone20", "topoetcone20",
                "ptvarcone20_TightTTVA_pt1000",
                "ptvarcone30_TightTTVA_pt1000", "ptvarcone30_TightTTVA_pt500",
                "ptcone20_TightTTVA_pt1000", "ptcone20_TightTTVA_pt500",
                "neflowisol20",
                "topoetcone30",
                "topoetcone40",
                "ptvarcone30", "ptvarcone40",
                "ptcone20", "ptcone30", "ptcone40",
                "trackParticleLinks",
                "caloClusterLinks",
                "AmbiguityLoose", "AmbiguityTight"
                ]

    if hWWCommon.Global.doORNoMuNearJetRemoval:
        varList.append("overlapsNoMuNearJetRemoval")

    if hWWCommon.Global.doORNoMuNearJetRemovalNoBJetPrecedence:
        varList.append("overlapsNoMuNearJetRemovalNoBJetPrecedence")

    if hWWCommon.Global.inputIsSimulation:
        varList.extend( [ "truthType", "truthOrigin",
                          #"bkgTruthType", "bkgTruthOrigin",
                          #"bkgMotherPdgId",
                          "firstEgMotherTruthType", "firstEgMotherTruthOrigin",
                          "firstEgMotherPdgId" ] )
        varList.extend( [ "truthPt", "truthEta", "truthPhi", "truthCharge" ] )
        varList.extend( [ "flavourTag" ] )
        pass
    varNames = electronScaleFactorVars()

    # Add the isolation true/false flag variables
    varList.extend( hWWCommon.Electrons.passIsoVarNameList )

    # Add trigger matching variables
    if hWWCommon.Global.doTriggerMatching:
        for trigName in (hWWCommon.Trigger.electronTriggerList+hWWCommon.Trigger.electronMuonTriggerList) :
            varList.append(hWWCommon.Trigger.triggerMatchPrefix+trigName)
            pass
        pass

    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")



# ====================================================================
# Define the jet variables to be written out
# ====================================================================
def jetScaleFactorVars():
    """ This function is needed, because we need to dynamically figure out what
    the efficiency scale-factor variable names are (including systematics)."""
    # Also add all the efficiency scale factor variables
    effiVarName = hWWCommon.Jets.effiVarName
    varList = [ ]
    effiVarSuffixList = hWWCommon.Jets.effiSysts
    varList.extend( [effiVarName+"___"+sysName for sysName in effiVarSuffixList ] )
    varNames = effiVarName
    # # JVT scale factors
    # varList.append( hWWCommon.Jets.effiJVTVarName )
    # for effiVarName in hWWCommon.Jets.effiJVTSysts :
    #     varList.extend( [hWWCommon.Jets.effiJVTVarName+"___"+sysName for sysName in hWWCommon.Jets.effiJVTSysts] )
    #     pass
    # Build the full string of variable names out of the list
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames

def jetVars():
    """ Here, we define which individual variables for the jets get written out."""
    varList = [ "pt", "eta", "phi", "m", "charge", "Jvt", # "JvtJvfcorr", "JvtRpt",
                hWWCommon.Jets.passJVTVarName, # "passJVT"
                hWWCommon.Jets.updateJVTName,  # "calibJvt"
                "passFJVT", "passFJVTTight", "fJvt",
                "DetectorEta",
                "btaggingLink",
                "Width", "nTracks",
                #"Split12",
                "overlaps",
                ]

    if hWWCommon.Global.doORNoMuNearJetRemoval:
        varList.append("overlapsNoMuNearJetRemoval")

    if hWWCommon.Global.doORNoMuNearJetRemovalNoBJetPrecedence:
        varList.append("overlapsNoMuNearJetRemovalNoBJetPrecedence")

    if hWWCommon.Global.inputIsSimulation:
        varList.extend( [ "hardScatterTruthMatchDeltaR", "hardScatterTruthJetPt" ] )
        varList.extend( [ "isJvtHS", "isJvtPU" ] )
        varList.extend( [ "PartonTruthLabelID", "HadronConeExclTruthLabelID" ] )
        varList.extend( [ "truthOrigin" ] )
        pass

    if hWWCommon.Jets.writeJetConstituents:
        varList.extend( ["constituentLinks","constituentWeights"] )
        pass

    # Build the full string of variable names out of the list
    varNames = jetScaleFactorVars()
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")



# ====================================================================
# Define the large-R jet variables to be written out
# ====================================================================
def fatJetVars():
    """ Here, we define which individual variables for the large-R jets get written out."""
    varList = [ "pt", "eta", "phi", "m", "charge",
                "D2", "isWJet", "isZJet", "passWMassCut", "passZMassCut",
                "passWSubstructure", "passZSubstructure"
                ]
    if hWWCommon.Global.inputIsSimulation:
        varList.extend( [ "hardScatterTruthMatchDeltaR", "hardScatterTruthJetPt" ] )
        varList.extend( [ "PartonTruthLabelID", "HadronConeExclTruthLabelID" ] )
        pass
    # Build the full string of variable names out of the list
    varNames = ""
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")



# ====================================================================
# Define the MET variables to be written out
# ====================================================================
def metScaleFactorVars():
    """ This function is needed, because we need to dynamically figure out what
    the efficiency scale-factor variable names are (including systematics)."""
    # Also add all the efficiency scale factor variables
    effiVarName = hWWCommon.MET.effiVarName
    varList = [ ]
    effiVarSuffixList = hWWCommon.MET.effiSysts
    varList.extend( [effiVarName+"___"+sysName for sysName in effiVarSuffixList ] )
    varNames = effiVarName
    # Build the full string of variable names out of the list
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames

def metVars():
    """ Here, we define which individual variables for the missingET get written out."""
    metVarName = hWWCommon.MET.effiVarName
    varList = [ "mpx", "mpy", "sumet", "metSig", "metOverSqrtSumET", "metOverSqrtHT",
                "metSigDirectional", "metRho", "metVarL", "metVarT" ]
    varNames = metScaleFactorVars()
    # Build the full string of variable names out of the list
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")



# ====================================================================
# Define the truth muon variables to be written out
# ====================================================================
def truthMuonVars():
    """ Here, we define which individual variables for the truth muons get written out."""
    varList = [ "px", "py", "pz", "e","pt", "eta", "phi", "m", "charge","pdgId","status","motherID","isFromTau"#, "muonType",
    #varList = [ "px", "py", "pz", "m", "pdgID","status","pt_dressed"#, "muonType",
                #"quality",
                #"Quality", "PassesIDCuts", "deltaPt", "momentumBalanceSignificance",
                #"InnerDetectorPt", "MuonSpectrometerPt",
                #"z0", "z0err", "sinTheta", "d0", "d0sig", # "z0sig", "d0err", "primVtxIsValid",
                #"ptvarcone30", "topoetcone20" # These two are used by the IsolationSelectionTool
                # "topoetcone20", "topoetcone30", "topoetcone40",
                # "ptvarcone20", "ptvarcone30", "ptvarcone40",
                # "ptcone20", "ptcone30", "ptcone40"
                ]

    varNames = ""
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")



# ====================================================================
# Define the truth electron variables to be written out
# ====================================================================
def truthElectronVars():
    """ Here, we define which individual variables for the truth electrons get written out."""
    varList = [ "px", "py", "pz", "e","pt", "eta", "phi", "m","charge","pdgId","status","motherID","isFromTau","motherID2"
                #"isLHLoose", "isLHMedium", "isLHTight",
                #"z0", "z0err", "sinTheta", "d0", "d0sig", # "z0sig", "d0err", "primVtxIsValid",
                #"ptvarcone20", "topoetcone20", # These two are used by the IsolationSelectionTool
                # "topoetcone20", "topoetcone30", "topoetcone40", #"topoetcone40_corrected",
                # "ptvarcone20", "ptvarcone30", "ptvarcone40",
                # "ptcone20", "ptcone30", "ptcone40",
                #"trackParticleLinks",
                #"caloClusterLinks",
                #"AmbiguityLoose","AmbiguityTight"
                ]

    varNames = ""
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")



# ====================================================================
# Define the truth jet variables to be written out
# ====================================================================
def truthJetVars():
    """ Here, we define which individual variables for the truth jets get written out."""
    varList = [ "pt", "eta", "phi", "m", "charge","GhostBHadronsFinalCount","GhostBHadronsFinalPt","GhostBQuarksFinalCount","GhostBQuarksFinalPt","GhostCHadronsFinalCount","GhostCHadronsFinalPt","GhostCQuarksFinalCount","GhostCQuarksFinalPt","ConeTruthLabelID","HadronConeExclTruthLabelID","TruthLabelDeltaR_B","TruthLabelDeltaR_C","PartonTruthLabelID"#, "JVF", "calibJvt", "Jvt", "JvtJvfcorr", "JvtRpt",
                #"MV2c00","MV2c10", "MV2c20",
                #"btaggingLink",
                #"PassLooseBad", "PassTightBad"
               ]

    varNames = ""
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")



# ====================================================================
# Define the truth MET variables to be written out
# ====================================================================
def truthMETVars():
    """ Here, we define which individual variables for the truth missingET get written out."""
    varList = [ "mpx", "mpy", "sumet" ]

    varNames = ""
    for varName in varList:
        varNames += ("."+varName)
        pass
    return varNames.lstrip(".")


def pAODCompulsoryContent():
    """ Here, we define the content which will get written out irrespective of whether we are processing reco or truth."""

    itemList = ["xAOD::EventInfo#EventInfo",
                "xAOD::EventAuxInfo#EventInfoAux."+eventInfoVars(),
                #"xAOD::EventAuxInfo#EventInfoAux.*",
                ]

    if hWWCommon.Global.writeTruthParticles:
        itemList.append("xAOD::TruthParticleContainer#TruthParticles")
        itemList.append("xAOD::TruthParticleAuxContainer#TruthParticlesAux.")
        itemList.append("xAOD::AuxContainerBase#TruthParticlesAux.")
        pass

    # Add the truth MET / TruthEvents
    if hWWCommon.Global.inputIsSimulation:
        itemList.extend(["xAOD::MissingETContainer#"+hWWCommon.TruthMET.finalCont,
                         "xAOD::MissingETAuxContainer#"+hWWCommon.TruthMET.finalCont+"Aux.*",
                         "xAOD::AuxContainerBase#"+hWWCommon.TruthMET.finalCont+"Aux."+truthMETVars(),
                         #"xAOD::AuxContainerBase#"+hWWCommon.TruthMET.finalCont+"*Aux."+truthMETVars(),
                         "xAOD::ShallowAuxContainer#"+hWWCommon.TruthMET.finalCont])
        itemList.append("xAOD::TruthEventContainer#TruthEvents")
        itemList.append("xAOD::AuxContainerBase#TruthEventsAux.weights.Q.X1.X2.XF1.XF2.PDGID1.PDGID2.PDFID1.PDFID2.crossSection.crossSectionError")
        pass

    # Schedule the broken-up AuxContainers to the output (and try to remove the others)
    if hWWCommon.Global.breakUpAuxContainers :
        from PhysicsxAODConfig import HWWCommonHelpers
        itemList = HWWCommonHelpers.replaceAuxContainers( itemList, hWWCommon.Global.auxContsToBreakUp )
        pass

    return itemList

def pAODRecoContent():
    """ Here, we define the content which will get written out when processing reco."""

    itemList = [# Needed for being able to later use the ExpressionParser
                # (which uses also the trigger information). Only 3 bytes/event.
                "xAOD::TrigConfKeys#TrigConfKeys",

                # "xAOD::ElectronContainer#"+hWWCommon.Electrons.finalCont+"*",
                # "xAOD::AuxContainerBase#"+hWWCommon.Electrons.finalCont+"*Aux."+electronVars(),
                # "xAOD::ShallowAuxContainer#"+hWWCommon.Electrons.finalCont+"*Aux.-originalObjectLink",

                "xAOD::MuonContainer#"+hWWCommon.Muons.finalCont,
                "xAOD::MuonContainer#"+hWWCommon.Muons.finalCont+"___MUON_*",
                "xAOD::AuxContainerBase#"+hWWCommon.Muons.finalCont+"Aux."+muonVars(),
                "xAOD::ShallowAuxContainer#"+hWWCommon.Muons.finalCont+"___MUON_*Aux.-originalObjectLink.-StatCombCBPars.-StatCombCBCovariance",

                "xAOD::MissingETContainer#"+hWWCommon.MET.finalCont+"*",
                "xAOD::MissingETAuxContainer#"+hWWCommon.MET.finalCont+"Aux.*",
                "xAOD::AuxContainerBase#"+hWWCommon.MET.finalCont+"Aux."+metVars(),
                "xAOD::AuxContainerBase#"+hWWCommon.MET.finalCont+"*Aux."+metVars(),
                "xAOD::ShallowAuxContainer#"+hWWCommon.MET.finalCont+"*",

                "xAOD::MissingETContainer#"+hWWCommon.MET.finalTrackCont+"*",
                "xAOD::MissingETAuxContainer#"+hWWCommon.MET.finalTrackCont+"Aux.*",
                "xAOD::AuxContainerBase#"+hWWCommon.MET.finalTrackCont+"Aux."+metVars(),
                "xAOD::AuxContainerBase#"+hWWCommon.MET.finalTrackCont+"*Aux."+metVars(),
                "xAOD::ShallowAuxContainer#"+hWWCommon.MET.finalTrackCont+"*",

                # Add also the b-tagging, but only mv2
                "xAOD::BTaggingContainer#BTagging_"+(hWWCommon.Jets.inCont.rstrip("Jets")),
                "xAOD::AuxContainerBase#BTagging_"+(hWWCommon.Jets.inCont.rstrip("Jets"))+"Aux.MV2c10_discriminant.DL1_pc.DL1_pb.DL1_pu",

                # Add also the egamma CaloClusters (only for the electrons that we write out)
                "xAOD::CaloClusterContainer#egammaClusters",
                "xAOD::CaloClusterAuxContainer#egammaClustersAux.e_sampl.eta_sampl",
                "xAOD::AuxContainerBase#egammaClustersAux.e_sampl.eta_sampl",

                # Add also the GSF TrackParticles (only for the electrons that we write out)
                "xAOD::TrackParticleContainer#GSFTrackParticles",
                "xAOD::TrackParticleAuxContainer#GSFTrackParticlesAux.-constituentLinks.-constituentWeights.-definingParametersCovMatrix.-parameterX.-parameterPX.-parameterPY.-parameterPZ",
                "xAOD::AuxContainerBase#GSFTrackParticlesAux.-constituentLinks.-constituentWeights.-definingParametersCovMatrix.-parameterX.-parameterPX.-parameterPY.-parameterPZ",
                ]

    for eleContName in hWWCommon.Electrons.finalContList() :
        itemList.append("xAOD::ElectronContainer#"+eleContName)
        if not "_" in eleContName :
            itemList.append("xAOD::AuxContainerBase#"+eleContName+"Aux."+electronVars())
            pass
        else :
            itemList.append("xAOD::ShallowAuxContainer#"+eleContName+"Aux.-originalObjectLink.-topoetcone20.-topoetcone20ptCorrection.-topoetcone30.-topoetcone30ptCorrection.-topoetcone40.-topoetcone40ptCorrection")
            pass

        pass

    # for muContName in hWWCommon.Muons.finalContList() :
    #     itemList.append("xAOD::MuonContainer#"+muContName)
    #     if not "_" in muContName :
    #         itemList.append("xAOD::AuxContainerBase#"+muContName+"Aux."+muonVars())
    #         pass
    #     else :
    #         itemList.append("xAOD::ShallowAuxContainer#"+muContName+"Aux.-originalObjectLink")
    #         pass
    #
    #     pass

    for jetContName in hWWCommon.Jets.finalContList() :
        itemList.append("xAOD::JetContainer#"+jetContName)
        if not "_" in jetContName :
            itemList.append("xAOD::AuxContainerBase#"+jetContName+"Aux."+jetVars())
            pass
        else :
            # itemList.append("xAOD::ShallowAuxContainer#"+jetContName+"Aux.-originalObjectLink.-selected")
            itemList.append("xAOD::ShallowAuxContainer#"+jetContName+"Aux.-originalObjectLink.-selected.-eta.-phi.-passJVT.-isBJet85.-effiSFJVT")
            pass

        pass

    if hWWCommon.Jets.writeJetConstituents:
        itemList.append("xAOD::CaloClusterContainer#CaloCalTopoClusters")
        itemList.append("xAOD::CaloClusterAuxContainer#CaloCalTopoClustersAux.calEta.calE.calPhi.calM")
        itemList.append("xAOD::AuxContainerBase#CaloCalTopoClustersAux.calEta.calE.calPhi.calM")
        pass

    # Write out the large-R jets, if requested
    if hWWCommon.FatJets():
        itemList.append("xAOD::JetContainer#"+hWWCommon.FatJets.finalCont)
        itemList.append("xAOD::JetContainer#"+hWWCommon.FatJets.finalCont+"___*")
        itemList.append("xAOD::AuxContainerBase#"+hWWCommon.FatJets.finalCont+"Aux."+fatJetVars())
        itemList.append("xAOD::ShallowAuxContainer#"+hWWCommon.FatJets.finalCont+"___*Aux.-originalObjectLink")
        pass

    if hWWCommon.Jets.writeTrackJets :
        itemList.append("xAOD::JetContainer#"+hWWCommon.Jets.inTrackJetsCont)

        trackJetVars="pt.eta.phi.m.btaggingLink" #".MV2c10"
        if hWWCommon.Global.inputIsSimulation:
            trackJetVars += ".PartonTruthLabelID.ConeTruthLabelID.HadronConeExclTruthLabelID"
            pass
        # Also add all the b-tagging efficiency scale factor variables
        effiVarName = hWWCommon.Jets.effiVarName
        effiVarSuffixList = hWWCommon.Jets.effiSysts
        # varList = [ ]
        # varList.extend( [effiVarName+"___"+sysName for sysName in effiVarSuffixList ] )
        trackJetVars += "."+effiVarName
        for varName in [effiVarName+"___"+sysName for sysName in effiVarSuffixList ]:
            trackJetVars += ("."+varName)
            pass
        itemList.append("xAOD::AuxContainerBase#"+hWWCommon.Jets.inTrackJetsCont+"Aux."+trackJetVars)
        itemList.append("xAOD::BTaggingContainer#BTagging_AntiKt4Track")
        itemList.append("xAOD::AuxContainerBase#BTagging_AntiKt4TrackAux.MV2c10_discriminant")
        pass

    if hWWCommon.Jets.writeAntiKt2TrackJets:
        trackJetVars2="pt.eta.phi.m"
        itemList.append("xAOD::JetContainer#AntiKt2PV0TrackJets")
        itemList.append("xAOD::AuxContainerBase#AntiKt2PV0TrackJetsAux."+trackJetVars2)
        pass

    if hWWCommon.Global.writeLeptonTrackParticles:
        itemList.append("xAOD::TrackParticleContainer#GSFTrackParticles")
        itemList.append("xAOD::TrackParticleAuxContainer#GSFTrackParticlesAux.")
        itemList.append("xAOD::TrackParticleContainer#InDetTrackParticles")
        itemList.append("xAOD::TrackParticleAuxContainer#InDetTrackParticlesAux.")
        itemList.append("xAOD::TrackParticleContainer#InDetTrackParticlesForward")
        itemList.append("xAOD::TrackParticleAuxContainer#InDetTrackParticlesForwardAux.")
        itemList.append("xAOD::TrackParticleContainer#CombinedMuonTrackParticles")
        itemList.append("xAOD::TrackParticleAuxContainer#CombinedMuonTrackParticlesAux.")
        itemList.append("xAOD::TrackParticleContainer#ExtrapolatedMuonTrackParticles")
        itemList.append("xAOD::TrackParticleAuxContainer#ExtrapolatedMuonTrackParticlesAux.")
        pass

    if hWWCommon.Global.writeLeptonCaloClusters:
        itemList.append("xAOD::CaloClusterContainer#egClusterCollection")
        itemList.append("xAOD::CaloClusterAuxContainer#egClusterCollectionAux.")
        pass

    if hWWCommon.Global.writeJetCaloClusters:
        itemList.append("xAOD::CaloClusterContainer#CaloCalTopoCluster")
        itemList.append("xAOD::CaloClusterAuxContainer#CaloCalTopoClusterAux.")
        pass

    # Schedule the broken-up AuxContainers to the output (and try to remove the others)
    if hWWCommon.Global.breakUpAuxContainers :
        from PhysicsxAODConfig import HWWCommonHelpers
        itemList = HWWCommonHelpers.replaceAuxContainers( itemList, hWWCommon.Global.auxContsToBreakUp )
        pass

    return itemList

def pAODTruthContent():
    """ Here, we define the content which will get written out when processing truth."""

    itemList = [# "xAOD::ElectronContainer#"+hWWCommon.TruthElectrons.finalCont+"*",
                # "xAOD::AuxContainerBase#"+hWWCommon.TruthElectrons.finalCont+"*Aux."+truthElectronVars(),
                # "xAOD::ShallowAuxContainer#"+hWWCommon.TruthElectrons.finalCont+"*Aux.-originalObjectLink.-overlaps",

                "xAOD::TruthParticleContainer#"+hWWCommon.TruthMuons.finalCont,
                "xAOD::TruthParticleContainer#"+hWWCommon.TruthMuons.finalCont+"___MUONS_*",
                "xAOD::AuxContainerBase#"+hWWCommon.TruthMuons.finalCont+"Aux."+truthMuonVars(),
                "xAOD::ShallowAuxContainer#"+hWWCommon.TruthMuons.finalCont+"___MUONS_*Aux.-originalObjectLink.-overlaps",
                ]

    for eleContName in hWWCommon.TruthElectrons.finalContList() :
        itemList.append("xAOD::TruthParticleContainer#"+eleContName)
        if not "_" in eleContName :
            itemList.append("xAOD::AuxContainerBase#"+eleContName+"Aux."+truthElectronVars())
            pass
        else :
            itemList.append("xAOD::ShallowAuxContainer#"+eleContName+"Aux.-originalObjectLink.-overlaps")
            pass

        pass

    # for muContName in hWWCommon.TrutMuons.finalContList() :
    #     itemList.append("xAOD::MuonContainer#"+muContName)
    #     if not "_" in muContName :
    #         itemList.append("xAOD::AuxContainerBase#"+muContName+"Aux."+truthMuonVars())
    #         pass
    #     else :
    #         itemList.append("xAOD::ShallowAuxContainer#"+muContName+"Aux.-originalObjectLink.-overlaps")
    #         pass
    #
    #     pass

    for jetContName in hWWCommon.TruthJets.finalContList() :
        itemList.append("xAOD::JetContainer#"+jetContName)
        if not "_" in jetContName :
            itemList.append("xAOD::AuxContainerBase#"+jetContName+"Aux."+truthJetVars())
            pass
        else :
            itemList.append("xAOD::ShallowAuxContainer#"+jetContName+"Aux.-originalObjectLink.-overlaps")
            pass

        pass

    # Schedule the broken-up AuxContainers to the output (and try to remove the others)
    if hWWCommon.Global.breakUpAuxContainers :
        from PhysicsxAODConfig import HWWCommonHelpers
        itemList = HWWCommonHelpers.replaceAuxContainers( itemList, hWWCommon.Global.auxContsToBreakUp )
        pass

    return itemList

# ====================================================================
# Define the container item list of the output mini-xAOD
# ====================================================================
def pAODContent():
    """This function defines then which 'containers' are written to disk."""

    itemList = pAODCompulsoryContent()

    if hWWCommon.Global.processReco:
        itemList += pAODRecoContent()

    if hWWCommon.Global.processTruth:
        itemList += pAODTruthContent()

    return itemList


# ====================================================================
# Define the meta-data item list of the output mini-xAOD
# ====================================================================
def pAODMetaDataContent():
    itemList = ["xAOD::CutBookkeeperContainer#*",
                "xAOD::CutBookkeeperAuxContainer#*",
                "IOVMetaDataContainer#*",
                "xAOD::LumiBlockRangeContainer#*",
                "xAOD::LumiBlockRangeAuxContainer#*",
                "xAOD::TriggerMenuContainer#*",
                "xAOD::TriggerMenuAuxContainer#*",
                "xAOD::FileMetaData#FileMetaData",
                "xAOD::FileMetaDataAuxInfo#FileMetaDataAux."
                ]
    return itemList
