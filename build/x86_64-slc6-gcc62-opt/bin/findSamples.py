#!/usr/bin/env python

__doc__ = """
This script creates a list of available datasets
from a list of DSIDs by querying AMI.
Known format variants are the following:
AOD, HIGG3D1, HIGG3D3
"""
import os
import sys, getopt, time, re
import pyAMI.atlas.api as atlasAPI
import pyAMI.client
client = pyAMI.client.Client('atlas')
atlasAPI.init()

def sizestring(nBytes):

    if nBytes == "NULL":
        return nBytes
    nGigaBytes = float(nBytes)*9.3132257461547852e-10
    sizestring = "{:0.3f}".format(nGigaBytes)
    return sizestring

def getDefaultTagStructure(dataType):
    tagStructure = ""

    if dataType == "AOD": tagStructure = "e,s,r"
    if dataType.__contains__("DAOD") or dataType.__contains__("NTUP_PILEUP"): tagStructure = "e,s,r,p"
    # if dataType.__contains__("NTUP_PILEUP"): tagStructure = "e,s,r,p"

    if tagStructure=="": print "Tagstructure is unknown for this input. Please provide it"
    
    return tagStructure


#_______________________________________________________________________________
def main():

    from argparse import ArgumentParser
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("infile",type=str,metavar="DSID_INFILE.TXT",help="DSID list to be read")
    parser.add_argument("--datatype",'-d',dest="datatype",default="AOD",help="The dataset type to search for (AOD, HIGG3D1, etc.)")
    parser.add_argument("--subcampaign",'-s',dest="subcampaign",default="mc16a",help="The subcampaign to search for (e.g. mc16a)")
    parser.add_argument("--tagstructure",'-t',dest="tagstructure",type=str,default="",help="A comma-separated list of tag letters - datasets with exactly one tag of each and in that order will be searched for (default constructed from datatype)")
    parser.add_argument("--ptag",'-p',dest="ptag",type=str,default="",help="Restrict the tag match to a specific ptag")
    parser.add_argument("--outfile_list",'-l',dest="outfile_list",default="list.txt",help="The name of the output file in list form")
    parser.add_argument("--outfile_csv",'-c',dest="outfile_csv",default="list.csv",help="The name of the output file in csv form")
    parser.add_argument("--verbose",'-v',dest="verbose",default=False,action="store_true",help="Add some extra printout on search results")
    parser.add_argument("--bare",'-b',dest="bare",default=False,action="store_true",help="print out only the dataset name")

    args = parser.parse_args()

    dataType     = args.datatype
    subCampaign  = args.subcampaign
    tagStructure = args.tagstructure

    # Check if production campaign is known and assign corresponding r-tag
    knownCampaigns = (("mc16a","9364"), ("mc16c","9781"), ("mc16d","10201"), ("mc16e","10724"))
    rtag = ""
    for thisCampaign, thisTag in knownCampaigns:
        if subCampaign==thisCampaign: rtag = thisTag
    if rtag == "":
       print "Unknown production campaign. Known campaigns are ", [campaign[0] for campaign in knownCampaigns]
       exit(2)

    dataType = dataType.replace("xAOD","AOD")
    if dataType == "HIGG3D1": dataType = "DAOD_HIGG3D1"
    if dataType == "HIGG3D3": dataType = "DAOD_HIGG3D3"

    # Check if data type is known and set corresponding datatype tag
    knownDataTypes = (("AOD","recon.AOD"),("DAOD_HIGG3D1","deriv.DAOD_HIGG3D1"),("DAOD_HIGG3D3","deriv.DAOD_HIGG3D3"),("NTUP_PILEUP","NTUP_PILEUP"))
    datatag = ""
    for thisType, thisTag in knownDataTypes:
        if dataType==thisType: datatag = thisTag
    if datatag == "":
       print "Unknown data type. Known types are ", [dataType[0] for dataType in knownDataTypes]
       exit(2)

    # Define default tagStructure for some cases
    if tagStructure == "": tagStructure = getDefaultTagStructure(dataType)
    if tagStructure == "":
        print "Abort program"
        exit(2)

    content_list = ""
    content_csv  = ""

    timestring = "\n# This file was generated on " + time.ctime() + "\n\n"
    content_list += timestring

    # construct the search string used to query AMI
    simType = "_s"
    if tagStructure.__contains__("a"): simType = "_a"
    searchString="%."+datatag+".%"+simType+"%_r"+rtag+"%"
    if args.verbose:
        content_list += "Ami search string = "+searchString+"\n\n"

    # construct the regular expression pattern to match with the dataset tags returned by AMI
    tagpattern_string = ""
    for tag in tagStructure.split(","):
        if tag == 'p' and args.ptag:
            tagpattern_string += tag+args.ptag
        else:
            tagpattern_string += tag+"[0-9]+_"
    tagpattern_string = tagpattern_string.rstrip("_") # Remove last "_" from tagpattern if ptag not specified
    tagpattern = re.compile(tagpattern_string)
    if args.verbose:
        content_list += "Match tag pattern = "+tagpattern.pattern+"\n\n"

    # Prepare header of list output file
    content_list += "DSID".ljust(10)+"Logistic Dataset Name".ljust(135)+"Production Status".ljust(35)+"Nevents".ljust(12)+"Size [Gb]".ljust(10)+"\n"+("-" * 202)
    print content_list
    content_list +="\n"

    # Prepare header of csv output file
    content_csv = timestring
    content_csv += "SampleID , xsection, kfactor , filtereff , uncertainty , mh , generator , process , simulation\n"
    # print content_csv
    content_csv +="\n"

    with open(args.infile) as f:
        lines = f.read().splitlines()

    for line in lines:

        # allow for comments and blank lines in the DSID input file
        # also print them in the output
        if line.startswith("#") or not line:
            print line
            content_list+=line+"\n"
            content_csv+=line+"\n"
            continue

        dsid = line
        dsid = dsid.strip() # remove whitespace

        # here is where we actually query AMI
        # returns a list of orderedDicts, 1 for each dataset returned from the search
        datasets = atlasAPI.list_datasets(client, patterns='mc16_13TeV.'+dsid+searchString, fields=['events','prodsys_status','cross_section','generator_filter_efficienty','generator_name','physics_short','conditions_tag','total_size'])
        # initialize tag match entries
        if args.verbose:
            tagMatch_listOutput = "".ljust(10)+"(none found)"
        else:
            tagMatch_listOutput = dsid.ljust(10)+"(none found)"
        tagMatch_csvOutput = ""

        if args.verbose:
            print dsid
            content_list+=dsid+"\n"
            print "".ljust(7)+"AMI search results:"
            content_list+="".ljust(7)+"AMI search results:"+"\n"
            if not datasets:
                print "".ljust(10)+"(none found)"
                content_list+="".ljust(10)+"(none found)"+"\n"

        for dataset in datasets:

            # Get dataset entry, only printing if verbose
            if args.verbose:
                dataset_search_result = "".ljust(10)+dataset['ldn'].ljust(135)+dataset['prodsys_status'].ljust(35)+dataset['events'].ljust(12)+sizestring(dataset['total_size'])
                print dataset_search_result
                content_list+=dataset_search_result+"\n"
            elif args.bare:
                dataset_search_result = dataset['ldn']
            else:
                dataset_search_result = dsid.ljust(10)+dataset['ldn'].ljust(135)+dataset['prodsys_status'].ljust(35)+dataset['events'].ljust(12)+sizestring(dataset['total_size'])

            if dataset['events'] == "0": continue

            # Check if dataset tags match the given tag pattern
            # e.g. e5769_s3126_r9364 would match e[0-9]+_s[0-9]+_r[0-9]
            tagstring = dataset['ldn'].split(".")[-1]
            if not tagpattern.match(tagstring):
                continue

            # Set tag match entry for list
            tagMatch_listOutput = dataset_search_result

            # Convert cross section from nb (ami default) to pb ahead of time
            # protects against rare case in which ami reports 'NULL' for cross_section
            xsec = dataset['cross_section']
            if xsec != 'NULL':
                xsec = float(xsec)
                xsec *= 1000
                xsec = str(xsec)

            # Get tag match entry for csv file
            tagMatch_csvOutput = dsid+", "+xsec+", KFACTOR "+dataset['generator_filter_efficienty']+", --, "
            tagMatch_csvOutput+= "mHIGGS, "+dataset['generator_name']+", "+dataset['physics_short']+", "+dataset['conditions_tag']

        # Add content to output texts, and print some info
        if args.verbose:
            print "".ljust(7)+"Tag pattern match:"
            content_list+="".ljust(7)+"Tag pattern match:"+"\n"
        print tagMatch_listOutput
        content_list+=tagMatch_listOutput+"\n"
        if args.verbose:
            print "\n"

        if tagMatch_csvOutput!="":
            content_csv+=tagMatch_csvOutput+"\n"

    print "Write dataset list to file ",args.outfile_list
    with open(args.outfile_list, 'w') as f:
        f.write(content_list)

    print "Write csv file ",args.outfile_csv
    with open(args.outfile_csv, 'w') as f:
        f.write(content_csv)

    return 0

#_______________________________________________________________________________
if __name__ == '__main__':
    os._exit(main())
