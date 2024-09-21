#!/usr/bin/python -i
####!/usr/bin/env python -i

import user  # look for .pythonrc.py for user init
import sys, os

# Make sure that the user specified the input file path/name to load
if len(sys.argv) < 2 :
    print "You didn't specify an input file to load! You should have typed:"
    print "readxAOD.py yourInputxAODFile.pool.root"
    pass

# Specifying the input file to load
aodFile = str(sys.argv[1])
aodFile = '/home/kkoeneke/VMWork/athena/HWWxAODTestArea/HiggsWWlnulnu/run/test3/HWWMinixAOD.pool.root'
print "Attempting to open input xAOD file: ", aodFile
print

import ROOT
import PyCintex
import AthenaROOTAccess.transientTree
#f = ROOT.TFile.Open (aodFile)
#assert f.IsOpen()

# Fill this in if you want to change the names of the transient branches.
branchNames = {}
#branchNames['ElectronCollection'] = 'ele'
#branchNames['PhotonCollection'] = 'gam'

#tt = AthenaROOTAccess.transientTree.makeTree(f, branchNames = branchNames)
# tt is the transient tree "CollectionTree_trans" containing the (proxies) to
# all available transient data object in the file f.
# The original, persistent tree is declared as a friend
# of CollectionTree_trans, so that the transient tree will provide
# access to both transient data objects and to their persistent counterparts.
