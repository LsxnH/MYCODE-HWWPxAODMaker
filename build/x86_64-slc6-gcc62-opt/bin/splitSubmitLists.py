#!/usr/bin/env python

# ==============================================================================
# File: splitSubmitLists.py
# Author: Karsten Koeneke <karsten.koeneke@cern.ch>
# Description: This file is a python executable that is meant for splitting the
# large submit lists into smaller ones for grid submission.
# ==============================================================================


import user  # look for .pythonrc.py for user init
import os,sys



inFileName = "submitList_HIGG3D1_mc16a.txt"

outFPre = inFileName.rstrip(".txt")

inFile = open(inFileName,'r')

outCommon        = open(outFPre+"__CommonOtherBkg.txt","w")
outSherpaDYBkg   = open(outFPre+"__SherpaDYBkg.txt","w")
outAlpgenDYBkg   = open(outFPre+"__AlpgenDYBkg.txt","w")
outMadGraphDYBkg = open(outFPre+"__MadGraphDYBkg.txt","w")
outPowhegDYBkg   = open(outFPre+"__PowhegDYBkg.txt","w")
outTopBkg        = open(outFPre+"__TopBkg.txt","w")
outH125Signal    = open(outFPre+"__HWWSignal.txt","w")
outHighMass      = open(outFPre+"__HWWHighMass.txt","w")
outSinglePhoton  = open(outFPre+"__SherpaSinglePhoton.txt","w")
# outHmumu       = open(outFPre+"__Hmumu.txt","w") ## Currently no Hmumu users of HWW PAODs afaik (Thomas)
outSystSamples   = open(outFPre+"__SystSamples.txt","w")


def getDSID(line):
    dsid = int(line.split(".")[1])
    return dsid

def isHWWSignal(line):
    dsid = getDSID(line)
    if dsid == 341079: return True
    if dsid == 343393: return True
    if dsid == 341080: return True
    if dsid == 341122: return True
    if dsid == 341155: return True
    if dsid == 342299: return True
    if dsid == 343953: return True
    if dsid == 345217: return True
    if 342282 <= dsid <= 342285: return True
    if 341421 <= dsid <= 341436: return True
    if 341449 <= dsid <= 341462: return True
    if 342684 <= dsid <= 343334: return True
    if 343365 <= dsid <= 343477: return True
    if 343987 <= dsid <= 343989: return True
    if 344299 <= dsid <= 344387: return True
    if 344733 <= dsid <= 344741: return True
    if 345120 <= dsid <= 345128: return True
    if 345211 <= dsid <= 345212: return True
    if 345242 <= dsid <= 345417: return True
    if 345270 <= dsid <= 345467: return True
    if 345465 <= dsid <= 345467: return True
    if 345586 <= dsid <= 345594: return True
    return False

def isHighMass(line):
    dsid = getDSID(line)
    if 302141 <= dsid <= 303256: return True
    if 307353 <= dsid <= 308009: return True
    if 341006 <= dsid <= 341034: return True
    if 343368 <= dsid <= 343377: return True
    if 343465 <= dsid <= 343466: return True
    if 343484 <= dsid <= 343499: return True
    if 302141 <= dsid <= 302165: return True
    if 303249 <= dsid <= 303256: return True
    if 344761 <= dsid <= 344770: return True
    if 344795 <= dsid <= 344819: return True
    if 345115 <= dsid <= 345118: return True
    if 345525 <= dsid <= 345527: return True
    if 310135 <= dsid <= 310150: return True
    return False

def isHmumu(line):
    dsid = getDSID(line)
    if 303046 <= dsid <= 303077: return True
    if 341190 <= dsid <= 341211: return True
    if 341677 <= dsid <= 341686: return True
    if 342992 <= dsid <= 343007: return True
    if 343340 <= dsid <= 343361: return True
    if 343959 <= dsid <= 343980: return True
    if 343990 <= dsid <= 344095: return True
    if 344388 <= dsid <= 344388: return True
    return False

def isSystSample(line):
    dsid = getDSID(line)
    if 363042 <= dsid <= 363089: return True
    if 363291 <= dsid <= 363300: return True
    if 363484 <= dsid <= 363485: return True
    if 410001 <= dsid <= 410006: return True
    if 410017 <= dsid <= 410020: return True
    if 410064 <= dsid <= 410065: return True
    if 410103 <= dsid <= 410110: return True
    if 410145 <= dsid <= 410146: return True
    if 410151 <= dsid <= 410154: return True
    if 410159 <= dsid <= 410164: return True
    if 410225 <= dsid <= 410226: return True
    if dsid == 410248: return True
    if 410511 <= dsid <= 410527: return True
    return False

def isTop(line):
    if isSystSample(line): return False
    dsid = getDSID(line)
    if 343362 <= dsid <= 343362: return True
    if 343637 <= dsid <= 343854: return True
    if 344171 <= dsid <= 344171: return True
    if 387250 <= dsid <= 387251: return True
    if 407200 <= dsid <= 407204: return True
    if 410000 <= dsid <= 410000: return True
    if 410003 <= dsid <= 410016: return True
    if 410021 <= dsid <= 410050: return True
    if 410066 <= dsid <= 410070: return True
    if 410189 <= dsid <= 410189: return True
    if 410252 <= dsid <= 410252: return True
    if 410472 <= dsid <= 410472: return True
    if 410500 <= dsid <= 410503: return True
    if 410658 <= dsid <= 410659: return True
    if 410644 <= dsid <= 410645: return True
    if 429007 <= dsid <= 429007: return True
    return False



def isSherpaDY(line):
    dsid = getDSID(line)
    if 304015 <= dsid <= 304021: return True
    if 344295 <= dsid <= 344298: return True
    if 344772 <= dsid <= 344782: return True
    if 361468 <= dsid <= 361491: return True
    if 363102 <= dsid <= 363122: return True
    if 363331 <= dsid <= 363354: return True
    if 363361 <= dsid <= 363483: return True
    if 363486 <= dsid <= 363486: return True
    if 364100 <= dsid <= 364215: return True
    return False

def isAlpgenDY(line):
    dsid = getDSID(line)
    if 361700 <= dsid <= 361874: return True
    return False

def isMadGraphDY(line):
    dsid = getDSID(line)
    if 343982 <= dsid <= 343986: return True
    if 361500 <= dsid <= 361534: return True
    if 361628 <= dsid <= 361642: return True
    if 363123 <= dsid <= 363170: return True
    if 363600 <= dsid <= 363748: return True
    return False

def isPowhegDY(line):
    dsid = getDSID(line)
    if 361100 <= dsid <= 361108: return True
    if 361664 <= dsid <= 361669: return True
    return False

def isSinglePhoton(line):
    dsid = getDSID(line)
    if 361039 <= dsid <= 361062: return True
    return False


# Sort the input alphabetically
lineList = inFile.readlines()
lineList.sort()
# Now, iterate over every line in the input file and write it to the appropriate file.
for line in lineList:
    if line.startswith("#"): continue
    if isHighMass(line):     outHighMass.write(line)
    elif isHWWSignal(line):  outH125Signal.write(line)
    # elif isHmumu(line):      outHmumu.write(line)
    elif isHmumu(line): continue
    elif isSherpaDY(line):     outSherpaDYBkg.write(line)
    elif isAlpgenDY(line):     outAlpgenDYBkg.write(line)
    elif isMadGraphDY(line):   outMadGraphDYBkg.write(line)
    elif isPowhegDY(line):     outPowhegDYBkg.write(line)
    elif isSystSample(line):   outSystSamples.write(line)
    elif isTop(line):          outTopBkg.write(line)
    elif isSinglePhoton(line): outSinglePhoton.write(line)
    else: outCommon.write(line)
    pass


# Close all files
inFile.close()
outCommon.close()
outH125Signal.close()
outHighMass.close()
# outHmumu.close()
outSherpaDYBkg.close()
outAlpgenDYBkg.close()
outMadGraphDYBkg.close()
outPowhegDYBkg.close()
outTopBkg.close()
outSystSamples.close()
outSinglePhoton.close()
