# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("HWWVHxAOD/VHAnalysisCommon.py")

# Import the module that allows to use named units, e.g. GeV
#from AthenaCommon.SystemOfUnits import *

# Import the steering flags for the common analysis
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon

# for messaging
from AthenaCommon.Logging import logging
hWWVH_msg = logging.getLogger( 'HWWVHAnalysis' )
hWWVH_msg.setLevel(hWWCommon.Global.logLevel)
# hWWVH_msg.setLevel(1) # DEBUG=1

# Import the steering flags for this analysis
import HWWVHxAOD.WHFlags as wh_flags
import HWWVHxAOD.ZHFlags as zh_flags


# ====================================================================
# Include the common configuration
# Note that this will only be included if it was NOT included before
# due to the include.block(...) statement in that file.
# ====================================================================
include("PhysicsxAODConfig/HWWAnalysisCommon.py")


finalStates = []
if hWWCommon.Global.do3Lep: finalStates.append(3)
if hWWCommon.Global.do4Lep: finalStates.append(4)

wh_flags.Global.writeMinixAOD = vars().get('writePAOD_WH')
zh_flags.Global.writeMinixAOD = vars().get('writePAOD_ZH')


for nLeptons in finalStates:
    if nLeptons == 3: vh_flags = wh_flags
    elif nLeptons == 4: vh_flags = zh_flags
    hWWVH_msg.info( "Using nLeptons=%s" % nLeptons )
    hWWVH_msg.info( "Using StreamName=%s" % vh_flags.Global.StreamName )

    if hWWCommon.Global.processReco:
        # Include the event candidate building
        include("HWWVHxAOD/VHCandidateBuilding.py")

    if hWWCommon.Global.processTruth:
        # Include the truth event candidate building
        include("HWWVHxAOD/VHTruthCandidateBuilding.py")

    # ====================================================================
    # Do the thinning of the underlying objects (TrackParticles,Truth,CaloClusters,...)
    # ====================================================================
    #if vh_flags.Global.writeLeptonTrackParticles:
    #    include("HWWlnulnuxAODConfig/HWWlnulnuThinning.py")

    # ====================================================================
    # Here, we create our output mini-xAOD file and configure what should go into it
    # ====================================================================
    if vh_flags.Global.writeMinixAOD:
        # Create a new mini-xAOD output stream object
        from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
        HWWVHOutStream = MSMgr.NewPoolRootStream( vh_flags.Global.StreamName, vh_flags.Global.FileName )

        hWWVH_msg.info( "For the output stream %s - " % HWWVHOutStream.GetEventStream().name() )

        # Filter the events
        # All events that are accepted by any algorithm in the AcceptAlgs list will be written out
        if vh_flags.Global.doSkimming :
            hWWVH_msg.info( "Applying an event selection based on these accept algorithms: %s" % vh_flags.Global.acceptAlgList )
            HWWVHOutStream.AcceptAlgs( vh_flags.Global.acceptAlgList )
            pass
        # We always filter based on the listed require algs. These are, e.g.,
        # the GRL filter, trigger fitler, vertex filter,...
        hWWVH_msg.info( "Applying an event selection based on these require algorithms: %s" % hWWCommon.Global.requireAlgList )
        # HWWVHOutStream.RequireAlgs(list(set(vh_flags.Global.requireAlgList + hWWCommon.Global.requireAlgList)))
        HWWVHOutStream.RequireAlgs( hWWCommon.Global.requireAlgList )

        # Use our common container item list to define the per-event content of the mini-xAOD
        #from HWWVHxAOD.mini_xAOD_content import minixAODContent, minixAODMetaDataContent
        import HWWVHxAOD.VHMinixAODContent as mxc
        if nLeptons == 3:
            HWWVHOutStream.AddItem( mxc.pAODWHContent() )
        elif nLeptons == 4:
            HWWVHOutStream.AddItem( mxc.pAODZHContent() )
        HWWVHOutStream.AddMetaDataItem( mxc.pAODMetaDataContent() )

        # Remove the old-style EventInfo object. This should really go into our derivation
        # if objKeyStore.isInInputFile('PileUpEventInfo', 'McEventInfo') :
        if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
            HWWVHOutStream.RemoveItem('EventInfo#*')
            HWWVHOutStream.AddItem(['EventInfo#HWWEventInfo'])

        # Print the final item list to the log file
        if hWWVH_msg.isEnabledFor(hWWVH_msg.mapLevelGaudiToLogging(DEBUG)):
            hWWVH_msg.debug( "OutputStream info:" )
            HWWVHOutStream.Print()
            pass
