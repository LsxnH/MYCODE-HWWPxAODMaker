##=============================================================================
## Name:        HWWCommonHelpers.py
##
## Author:      Karsten Koeneke
## Created:     October 2014
##
##=============================================================================

__doc__ = """Here, some usefull helper functions are defined."""
__version__ = "0.0.1"
__author__  = "Karsten Koeneke <karsten.koeneke@cern.ch>"




class SystematicsTracker(object) :
    """
    This class is meant to track all systematics names of all physics objects.
    It provides methods to return the relevant systematic names for a given
    object. It also provides methods to return all relevant container names for
    the known systematics. The default convention is that the container names
    are build using an optional prefix, the base name, a separator (default is
    '___'), and the systematic name.
    """

    def __init__ ( self, name="SystematicsTracker", **kw ):
        self.name = name
        self.separator = kw.get( 'separator', "___" )
        #print "kw:", kw
        self.systDict  = {}
        for key, value in kw.iteritems():
            if key == "separator": continue
            self.systDict[key] = value
            pass
        return

    def dump(self):
        print "Name      =", self.name
        print "separator =", self.separator
        print "systematics dictionary: "
        for key in self.systDict.keys():
            print "  %s: %s" % (key, self.systDict[key])
            pass
        return

    def setSystematics( self, objectType="", systematics=[] ):
        """
        Adding systematics for one type of object, e.g., muon.
        """
        assert type(systematics)==list
        assert type(objectType)==str
        self.systDict[objectType] = systematics
        return

    def systematics( self, objectTypes=[] ):
        """
        This function returns the list of systematics for the provided object
        types.
        """
        systList = []
        for objType in objectTypes:
            if not self.systDict.keys().__contains__(objType):
                print "ERROR: Current object type with name='%s' is not known" % objType
                print "ERROR: The known object types are:", self.systDict.keys()
                return
            systList += self.systDict[objType]
            pass
        return systList

    def containers( self, definitions=[] ):
        """
        This function takes a list of definitions. Each definition defines one
        list of container names that should be returned. It is ensured that all
        these lists must have the same lenght. The container names will be build
        from the first string entry in the provided tuple (each entry in the
        definitions list is a tuple), plus the self.separator, plus the suffix.
        The suffix is the systematic name. The systematic names are aggregated
        by the second item in each tuple, which must be a list. This list lists
        the types of systematics that should be considered. For example, this:
        definitions = [ ('BaseName', ['own','electron','muon','jet']),
                        ('AnotherName', ['','electron','muon','jetNOSUFFIX']) ]
        will result in a return value that looks like this:
        [ ['BaseName','BaseName___EleSyst1','BaseName___MuSyst1','BaseName___JetSyst1','BaseName___JetSyst2'],
          ['AnotherName','AnotherName___EleSyst1','AnotherName___MuSyst1','AnotherName','AnotherName'] ]
        Note that an empty string or 'own' will result in no suffix for the base
        name. While a systematic name directly followed by "NOSUFFIX" will
        include the base name into the resulting container list for the exact
        number of times that the corresponding systematic exists, e.g., in the
        above example resulting in two times 'AnotherName' for the two jet
        systematics.
        The return value is a list of lists. All inner lists are ensured to have
        the same lenght. And each of these inner lists corresponds to one
        definition tuple, e.g., in the above example, there are two inner lists
        of the same length, each one corresponding to one of the two given tuples.
        """
        _finalLists = []
        for defi in definitions:
            tmpList = []
            #print "defi:", defi
            baseName = defi[0]
            assert type(baseName)==str
            suffixes = defi[1]
            #print "suffixes:",suffixes
            assert type(suffixes)==list
            # iterate over all suffixes and actually build them
            for suffix in suffixes:
                if suffix=='' or suffix=='own':
                    tmpList.append( baseName )
                    pass
                elif suffix.endswith("NOSUFFIX"):
                    tmpSuffix = suffix.rstrip("NOSUFFIX")
                    tmpSystematics = self.systematics([tmpSuffix])
                    for tmpSyst in tmpSystematics:
                        tmpList.append( baseName )
                        pass
                    pass
                else:
                    tmpSystematics = self.systematics([suffix])
                    for tmpSuffix in tmpSystematics:
                        tmpList.append( baseName + self.separator + tmpSuffix  )
                        pass
                    pass
                pass
            # add the resulting inner list to the overall one
            _finalLists.append(tmpList)
            pass
        # Make sure all lists have the same lenght
        assert len(_finalLists)>0
        listLen = len(_finalLists[0])
        for finList in _finalLists:
            assert listLen==len(finList)
            pass
        # if len(_finalLists)==1: return _finalLists[0]
        return _finalLists

    pass



def buildContainerNames( prefix="", baseName="", separator="___", systList=[] ) :
    """
    This function is building the list of all containers out of the give arguments.
    """
    _containerNameList = [ prefix + baseName ]
    for sysVarName in systList :
        if sysVarName=="": _containerNameList.append( prefix + baseName )
        else:              _containerNameList.append( prefix + baseName + separator + sysVarName )
        pass
    return _containerNameList




def replaceAuxContainers( itemList, auxContsToBreakUp ) :
    """
    This function is trying to replace the full AuxContainers, e.g.,
    JetAuxContainer, in the output item list (the list that defines
    what gets written to the output file) with the fully dynamic
    AuxContainerBase class.
    """
    for auxContName in auxContsToBreakUp :
        currentItem = ""
        # Find the existing item in the itemList and remove it
        for item in itemList :
            if item.__contains__(auxContName) and item.__contains__("Aux") :
                currentItem = item
                itemList.remove(item)
                break
            pass
        # Try to get the individual variable selection, if any, and use it
        itemVars = ""
        if currentItem.__contains__("Aux.") and not currentItem.endswith("Aux.") :
            itemVars = currentItem.split("Aux.")[1]
            pass
        # Now, add the new item to the itemList
        if auxContName.__contains__("Event") and not auxContName.__contains__("TruthEventAux") \
              and not currentItem.__contains__("Container") :
            itemList.append( "xAOD::AuxInfoBase#"+auxContName+itemVars )
            pass
        else:
            itemList.append( "xAOD::AuxContainerBase#"+auxContName+itemVars )
            pass
        pass
    return itemList

def search_file(filename, search_path):
    """
    Given a search path, find a file
    """
    from string import split
    from os.path import exists, join, abspath
    file_found = 0
    paths = split(search_path, ':')
    for path in paths:
        if exists(join(path, filename)):
            file_found = 1
            break
    if file_found:
        return abspath(join(path, filename))
    else:
        return None