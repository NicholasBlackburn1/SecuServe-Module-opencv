"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""
import __init__




def main():
    __init__.console_Log.Warning("Initing zmq")
    context = __init__.zmq.Context()
    sender = context.socket(__init__.zmq.PUB)
    
    controller = context.socket(__init__.zmq.SUB)
    controller.setsockopt(__init__.zmq.SUBSCRIBE, b'')
    
    sender.bind("tcp://"+"127.0.0.1:5001")
    controller.connect("tcp://"+"127.0.0.1:5000")
    __init__.console_Log.PipeLine_Ok("running zmq")
    
    __init__.console_Log.Debug("Waiting for Zmq to recv Control Message...")

    while controller.recv_json() != None:
        if(controller.recv_json() == {"controller":"start"}):
            __init__.console_Log.Warning("running VideoProcessing Pipeline...")
            __init__.videoRequired.RequiredCode.setupPipeline(__init__.videoRequired.RequiredCode(),sender)
                
            
if __name__ == "__main__":
    main()
