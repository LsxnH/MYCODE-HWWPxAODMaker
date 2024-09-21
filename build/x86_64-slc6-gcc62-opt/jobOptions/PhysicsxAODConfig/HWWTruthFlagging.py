# ====================================================================
# Here, we will run all needed truth-flagging and calculations.
# This means, here, we crawl throuh the truth record, do some
# calculations and determine some quantities from it, and attach the
# results to the xAOD::EventInfo.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWTruthFlagging.py")


# Print a status message
hWW_msg.info("Running truth flagging calculations")



# ====================================================================
# Decorate the xAOD::EventInfo object with some MCTruth-based quantities
# ====================================================================
# Sherpa needs some special treatment
isFromSherpa = True
isNNLOPS = False
try:
    generator = af.fileinfos['metadata']['/TagInfo']['generators']
    hWW_msg.info("Generator name: %s" % generator)
    if "Powheg" in generator or "MadGraph" in generator or "McAtNlo" in generator: isFromSherpa = False
except:
    try:
        hWW_msg.info("Trying to infer generator type from MC channel number...")
        mcChannelNumber = af.mc_channel_numbers[0]
        if mcChannelNumber in [410009]: isFromSherpa = False
        if mcChannelNumber in range(361700,361899): isFromSherpa = False
        if mcChannelNumber in range(361100,361110): isFromSherpa = False
        if mcChannelNumber in range(363600,363671): isFromSherpa = False
        if mcChannelNumber in range(363123,363170): isFromSherpa = False
        if mcChannelNumber in range(363725,363748): isFromSherpa = False
        if mcChannelNumber in range(361500,361534): isFromSherpa = False
        if mcChannelNumber in range(361628,361642): isFromSherpa = False
    except:
        hWW_msg.warning("THIS SAMPLE DOES NOT HAVE METADATA INFO .... asusming SHERPA!!!")
        pass
    pass
try:
    mcChannelNumber = af.mc_channel_numbers[0]
    if mcChannelNumber in [345324]: isNNLOPS = True
except:
    hWW_msg.warning("THIS SAMPLE DOES NOT HAVE METADATA INFO .... asusming no NNLOPS!!!")
    pass

ToolSvc += CfgMgr.TruthWeightTools__HiggsWeightTool( "HWWHiggsWeightTool",
                                                     OutputLevel = VERBOSE,
                                                     RequireFinite = True,
                                                     WeightCutOff = 100.0,
                                                     ForceNNLOPS = True,
                                                     #ForceVBF = False,
                                                     #ForceVH = False
                                                     )

hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__TruthAlg("HWWTruthFlaggingAlg",
                                              #OutputLevel = VERBOSE,
                                              TruthInputContainer      = "TruthEvents",
                                              TruthJetInputContainer   = "AntiKt4TruthJets",
                                              TruthWZJetInputContainer = "AntiKt4TruthWZJets",
                                              TruthMetInputContainer   = "MET_Truth",
                                              TruthElectronInputContainer   = "TruthElectrons",
                                              TruthMuonInputContainer   = "TruthMuons",
                                              IsSherpa                 = isFromSherpa,
                                              IsNNLOPS                 = isNNLOPS,
                                              HiggsWeightTool          = ToolSvc.HWWHiggsWeightTool
                                              )
