#!/usr/bin/env python

from argparse import ArgumentParser


def main():
    docText = '''
    This is a small tool to generate a combined samplelist file from a list of samplelist files.
    It will take the lists in the given order and take dataset names to dump them in the combined samplelist file (taking only one dataset name for each dataset ID).
    '''
    parser = ArgumentParser(description=docText)
    parser.add_argument("--input-fullsim", dest="fileListFullSim", help="List of samplelist files to consider for FullSim (comma separated).")
    parser.add_argument("--input-af2", dest="fileListAF2", help="List of samplelist files to consider for AF2 (comma separated).")
    args = parser.parse_args()

    fileListFullSim = args.fileListFullSim.split(",")
    fileListAF2 = args.fileListAF2.split(",")
    sampleDictFullSim = {}
    sampleDictAF2 = {}

    for fileName in fileListFullSim :
        sampleList = None
        with open(fileName, "r") as inFile :
            sampleList = filter(None, (line.rstrip() for line in inFile))
            pass
        for sample in sampleList :
            sampleID = sample.split(".")[1]
            if sampleID in sampleDictFullSim.keys() : continue
            sampleDictFullSim[sampleID] = sample
            pass
        pass

    for fileName in fileListAF2 :
        sampleList = None
        with open(fileName, "r") as inFile :
            sampleList = filter(None, (line.rstrip() for line in inFile))
            pass
        for sample in sampleList :
            sampleID = sample.split(".")[1]
            if sampleID in sampleDictAF2.keys() : continue
            sampleDictAF2[sampleID] = sample
            pass
        pass

    with open("samplelist_HIGG3D1_mc15_Combined.txt", "w") as outFile :
        for line in sorted(sampleDictFullSim.values()) :
            outFile.write(line+"\n")
            pass
        for line in sorted(sampleDictAF2.values()) :
            outFile.write(line+"\n")
            pass
        pass
    
    pass


if __name__ == "__main__" :
    main()
    pass
