"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""


from pipeline import pipelineStates

from util import consoleLog
import zmq


context = zmq.Context()

# inits Sender and reciver Sockets for the Module
sender = context.socket(zmq.PUB)
receiver = context.socket(zmq.SUB)

receiver.setsockopt(zmq.SUBSCRIBE, b"")


def main():
    consoleLog.Warning("Initing zmq")

    sender.bind("tcp://" + "127.0.0.1:5001")
    receiver.connect("tcp://" + "127.0.0.1:5000")

    consoleLog.PipeLine_Ok("running zmq")

    watchdog = 0

    consoleLog.Warning("running VideoProcessing Pipeline...")

    # sets pipeline starting state so Fsm has all needed to run
    pipe = pipelineStates.PipeLine()
    pipe.on_event(pipelineStates.States.SETUP_PIPELINE, sender,receiver)
    pipe.on_event(pipelineStates.States.TRAIN_MODEL, sender,receiver)
    pipe.on_event(pipelineStates.States.RUN_RECONITION, sender,receiver)


if __name__ == "__main__":
    main()
