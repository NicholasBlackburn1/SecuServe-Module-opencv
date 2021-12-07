import zmq
from colorama import Fore, Back, Style

context = zmq.Context()
controller = context.socket(zmq.XSUB)
controller.setsockopt(zmq.SUBSCRIBE, b"")
controller.connect("tcp://" + "127.0.0.1:5001")


poller = zmq.Poller()
poller.register(controller, zmq.POLLIN)


print(Fore.LIGHTGREEN_EX + f"Starting Zmq Pipeline Monitor...")
while True:

    evts = dict(poller.poll(timeout=100))
    if controller in evts:

        topic = controller.recv_string()
        status = controller.recv_json()
        print(topic)

        if topic == "PIPELINE":
            print(Fore.YELLOW + f"Topic: {topic} => {status}")
            print(Fore.RESET)

        if topic == "USERS":
            print(Fore.GREEN + f"Topic: {topic} => {status}")
            print(Fore.RESET)

        if topic == "ERROR":
            print(Fore.RED + f"Topic: {topic} => {status}")
            print(Fore.RESET)


        
        if topic == "LIVENESS":
            print(Fore.CYAN + f"Topic: {topic} => {status}")
            print(Fore.RESET)
