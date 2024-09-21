##=============================================================================
## Name:        HWWFakeFactorPAODContent.py
##
## Author:      Olivier Arnaez
## Created:     October 2015
##
## Description: Here, we define the content that will be written for the
##              Physics AOD (PAOD) output file.
##=============================================================================

# Import the steering flags for this analysis
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon
from HWWFakeFactorxAOD.HWWFakeFactorFlags import hWWFakes

# Import the common content
from PhysicsxAODConfig import CommonPAODContent


# ====================================================================
# Define the container item list of the output Physics AOD (PAOD)
# ====================================================================
def pAODContent():
    """This function defines then which 'containers' are written to disk."""
    # Take the common parts
    itemList = CommonPAODContent.pAODContent()

    # Now, add specific parts
    itemList.append("xAOD::CompositeParticleContainer#EventFake*")
    itemList.append("xAOD::CompositeParticleAuxContainer#EventFake*")
    itemList.append("xAOD::AuxContainerBase#EventFake*Aux.-px.-py.-pz.-e.-charge.-pdgId")
    # InDet TrackParticles (to get the next-to-innermost pixel layer hits)
    itemList.append("xAOD::TrackParticleContainer#InDetTrackParticles")
    itemList.append("xAOD::TrackParticleAuxContainer#InDetTrackParticlesAux.-constituentLinks.-constituentWeights.-definingParametersCovMatrix.-parameterX.-parameterPX.-parameterPY.-parameterPZ")
    itemList.append("xAOD::AuxContainerBase#InDetTrackParticlesAux.-constituentLinks.-constituentWeights.-definingParametersCovMatrix.-parameterX.-parameterPX.-parameterPY.-parameterPZ")

    # Get output list entries to check if the relevant trigger variables are already there
    eventInfoItems = ""
    muonsItems = ""
    electronsItems = ""
    for entry in itemList:
        if "xAOD::EventAuxInfo#EventInfoAux." in entry: eventInfoItems = entry
        if "xAOD::AuxContainerBase#"+hWWCommon.Muons.finalCont+"Aux." in entry: muonsItems = entry
        if "xAOD::AuxContainerBase#"+hWWCommon.Electrons.finalCont+"Aux." in entry: electronsItems = entry
        pass

    # Add additional Fakes specific EventInfo and AuxContainerBase variables
    fakesEventInfoList = ""
    fakesMuonsMatchList = ""
    fakesElectronsMatchList = ""
    for trigName in hWWFakes.Trigger.allFakableLeptonsTriggerList :
        # trigger pass and prescale
        trigPassName = hWWCommon.Trigger.triggerPassPrefix+trigName
        if ("."+trigPassName) not in eventInfoItems:
            fakesEventInfoList += "."+trigPassName
            pass
        fakesEventInfoList += ".prescale_"+trigName
        pass
    # muon trigger matching items
    for trigName in hWWFakes.Trigger.fakesMuonTriggerList :
        trigMatchName = hWWCommon.Trigger.triggerMatchPrefix+trigName
        if ("."+trigMatchName) not in muonsItems:
            fakesMuonsMatchList += "."+trigMatchName
            pass
        pass
    # electron trigger matching items
    for trigName in hWWFakes.Trigger.fakesElectronTriggerList :
        trigMatchName = hWWCommon.Trigger.triggerMatchPrefix+trigName
        if ("."+trigMatchName) not in electronsItems:
            fakesElectronsMatchList += "."+trigMatchName
            pass
        pass

    # We need to append the additional information to the already existing ItemList entry
    itemList = [(entry+fakesEventInfoList if ("xAOD::EventAuxInfo#EventInfoAux." in entry) else entry) for entry in itemList]
    # Muon trigger matching
    itemList = [(entry+fakesMuonsMatchList if ("xAOD::AuxContainerBase#"+hWWCommon.Muons.finalCont+"Aux." in entry) else entry) for entry in itemList]
    # Electron trigger matching
    itemList = [(entry+fakesElectronsMatchList if ("xAOD::AuxContainerBase#"+hWWCommon.Electrons.finalCont+"Aux." in entry) else entry) for entry in itemList]


    # For debugging, if you want to check what is scheduled to be written out
    print "PAOD content scheduled to be written out: "
    for it in itemList:
        print it

    return itemList


# ====================================================================
# Define the meta-data item list of the output Physics AOD (PAOD)
# ====================================================================
def pAODMetaDataContent():
    # Take the common parts
    itemList = CommonPAODContent.pAODMetaDataContent()
    return itemList
