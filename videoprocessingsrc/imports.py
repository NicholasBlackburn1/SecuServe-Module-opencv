from logging import log
from numbers import Number
import gc
from os.path import join
import shutil
from tokenize import Double
import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import time
import logging
import zmq
from time import sleep
import threading
import sys
import math
from pathlib import Path
from requests import Session
import sqlalchemy as db
import sqlalchemy.dialects.sqlite
from configparser import ConfigParser
from sqlalchemy.orm import sessionmaker
import wget

import pathlib
from configparser import ConfigParser
from logging import log
from numbers import Number

from os.path import join
import shutil
from tokenize import Double
import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import time
import logging
import zmq
from time import sleep
import threading

import math
from pipeline import faceDataStruture as userData
import consoleLog as consoleLog
from pipeline import videoRequired as pipeline

from requests import Session
import sqlalchemy as db
import sqlalchemy.dialects.sqlite
from configparser import ConfigParser
from sqlalchemy.orm import sessionmaker
import wget

import pathlib
from configparser import ConfigParser

from colorama import Fore, Back, Style

import database as mydb

import threading,queue
import zmq.asyncio