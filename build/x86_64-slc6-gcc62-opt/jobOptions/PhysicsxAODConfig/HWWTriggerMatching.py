# ====================================================================
# Here we do the trigger matching on the muon and electron objects
# ====================================================================


# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWTriggerMatching.py")



# ====================================================================
# Create an instance of the HWWTriggerTool and configure it
# ====================================================================
ToolSvc += CfgMgr.HWW__TriggerTool( "HWWTriggerMatchingTool",
                                    # OutputLevel       = DEBUG,
                                    VarPrefix         = hWWCommon.Trigger.triggerMatchPrefix,
                                    MuonMatchList     = hWWCommon.Trigger.muonTriggerList,
                                    ElectronMatchList = hWWCommon.Trigger.electronTriggerList,
                                    ElMuMatchList     = hWWCommon.Trigger.electronMuonTriggerList
                                    )


# ====================================================================
# Create an instance of the HWWTriggerAlg, which executes the trigger matching using HWWTriggerTool
# ====================================================================
hWWCommonEffiScaleFactorSeq += CfgMgr.HWW__TriggerAlg( "HWWTriggerMatchingAlg",
                                                #OutputLevel          = DEBUG,
                                                TrigTool             = ToolSvc.HWWTriggerMatchingTool,
                                                Muons                = hWWCommon.Muons.finalCont,
                                                Electrons            = hWWCommon.Electrons.finalCont,
                                                PerformMuonMatch     = True,
                                                PerformElectronMatch = True,
                                                PerformElMuMatch     = True
                                                )
