from configparser import ConfigParser
from urllib import request

from util import const
from pathlib import Path
from util import consoleLog
import sqlalchemy as db
from sqlalchemy import orm
import requests


###########

#TODO: fix database stuff to communicate with the api server

"""
#! data to grab
   mydb.getName(mydb.getFaces(), i),
                mydb.getStatus(mydb.getFaces(), i),
                mydb.getImageName(mydb.getFaces(), i),
                mydb.getImageUrI(mydb.getFaces(), i),
                mydb.getPhoneNum(mydb.getFaces(), i),
"""


###########

# Gets the Face Data from the Face data
#! this section is for handling all the db interactions with the api server
def getFaces():
    result_set =requests.get(url="http://127.0.0.1:2020/secuserve/api/v1.0/database/faces/getallfaces")
    consoleLog.PipeLine_Data("data from daabase"+ str(result_set.json()))
    return result_set.json()



####

#? gets the user inbfo form the user sb

####
#! gets users from user db
def getUsers():
    result_set =requests.get(url="http://127.0.0.1:2020/secuserve/api/v1.0/database/users/getallusers")
    consoleLog.PipeLine_Data("users from daabase"+ str(result_set.json()))
    return result_set.json()

#! gets the statays of the user
def getStatus(usr_data):
    consoleLog.Warning('User status is'+ str(usr_data[2]) + " for user"+ str(usr_data[1]))
    return usr_data[2]

# gets the user name of the user

def getName(usr_data):
    consoleLog.Warning('User name is'+ str(usr_data[1]) + " for user id"+ str(usr_data[0]))
    return usr_data[1]


#! make sure to rewrite sll the data flow to ue new db method instead of dirty db (reding from db directly)"


"""
Return the amout of Entrys in the  dataBase 
"""


def getAmountOfEntrys():
    # Read config.ini file
    config_object = ConfigParser()
    config_object.read(const.PATH)

    # Get the password
    database = config_object["DATABASE"]

    engine = db.create_engine(
        "sqlite:////home/nicky/Documents/SECUSERVE/SecuServeFiles/db.sqlite3"
    )
    Session = orm.sessionmaker(bind=engine)
    session = Session()

    metadata = db.MetaData()
    faces = db.Table(
        database["table"], metadata, autoload=True, autoload_with=engine
    )
    databasecount = int(float(session.query(faces).count()))
    return databasecount


def getKey(result_set, i):
    print(result_set[i])
    return result_set[i]


def getID(result_set, i):
    id, useruuid, user, groub, image, imageurl = result_set[i]
    return id

    # gets Database entry name


