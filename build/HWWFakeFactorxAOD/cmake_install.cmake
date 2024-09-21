# Install script for directory: /home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD

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

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/src/HWWFakeFactorxAOD" TYPE DIRECTORY FILES "/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD/" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/\\.git$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xDebugx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/libHWWFakeFactorxAODLib.so.dbg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/libHWWFakeFactorxAODLib.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWFakeFactorxAODLib.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWFakeFactorxAODLib.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/cvmfs/sft.cern.ch/lcg/releases/binutils/2.28-19981/x86_64-slc6-gcc62-opt/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWFakeFactorxAODLib.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xDebugx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/libHWWFakeFactorxAOD.so.dbg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE MODULE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/libHWWFakeFactorxAOD.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWFakeFactorxAOD.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWFakeFactorxAOD.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/cvmfs/sft.cern.ch/lcg/releases/binutils/2.28-19981/x86_64-slc6-gcc62-opt/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWFakeFactorxAOD.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWFakeFactorxAOD" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWFakeFactorxAOD/HWWFakeFactorxAODConf.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process( COMMAND ${CMAKE_COMMAND} -E touch
      $ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/HWWFakeFactorxAOD/__init__.py )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWFakeFactorxAOD" TYPE FILE RENAME "HWWFakeFactorFlags.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD/python/HWWFakeFactorFlags.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWFakeFactorxAOD" TYPE FILE RENAME "HWWFakeFactorPAODContent.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD/python/HWWFakeFactorPAODContent.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWFakeFactorxAOD" TYPE FILE RENAME "__init__.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD/python/__init__.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWFakeFactorxAOD" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWFakeFactorxAOD/HWWFakeFactorFlags.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWFakeFactorxAOD" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWFakeFactorxAOD/HWWFakeFactorPAODContent.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWFakeFactorxAOD" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWFakeFactorxAOD/__init__.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/HWWFakeFactorxAOD" TYPE FILE RENAME "HWWFakeFactorAnalysisCommon.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD/share/HWWFakeFactorAnalysisCommon.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/HWWFakeFactorxAOD" TYPE FILE RENAME "HWWFakeLeptonEventCandidateBuilding.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD/share/HWWFakeLeptonEventCandidateBuilding.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/HWWFakeFactorxAOD" TYPE FILE RENAME "HWWReadTest.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD/share/HWWReadTest.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/HWWFakeFactorxAOD" TYPE FILE RENAME "HWWlnulnuThinning.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD/share/HWWlnulnuThinning.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/HWWFakeFactorxAOD" TYPE FILE RENAME "readxAOD.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWFakeFactorxAOD/share/readxAOD.py")
endif()

