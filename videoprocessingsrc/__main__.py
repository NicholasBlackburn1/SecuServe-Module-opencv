"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""

import imports
import pipelineStates
import const

imports.zmq.asyncio.install()

context = imports.zmq.asyncio.Context()

# inits Sender and reciver Sockets for the Module
sender = context.socket(imports.zmq.PUB)
receiver = context.socket(imports.zmq.SUB)

receiver.setsockopt(imports.zmq.SUBSCRIBE, b'')

def main():
    imports.consoleLog.Warning("Initing zmq")
    
    receiver.connect("tcp://"+"127.0.0.1:5000")
    sender.bind("tcp://"+"*:5001") 
    
    imports.consoleLog.PipeLine_Ok("running zmq")
    imports.consoleLog.Debug("Waiting for Zmq to recv Control Message...")
    watchdog = 0
    
    
    poller = imports.zmq.Poller()
    poller.register(receiver, imports.zmq.POLLIN)
        
    while True:
    
    
        
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
