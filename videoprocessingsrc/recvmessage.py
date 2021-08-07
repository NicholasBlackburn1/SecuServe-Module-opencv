

import zmq

context = zmq.Context()
controller = context.socket(zmq.SUB)
controller.setsockopt(zmq.SUBSCRIBE, b'')
controller.connect("tcp://"+"127.0.0.1:5001")


poller = zmq.Poller()
poller.register(controller, zmq.POLLIN)

while True:
    
    evts = dict(poller.poll(timeout=.5))
    if controller in evts:
        topic = controller.recv_string()
        status = controller.recv_json()
        print(f"Topic: {topic} => {status}")