"""
This is were u config the the start up of the app
"""
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
import os
import threading
import queue
import math
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
from sklearn import neighbors
import logging
import json



DATABASE_PATH = str(pathlib.Path().absolute())+"/data/"+"Config.ini"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

