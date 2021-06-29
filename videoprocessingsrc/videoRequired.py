"""
This class is for the required opencv
parts 
"""

import __init__

class RequiredCode(object):
    
    # Makes startup dirs

    def makefiledirs(self):
        __init__.console_log.Warning("Creating Folder Dirs")
        __init__.Path(self.rootDirPath).mkdir(parents=True, exist_ok=True)
        __init__.Path(self.imagePathusers).mkdir(parents=True, exist_ok=True)
        __init__.Path(self.configPath).mkdir(parents=True, exist_ok=True)
        __init__.Path(self.plateImagePath).mkdir(parents=True, exist_ok=True)
        __init__.console_log.Warning("Made Folder Dirs")


# Encodes all the Nessiscary User info into Json String so it can be easly moved arround

    def UserDataList(self):
        i = 0

        while True:
            # example Json string  [{"uuid":"Tesla", "name":2, "status":"New York",image:none, url:}]

            # this is Where the Data gets Wrapped into am DataList with uuid First key
            local_data = {
                __init__.db.getUserUUID(__init__.db.getFaces(), i): __init__.UserData(__init__.db.getName(__init__.db.getFaces(), i), __init__.db.getStatus(__init__.db.getFaces(), i), __init__.db.getImageName(__init__.db.getFaces(), i), __init__.db.getImageUrI(__init__.db.getFaces(), i), __init__.db.getPhoneNum(__init__.db.getFaces(), i))
            }

            __init__.userList.append(local_data)

            i += 1

            # Checks to see if i == the database amount hehe
            if(i == __init__.db.getAmountOfEntrys()):
                return
# saves downloaded Image Converted to black and white

    def downloadFacesAndProssesThem(self, userData, filepath):

        __init__.Path(filepath+"/").mkdir(parents=True, exist_ok=True)
        
        if(not __init__.os.path.exists(filepath+userData.image+".jpg")):
            __init__.wget.download(userData.downloadUrl, str(filepath))

        # this function will load and prepare face encodes  for
    # Fully Downloades USer Images and Returns No data

    def downloadUserFaces(self, imagePath):

        index = 0

        # gets users names statuses face iamges and the urls from the tuples
        while True:
            __init__.userinfo = self.userList[index][__init__.db.getUserUUID(
                __init__.db.getFaces(), index)]

         

            self.downloadFacesAndProssesThem(__init__.userList[index][__init__.db.getUserUUID(
                __init__.db.getFaces(), index)], imagePath+str(__init__.db.getUserUUID(__init__.db.getFaces(), index)))
            __init__.console_log.PipeLine_Data("downloaded"+" "+str(index) +" out of " +str(__init__.db.getAmountOfEntrys()) + "\n")

            index += 1

            if(index == __init__.db.getAmountOfEntrys()):
                __init__.console_log.Warning("Done Downloading Images UWU....")
                return

                # Add names of the ecodings to thw end of list
