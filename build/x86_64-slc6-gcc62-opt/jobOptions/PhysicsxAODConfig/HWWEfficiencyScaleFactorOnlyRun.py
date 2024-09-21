# ====================================================================
# This is a fragment that schedules to run ONLY the efficiency and
# scale-factor calculations and write out a new file with the results
# attached. The output stream name will be the same as the input stream
# name.
# ====================================================================

# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("PhysicsxAODConfig/HWWEfficiencyScaleFactorOnlyRun.py")


# Print a status message
hWW_msg.info("Running ONLY the efficiency and scale-factor calculations")



# ====================================================================
# Switch off everything that is not needed.
# ====================================================================

# First, the output streams
hWWCommon.Global.do1Lep    = False
hWWCommon.Global.do2Lep    = False
hWWCommon.Global.do3Lep    = False
hWWCommon.Global.do4Lep    = False
hWWCommon.Global.doFakeLep = False

# Now, the individual configruations
hWWCommon.Global.doPileupReweighting    = True
hWWCommon.Global.doEventPreSelection    = False
hWWCommon.Global.doTruthFlagging        = False
hWWCommon.Global.doCalibrations         = False
hWWCommon.Global.doSelections           = False
hWWCommon.Global.doOverlapRemoval       = False
hWWCommon.Global.doCandidateBuilding    = False
hWWCommon.Global.doFilterEffiSFSeq      = False
hWWCommon.Global.doTriggerSelection     = False
hWWCommon.Global.doTriggerMatching      = False
hWWCommon.Global.doThinning             = False
hWWCommon.Global.doP4Systematics        = False



# ====================================================================
# Include the common configuration
# Note that this will only be included if it was NOT included before
# due to the include.block(...) statement in that file.
# ====================================================================
include("PhysicsxAODConfig/HWWAnalysisCommon.py")



# ====================================================================
# Create the new output stream and name it exactly the same as the input
# Copy over all items fron the input file to the output file, both event data
# and meta data. This should include the new efficiencies and scale-factors.
# ==============================================================================

# First, get the name of the input stream
inputStreamName = af.fileinfos["stream_names"][0]
hWW_msg.info("Extracted input stream name: %s" % inputStreamName)
inputStreamName = vars().get('OUTSTREAMNAME', "PAOD")
hWW_msg.info("Using output stream name: %s" % inputStreamName)

# Now, actually create the new output stream/file and copy everything over
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
outStreamWithEff = MSMgr.NewPoolRootStream( inputStreamName, inputStreamName+"_WithEffSF.merge.pool.root" )
outStreamWithEff.GetEventStream().TakeItemsFromInput = True
outStreamWithEff.GetMetaDataStream().TakeItemsFromInput = True


# # Create a new mini-xAOD output stream object
# from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
# outStreamWithEff = MSMgr.NewPoolRootStream( hWWlnulnu.Global.StreamName, hWWlnulnu.Global.FileName )
#
# # Filter the events
# # All events that are accepted by any algorithm in the AcceptAlgs list will be written out
# if hWWlnulnu.Global.doSkimming :
#     hWW_msg.info( "Applying an event selection based on these accept algorithms: %s" % hWWlnulnu.Global.acceptAlgList )
#     outStreamWithEff.AcceptAlgs( hWWlnulnu.Global.acceptAlgList )
#     pass
# # We always filter based on the listed require algs. These are, e.g.,
# # the GRL filter, trigger fitler, vertex filter,...
# hWW_msg.info( "Applying an event selection based on these requite algorithms: %s" % hWWCommon.Global.requireAlgList )
# outStreamWithEff.RequireAlgs( hWWCommon.Global.requireAlgList )
#
# # Use our common container item list to define the per-event content of the mini-xAOD
# from HWWlnulnuxAODConfig.HWWlnulnuPAODContent import pAODContent, pAODMetaDataContent
# outStreamWithEff.AddItem( pAODContent() )
# outStreamWithEff.AddMetaDataItem( pAODMetaDataContent() )
#
# # Remove the old-style EventInfo object. This should really go into our derivation
# if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
#     outStreamWithEff.RemoveItem('EventInfo#*')
#     outStreamWithEff.AddItem( ['EventInfo#HWWEventInfo'])
#     pass
#
# # Print the final item list to the log file
# if hWW_msg.isEnabledFor(hWWlnulnu_msg.mapLevelGaudiToLogging(DEBUG)):
#     hWW_msg.debug( "OutputStream info:")
#     outStreamWithEff.Print()
#     pass
