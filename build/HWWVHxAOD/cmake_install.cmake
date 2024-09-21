# Install script for directory: /home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/src/HWWVHxAOD" TYPE DIRECTORY FILES "/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD/" USE_SOURCE_PERMISSIONS REGEX "/\\.svn$" EXCLUDE REGEX "/\\.git$" EXCLUDE REGEX "/[^/]*\\~$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xDebugx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/libHWWVHxAODLib.so.dbg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/libHWWVHxAODLib.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWVHxAODLib.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWVHxAODLib.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/cvmfs/sft.cern.ch/lcg/releases/binutils/2.28-19981/x86_64-slc6-gcc62-opt/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWVHxAODLib.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xDebugx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/libHWWVHxAOD.so.dbg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE MODULE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/lib/libHWWVHxAOD.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWVHxAOD.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWVHxAOD.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/cvmfs/sft.cern.ch/lcg/releases/binutils/2.28-19981/x86_64-slc6-gcc62-opt/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libHWWVHxAOD.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE OPTIONAL FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWVHxAOD/HWWVHxAODConf.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process( COMMAND ${CMAKE_COMMAND} -E touch
      $ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD/__init__.py )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE RENAME "VHFlags.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD/python/VHFlags.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE RENAME "VHMinixAODContent.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD/python/VHMinixAODContent.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE RENAME "WHFlags.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD/python/WHFlags.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE RENAME "ZHFlags.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD/python/ZHFlags.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE RENAME "__init__.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD/python/__init__.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWVHxAOD/VHFlags.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWVHxAOD/VHMinixAODContent.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWVHxAOD/WHFlags.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWVHxAOD/ZHFlags.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/python/HWWVHxAOD" TYPE FILE FILES "/home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/python/HWWVHxAOD/__init__.pyc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/HWWVHxAOD" TYPE FILE RENAME "VHAnalysisCommon.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD/share/VHAnalysisCommon.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/HWWVHxAOD" TYPE FILE RENAME "VHCandidateBuilding.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD/share/VHCandidateBuilding.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xMainx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/jobOptions/HWWVHxAOD" TYPE FILE RENAME "VHTruthCandidateBuilding.py" FILES "/hepustc/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/HWWVHxAOD/share/VHTruthCandidateBuilding.py")
endif()

