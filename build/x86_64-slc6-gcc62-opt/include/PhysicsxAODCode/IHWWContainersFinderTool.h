///////////////////////// -*- C++ -*- /////////////////////////////
// IHWWContainersFinderTool.h
// Header file for class HWW::IContainersFinderTool
// Author: Thomas Maier <tmaier@cern.ch>
///////////////////////////////////////////////////////////////////
#ifndef HWWCOMMONXAODCODE_IHWWCONTAINERSFINDERTOOL_H
#define HWWCOMMONXAODCODE_IHWWCONTAINERSFINDERTOOL_H 1

// STL includes
#include <vector>

// FrameWork includes
#include "AsgTools/IAsgTool.h"


namespace HWW {
  /// Define the possible types of systematic variations
  enum SystematicType { UNKNOWN, ORIGNIAL, NOMINAL, FOURMOM, WEIGHT };

  /// Make some typedefs
  typedef std::pair<std::string, SystematicType> ContNameAndSysType_t;
  typedef std::vector<ContNameAndSysType_t> ContNameAndSysTypeVec_t;


  class IContainersFinderTool
    : virtual public asg::IAsgTool
  {
    /// Declare the interface ID for this pure-virtual interface class to the Athena framework
    ASG_TOOL_INTERFACE(HWW::IContainersFinderTool)

    ///////////////////////////////////////////////////////////////////
    // Public methods:
    ///////////////////////////////////////////////////////////////////
  public:
    /// Get all container names with their systematic types, given one container name (looking for xAOD::IParticleContainer)
    virtual StatusCode containerNamesAndSysTypes( ContNameAndSysTypeVec_t&, const std::string& ) const = 0;
    // virtual ContNameAndSysTypeVec_t containerNamesAndSysTypes( const std::string&, const std::vector<SystematicType>& ) const = 0;

    /// Get all container names with their systematic types, given one container name (looking for xAOD::JetContainer)
    virtual StatusCode jetNamesAndSysTypes( ContNameAndSysTypeVec_t&, const std::string& ) const = 0;

    /// Get all container names with their systematic types, given one container name (looking for xAOD::ElectronContainer)
    virtual StatusCode electronNamesAndSysTypes( ContNameAndSysTypeVec_t&, const std::string& ) const = 0;

    /// Get all container names with their systematic types, given one container name (looking for xAOD::MuonContainer)
    virtual StatusCode muonNamesAndSysTypes( ContNameAndSysTypeVec_t&, const std::string& ) const = 0;

    /// Get all container names with their systematic types, given one container name (looking for xAOD::MissingETContainer)
    virtual StatusCode metNamesAndSysTypes( ContNameAndSysTypeVec_t&, const std::string& ) const = 0;

  };

} // End: namespace HWW

#endif //> !HWWCOMMONXAODCODE_IHWWCONTAINERSFINDERTOOL_H
