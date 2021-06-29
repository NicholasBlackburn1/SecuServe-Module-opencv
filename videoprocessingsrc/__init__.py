"""
This is were u config the the start up of the app
"""
import dataclasses

import pickle
import os
import wget
import pathlib
import cv2
import logging
import pathlib
from tokenize import Double
from requests import Session
import sqlalchemy as db
import sqlalchemy.dialects.sqlite
from configparser import ConfigParser
from sqlalchemy.orm import sessionmaker
import zmq

import threading
import queue
import math
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
from sklearn import neighbors
import logging
import json
import faceDataStruture as UserData
import requests
import logging
from colorama import init, Fore, Back, Style
import consoleLog

# this is all the global paths needed throuht the program
DATABASE_PATH = str(pathlib.Path().absolute())+"/data/"+"Config.ini"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

watchdog = 0
imagename = datetime.now().strftime("%Y_%m_%d-%I_%M_%S")
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

# gets Config file
print("Example Config"+str(pathlib.Path().absolute()) +
        "/src/prosessing/"+"Config.ini")
# Read config.ini file
config_object = ConfigParser()
config_object.read(str(pathlib.Path().absolute()) +
                    "/src/prosessing/"+"Config.ini")

logconfig = config_object['LOGGING']
zmqconfig = config_object['ZMQ']
opencvconfig = config_object['OPENCV']
fileconfig = config_object['FILE']
smsconfig = config_object['SMS']

current_time = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p_%s")

rootDirPath = fileconfig['rootDirPath']
configPath = fileconfig['rootDirPath']+fileconfig['configPath']
imagePath = fileconfig['rootDirPath'] + fileconfig['imagePath']
imagePathusers = fileconfig['rootDirPath'] + fileconfig['imagePathusers']
plateImagePath = fileconfig['rootDirPath'] + fileconfig['platePath']
loggingPath = fileconfig['rootDirPath'] + fileconfig['loggingPath']

Modelpath = str(imagePathusers+'Face.Model')


userList = []

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler(str(loggingPath)+"Cv_PipeLine"+str(current_time)+".uwu", 'a'))

default_endpoint = 'https://textbelt.com/text'