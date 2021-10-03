
import imports
from util import const
# Gets the Face Data from the Face data

#TODO: NEED TO ONLY USE LIFE TIME DATABASE FOR FACES 

def getFaces():
    # Read config.ini file
    config_object = imports.ConfigParser()
    config_object.read(const.PATH)

    # Get the password
    database = config_object["DATABASE"]

    engine = imports.db.create_engine('sqlite:////mnt/SecuServe/db.sqlite3')
    connection = engine.connect()
    metadata = imports.db.MetaData()
    faces = imports.db.Table(database['table'], metadata,
                     autoload=True, autoload_with=engine)
    query = imports.db.select([faces])
    result_proxy = connection.execute(query)
    result_set = result_proxy.fetchall()
    return(result_set)


'''
Return the amout of Entrys in the  dataBase 
'''
def getAmountOfEntrys():
    # Read config.ini file
    config_object = imports.ConfigParser()
    config_object.read(const.PATH)

    # Get the password
    database = config_object["DATABASE"]

    engine = imports.db.create_engine('sqlite:////mnt/SecuServe/db.sqlite3')
    Session = imports.sessionmaker(bind=engine)
    session = Session()

    metadata = imports.db.MetaData()
    faces = imports.db.Table(database['table'], metadata,
                     autoload=True, autoload_with=engine)
    databasecount = int(float(session.query(faces).count()))
    return databasecount


def getKey(result_set, i):
    print(result_set[i])
    return result_set[i]


def getID(result_set, i):
    id, useruuid, user, groub, image, imageurl = result_set[i]
    return id

    # gets Database entry name


def getName(result_set, i):
    id, useruuid, user, group, image, imageurl,phoneNum = result_set[i]
    return user


def getStatus(result_set, i):
    id, useruuid, user, group, image, imageurl,phoneNum = result_set[i]
    return group


def getImageName(result_set, i):
    id, useruuid,user, group, image, imageurl,phoneNum = result_set[i]
    return image

def getImageUrI(result_set, i):
    id, useruuid, user, group, image, imageurl,phoneNum = result_set[i]
    return imageurl

def getUserUUID(result_set, i):
    id, useruuid,user, group, image, imageurl,phoneNum = result_set[i]
    return useruuid

def getPhoneNum(result_set, i):
    id, useruuid, user, group, image, imageurl,phoneNum = result_set[i]
    return phoneNum

def getLifefaces(result_set):
    id,seenFaces,seenPlates,seenReconized,seenUnReconized = result_set
    return seenFaces


def getLifePlates(result_set, i):
    id,seenFaces,seenPlates,seenReconized,seenUnReconized = result_set[i]
    return seenPlates
