"""
This class is for the required opencv
parts 
TODO: Setup pipeline send mesg basted on what part of pipe line its in
TODO: COnvert Pipeline to state macheene
"""


from os import stat
import imports

class RequiredCode(object):
    
    # this allows me to set up pipe line easyerly  but for the cv module
    def setupPipeline(self,sender):
        pipeline_start_setup = imports.datetime.now()
        #this sends a stats message back to the main controller and to the messaging and webserver modules
        self.sendProgramStatus(sender,"setup","seting up pipeline to run",pipeline_start_setup)
        
        imports.gc.enable()
        imports.sys.stdout.write = imports.const.logger.info
        
        if(not imports.os.path.exists(imports.const.rootDirPath)):
            imports.console_Log.Warning("creating Dirs")
            self.makefiledirs()
        
        # prints Config of program, the opencv build info and if opencv is optimized
        imports.console_Log.Debug("Example Config"+str(imports.config.const.PATH))
        imports.console_Log.PipeLine_init(imports.cv2.getBuildInformation())
        imports.console_Log.Warning("is opencv opdemised"+str(imports.cv2.useOptimized()))
        
         # Database connection handing
        imports.console_Log.Warning("Connecting to the Database Faces")
        imports.console_Log.PipeLine_Data( imports.mydb.getFaces())
        imports.console_Log.Warning("connected to database Faces")

        # Updates Data in the Usable data list uwu
        self.UserDataList()

        imports.console_Log.Warning("Setting up cv")

        # Downlaods all the Faces
        self.downloadUserFaces(imports.const.imagePathusers)
        __init__.console_Log.PipeLine_Ok("PipeLine Setup End time"+str( imports.datetime.now() -  pipeline_start_setup))
        
         # updates stats message 
        self.sendProgramStatus(sender,"done","finishes up pipeline to run",imports.datetime.now()-pipeline_start_setup)
       
        self.trainPipeLine(sender)
            
    # This trains the face model for the  pipeline
    def trainPipeLine(self,sender):
        pipeline_train_knn = imports.datetime.now()
         # updates stats message 
        self.sendProgramStatus(sender,"training","starting  to train model",imports.datetime.now() - pipeline_train_knn)
       
        imports.console_Log.Warning("Training Model Going to take a while UwU..... ")
        imports.knnClasifiyer.train(train_dir=imports.const.imagePathusers,
                  model_save_path=imports.const.Modelpath, n_neighbors=2)
        
        imports.console_Log.PipeLine_Ok("Done Train Knn pipeline timer" + str(imports.datetime.now() - pipeline_train_knn))
        imports.console_Log.Warning("Done Training Model.....")
        
        self.sendProgramStatus(sender,"done","done  training model",imports.datetime.now() - pipeline_train_knn)
       
        # cleans mess as we keep prosessing
        imports.gc.collect()
        self.reconitionPipeline(sender)
        
        
    def reconitionPipeline(self,sender):
        
          # Camera Stream gst setup
        gst_str = ("rtspsrc location={} latency={}  ! rtph264depay  ! nvv4l2decoder ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert !appsink".format(
            str(imports.const.opencvconfig['Stream_intro']+imports.const.opencvconfig['Stream_ip']+":"+imports.const.opencvconfig['Stream_port']), 400, 720, 480))

        imports.console_Log.Warning("Looking for Faces...")

        i = 0
        face_index = 0
        process_this_frame = 25
        status = None
        pipeline_video_prossesing =  imports.datetime.now()

        cap =  imports.videoThread.ThreadingClass(gst_str)
        face_processing_pipeline_timer =  imports.datetime.now()
        
        #TODO: fix this and remove while 0<1
        while 0 < 1:
            process_this_frame = process_this_frame + 1

            if process_this_frame % 30 == 0:

                frame = cap.read()
                #print(cap.read().get(cv2. CV_CAP_PROP_FPS))
                #frame = cv2.imread("/mnt/SecuServe/user/people/a93121a4-cc4b-11eb-b91f-00044beaf015/a924857a-cc4b-11eb-b91f-00044beaf015 (1).jpg",cv2.IMREAD_COLOR)
                img =  imports.cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                predictions =  imports.knnClasifiyer.predict(
                    img, model_path=imports.const.Modelpath, distance_threshold=0.65)
                # print(process_this_frame)

                """
                    This Section is Dedicated to dealing with user Seperatation via the User Stats data tag
                """
                font =  imports.cv2.FONT_HERSHEY_DUPLEX
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
                            imports.userStats.userUnknown(imports.const.opencvconfig, name, frame, font, imagename=self.imagename, imagePath=self.imagePath,
                                             left=left, right=right, bottom=bottom, top=top, framenum=process_this_frame)
                        # print("user is unknown")
                            imports.logging.info("unknowns Here UwU!")
                            #message.sendCapturedImageMessage("eeeep there is an unknown",4123891615,'http://192.168.5.7:2000/unknown',self.smsconfig['textbelt-key'])
                            imports.console_Log.PipeLine_Ok("stop face prossesing timer unknown" +
                                  str( imports.datetime.now()-face_processing_pipeline_timer))
                          
                            imports.watchdog +=1

                        else:
                            if name in imports.userList[i]:
                                userinfo = imports.userList[i][name]
                                status = userinfo.status
                                name = userinfo.user
                                phone = userinfo.phoneNum

                                if phone == None:
                                    phone = 4123891615

                                #print("User UUID:"+ str(userinfo)+ " "+ str(name) + "   "+ str(status))

                                if (status == 'Admin'):
                                    imports.logging.info(
                                        "got an Admin The name is"+str(name))
                                    imports.userStats.userAdmin(status, name, frame, font, self.imagename,
                                                   imports.const.imagePath, left, right, bottom, top, process_this_frame)
                                    imports.console_Log.PipeLine_Ok("Stping face prossesing timer in admin" + str(imports.datetime.now()-face_processing_pipeline_timer))
                                    imports.watchdog +=1
                                    

                                if (status == 'User'):
                                    imports.logging.info(
                                        "got an User Human The name is"+str(name))
                                    imports.userStats.userUser(status=status, name=name, frame=frame, font=font, imagename=self.imagename,
                                                  imagePath=imports.const.imagePath, left=left, right=right, bottom=bottom, top=top, framenum=process_this_frame)
                                    
                                    imports.console_Log.Warning(
                                        "eeeep there is an User They Might be evil so um let them in"+"  `"+"There Name is:" + str(name))
                                    imports.console_Log.PipeLine_Ok(
                                        "Stping face prossesing timer in user" + str(imports.datetime.now()-face_processing_pipeline_timer))
                                    imports.watchdog +=1

                                if (status == 'Unwanted'):
                                    imports.logging.info(
                                        "got an Unwanted Human The name is"+str(name))
                                    imports.userStats.userUnwanted(status=status, name=name, frame=frame, font=font, imagename=self.imagename,
                                                      imagepath=imports.const.imagePath, left=left, right=right, bottom=bottom, top=top, framenum=process_this_frame)
                                    imports.console_Log.PipeLine_Ok("Stping face prossesing timer in unwanted" + str(
                                    imports.datetime.now()-face_processing_pipeline_timer))
                                    imports.watchdog +=1
                                  

                                if(self.getAmountofFaces(imports.face_recognition, frame) > 1):
                                    imports.userStats.userGroup(frame=frame, font=font, imagename=self.imagename, imagepath=self.imagePath, left=left, right=right, bottom=bottom, top=top)
                                    imports.console_Log.PipeLine_Ok("Stping face prossesing timer in Group" + str(imports.datetime.now()-face_processing_pipeline_timer))
                                    #message.sendCapturedImageMessage("eeeep there is Gagle of Peope I dont know what to do",phone,'http://192.168.5.8:2000/group',self.smsconfig['textbelt-key'])
                                    
                                    

                            else:

                                imports.console_Log.Warning(
                                    "not the correct obj in list" + str(imports.const.userList[i]))
                                # allows counter ro count up to the ammount in the database
                                if(i >  len(imports.const.userList)):
                                    i+=1
                                    
                                # allows the countor to reset to zero 
                                if(i == len(imports.const.userList)):
                                    i=0
                                    
                                    
                                
                                

                    else:

                        imports.console_Log.PipeLine_Ok(
                   
                            "Time For non Face processed frames" + str(imports.datetime.now()-face_processing_pipeline_timer))

                        return

            else:
               
                exit(1001)
            return
        
        
    
    # Makes startup dirs

    def makefiledirs(self):
        imports.console_Log.Warning("Creating Folder Dirs")
        imports.Path(self.rootDirPath).mkdir(parents=True, exist_ok=True)
        imports.Path(self.imagePathusers).mkdir(parents=True, exist_ok=True)
        imports.Path(self.configPath).mkdir(parents=True, exist_ok=True)
        imports.Path(self.plateImagePath).mkdir(parents=True, exist_ok=True)
        imports.console_Log.Warning("Made Folder Dirs")


# Encodes all the Nessiscary User info into Json String so it can be easly moved arround

    def UserDataList(self):
        i = 0

        while True:
            # example Json string  [{"uuid":"Tesla", "name":2, "status":"New York",image:none, url:}]

            # this is Where the Data gets Wrapped into am DataList with uuid First key
            local_data = {
                imports.mydb.getUserUUID(imports.mydb.getFaces(), i): imports.faceDataStruture.UserData(imports.mydb.getName(imports.mydb.getFaces(), i), imports.mydb.getStatus(imports.mydb.getFaces(), i), imports.mydb.getImageName(imports.mydb.getFaces(), i), imports.mydb.getImageUrI(imports.mydb.getFaces(), i), imports.mydb.getPhoneNum(imports.mydb.getFaces(), i))
            }

            __init__.const.userList.append(local_data)

            i += 1

            # Checks to see if i == the database amount hehe
            if(i == __init__.mydb.getAmountOfEntrys()):
                return
# saves downloaded Image Converted to black and white

    def downloadFacesAndProssesThem(self, userData, filepath):

        imports.Path(filepath+"/").mkdir(parents=True, exist_ok=True)
        
        if(not imports.os.path.exists(filepath+userData.image+".jpg")):
            imports.wget.download(userData.downloadUrl, str(filepath))

        # this function will load and prepare face encodes  for
    # Fully Downloades USer Images and Returns No data

    def downloadUserFaces(self, imagePath):

        index = 0

        # gets users names statuses face iamges and the urls from the tuples
        while True:
            imports.userinfo = imports.const.userList[index][imports.mydb.getUserUUID(
                imports.mydb.getFaces(), index)]

         

            self.downloadFacesAndProssesThem(imports.const.userList[index][imports.mydb.getUserUUID(
                imports.mydb.getFaces(), index)], imagePath+str(imports.mydb.getUserUUID(imports.mydb.getFaces(), index)))
            imports.console_Log.PipeLine_Data("downloaded"+" "+str(index+1) +" out of " +str(imports.mydb.getAmountOfEntrys()) + "\n")

            index += 1

            if(index == imports.mydb.getAmountOfEntrys()):
                imports.console_Log.Warning("Done Downloading Images UWU....")
                return

                # Add names of the ecodings to thw end of list


    # Sends Program Status to Socket
    def sendProgramStatus(self,sender,status,pipelinePos,time):
        sender.send_string("PIPELINE")
        sender.send_json({"status":str(status),"pipelinePos":str(pipelinePos),"time": str(time)})
        