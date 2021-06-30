"""
This class is for the required opencv
parts 
"""

import __init__

class RequiredCode(object):
    
    # this allows me to set up pipe line easyerly  but for the cv module
    def setupPipeline(self):
        __init__.gc.enable()
        __init__.sys.stdout.write = __init__.logger.info
        
        if(not __init__.os.path.exists(self.rootDirPath)):
            __init__.console_log.Warning("creating Dirs")
            self.makefiledirs()
            
        __init__.console_log.Debug("Example Config"+str(__init__.PATH))
        __init__.console_log.PipeLine_init(__init__.cv2.getBuildInformation())
        __init__.console_log.Warning("is opencv opdemised"+str(__init__.cv2.useOptimized()))
        
         # Database connection handing
        __init__.console_log.Warning("Connecting to the Database Faces")
        __init__.console_log.PipeLine_Data( __init__.db.getFaces())
        __init__.console_log.Warning("connected to database Faces")

        # Updates Data in the Usable data list uwu
        self.UserDataList()

        __init__.console_log.Warning("Setting up cv")

        # Downlaods all the Faces
        self.downloadUserFaces(__init__.imagePathusers)

        __init__.console_log.PipeLine_Ok("PipeLine Setup End time"+str( __init__.datetime.now() -  __init__.pipeline_start_setup))
        return True
            
    # This trains the face model for the  pipeline
    def trainPipeLine(self):
        __init__.console_log.Warning("Training Model Going to take a while UwU..... ")
        __init__.knnClasifiyer.train(train_dir=__init__.imagePathusers,
                  model_save_path=__init__.Modelpath, n_neighbors=2)
        
        __init__.console_log.PipeLine_Ok("Done Train Knn pipeline timer" + str(__init__.datetime.now() - __init__.pipeline_train_knn))
        __init__.console_log.Warning("Done Training Model.....")
        
        # cleans mess as we keep prosessing
        __init__.gc.collect()
        
        
    def reconitionPipeline(self):
          # Camera Stream gst setup
        gst_str = ("rtspsrc location={} latency={}  ! rtph264depay  ! nvv4l2decoder ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert !appsink".format(
            str(self.opencvconfig['Stream_intro']+self.opencvconfig['Stream_ip']+":"+self.opencvconfig['Stream_port']), 400, 720, 480))

        __init__.console_log.Warning("Looking for Faces...")

        i = 0
        face_index = 0
        process_this_frame = 25
        status = None
        pipeline_video_prossesing =  __init__.datetime.now()

        cap =  __init__.videoThread.ThreadingClass(gst_str)
        face_processing_pipeline_timer =  __init__.atetime.now()
        while 0 < 1:
            process_this_frame = process_this_frame + 1

            if process_this_frame % 30 == 0:

                frame = cap.read()
                #print(cap.read().get(cv2. CV_CAP_PROP_FPS))
                #frame = cv2.imread("/mnt/SecuServe/user/people/a93121a4-cc4b-11eb-b91f-00044beaf015/a924857a-cc4b-11eb-b91f-00044beaf015 (1).jpg",cv2.IMREAD_COLOR)
                img =  __init__.cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                predictions =  __init__.knnClasifiyer.predict(
                    img, model_path=self.Modelpath, distance_threshold=0.65)
                # print(process_this_frame)

                """
                    This Section is Dedicated to dealing with user Seperatation via the User Stats data tag
                """
                font =  __init__.cv2.FONT_HERSHEY_DUPLEX
                sent = False

                # Display t he results
                for name, (top, right, bottom, left) in predictions:
                    
                    

                    # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                    top *= 2
                    right *= 2
                    bottom *= 2
                    left *= 2
                    print(process_this_frame)
                    print(name)

                    if(name != None):

                        if(name == 'unknown' and status == None):
                            __init__.userStats.userUnknown(self.opencvconfig, name, frame, font, imagename=self.imagename, imagePath=self.imagePath,
                                             left=left, right=right, bottom=bottom, top=top, framenum=process_this_frame)
                        # print("user is unknown")
                            __init__.logging.info("unknowns Here UwU!")
                            #message.sendCapturedImageMessage("eeeep there is an unknown",4123891615,'http://192.168.5.7:2000/unknown',self.smsconfig['textbelt-key'])
                            __init__.console_log.PipeLine_Ok("stop face prossesing timer unknown" +
                                  str( __init__.datetime.now()-face_processing_pipeline_timer))
                          
                            self.watchdog +=1

                        else:
                            if name in self.userList[i]:
                                userinfo = self.userList[i][name]
                                status = userinfo.status
                                name = userinfo.user
                                phone = userinfo.phoneNum

                                if phone == None:
                                    phone = 4123891615

                                #print("User UUID:"+ str(userinfo)+ " "+ str(name) + "   "+ str(status))

                                if (status == 'Admin'):
                                    __init__.logging.info(
                                        "got an Admin The name is"+str(name))
                                    __init__.userStats.userAdmin(status, name, frame, font, self.imagename,
                                                   self.imagePath, left, right, bottom, top, process_this_frame)
                                    __init__.console_log.PipeLine_Ok("Stping face prossesing timer in admin" + str(datetime.now()-face_processing_pipeline_timer))
                                    __init__.watchdog +=1
                                    

                                if (status == 'User'):
                                    __init__.logging.info(
                                        "got an User Human The name is"+str(name))
                                    __init__.userStats.userUser(status=status, name=name, frame=frame, font=font, imagename=self.imagename,
                                                  imagePath=self.imagePath, left=left, right=right, bottom=bottom, top=top, framenum=process_this_frame)
                                    
                                    __init__.console_log.Warning(
                                        "eeeep there is an User They Might be evil so um let them in"+"  `"+"There Name is:" + str(name))
                                    __init__.console_log.PipeLine_Ok(
                                        "Stping face prossesing timer in user" + str(__init__.datetime.now()-face_processing_pipeline_timer))
                                    __init__.watchdog +=1

                                if (status == 'Unwanted'):
                                    __init__.logging.info(
                                        "got an Unwanted Human The name is"+str(name))
                                    __init__.userStats.userUnwanted(status=status, name=name, frame=frame, font=font, imagename=self.imagename,
                                                      imagepath=self.imagePath, left=left, right=right, bottom=bottom, top=top, framenum=process_this_frame)
                                    __init__.console_log.PipeLine_Ok("Stping face prossesing timer in unwanted" + str(
                                    __init__.datetime.now()-face_processing_pipeline_timer))
                                    __init__.watchdog +=1
                                  

                                if(self.getAmountofFaces(__init__.face_recognition, frame) > 1):
                                    __init__.userStats.userGroup(frame=frame, font=font, imagename=self.imagename, imagepath=self.imagePath, left=left, right=right, bottom=bottom, top=top)
                                    __init__.console_log.PipeLine_Ok("Stping face prossesing timer in Group" + str(__init__.datetime.now()-face_processing_pipeline_timer))
                                    #message.sendCapturedImageMessage("eeeep there is Gagle of Peope I dont know what to do",phone,'http://192.168.5.8:2000/group',self.smsconfig['textbelt-key'])
                                    
                                    

                            else:

                                __init__.console_log.Warning(
                                    "not the correct obj in list" + str(self.userList[i]))
                                # allows counter ro count up to the ammount in the database
                                if(i >  len(self.userList)):
                                    i+=1
                                    
                                # allows the countor to reset to zero 
                                if(i == len(self.userList)):
                                    i=0
                                    
                                    
                                
                                

                    else:

                        __init__.console_log.PipeLine_Ok(
                            "Time For non Face processed frames" + str(__init__.datetime.now()-face_processing_pipeline_timer))

                        return

            else:
                pass
        
        
    
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
