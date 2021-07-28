"""
dirty const setup 
"""

import imports


# this is all the global paths needed throuht the program
PATH = str(imports.pathlib.Path().absolute())+"/data/"+"Config.ini"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

watchdog = 0
imagename = imports.datetime.now().strftime("%Y_%m_%d-%I_%M_%S")
imports.os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
# Read config.ini file
config_object = imports.ConfigParser()
config_object.read(PATH)

logconfig = config_object['LOGGING']
zmqconfig = config_object['ZMQ']
opencvconfig = config_object['OPENCV']
fileconfig = config_object['FILE']
smsconfig = config_object['SMS']

current_time = imports.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p_%s")

rootDirPath = fileconfig['rootDirPath']
configPath = fileconfig['rootDirPath']+fileconfig['configPath']
imagePath = fileconfig['rootDirPath'] + fileconfig['imagePath']
imagePathusers = fileconfig['rootDirPath'] + fileconfig['imagePathusers']
plateImagePath = fileconfig['rootDirPath'] + fileconfig['platePath']
loggingPath = fileconfig['rootDirPath'] + fileconfig['loggingPath']

Modelpath = str(imagePathusers+'Face.Model')


userList = []


imports.logging.basicConfig(level=imports.logging.INFO, format='%(message)s')
logger = imports.logging.getLogger()
logger.addHandler(imports.logging.FileHandler(str(loggingPath)+"Cv_PipeLine"+str(current_time)+".uwu", 'a'))

default_endpoint = 'https://textbelt.com/text'


print("in const")