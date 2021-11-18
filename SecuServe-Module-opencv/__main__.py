"""
This class is for running my video pipeline 
TODO: add code to launc from zmq
"""


from zmq.sugar import poll
from pipeline import pipelineStates

from util import consoleLog
import zmq
import imagezmq

context = zmq.Context()

# inits Sender and reciver Sockets for the Module
sender = context.socket(zmq.PUB)
receiver = context.socket(zmq.SUB)
imagesocket = None

receiver.setsockopt(zmq.SUBSCRIBE, b"")


poller = zmq.Poller()
poller.register(receiver, zmq.POLLIN)


def main():
    watchdog = 0

    consoleLog.Warning("Initing zmq")

    sender.bind("tcp://" + "127.0.0.1:5001")
    receiver.connect("tcp://" + "127.0.0.1:5000")
    imagesocket = imagezmq.ImageSender(connect_to="tcp://127.0.0.1:5555", REQ_REP=False)

    consoleLog.PipeLine_Ok("running zmq")
    consoleLog.Warning("running VideoProcessing Pipeline...")



    # sets pipeline starting state so Fsm has all needed to run
    pipe = pipelineStates.PipeLine()
    pipe.on_event(pipelineStates.States.SETUP_PIPELINE, sender,receiver,poller,imagesocket)
    pipe.on_event(pipelineStates.States.TRAIN_MODEL, sender,receiver,poller,imagesocket)
    pipe.on_event(pipelineStates.States.RUN_RECONITION, sender,receiver,poller,imagesocket)


if __name__ == "__main__":
    main()
