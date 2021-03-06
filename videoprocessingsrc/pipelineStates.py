"""
this is the file holds the Pipeline and controls Pipline
watch dog count to frozen 
"""
from enum import Enum


from zmq.sugar.frame import Message
import videoRequired
import consoleLog
from state import State
from datetime import datetime, time

class States(Enum):
    IDLE = 0
    SETUP_PIPELINE = 1
    TRAIN_MODEL = 2
    RUN_RECONITION = 4
    ERROR = 5

# Start of our states
class SetupPipeLine(State):
    """
    The state which Sets Up Whole opencv pipeline
    """

    def on_event(self, event,sender):
        if event == States.SETUP_PIPELINE:
            videoRequired.RequiredCode.setupPipeline(videoRequired.RequiredCode(),sender)
            self.next_state(States.TRAIN_MODEL)
            return TrainPipeline()

        return self


class TrainPipeline(State):
    """
    The state which Trains the Reconized face Models
    """

    def on_event(self, event,sender):
        if event == States.TRAIN_MODEL:
            videoRequired.RequiredCode.trainPipeLine(videoRequired.RequiredCode(),sender)
            self.next_state(States.RUN_RECONITION)
            return RunReconitionPipeLine()

        return self
    
    
class RunReconitionPipeLine(State):
    """
    The state which Reconizes Faces
    """

    def on_event(self, event,sender):
        if event == States.RUN_RECONITION:
            videoRequired.RequiredCode.reconitionPipeline(videoRequired.RequiredCode(),sender)
            
            if(videoRequired.RequiredCode.reconitionPipeline(videoRequired.RequiredCode(),sender) == States.ERROR):
                return Error()
            
        return self

class Idle(State):
    """
    The state which The program waits for a face to be spotted 
    """

    def on_event(self, event,sender):
        if event == States.IDLE:
            videoRequired.imports.consoleLog.Warning("Idleing....")
            videoRequired.imports.time.sleep(.5)
            

        return self
    
    
class Error(State):
    """
    The state which The program waits for a face to be spotted 
    """
    msg = None
    def __init__(self,message):
        self.msg = message
    

    def on_event(self, event,sender):
        if event == States.ERROR:
            videoRequired.imports.consoleLog.Error("ERROR....")
            sender.send_string("ERROR")
            sender.send_json({"error":str(self.msg),"time":str(datetime.now())})
            return 

        return self
    


class PipeLine(object):
    """ 
    A simple state machine that mimics the functionality of a device from a 
    high level.
    """
    
    def __init__(self):
        """ Initialize the components. """

        # Start with a default state.
        self.state  = SetupPipeLine()
     

    def on_event(self, event,sender):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event,sender)
        
    def getCurrentStat(self):
        return self.state
                