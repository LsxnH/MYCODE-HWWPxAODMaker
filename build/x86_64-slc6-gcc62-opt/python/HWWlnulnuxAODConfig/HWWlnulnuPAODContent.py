##=============================================================================
## Name:        HWWlnulnuPAODContent.py
##
## Author:      Karsten Koeneke
## Created:     August 2014
##
## Description: Here, we define the content that will be written for the
##              Physics AOD (PAOD) output file.
##=============================================================================

# Import the steering flags for this analysis
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon
from HWWlnulnuxAODConfig.HWWlnulnuAnalysisFlags import hWWlnulnu

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
    if hWWCommon.Global.processReco:
        itemList.append("xAOD::CompositeParticleContainer#EventEE*")
        itemList.append("xAOD::CompositeParticleContainer#EventEM*")
        itemList.append("xAOD::CompositeParticleContainer#EventME*")
        itemList.append("xAOD::CompositeParticleContainer#EventMM*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventEE*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventEM*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventME*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventMM*")
        itemList.append("xAOD::AuxContainerBase#EventEE*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventEM*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventME*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventMM*Aux.-px.-py.-pz.-e.-charge.-pdgId")

    if hWWCommon.Global.processTruth:
        # also add truth events
        itemList.append("xAOD::CompositeParticleContainer#EventTruthEE*")
        itemList.append("xAOD::CompositeParticleContainer#EventTruthEM*")
        itemList.append("xAOD::CompositeParticleContainer#EventTruthME*")
        itemList.append("xAOD::CompositeParticleContainer#EventTruthMM*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventTruthEE*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventTruthEM*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventTruthME*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventTruthMM*")
        itemList.append("xAOD::AuxContainerBase#EventTruthEE*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventTruthEM*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventTruthME*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventTruthMM*Aux.-px.-py.-pz.-e.-charge.-pdgId")

    return itemList


# ====================================================================
# Define the meta-data item list of the output Physics AOD (PAOD)
# ====================================================================
def pAODMetaDataContent():
    # Take the common parts
    itemList = CommonPAODContent.pAODMetaDataContent()
    return itemList
