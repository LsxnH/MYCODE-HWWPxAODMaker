///////////////////////// -*- C++ -*- /////////////////////////////
// IHWWSelectionTool.h
// Header file for class HWW::ITriggerTool
// Author: Thomas Maier <tmaier@cern.ch>
///////////////////////////////////////////////////////////////////
#ifndef PATCORE_IHWWTRIGGERTOOL_H
#define PATCORE_IHWWTRIGGERTOOL_H 1

// STL includes
#include <vector>

// FrameWork includes
#include "AsgTools/IAsgTool.h"

// EDM includes
#include "xAODMuon/MuonContainer.h"
#include "xAODEgamma/ElectronContainer.h"

// Forward declaration
namespace xAOD{
  class IParticle;
}



namespace HWW {
  class ITriggerTool
    : virtual public asg::IAsgTool
  {
    /// Declare the interface ID for this pure-virtual interface class to the Athena framework
    ASG_TOOL_INTERFACE(HWW::ITriggerTool)


    ///////////////////////////////////////////////////////////////////
    // Public methods:
    ///////////////////////////////////////////////////////////////////
  public:

    ///////////////////////////////////////////////////////////////////
    // Const methods:
    ///////////////////////////////////////////////////////////////////

    /// Single lepton trigger matching methods
    virtual bool match( const xAOD::IParticle* ) const = 0;
    virtual bool match( const xAOD::IParticle*, const std::string& ) const = 0;
    virtual bool match( const xAOD::Muon* ) const = 0;
    virtual bool match( const xAOD::Muon*, const std::string& ) const = 0;
    virtual bool match( const xAOD::MuonContainer* ) const = 0;
    virtual bool match( const xAOD::MuonContainer*, const std::string& ) const = 0;
    virtual bool match( const xAOD::Electron* ) const = 0;
    virtual bool match( const xAOD::Electron*, const std::string& ) const = 0;
    virtual bool match( const xAOD::ElectronContainer* ) const = 0;
    virtual bool match( const xAOD::ElectronContainer*, const std::string& ) const = 0;

    /// Di-lepton trigger matching methods
    // virtual bool match( std::vector<const xAOD::IParticle*>& partVec, const std::string& ) const = 0;
    // virtual bool match( std::vector<const xAOD::IParticle*>& partVec ) const = 0;
    virtual bool match( const xAOD::IParticleContainer*, const xAOD::IParticleContainer*, const std::string& ) const = 0;
    virtual bool match( const xAOD::IParticleContainer*, const xAOD::IParticleContainer* ) const = 0;

  };

} // End: namespace HWW

#endif //> !PATCORE_IHWWTRIGGERTOOL_H
