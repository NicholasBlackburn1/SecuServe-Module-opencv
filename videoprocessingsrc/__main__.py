"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""
import __init__




def main():
    
    context = __init__.zmq.Context()
    sender = context.socket(__init__.zmq.PUB)
    
    controller = context.socket(__init__.zmq.SUB)
    controller.setsockopt(__init__.zmq.SUBSCRIBE, b'')
    
    sender.bind("tcp://"+"127.0.0.1:5001")
    controller.connect("tcp://"+"127.0.0.1:5000")
    
    print("in Main program")

    while True:
        __init__.console_Log.Debug("Starting the Pipe Line via Controller")
        if(controller.recv_json() == {"controller":"start"}):
            __init__.videoRequired.RequiredCode.setupPipeline(__init__.videoRequired.RequiredCode(),sender)
                
            
if __name__ == "__main__":
    main()
