# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("HWWFakeFactorxAOD/HWWFakeFactorCommon.py")

# Import the module that allows to use named units, e.g. GeV
from AthenaCommon.SystemOfUnits import *

# Import the steering flags for the common analysis
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon

# Import the steering flags for this analysis
from HWWFakeFactorxAOD.HWWFakeFactorFlags import hWWFakes

# for messaging
from AthenaCommon.Logging import logging
hWWFakes_msg = logging.getLogger( 'HWWFakeFactor' )
hWWFakes_msg.setLevel(hWWCommon.Global.logLevel)


# ====================================================================
# Include the common configuration
# Note that this will only be included if it was NOT included before
# due to the include.block(...) statement in that file.
# ====================================================================
include("PhysicsxAODConfig/HWWAnalysisCommon.py")



# ====================================================================
# Do the final event candidate building
# ====================================================================
include("HWWFakeFactorxAOD/HWWFakeLeptonEventCandidateBuilding.py")



# ====================================================================
# Do the thinning of the underlying objects (TrackParticles,Truth,CaloClusters,...)
# ====================================================================
# if hWWFakes.Global.writeLeptonTrackParticles:
#     include("HWWlnulnuxAODConfig/HWWlnulnuThinning.py")
#     pass



# ====================================================================
# Here, we create our output mini-xAOD file and configure what should go into it
# ====================================================================
if hWWFakes.Global.writeMinixAOD:
    # Create a new mini-xAOD output stream object
    from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
    HWWFakesOutStream = MSMgr.NewPoolRootStream( hWWFakes.Global.StreamName, hWWFakes.Global.FileName )

    # Filter the events
    # All events that are accepted by any algorithm in the AcceptAlgs list will be written out
    if hWWFakes.Global.doSkimming :
        hWWFakes_msg.info( "Applying an event selection based on these accept algorithms: %s" % hWWFakes.Global.acceptAlgList )
        HWWFakesOutStream.AcceptAlgs( hWWFakes.Global.acceptAlgList )
        pass
    # We always filter based on the listed require algs. These are, e.g.,
    # the GRL filter, trigger filter, vertex filter,...
    hWWFakes_msg.info( "Applying an event selection based on these requite algorithms: %s" % hWWCommon.Global.requireAlgList )
    HWWFakesOutStream.RequireAlgs( hWWCommon.Global.requireAlgList )

    # Use our common container item list to define the per-event content of the mini-xAOD
    from HWWFakeFactorxAOD.HWWFakeFactorPAODContent import pAODContent, pAODMetaDataContent
    HWWFakesOutStream.AddItem( pAODContent() )
    HWWFakesOutStream.AddMetaDataItem( pAODMetaDataContent() )

    # Remove the old-style EventInfo object. This should really go into our derivation
    # if objKeyStore.isInInputFile('PileUpEventInfo', 'McEventInfo') :
    if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
        HWWFakesOutStream.RemoveItem('EventInfo#*')
        HWWFakesOutStream.AddItem( ['EventInfo#HWWEventInfo'])
        pass

    # Print the final item list to the log file
    if hWWFakes_msg.isEnabledFor(hWWFakes_msg.mapLevelGaudiToLogging(DEBUG)):
        hWWFakes_msg.debug( "OutputStream info:")
        HWWFakesOutStream.Print()
        pass
    pass
