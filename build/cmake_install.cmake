# Install script for directory: /home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/InstallArea/x86_64-slc6-gcc62-opt")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "RelWithDebInfo")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "0")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE DIRECTORY FILES "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig.cmake"
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake/modules" TYPE DIRECTORY FILES "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules/" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/\\.git$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE DIRECTORY FILES "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig.cmake"
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE DIRECTORY FILES "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig.cmake"
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE DIRECTORY FILES "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig.cmake"
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/." TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/packages.txt")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/." TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/compilers.txt")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/HWWPhysicsxAODMakerConfig-targets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/HWWPhysicsxAODMakerConfig-targets.cmake"
         "/home/hengli/testarea/HWWPxAODMaker/build/CMakeFiles/Export/cmake/HWWPhysicsxAODMakerConfig-targets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/HWWPhysicsxAODMakerConfig-targets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/cmake/HWWPhysicsxAODMakerConfig-targets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/CMakeFiles/Export/cmake/HWWPhysicsxAODMakerConfig-targets.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ww][Ii][Tt][Hh][Dd][Ee][Bb][Ii][Nn][Ff][Oo])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/CMakeFiles/Export/cmake/HWWPhysicsxAODMakerConfig-targets-relwithdebinfo.cmake")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/hengli/testarea/HWWPxAODMaker/build/atlas_export_sanitizer.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/HWWPhysicsxAODMakerConfig.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/HWWPhysicsxAODMakerConfig-version.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/." TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/setup.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/." TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/ClientCMakeLists.txt")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/." TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/ReleaseData")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  if( NOT EXISTS /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.rootmap )
                        message( WARNING "Creating partial /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.rootmap" )
                        execute_process( COMMAND /cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules/scripts/mergeFiles.sh /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.rootmap
                           /home/hengli/testarea/HWWPxAODMaker/build/CMakeFiles/HWWPhysicsxAODMakerRootMapMergeFiles.txt )
                     endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.rootmap")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  if( NOT EXISTS /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/share/clid.db )
                        message( WARNING "Creating partial /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/share/clid.db" )
                        execute_process( COMMAND /cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules/scripts/mergeClids.sh /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/share/clid.db
                           /home/hengli/testarea/HWWPxAODMaker/build/CMakeFiles/HWWPhysicsxAODMakerClidMergeFiles.txt )
                     endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/share/clid.db")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  if( NOT EXISTS /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.components )
                        message( WARNING "Creating partial /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.components" )
                        execute_process( COMMAND /cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules/scripts/mergeFiles.sh /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.components
                           /home/hengli/testarea/HWWPxAODMaker/build/CMakeFiles/HWWPhysicsxAODMakerComponentsMergeFiles.txt )
                     endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.components")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  if( NOT EXISTS /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.confdb )
                        message( WARNING "Creating partial /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.confdb" )
                        execute_process( COMMAND /cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules/scripts/mergeFiles.sh /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.confdb
                           /home/hengli/testarea/HWWPxAODMaker/build/CMakeFiles/HWWPhysicsxAODMakerConfdbMergeFiles.txt )
                     endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/HWWPhysicsxAODMaker.confdb")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE DIRECTORY FILES "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig.cmake"
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE DIRECTORY FILES "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/modules" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/cmake" TYPE FILE FILES
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig.cmake"
    "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/cmake/LCGConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/." TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/env_setup.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/." TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/README.txt")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/." TYPE FILE FILES "/cvmfs/atlas.cern.ch/repo/sw/software/21.2/AthAnalysis/21.2.56/InstallArea/x86_64-slc6-gcc62-opt/LICENSE.txt")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/hengli/testarea/HWWPxAODMaker/build/HWWFakeFactorxAOD/cmake_install.cmake")
  include("/home/hengli/testarea/HWWPxAODMaker/build/HWWVHxAOD/cmake_install.cmake")
  include("/home/hengli/testarea/HWWPxAODMaker/build/HWWlnulnuxAODConfig/cmake_install.cmake")
  include("/home/hengli/testarea/HWWPxAODMaker/build/PhysicsxAODCode/cmake_install.cmake")
  include("/home/hengli/testarea/HWWPxAODMaker/build/PhysicsxAODConfig/cmake_install.cmake")
  include("/home/hengli/testarea/HWWPxAODMaker/build/TruthWeightTools/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/hengli/testarea/HWWPxAODMaker/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
