# ====================================================================
# block that this file is included twice
# ====================================================================
include.block("HWWlnulnuxAODConfig/HWWlnulnuAnalysisCommon.py")

# Import the module that allows to use named units, e.g. GeV
from AthenaCommon.SystemOfUnits import *

# Import the steering flags for the common analysis
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon

# Import the steering flags for this analysis
from HWWlnulnuxAODConfig.HWWlnulnuAnalysisFlags import hWWlnulnu

# for messaging
from AthenaCommon.Logging import logging
hWWlnulnu_msg = logging.getLogger( 'HWWlnulnuAnalysis' )
hWWlnulnu_msg.setLevel(hWWCommon.Global.logLevel)


# ====================================================================
# Include the common configuration
# Note that this will only be included if it was NOT included before
# due to the include.block(...) statement in that file.
# ====================================================================
include("PhysicsxAODConfig/HWWAnalysisCommon.py")



# ====================================================================
# Do the final event candidate building
# ====================================================================
if hWWCommon.Global.processReco:
    include("HWWlnulnuxAODConfig/HWWlnulnuEventCandidateBuilding.py")

# ====================================================================
# Do the final truth event candidate building
# ====================================================================
if hWWCommon.Global.processTruth:
    include("HWWlnulnuxAODConfig/HWWlnulnuTruthEventCandidateBuilding.py")



# # ====================================================================
# # Write the PxAODs with a third lepton out, if doFakeZJets == True
# # Turn the others OFF (for now)
# # ====================================================================
# if hWWCommon.Global.doFakeZJets:
#     hWWlnulnu.Global.write2LFakePxAOD          = True
#     hWWlnulnu.Global.writeZFakePxAOD           = True
#     hWWlnulnu.Global.writeTopFakePxAOD         = True
#     hWWlnulnu.Global.writeMinixAOD             = True # For testing how this affects overlap removal and MET building
#     hWWlnulnu.Global.writeDifferentFlavorPxAOD = True # For testing how this affects overlap removal and MET building
#     hWWlnulnu.Global.writeDiJetPxAOD           = False
#     hWWlnulnu.Global.writeDiJetDFPxAOD         = False
#     pass


# ====================================================================
# Get which files to write out from the variables provided in running command
# ====================================================================
hWWlnulnu.Global.writeMinixAOD             = vars().get('writePAOD_2L')
hWWlnulnu.Global.writeDifferentFlavorPxAOD = vars().get('writePAOD_2LDF')
hWWlnulnu.Global.writeDiJetPxAOD           = vars().get('writePAOD_2LJJ')
hWWlnulnu.Global.writeDiJetDFPxAOD         = vars().get('writePAOD_2LJJDF')
hWWlnulnu.Global.write2LFakePxAOD          = vars().get('writePAOD_2LFake')
hWWlnulnu.Global.writeZFakePxAOD           = vars().get('writePAOD_2LZFake')
hWWlnulnu.Global.writeTopFakePxAOD         = vars().get('writePAOD_2LTopFake')





# ====================================================================
# Here, we create our output mini-xAOD file and configure what should go into it
# ====================================================================
if hWWlnulnu.Global.writeMinixAOD:
    # Create a new mini-xAOD output stream object
    from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
    HWWlnulnuOutStream = MSMgr.NewPoolRootStream( hWWlnulnu.Global.StreamName, hWWlnulnu.Global.FileName )

    hWWlnulnu_msg.info( "For the output stream %s - " % HWWlnulnuOutStream.GetEventStream().name() )

    # Filter the events
    # All events that are accepted by any algorithm in the AcceptAlgs list will be written out
    if hWWlnulnu.Global.doSkimming :
        hWWlnulnu_msg.info( "Applying an event selection based on these accept algorithms: %s" % hWWlnulnu.Global.acceptAlgList )
        HWWlnulnuOutStream.AcceptAlgs( hWWlnulnu.Global.acceptAlgList )
        pass
    # We always filter based on the listed require algs. These are, e.g.,
    # the GRL filter, trigger fitler, vertex filter,...
    hWWlnulnu_msg.info( "Applying an event selection based on these require algorithms: %s" % hWWCommon.Global.requireAlgList )
    HWWlnulnuOutStream.RequireAlgs( hWWCommon.Global.requireAlgList )

    # Use our common container item list to define the per-event content of the mini-xAOD
    from HWWlnulnuxAODConfig.HWWlnulnuPAODContent import pAODContent, pAODMetaDataContent
    HWWlnulnuOutStream.AddItem( pAODContent() )
    HWWlnulnuOutStream.AddMetaDataItem( pAODMetaDataContent() )

    # Remove the old-style EventInfo object. This should really go into our derivation
    # if objKeyStore.isInInputFile('PileUpEventInfo', 'McEventInfo') :
    if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
        HWWlnulnuOutStream.RemoveItem('EventInfo#*')
        HWWlnulnuOutStream.AddItem( ['EventInfo#HWWEventInfo'])
        pass

    # Print the final item list to the log file
    if hWWlnulnu_msg.isEnabledFor(hWWlnulnu_msg.mapLevelGaudiToLogging(DEBUG)):
        hWWlnulnu_msg.debug( "OutputStream info:")
        HWWlnulnuOutStream.Print()
        pass
    pass



# ====================================================================
# Here, we create our output mini-xAOD file and configure what should go into it.
# This one will only contain events with at least one valid different-flavor candidate.
# ====================================================================
if hWWlnulnu.Global.writeDifferentFlavorPxAOD:
    # Create a new mini-xAOD output stream object
    from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
    HWWlnulnuDFOutStream = MSMgr.NewPoolRootStream( hWWlnulnu.Global.DFStreamName, hWWlnulnu.Global.DFFileName )

    hWWlnulnu_msg.info( "For the output stream %s - " % HWWlnulnuDFOutStream.GetEventStream().name() )

    # Filter the events
    # All events that are accepted by any algorithm in the AcceptAlgs list will be written out
    if hWWlnulnu.Global.doSkimming :
        dfAcceptAlgList = []
        for algName in hWWlnulnu.Global.acceptAlgList:
            if hWWCommon.Global.processReco:
                if algName.__contains__("HWWElElFullEventExistsAlg") or algName.__contains__("HWWMuMuFullEventExistsAlg"): continue
                pass
            if hWWCommon.Global.processTruth:
                if algName.__contains__("HWWElElFullTruthEventExistsAlg") or algName.__contains__("HWWMuMuFullTruthEventExistsAlg"): continue
                pass
            dfAcceptAlgList.append(algName)
            pass
        hWWlnulnu_msg.info( "Applying an event selection based on these accept algorithms: %s" % dfAcceptAlgList )
        HWWlnulnuDFOutStream.AcceptAlgs( dfAcceptAlgList )
        pass
    # We always filter based on the listed require algs. These are, e.g.,
    # the GRL filter, trigger fitler, vertex filter,...
    # TODO: this needs to change for the Truth/Reco combination running
    hWWlnulnu_msg.info( "Applying an event selection based on these require algorithms: %s" % hWWCommon.Global.requireAlgList )
    HWWlnulnuDFOutStream.RequireAlgs( hWWCommon.Global.requireAlgList )

    # Use our common container item list to define the per-event content of the mini-xAOD
    from HWWlnulnuxAODConfig.HWWlnulnuPAODContent import pAODContent, pAODMetaDataContent
    for pAODItem in pAODContent():
        # Don't add the same-flavor event objects to this different-flavor output file
        if hWWCommon.Global.processReco:
            if pAODItem.__contains__(hWWlnulnu.Event.eeEvent ) or pAODItem.__contains__(hWWlnulnu.Event.mmEvent): continue
        if hWWCommon.Global.processTruth:
            if pAODItem.__contains__(hWWlnulnu.TruthEvent.eeEvent ) or pAODItem.__contains__(hWWlnulnu.TruthEvent.mmEvent): continue
        HWWlnulnuDFOutStream.AddItem( [pAODItem] )
    HWWlnulnuDFOutStream.AddMetaDataItem( pAODMetaDataContent() )

    # Remove the old-style EventInfo object. This should really go into our derivation
    # if objKeyStore.isInInputFile('PileUpEventInfo', 'McEventInfo') :
    if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
        HWWlnulnuDFOutStream.RemoveItem('EventInfo#*')
        HWWlnulnuDFOutStream.AddItem( ['EventInfo#HWWEventInfo'])
        pass

    # Print the final item list to the log file
    if hWWlnulnu_msg.isEnabledFor(hWWlnulnu_msg.mapLevelGaudiToLogging(DEBUG)):
        hWWlnulnu_msg.debug( "OutputStream info:")
        HWWlnulnuDFOutStream.Print()
        pass
    pass




# ====================================================================
# If one of the di-jet PxAODs is being written out, run the event filters
# ====================================================================
if hWWlnulnu.Global.writeDiJetPxAOD or hWWlnulnu.Global.writeDiJetDFPxAOD:
    hWWEventCandSeq += CfgMgr.HWW__EventSelectionAlg("HWWDiJetSFEventSelectionAlg",
                            InputContainerList = [hWWlnulnu.Event.eeEvent, hWWlnulnu.Event.mmEvent],
                            MinNJets           = 2
                            )
    hWWEventCandSeq += CfgMgr.HWW__EventSelectionAlg("HWWDiJetDFEventSelectionAlg",
                            InputContainerList = [hWWlnulnu.Event.emEvent, hWWlnulnu.Event.meEvent],
                            MinNJets           = 2
                            )
    pass

# ====================================================================
# Here, we create our output mini-xAOD file and configure what should go into it.
# This one will only contain events with at least two jets
# ====================================================================
if hWWlnulnu.Global.writeDiJetPxAOD:
    # Create a new mini-xAOD output stream object
    from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
    HWWlnulnuDiJetOutStream = MSMgr.NewPoolRootStream( hWWlnulnu.Global.DiJetStreamName, hWWlnulnu.Global.DiJetFileName )

    hWWlnulnu_msg.info( "For the output stream %s - " % HWWlnulnuDiJetOutStream.GetEventStream().name() )

    # Filter the events
    if hWWlnulnu.Global.doSkimming :
        hWWlnulnu_msg.info( "Applying an event selection based on these accept algorithms: HWWDiJetSFEventSelectionAlg or HWWDiJetDFEventSelectionAlg" )
        HWWlnulnuDiJetOutStream.AcceptAlgs( ["HWWDiJetSFEventSelectionAlg","HWWDiJetDFEventSelectionAlg"] )
        pass
    # We always filter based on the listed require algs. These are, e.g.,
    # the GRL filter, trigger fitler, vertex filter,...
    hWWlnulnu_msg.info( "Applying an event selection based on these require algorithms: %s" % hWWCommon.Global.requireAlgList )
    HWWlnulnuDiJetOutStream.RequireAlgs( hWWCommon.Global.requireAlgList )

    # Use our common container item list to define the per-event content of the mini-xAOD
    from HWWlnulnuxAODConfig.HWWlnulnuPAODContent import pAODContent, pAODMetaDataContent
    HWWlnulnuDiJetOutStream.AddItem( pAODContent() )
    HWWlnulnuDiJetOutStream.AddMetaDataItem( pAODMetaDataContent() )

    # Remove the old-style EventInfo object. This should really go into our derivation
    # if objKeyStore.isInInputFile('PileUpEventInfo', 'McEventInfo') :
    if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
        HWWlnulnuDiJetOutStream.RemoveItem('EventInfo#*')
        HWWlnulnuDiJetOutStream.AddItem( ['EventInfo#HWWEventInfo'])
        pass

    # Print the final item list to the log file
    if hWWlnulnu_msg.isEnabledFor(hWWlnulnu_msg.mapLevelGaudiToLogging(DEBUG)):
        hWWlnulnu_msg.debug( "OutputStream info:")
        HWWlnulnuDiJetOutStream.Print()
        pass
    pass




# ====================================================================
# Here, we create our output mini-xAOD file and configure what should go into it.
# This one will only contain events with at least two jets and different-flavor leptons
# ====================================================================
if hWWlnulnu.Global.writeDiJetDFPxAOD:
    # Create a new mini-xAOD output stream object
    from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
    HWWlnulnuDiJetDFOutStream = MSMgr.NewPoolRootStream( hWWlnulnu.Global.DiJetDFStreamName, hWWlnulnu.Global.DiJetDFFileName )

    hWWlnulnu_msg.info( "For the output stream %s - " % HWWlnulnuDiJetDFOutStream.GetEventStream().name() )

    # Filter the events
    if hWWlnulnu.Global.doSkimming :
        hWWlnulnu_msg.info( "Applying an event selection based on these accept algorithms: HWWDiJetDFEventSelectionAlg" )
        HWWlnulnuDiJetDFOutStream.AcceptAlgs( ["HWWDiJetDFEventSelectionAlg"] )
        pass
    # We always filter based on the listed require algs. These are, e.g.,
    # the GRL filter, trigger fitler, vertex filter,...
    hWWlnulnu_msg.info( "Applying an event selection based on these require algorithms: %s" % hWWCommon.Global.requireAlgList )
    HWWlnulnuDiJetDFOutStream.RequireAlgs( hWWCommon.Global.requireAlgList )

    # Use our common container item list to define the per-event content of the mini-xAOD
    from HWWlnulnuxAODConfig.HWWlnulnuPAODContent import pAODContent, pAODMetaDataContent
    for pAODItem in pAODContent():
        # Don't add the same-flavor event objects to this different-flavor output file
        if pAODItem.__contains__(hWWlnulnu.Event.eeEvent ) or pAODItem.__contains__(hWWlnulnu.Event.mmEvent) : continue
        HWWlnulnuDiJetDFOutStream.AddItem( [pAODItem] )
    HWWlnulnuDiJetDFOutStream.AddMetaDataItem( pAODMetaDataContent() )

    # Remove the old-style EventInfo object. This should really go into our derivation
    # if objKeyStore.isInInputFile('PileUpEventInfo', 'McEventInfo') :
    if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
        HWWlnulnuDiJetDFOutStream.RemoveItem('EventInfo#*')
        HWWlnulnuDiJetDFOutStream.AddItem( ['EventInfo#HWWEventInfo'])
        pass

    # Print the final item list to the log file
    if hWWlnulnu_msg.isEnabledFor(hWWlnulnu_msg.mapLevelGaudiToLogging(DEBUG)):
        hWWlnulnu_msg.debug( "OutputStream info:")
        HWWlnulnuDiJetDFOutStream.Print()
        pass
    pass




# ====================================================================
# Here, we create our output mini-xAOD file and configure what should go into it.
# This one will only contain events with at least one valid fake candidate.
# ====================================================================
if hWWlnulnu.Global.write2LFakePxAOD:
    # Create a new mini-xAOD output stream object
    from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
    HWWlnulnuFakesOutStream = MSMgr.NewPoolRootStream( hWWlnulnu.Global.FakesStreamName, hWWlnulnu.Global.FakesFileName )

    hWWlnulnu_msg.info( "For the output stream %s - " % HWWlnulnuFakesOutStream.GetEventStream().name() )

    # Filter the events
    if hWWlnulnu.Global.doSkimming :
        hWWEventCandSeq += CfgMgr.HWW__EventSelectionAlg("HWWFakesEventSelectionAlg",
                                InputContainerList = [hWWlnulnu.Event.eeEvent, hWWlnulnu.Event.mmEvent, hWWlnulnu.Event.emEvent, hWWlnulnu.Event.meEvent],
                                MinNOtherLeptons   = 1
                                )
        hWWlnulnu_msg.info( "Applying an event selection based on these accept algorithms: HWWFakesEventSelectionAlg" )
        HWWlnulnuFakesOutStream.AcceptAlgs( ["HWWFakesEventSelectionAlg"] )
        pass
    # We always filter based on the listed require algs. These are, e.g.,
    # the GRL filter, trigger fitler, vertex filter,...
    hWWlnulnu_msg.info( "Applying an event selection based on these require algorithms: %s" % hWWCommon.Global.requireAlgList )
    HWWlnulnuFakesOutStream.RequireAlgs( hWWCommon.Global.requireAlgList )

    # Use our common container item list to define the per-event content of the mini-xAOD
    from HWWlnulnuxAODConfig.HWWlnulnuPAODContent import pAODContent, pAODMetaDataContent
    HWWlnulnuFakesOutStream.AddItem( pAODContent() )
    HWWlnulnuFakesOutStream.AddMetaDataItem( pAODMetaDataContent() )

    # Remove the old-style EventInfo object. This should really go into our derivation
    # if objKeyStore.isInInputFile('PileUpEventInfo', 'McEventInfo') :
    if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
        HWWlnulnuFakesOutStream.RemoveItem('EventInfo#*')
        HWWlnulnuFakesOutStream.AddItem( ['EventInfo#HWWEventInfo'])
        pass

    # Print the final item list to the log file
    if hWWlnulnu_msg.isEnabledFor(hWWlnulnu_msg.mapLevelGaudiToLogging(DEBUG)):
        hWWlnulnu_msg.debug( "OutputStream info:")
        HWWlnulnuFakesOutStream.Print()
        pass
    pass



# ====================================================================
# Here, we create our output mini-xAOD file and configure what should go into it.
# This one will only contain events with at least one valid Z+fake candidate.
# ====================================================================
if hWWlnulnu.Global.writeZFakePxAOD:
    # Create a new mini-xAOD output stream object
    from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
    HWWlnulnuZFakesOutStream = MSMgr.NewPoolRootStream( hWWlnulnu.Global.ZFakesStreamName, hWWlnulnu.Global.ZFakesFileName )

    hWWlnulnu_msg.info( "For the output stream %s - " % HWWlnulnuZFakesOutStream.GetEventStream().name() )

    # Filter the events
    if hWWlnulnu.Global.doSkimming :
        hWWEventCandSeq += CfgMgr.HWW__EventSelectionAlg("HWWZFakesEventSelectionAlg",
                                InputContainerList = [hWWlnulnu.Event.eeEvent, hWWlnulnu.Event.mmEvent],
                                MinNOtherLeptons   = 1
                                )
        hWWlnulnu_msg.info( "Applying an event selection based on these accept algorithms: HWWZFakesEventSelectionAlg" )
        HWWlnulnuZFakesOutStream.AcceptAlgs( ["HWWZFakesEventSelectionAlg"] )
        pass
    # We always filter based on the listed require algs. These are, e.g.,
    # the GRL filter, trigger fitler, vertex filter,...
    hWWlnulnu_msg.info( "Applying an event selection based on these require algorithms: %s" % hWWCommon.Global.requireAlgList )
    HWWlnulnuZFakesOutStream.RequireAlgs( hWWCommon.Global.requireAlgList )

    # Use our common container item list to define the per-event content of the mini-xAOD
    from HWWlnulnuxAODConfig.HWWlnulnuPAODContent import pAODContent, pAODMetaDataContent
    HWWlnulnuZFakesOutStream.AddItem( pAODContent() )
    HWWlnulnuZFakesOutStream.AddMetaDataItem( pAODMetaDataContent() )

    # Remove the old-style EventInfo object. This should really go into our derivation
    # if objKeyStore.isInInputFile('PileUpEventInfo', 'McEventInfo') :
    if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
        HWWlnulnuZFakesOutStream.RemoveItem('EventInfo#*')
        HWWlnulnuZFakesOutStream.AddItem( ['EventInfo#HWWEventInfo'])
        pass

    # Print the final item list to the log file
    if hWWlnulnu_msg.isEnabledFor(hWWlnulnu_msg.mapLevelGaudiToLogging(DEBUG)):
        hWWlnulnu_msg.debug( "OutputStream info:")
        HWWlnulnuZFakesOutStream.Print()
        pass
    pass



# ====================================================================
# Here, we create our output mini-xAOD file and configure what should go into it.
# This one will only contain events with at least one valid ttbar+fake candidate.
# ====================================================================
if hWWlnulnu.Global.writeTopFakePxAOD:
    # Create a new mini-xAOD output stream object
    from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
    HWWlnulnuTopFakesOutStream = MSMgr.NewPoolRootStream( hWWlnulnu.Global.TopFakesStreamName, hWWlnulnu.Global.TopFakesFileName )

    hWWlnulnu_msg.info( "For the output stream %s - " % HWWlnulnuTopFakesOutStream.GetEventStream().name() )

    # Filter the events
    if hWWlnulnu.Global.doSkimming :
        hWWEventCandSeq += CfgMgr.HWW__EventSelectionAlg("HWWTopFakesEventSelectionAlg",
                                InputContainerList = [hWWlnulnu.Event.eeEvent, hWWlnulnu.Event.mmEvent, hWWlnulnu.Event.emEvent, hWWlnulnu.Event.meEvent],
                                MinNOtherLeptons   = 1,
                                MinNBJets          = 1,
                                TaggerName         = hWWCommon.Jets.bTagName,
                                BTagOperatingPoint = hWWCommon.Jets.bTagWPNumber
                                )
        hWWlnulnu_msg.info( "Applying an event selection based on these accept algorithms: HWWTopFakesEventSelectionAlg" )
        HWWlnulnuTopFakesOutStream.AcceptAlgs( ["HWWTopFakesEventSelectionAlg"] )
        pass
    # We always filter based on the listed require algs. These are, e.g.,
    # the GRL filter, trigger fitler, vertex filter,...
    hWWlnulnu_msg.info( "Applying an event selection based on these require algorithms: %s" % hWWCommon.Global.requireAlgList )
    HWWlnulnuTopFakesOutStream.RequireAlgs( hWWCommon.Global.requireAlgList )

    # Use our common container item list to define the per-event content of the mini-xAOD
    from HWWlnulnuxAODConfig.HWWlnulnuPAODContent import pAODContent, pAODMetaDataContent
    HWWlnulnuTopFakesOutStream.AddItem( pAODContent() )
    HWWlnulnuTopFakesOutStream.AddMetaDataItem( pAODMetaDataContent() )

    # Remove the old-style EventInfo object. This should really go into our derivation
    # if objKeyStore.isInInputFile('PileUpEventInfo', 'McEventInfo') :
    if eventDataItems.__contains__("PileUpEventInfo#McEventInfo") :
        HWWlnulnuTopFakesOutStream.RemoveItem('EventInfo#*')
        HWWlnulnuTopFakesOutStream.AddItem( ['EventInfo#HWWEventInfo'])
        pass

    # Print the final item list to the log file
    if hWWlnulnu_msg.isEnabledFor(hWWlnulnu_msg.mapLevelGaudiToLogging(DEBUG)):
        hWWlnulnu_msg.debug( "OutputStream info:")
        HWWlnulnuTopFakesOutStream.Print()
        pass
    pass
