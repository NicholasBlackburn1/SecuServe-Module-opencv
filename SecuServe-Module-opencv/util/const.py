"""
dirty const setup 
"""

import imports

# this is all the global paths needed throuht the program
PATH = str(imports.pathlib.Path().absolute()) + "/data/" + "Config.ini"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

unknown_faces = 0
watchdog = 0

imports.os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
print(PATH)
# Read config.ini file
config_object = imports.ConfigParser()
config_object.read(PATH)

logconfig = config_object["LOGGING"]
zmqconfig = config_object["ZMQ"]
opencvconfig = config_object["OPENCV"]
fileconfig = config_object["FILE"]
phoneconfig = config_object["PHONE"]

current_time = imports.datetime.now()

rootDirPath = fileconfig["rootDirPath"]
configPath = fileconfig["rootDirPath"] + fileconfig["configPath"]
imagePath = fileconfig["rootDirPath"] + fileconfig["imagePath"]
imagePathusers = fileconfig["rootDirPath"] + fileconfig["imagePathusers"]
plateImagePath = fileconfig["rootDirPath"] + fileconfig["platePath"]
loggingPath = fileconfig["rootDirPath"] + fileconfig["loggingPath"]


adminPath = str(
    fileconfig["rootDirPath"] + fileconfig["imagePath"] + fileconfig["adminimg"]
)
usrPath = str(
    fileconfig["rootDirPath"] + fileconfig["imagePath"] + fileconfig["usrimg"]
)
unwantedPath = str(
    fileconfig["rootDirPath"] + fileconfig["imagePath"] + fileconfig["unwantedimg"]
)
unknownPath = str(
    fileconfig["rootDirPath"] + fileconfig["imagePath"] + fileconfig["unknownimg"]
)
groupPath = str(
    fileconfig["rootDirPath"] + fileconfig["imagePath"] + fileconfig["groupimg"]
)
Modelpath = str(imagePathusers + "Face.Model")


userList = []


imports.logging.basicConfig(level=imports.logging.INFO, format="%(message)s")
logger = imports.logging.getLogger()
# logger.addHandler(imports.logging.FileHandler(str(loggingPath)+"Cv_PipeLine"+str(current_time)+".uwu", 'a'))

default_endpoint = "https://textbelt.com/text"

system_on_led = 12  # BOARD pin 12
processing_led = 18  # BOARD pin 18
reconizing_face = 20

admin_pic_url = "http://192.168.5.8/admin"
user_pic_url = "http://192.168.5.8/user"
unwanted_pic_url = "http://192.168.5.8/unwanted"
unknown_pic_url = "http://192.168.5.8/unknown"
group_pic_url = "http://192.168.5.8/group"


facepredict = 0

StopingMess = "Stoping face prossesing timer in"

faceTolorace = 0.56

isdevpc = True
