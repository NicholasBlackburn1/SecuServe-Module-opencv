"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""

import imports
import pipelineStates
import const

context = imports.zmq.Context()
sender = context.socket(imports.zmq.PUB)
controller = context.socket(imports.zmq.SUB)

def main():
    imports.consoleLog.Warning("Initing zmq")

   
    
 
    controller.setsockopt(imports.zmq.SUBSCRIBE, b'')
    
    sender.bind("tcp://"+"127.0.0.1:5001")
    controller.connect("tcp://"+"127.0.0.1:5000")
    
    imports.consoleLog.PipeLine_Ok("running zmq")
    imports.consoleLog.Debug("Waiting for Zmq to recv Control Message...")
    watchdog = 0
    
  
    
    # loops to recv json message

    #if(controller.recv_json() == {"controller":"start"}):
    imports.consoleLog.Warning("running VideoProcessing Pipeline...")
    
    # sets pipeline starting state so Fsm has all needed to run
    pipe = pipelineStates.PipeLine()
    pipe.on_event(pipelineStates.States.SETUP_PIPELINE,sender)
    pipe.on_event(pipelineStates.States.TRAIN_MODEL,sender)
    pipe.on_event(pipelineStates.States.RUN_RECONITION,sender)

   


        
    
    
                
            
if __name__ == "__main__":
    main()
