"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""


from pipeline import pipelineStates
from util import const
from util import consoleLog
import zmq

zmq.asyncio.install()

context = zmq.asyncio.Context()

# inits Sender and reciver Sockets for the Module
sender = context.socket(zmq.PUB)


def main():
    consoleLog.Warning("Initing zmq")

    sender.bind("tcp://" + "*:5001")

    consoleLog.PipeLine_Ok("running zmq")
    watchdog = 0

    consoleLog.Warning("running VideoProcessing Pipeline...")

    # sets pipeline starting state so Fsm has all needed to run
    pipe = pipelineStates.PipeLine()
    pipe.on_event(pipelineStates.States.SETUP_PIPELINE, sender)
    pipe.on_event(pipelineStates.States.TRAIN_MODEL, sender)
    pipe.on_event(pipelineStates.States.RUN_RECONITION, sender)

    """    
        if(topic == "MANAGER" and status['mode'] == "stopcv"):
            sender.send_string("SHUTDOWN")
            sender.send_json({"mode":"shutdown","restart":False,"time":str(datetime.now())})
            consoleLog.Warning("Shutting down Opencv Pipeline ...")
            consoleLog.Error("by wor")
            break
    """


if __name__ == "__main__":
    main()
