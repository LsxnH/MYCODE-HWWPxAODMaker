#!/bin/bash
#
# Copyright (C) 2002-2017 CERN for the benefit of the ATLAS collaboration
#
# This script is used by CTest to run the test ut_HiggsWeightTool_test with the correct
# environment setup, and post processing.
#

# Transmit errors:
set -e

# Set up the runtime environment:
source /home/hengli/testarea/HWWPxAODMaker/build/x86_64-slc6-gcc62-opt/setup.sh

# Turn off xAOD monitoring for the test:
export XAOD_ACCESSTRACER_FRACTION=0

# Set the package name, which may be used by post.sh later on:
export ATLAS_CTEST_PACKAGE=TruthWeightTools

# Run a possible pre-exec script:
# No pre-exec necessary

# Run the test:
/home/hengli/testarea/HWWPxAODMaker/build/TruthWeightTools/test-bin/ut_HiggsWeightTool_test.exe 2>&1 | tee ut_HiggsWeightTool_test.log; \
    test ${PIPESTATUS[0]} -eq 0

# Set the test's return code in the variable expected by post.sh:
export testStatus=${PIPESTATUS[0]}

# Put the reference file in place if it exists:
if [ -f /home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/TruthWeightTools/share/ut_HiggsWeightTool_test.ref ] &&
    [ "/home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/TruthWeightTools" != "/home/hengli/testarea/HWWPxAODMaker/build/TruthWeightTools" ]; then
    /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/Cmake/3.11.0/Linux-x86_64/bin/cmake -E make_directory ../share
    /cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase/x86_64/Cmake/3.11.0/Linux-x86_64/bin/cmake -E create_symlink \
     /home/hengli/testarea/HWWPxAODMaker/HWWPhysicsxAODMaker/TruthWeightTools/share/ut_HiggsWeightTool_test.ref ../share/ut_HiggsWeightTool_test.ref
fi

# Run a post-exec script:
if type post.sh >/dev/null 2>&1; then
    post.sh ut_HiggsWeightTool_test ""
fi
