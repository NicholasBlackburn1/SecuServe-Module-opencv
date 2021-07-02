"""
dirty const setup 
"""

import __init__


# this is all the global paths needed throuht the program
PATH = str(__init__.pathlib.Path().absolute())+"/data/"+"Config.ini"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

watchdog = 0
imagename = __init__.datetime.now().strftime("%Y_%m_%d-%I_%M_%S")
__init__.os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
# Read config.ini file
config_object = __init__.ConfigParser()
config_object.read(PATH)

logconfig = config_object['LOGGING']
zmqconfig = config_object['ZMQ']
opencvconfig = config_object['OPENCV']
fileconfig = config_object['FILE']
smsconfig = config_object['SMS']

current_time = __init__.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p_%s")

rootDirPath = fileconfig['rootDirPath']
configPath = fileconfig['rootDirPath']+fileconfig['configPath']
imagePath = fileconfig['rootDirPath'] + fileconfig['imagePath']
imagePathusers = fileconfig['rootDirPath'] + fileconfig['imagePathusers']
plateImagePath = fileconfig['rootDirPath'] + fileconfig['platePath']
loggingPath = fileconfig['rootDirPath'] + fileconfig['loggingPath']

Modelpath = str(imagePathusers+'Face.Model')


userList = []


__init__.logging.basicConfig(level=__init__.logging.INFO, format='%(message)s')
logger = __init__.logging.getLogger()
logger.addHandler(__init__.logging.FileHandler(str(loggingPath)+"Cv_PipeLine"+str(current_time)+".uwu", 'a'))

default_endpoint = 'https://textbelt.com/text'


context = __init__.zmq.Context()
socketrecv = context.socket(__init__.zmq.SUB)
socketsend = context.socket(__init__.zmq.PUB)

socketrecv.connect("tcp://"+zmqconfig['ip']+":"+zmqconfig['port'])
socketsend.bind("tcp://"+zmqconfig['ip']+":"+zmqconfig['port-send'])

recv_data = socketrecv.recv_json()