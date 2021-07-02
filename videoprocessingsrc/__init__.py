"""
This is were u config the the start up of the app
"""
import dataclasses


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

import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
from sklearn import neighbors
import logging

import logging
from colorama import init, Fore, Back, Style
import consoleLog
import faceDataStruture
import knnClasifiyer
from datetime import datetime
import database
import videoRequired
from networkBackend import NetworkManager
import const