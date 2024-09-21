# ====================================================================
# Here, we will run all event pre-selections.
# This includes things like requireing that we find at least one
# primary vertex in the event, pre-selecting events based on an OR
# of trigger decisions, GRL selection (if requested), etc.
# If we run this, this also means that all subsequent algorithms will
# only run, if an event passes all of these pre-selections. This is
# in part intended to speed up the job (as some algorithms take a long
# time to run), as well to actually allow some to run and not crash
# (as for example, some require that there is a primary vertex in the
# event).
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWEventPreSelection.py")


# Print a status message
hWW_msg.info("Running event pre-selections")


# ====================================================================
# Do the heavy flavor sample overlap removal for Alpgen samples
# ====================================================================
hWWCommonPreFilterSeq += CfgMgr.HFORSelectionAlg( "HWWHFORSelectionAlg" )
hWWCommon.Global.requireAlgList.append("HWWHFORSelectionAlg")


# ====================================================================
# Only add the GoodRunsList selection if we run on data, but NOT for Monte Carlo:
# ====================================================================
if vars().has_key('doGRLSelection'): hWWCommon.Global.doGRLSelection = doGRLSelection
hWW_msg.info( "The user requested to use hWWCommon.Global.doGRLSelection = %s" % hWWCommon.Global.doGRLSelection )
if not hWWCommon.Global.inputIsSimulation and hWWCommon.Global.doGRLSelection :
    # /afs/cern.ch/user/a/atlasdqm/www/Atlas/GROUPS/DATAPREPARATION/InteractionsperCrossing
    # http://atlasdqm.web.cern.ch/atlasdqm/grlgen/All_Good/

    hWWCommonPreFilterSeq += CfgMgr.HWW__GoodRunsListSelectionAlg( "HWWGoodRunsListSelectionAlg",
                                                                   #OutputLevel       = VERBOSE,
                                                                   GoodRunsListVec = hWWCommon.Global.grlFileList
                                                                   )
    hWWCommon.Global.requireAlgList.append("HWWGoodRunsListSelectionAlg")
    pass


# ====================================================================
# Veto data event with a bad event quality
# ====================================================================
hWWCommonPreFilterSeq += CfgMgr.EventQualityFilterAlg( "HWWEventQualityFilter" )
hWWCommon.Global.requireAlgList.append("HWWEventQualityFilter")


# ====================================================================
# Release 21 Jet Event Cleaning
# ====================================================================
hWWCommonPreFilterSeq += CfgMgr.HWW__JetEventCleaningAlg("HWWJetEventCleaningAlg")
hWWCommon.Global.requireAlgList.append("HWWJetEventCleaningAlg")


# ====================================================================
# Veto events without a good primary vertex
# ====================================================================
hWWCommonPreFilterSeq += CfgMgr.HWW__PrimaryVertexFilterAlg("HWWPrimaryVertexFilterAlg", OutputLevel = WARNING)
hWWCommon.Global.requireAlgList.append("HWWPrimaryVertexFilterAlg")


# ====================================================================
# Trigger selection
# ====================================================================
if hWWCommon.Global.doTriggerSelection :
    # Set up the needed tools
    ToolSvc += CfgMgr.TrigConf__xAODConfigTool("TrigConfig", OutputLevel = WARNING)
    ToolSvc += CfgMgr.Trig__TrigDecisionTool("TrigDecisionTool",
                                             OutputLevel     = WARNING,
                                             ConfigTool      = ToolSvc.TrigConfig,
                                             TrigDecisionKey = "xTrigDecision" )
    # And use them in the algorithm to select the event based on an OR of all given trigger names.
    # Also, decorate the EventInfo object with the pass/fail results for every trigger.
    hWWCommonPreFilterSeq += CfgMgr.TriggerSelectionAlg("HWWTriggerAlg",
                                                        TrigDecisionTool = ToolSvc.TrigDecisionTool,
                                                        TriggerList      = hWWCommon.Trigger.allTriggerList,
                                                        VarNamePrefix    = hWWCommon.Trigger.triggerPassPrefix
                                                        )
    hWWCommon.Global.requireAlgList.append("HWWTriggerAlg")
    pass

# ====================================================================
# Decorate the xAOD::EventInfo object
# ====================================================================
hWWCommonPreFilterSeq += CfgMgr.HWW__EventInfoDecorationAlg("HWWEventInfoDecorationAlg")



# ====================================================================
# Temporary fix: Get the old-style EventInfo object and write out
# only the essentials, i.e., remove the information regarding the
# pileup sub-events.
# ====================================================================
if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
    hWW_msg.info("Attempting to reduce the old-style EventInfo object")
    hWWCommonPreFilterSeq += CfgMgr.ReducePileUpEventInfoAlg("HWWEventInfoReducer",
                                                             #OutputLevel          = VERBOSE,
                                                             ReducedEventInfoName = "HWWEventInfo" )
    pass
