# ====================================================================
# In this file, we will create our own sub-sequence that always runs
# through all its algorithms, irespective of the algorithm accepting
# an event or not.
# We will attach all the MET building algorithms.
# ====================================================================


# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWMETBuilding.py")


# Print a status message
hWW_msg.info("Running missingET building")



# ====================================================================
# Recalculate missingET (including all systematic four-momentum
# variations of the input physics objects)
# ====================================================================

# Create the new (mc15) met maker tool
ToolSvc += CfgMgr.met__METMaker("METMaker",
                                OutputLevel      = WARNING,
                                JetSelection     = "Tight",
                                #JetRejectionDec  = "passFJVT",
                                JetJvtMomentName = hWWCommon.Jets.updateJVTName,
				DoPFlow		 = hWWCommon.Jets.doPFlowJets )



# Figure out what type of jet collection we are using and adjust the met names
jetContName = hWWCommon.Jets.inCont
if jetContName.__contains__("LCTopo"):
    hWWCommon.MET.inMap  = "METAssoc_AntiKt4LCTopo"
    hWWCommon.MET.inCore = "MET_Core_AntiKt4LCTopo"
    hWW_msg.info("Changed METMapName to:  %s" % hWWCommon.MET.inMap)
    hWW_msg.info("Changed METCoreName to: %s" % hWWCommon.MET.inCore)
    pass

if jetContName.__contains__("EMPFlow"):
    hWWCommon.MET.inMap  = "METAssoc_AntiKt4EMPFlow"
    hWWCommon.MET.inCore = "MET_Core_AntiKt4EMPFlow"
    hWW_msg.info("Changed METMapName to:  %s" % hWWCommon.MET.inMap)
    hWW_msg.info("Changed METCoreName to: %s" % hWWCommon.MET.inCore)
    pass

## Determine JetCollection setting for met significance tool
jetCollectionType = "AntiKt4EMTopo"
if hWWCommon.Jets.doPFlowJets:
    jetCollectionType = "AntiKt4EMPFlow"
    pass

## Create met significance tool
ToolSvc += CfgMgr.met__METSignificance("METSignificance",
                                       #OutputLevel      = VERBOSE,
                                       SoftTermParam    = 0,     # 0 corresponds to met::Random
                                       TreatPUJets      = True,
                                       DoPhiReso        = True,
                                       IsAFII           = hWWCommon.Global.inputSimulationType == "AFII",
                                       IsDataJet        = False, # To date (Jan 2019) the recommendation is to set this to false for data and MC
                                       JetCollection    = jetCollectionType
                                       )

# Get the names of all input containers
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.Muons.calibPreSelCont,['','electronNOSUFFIX','muon','jetNOSUFFIX','fatjetNOSUFFIX']),
                                       (hWWCommon.Electrons.calibPreSelCont,['','electron','muonNOSUFFIX','jetNOSUFFIX','fatjetNOSUFFIX']),
                                       (hWWCommon.Jets.calibCont,['','electronNOSUFFIX','muonNOSUFFIX','jet','fatjetNOSUFFIX']),
                                       (hWWCommon.MET.finalCont,['','electron','muon','jet','fatjet']),
                                       (hWWCommon.MET.finalTrackCont,['','electron','muon','jet','fatjet'])
                                       ] )

# This loop over all four-momentum systematics is done and for each one, a new
# instance of the METMakerAlg is created.
for inMuonCont, inElectronCont, inJetCont, outMETContainer, outTrackMETContainer in zip(*tmpInOut) :

    systSuffixName = ""
    if outMETContainer.__contains__("___"): systSuffixName = outMETContainer.split("___")[1]
    nameSuffix = systSuffixName.replace("_","")

    metAlgName = "HWWMETMakerAlg"+nameSuffix
    inMETMap  = hWWCommon.MET.inMap
    inMETCore = hWWCommon.MET.inCore

    hWW_msg.debug("Building METMakerAlg with name %s:" % metAlgName)
    hWW_msg.debug("    inMuonCont           = %s" % inMuonCont)
    hWW_msg.debug("    inElectronCont       = %s" % inElectronCont)
    hWW_msg.debug("    inJetCont            = %s" % inJetCont)
    hWW_msg.debug("    inMETMapName         = %s" % inMETMap)
    hWW_msg.debug("    inMETCore            = %s" % inMETCore)
    hWW_msg.debug("    outMETContainer      = %s" % outMETContainer)
    hWW_msg.debug("    outTrackMETContainer = %s" % outTrackMETContainer)

    hWWCommonSeq += CfgMgr.HWW__METMakerAlg( metAlgName,
                                             METMakerTool         = ToolSvc.METMaker,
                                             METSignificanceTool  = ToolSvc.METSignificance,
                                             InputMETMap          = inMETMap,
                                             InputMETCore         = inMETCore,
                                             InputJets            = inJetCont,
                                             InputMuons           = inMuonCont,
                                             InputElectrons       = inElectronCont,
                                             InputPhotons         = "",
                                             InputTaus            = "",
                                             DoMuonJetAssociation = True,
                                             OutputTrackMET       = outTrackMETContainer,
                                             OutputMET            = outMETContainer
                                             )
    pass


# # ====================================================================
# # Also build the Tight MissingET for testing
# # ====================================================================
# otherMETList = []
# outTightMETContainer      = hWWCommon.MET.finalCont + "Tight"
# outTightTrackMETContainer = hWWCommon.MET.finalTrackCont + "Tight"
# otherMETList.append(outTightMETContainer)
# hWWCommonSeq += CfgMgr.HWW__METMakerAlg( "HWWMETMakerAlgTight",
#                                          METMakerTool         = ToolSvc.METMakerTight,
#                                          InputMETMap          = hWWCommon.MET.inMap,
#                                          InputMETCore         = hWWCommon.MET.inCore,
#                                          InputJets            = hWWCommon.Jets.calibCont,
#                                          InputMuons           = hWWCommon.Muons.calibPreSelCont,
#                                          InputElectrons       = hWWCommon.Electrons.calibPreSelCont,
#                                          InputPhotons         = "",
#                                          InputTaus            = "",
#                                          DoMuonJetAssociation = True,
#                                          OutputMET            = outTightMETContainer
#                                          )



# ====================================================================
# Do the systematic variations of the missingET soft terms
# ====================================================================

# Create an instance of the missingET systematics tool for soft term systematics
ToolSvc += CfgMgr.met__METSystematicsTool("HWWMetSystematicsTool",
                                          OutputLevel        = WARNING,
                                          #ConfigPrefix       = hWWCommon.MET.configPrefix, # Default is fine
                                          ConfigJetTrkFile   = hWWCommon.MET.configJetTrkFile,
                                          #ConfigSoftCaloFile = hWWCommon.MET.configSoftCaloFile,
                                          ConfigSoftTrkFile  = hWWCommon.MET.configSoftTrkFile
                                          #JetColl            = hWWCommon.Jets.calibCont
                                          )
hWWCommonSeq += CfgMgr.HWW__METCalibrationSmearingAlg("HWWMETSoftTermUncertaintiesAlg",
                                                      #OutputLevel             = VERBOSE,
                                                      METSystematicsTool      = ToolSvc.HWWMetSystematicsTool,
                                                      InputContainer          = hWWCommon.MET.finalCont,
                                                      InputMETMap             = hWWCommon.MET.inMap,
                                                      OutputMETFinalName      = hWWCommon.MET.inObject,
                                                      METSystematicVariations = hWWCommon.MET.p4TSTSysts+hWWCommon.MET.p4CSTSysts
                                                      )
# Add the relevant systematics
hWWCommonSeq += CfgMgr.HWW__METCalibrationSmearingAlg("HWWTrackMETSoftTermUncertaintiesAlg",
                                                      #OutputLevel             = VERBOSE,
                                                      METSystematicsTool      = ToolSvc.HWWMetSystematicsTool,
                                                      InputContainer          = hWWCommon.MET.finalTrackCont,
                                                      InputMETMap             = hWWCommon.MET.inMap,
                                                      OutputMETFinalName      = hWWCommon.MET.inObject,
                                                      METSystematicVariations = hWWCommon.MET.p4TSTSysts+hWWCommon.MET.p4CSTSysts+hWWCommon.MET.p4JetTrkSysts
                                                      #METSystematicVariations = hWWCommon.MET.p4Systs
                                                      )


# ====================================================================
# Remove all non-final terms from the MET containers to keep their sizes small
# ====================================================================
# Get the names of all input containers
tmpInOut = HWWSysTracker.containers( [ (hWWCommon.MET.finalCont,['','electron','muon','jet','fatjet']),
                                       (hWWCommon.MET.finalTrackCont,['','electron','muon','jet','fatjet'])
                                       ] )
# Turn tmpInOut into one flat list (instead of a list of lists)
metContainerNameList = [item for sublist in tmpInOut for item in sublist]
# metContainerNameList.extend(otherMETList)
for metContainer in metContainerNameList:
    metAlgName = "HWWMETReducerAlg"+(metContainer.replace("_",""))
    hWW_msg.debug("Building METReducerAlg with name %s:" % metAlgName)
    hWW_msg.debug("    METContainer = %s" % metContainer)
    hWWCommonSeq += CfgMgr.HWW__METReducerAlg( metAlgName, METContainer = metContainer )
    pass
