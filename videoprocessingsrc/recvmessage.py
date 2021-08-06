

import zmq

context = zmq.Context()
controller = context.socket(zmq.SUB)
controller.setsockopt(zmq.SUBSCRIBE, b'')
controller.connect("tcp://"+"127.0.0.1:5001")

while controller.recv() != None:
    print(controller.recv())
    