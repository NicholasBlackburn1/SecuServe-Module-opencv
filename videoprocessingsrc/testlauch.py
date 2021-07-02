import zmq

context = zmq.Context()
socketrecv = context.socket(zmq.PUB)
socketrecv.bind("tcp://"+"127.0.0.1"+":"+"5000")

print("Sending start sig")
socketrecv.send_json({"controller": "Start"})
print("sent start sig")