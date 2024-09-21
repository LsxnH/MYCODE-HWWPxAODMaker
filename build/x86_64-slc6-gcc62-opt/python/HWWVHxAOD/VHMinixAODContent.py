##=============================================================================
## Name:        HWWlnulnuMinixAODContent.py
##
## Author:      Karsten Koeneke
## Created:     August 2014
##
## Description: Here, we define the content that will be written for the
##              mini-xAOD output file.
##=============================================================================

# Import the steering flags for this analysis
from PhysicsxAODConfig.HWWCommonAnalysisFlags import hWWCommon

# Import the common content
from PhysicsxAODConfig import CommonPAODContent


# ====================================================================
# Define the container item list of the output PAOD for WH
# ====================================================================
def pAODWHContent():
    """This function defines then which 'containers' are written to disk."""
    # Take the common parts
    itemList = CommonPAODContent.pAODContent()

    # Now, add specific parts
    if hWWCommon.Global.processReco:
        itemList.append("xAOD::CompositeParticleContainer#EventWH*")
        itemList.append("xAOD::CompositeParticleContainer#EventWH*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventWH*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventWH*")
        itemList.append("xAOD::AuxContainerBase#EventWH*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventWH*Aux.-px.-py.-pz.-e.-charge.-pdgId")

    if hWWCommon.Global.processTruth:
        # also add truth events
        itemList.append("xAOD::CompositeParticleContainer#EventTruthWH*")
        itemList.append("xAOD::CompositeParticleContainer#EventTruthWH*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventTruthWH*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventTruthWH*")
        itemList.append("xAOD::AuxContainerBase#EventTruthWH*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventTruthWH*Aux.-px.-py.-pz.-e.-charge.-pdgId")

    return itemList

# ====================================================================
# Define the container item list of the output PAOD for ZH
# ====================================================================
def pAODZHContent():
    """This function defines then which 'containers' are written to disk."""
    # Take the common parts
    itemList = CommonPAODContent.pAODContent()

    # Now, add specific parts
    if hWWCommon.Global.processReco:
        itemList.append("xAOD::CompositeParticleContainer#EventZH*")
        itemList.append("xAOD::CompositeParticleContainer#EventZH*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventZH*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventZH*")
        itemList.append("xAOD::AuxContainerBase#EventZH*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventZH*Aux.-px.-py.-pz.-e.-charge.-pdgId")

    if hWWCommon.Global.processTruth:
        # also add truth events
        itemList.append("xAOD::CompositeParticleContainer#EventTruthZH*")
        itemList.append("xAOD::CompositeParticleContainer#EventTruthZH*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventTruthZH*")
        itemList.append("xAOD::CompositeParticleAuxContainer#EventTruthZH*")
        itemList.append("xAOD::AuxContainerBase#EventTruthZH*Aux.-px.-py.-pz.-e.-charge.-pdgId")
        itemList.append("xAOD::AuxContainerBase#EventTruthZH*Aux.-px.-py.-pz.-e.-charge.-pdgId")

    return itemList

# ====================================================================
# Define the meta-data item list of the output mini-xAOD
# ====================================================================
def pAODMetaDataContent():
    # Take the common parts
    itemList = CommonPAODContent.pAODMetaDataContent()
    return itemList
