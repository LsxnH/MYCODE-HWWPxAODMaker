##=============================================================================
## Name:        SelectDFEventsAlg
##
## Author:      Karsten Koeneke
## Created:     October 2015
##
## Description: This short algorithm makes a very simple selection on events,
##              i.e., only selecting events that have at least one EM or ME candidate.
## =============================================================================

__doc__ = """This short algorithm makes a very simple selection on events,
i.e., only selecting events that have at least one EM or ME candidate.
"""
__version__ = "0.0.1"
__author__  = "Karsten Koeneke <karsten.koeneke@cern.ch>"


# Import the needed modules
import AthenaPython.PyAthena as PyAthena
from AthenaPython.PyAthena import StatusCode

class SelectDFEventsAlg( PyAthena.Alg ):
    """
    This short algorithm makes a very simple selection on events,
    i.e., only selecting events that have at least one EM or ME candidate.
    """

    def __init__ ( self, name = "SelectDFEventsAlg", **kw ):
        ## initialize base class
        kw['name'] = name
        super(SelectDFEventsAlg, self).__init__(**kw)
        # Get the properties
        self.inputNames  = kw.get( 'InputNames', ["EventME","EventEM"] )
        ## Get the storgate handle
        self.storeGateSvc = None
        return


    def initialize(self):
        self.msg.debug( '==> initialize %s...', self.name() )
        self.msg.debug( 'InputNames = %s...', self.inputNames )

        ## Get the StoreGate service
        self.storeGateSvc = PyAthena.py_svc('StoreGateSvc')
        if self.storeGateSvc is None:
            self.msg.error("Problem retrieving StoreGateSvc pointer!")
            return StatusCode.Failure
        return StatusCode.Success


    def execute(self):
        self.msg.debug( '==> execute %s...' % (self.name()) )

        keepEvent = False
        # Loop over all given event objects
        for inName in self.inputNames :
            # Get the input collections from StoreGate
            event = self.storeGateSvc[ inName ]
            if event.size():
                keepEvent = True
                break
            pass

        # Actually set the decision if this event passes or failes
        self.setFilterPassed(keepEvent)
        return StatusCode.Success


    def finalize(self):
        return StatusCode.Success
