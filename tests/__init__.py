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
import requests
import logging
from colorama import init, Fore, Back, Style
import videoprocessingsrc.consoleLog
import videoprocessingsrc.faceDataStruture
import videoprocessingsrc.knnClasifiyer

TEST_TRAIN_DIR = str(pathlib.Path().absolute())+"/data/testTraining/"
TEST_FACE_IMAGE = str(pathlib.Path().absolute())+"/data/images/me.jpg"

READIMAGE= cv2.imread(TEST_FACE_IMAGE,cv2.IMREAD_COLOR)
