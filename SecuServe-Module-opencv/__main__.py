"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""

import imports
from pipeline import pipelineStates
from util import const

imports.zmq.asyncio.install()

context = imports.zmq.asyncio.Context()

# inits Sender and reciver Sockets for the Module
sender = context.socket(imports.zmq.PUB)

def main():
    imports.consoleLog.Warning("Initing zmq")
    
    sender.bind("tcp://"+"*:5001") 
    
    imports.consoleLog.PipeLine_Ok("running zmq")
    watchdog = 0


    imports.consoleLog.Warning("running VideoProcessing Pipeline...")
    
    # sets pipeline starting state so Fsm has all needed to run
    pipe = pipelineStates.PipeLine()
    pipe.on_event(pipelineStates.States.SETUP_PIPELINE,sender)
    pipe.on_event(pipelineStates.States.TRAIN_MODEL,sender)
    pipe.on_event(pipelineStates.States.RUN_RECONITION,sender)
    
    """    
        if(topic == "MANAGER" and status['mode'] == "stopcv"):
            sender.send_string("SHUTDOWN")
            sender.send_json({"mode":"shutdown","restart":False,"time":str(imports.datetime.now())})
            imports.consoleLog.Warning("Shutting down Opencv Pipeline ...")
            imports.consoleLog.Error("by wor")
            break
    """
        




    
    
    
                
            
if __name__ == "__main__":
    main()
