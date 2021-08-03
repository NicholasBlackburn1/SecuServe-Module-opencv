"""
This class is for the required opencv
parts 
TODO: Setup pipeline send mesg basted on what part of pipe line its in
TODO: COnvert Pipeline to state machine
State machine -> Discreet Finite States of of operations and clear transitions of states, seperation of states, trigger signals, 

"""


from os import stat
import imports
import const
import pipelineStates
import knnClasifiyer
import videoThread

class RequiredCode(object):
    
    # this allows me to set up pipe line easyerly  but for the cv module
    def setupPipeline(self):
        pipeline_start_setup = imports.datetime.now()
        #this sends a stats message back to the main controller and to the messaging and webserver module
        
        imports.gc.enable()
        imports.sys.stdout.write = const.logger.info
        
        if(not imports.os.path.exists(const.rootDirPath)):
            imports.consoleLog.Warning("creating Dirs")
            self.makefiledirs()
        
        # prints Config of program, the opencv build info and if opencv is optimized
        imports.consoleLog.Debug("Example Config"+str(const.PATH))
        imports.consoleLog.PipeLine_init(imports.cv2.getBuildInformation())
        imports.consoleLog.Warning("is opencv opdemised"+str(imports.cv2.useOptimized()))
        
         # Database connection handing
        imports.consoleLog.Warning("Connecting to the Database Faces")
        imports.consoleLog.PipeLine_Data( imports.mydb.getFaces())
        imports.consoleLog.Warning("connected to database Faces")

        # Updates Data in the Usable data list uwu
        self.UserDataList()

        imports.consoleLog.Warning("Setting up cv")

        # Downlaods all the Faces
        self.downloadUserFaces(const.imagePathusers)
        imports.consoleLog.PipeLine_Ok("STAGE COMPLETE"+str( imports.datetime.now() -  pipeline_start_setup))
        return
         # updates stats message 
        #self.sendProgramStatus(sender,enums.PipeLineStates.STAGE_COMPLETE,"finishes up pipeline to run",imports.datetime.now()-pipeline_start_setup)
        
        
            
    # This trains the face model for the  pipeline
    def trainPipeLine(self):
        pipeline_train_knn = imports.datetime.now()
         # updates stats message 
        #self.sendProgramStatus(sender,enums.PipeLineStates.TRAIN_MODEL,"starting  to train model",imports.datetime.now() - pipeline_train_knn)
       
        imports.consoleLog.Warning("Training Model Going to take a while UwU..... ")
        knnClasifiyer.train(train_dir=const.imagePathusers,
                  model_save_path=const.Modelpath, n_neighbors=2)
        
        imports.consoleLog.PipeLine_Ok("Done Train Knn pipeline timer" + str(imports.datetime.now() - pipeline_train_knn))
        imports.consoleLog.Warning("Done Training Model.....")
        return
        #self.sendProgramStatus(sender,enums.PipeLineStates.STAGE_COMPLETE,"done  training model",imports.datetime.now() - pipeline_train_knn)
        
    def reconitionPipeline(self):
        
         # cleans mess as we keep prosessing
        imports.gc.collect()
    
          # Camera Stream gst setup
        gst_str = ("rtspsrc location={} latency={}  ! rtph264depay  ! nvv4l2decoder ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert !appsink".format(
            str(const.opencvconfig['Stream_intro']+const.opencvconfig['Stream_ip']+":"+const.opencvconfig['Stream_port']), 400, 720, 480))

        imports.consoleLog.Warning("Looking for Faces...")

        i = 0
        face_index = 0
        process_this_frame = 25
        status = None
        pipeline_video_prossesing =  imports.datetime.now()

        cap =  videoThread.ThreadingClass(gst_str)
        face_processing_pipeline_timer =  imports.datetime.now()
        
        #TODO: GET RECONITION TO IDLE when it sees no faces so it does not waste time waiting for faces
        while True:
            process_this_frame = process_this_frame + 1
            
            if(const.watchdog == 10):
                print("WATCHDOG OVERRAIN")
                break
                
            if process_this_frame % 30 == 0:

                frame = cap.read()
                img =  imports.cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                predictions =  knnClasifiyer.predict(
                    img, knn_clf= knnClasifiyer.loadTrainedModel(knn_clf =None, model_path=const.Modelpath), distance_threshold=0.65)
                # print(process_this_frame)

                """
                    This Section is Dedicated to dealing with user Seperatation via the User Stats data tag
                """
                font =  imports.cv2.FONT_HERSHEY_DUPLEX
                sent = False

                if(self.getAmmountOfFaces(frame) <= 0):
                    imports.consoleLog.Warning("No faces seen waiting for faces")
                    pipeline.on_event(pipelineStates.States.IDLE) 
                              
                if(self.getAmmountOfFaces(frame) > 0):
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
                                imports.consoleLog.PipeLine_Ok("stop face prossesing timer unknown" +
                                    str( imports.datetime.now()-face_processing_pipeline_timer))
                            
                                imports.watchdog +=1

                            else:
                                if name in const.userList[i]:
                                    userinfo = const.userList[i][name]
                                    status = userinfo[2]
                                    name = userinfo[1]
                                    phone = userinfo[4]

                                    if phone == None or 0000000000:
                                        phone = 4123891615

                                    #print("User UUID:"+ str(userinfo)+ " "+ str(name) + "   "+ str(status))

                                    if (status == 'Admin'):
                                        imports.logging.info(
                                            "got an Admin The name is"+str(name))
                                        imports.userStats.userAdmin(status, name, frame, font, self.imagename,
                                                    imports.const.imagePath, left, right, bottom, top, process_this_frame)
                                        imports.consoleLog.PipeLine_Ok("Stping face prossesing timer in admin" + str(imports.datetime.now()-face_processing_pipeline_timer))
                                        imports.watchdog +=1 

                                    if (status == 'User'):
                                        imports.logging.info(
                                            "got an User Human The name is"+str(name))
                                        imports.userStats.userUser(status=status, name=name, frame=frame, font=font, imagename=self.imagename,
                                                    imagePath=imports.const.imagePath, left=left, right=right, bottom=bottom, top=top, framenum=process_this_frame)
                                        
                                        imports.consoleLog.Warning(
                                            "eeeep there is an User They Might be evil so um let them in"+"  `"+"There Name is:" + str(name))
                                        imports.consoleLog.PipeLine_Ok(
                                            "Stping face prossesing timer in user" + str(imports.datetime.now()-face_processing_pipeline_timer))
                                        

                                    if (status == 'Unwanted'):
                                        imports.logging.info(
                                            "got an Unwanted Human The name is"+str(name))
                                        imports.userStats.userUnwanted(status=status, name=name, frame=frame, font=font, imagename=self.imagename,
                                                        imagepath=imports.const.imagePath, left=left, right=right, bottom=bottom, top=top, framenum=process_this_frame)
                                        imports.consoleLog.PipeLine_Ok("Stping face prossesing timer in unwanted" + str(
                                        imports.datetime.now()-face_processing_pipeline_timer))
                                        
                                    

                                    if(self.getAmountofFaces(imports.face_recognition, frame) > 1):
                                        imports.userStats.userGroup(frame=frame, font=font, imagename=self.imagename, imagepath=self.imagePath, left=left, right=right, bottom=bottom, top=top)
                                        imports.consoleLog.PipeLine_Ok("Stping face prossesing timer in Group" + str(imports.datetime.now()-face_processing_pipeline_timer))
                                        #message.sendCapturedImageMessage("eeeep there is Gagle of Peope I dont know what to do",phone,'http://192.168.5.8:2000/group',self.smsconfig['textbelt-key'])
                                        
                                        

                                else:

                                    imports.consoleLog.Warning(
                                        "not the correct obj in list" + str(imports.const.userList[i]))
                                    # allows counter ro count up to the ammount in the database
                                    if(i >  len(imports.const.userList)):
                                        i+=1
                                        
                                    # allows the countor to reset to zero 
                                    if(i == len(imports.const.userList)):
                                        i=0
                                        
                                        
                                    
                                    

                        else:
                            
                            imports.consoleLog.PipeLine_Ok("Time For non Face processed frames" + str(imports.datetime.now()-face_processing_pipeline_timer))
                            return
                if const.watchdog == 10:
                    break
        
    # returns ammount of seenfaces
    def getAmmountOfFaces(self,image):
        return len(imports.face_recognition.face_locations(image, model="cnn",number_of_times_to_upsample=0))
    
    # Makes startup dirs

    def makefiledirs(self):
        imports.consoleLog.Warning("Creating Folder Dirs")
        imports.Path(self.rootDirPath).mkdir(parents=True, exist_ok=True)
        imports.Path(self.imagePathusers).mkdir(parents=True, exist_ok=True)
        imports.Path(self.configPath).mkdir(parents=True, exist_ok=True)
        imports.Path(self.plateImagePath).mkdir(parents=True, exist_ok=True)
        imports.consoleLog.Warning("Made Folder Dirs")

         
    def covertDictUserData(self,i):
        user =const.userList[i][imports.userData.UserData()]
        print(user)

# Encodes all the Nessiscary User info into Json String so it can be easly moved arround

    def UserDataList(self):
        i = 0

        while True:
            # example Json string  [{"uuid":"Tesla", "name":2, "status":"New York",image:none, url:}]

            # this is Where the Data gets Wrapped into am DataList with uuid First key
            userinfo = imports.userData.UserData(imports.mydb.getName(imports.mydb.getFaces(), i), imports.mydb.getStatus(imports.mydb.getFaces(), i), imports.mydb.getImageName(imports.mydb.getFaces(), i), imports.mydb.getImageUrI(imports.mydb.getFaces(), i), imports.mydb.getPhoneNum(imports.mydb.getFaces(), i))
            local_data = {
                imports.mydb.getUserUUID(imports.mydb.getFaces(), i) : userinfo.__repr__()}

            const.userList.append(local_data)   
            print(local_data)
            
            
            

            i += 1

            # Checks to see if i == the database amount hehe
            if(i == imports.mydb.getAmountOfEntrys()):
                return
            
   
        
# saves downloaded Image Converted to black and white

    def downloadFacesAndProssesThem(self, data, filepath):
        # pulls right info from data
        filename = str(data[2])
        url = str(data[3])
        
        imports.Path(filepath+"/").mkdir(parents=True, exist_ok=True)
        
        if(not imports.os.path.exists(filepath+filename)):
            imports.wget.download(url, str(filepath))

        # this function will load and prepare face encodes  for
    # Fully Downloades USer Images and Returns No data

    def downloadUserFaces(self, imagePath):

        index = 0

        # gets users names statuses face iamges and the urls from the tuples
        while True:
            imports.userinfo = const.userList[index][imports.mydb.getUserUUID(
                imports.mydb.getFaces(), index)]
            
            print(const.userList[index][imports.mydb.getUserUUID(
                imports.mydb.getFaces(), index)])

            self.downloadFacesAndProssesThem(const.userList[index][imports.mydb.getUserUUID(
                imports.mydb.getFaces(), index)], imagePath+str(imports.mydb.getUserUUID(imports.mydb.getFaces(), index)))
            imports.consoleLog.PipeLine_Data("downloaded"+" "+str(index+1) +" out of " +str(imports.mydb.getAmountOfEntrys()) + "\n")

            index += 1

            if(index == imports.mydb.getAmountOfEntrys()):
                imports.consoleLog.Warning("Done Downloading Images UWU....")
                return

                # Add names of the ecodings to thw end of list


    # Sends Program Status to Socket
    def sendProgramStatus(self,sender,status,pipelinePos,time):
        sender.send_string("PIPELINE")
        sender.send_json({"status":str(status),"pipelinePos":str(pipelinePos),"time": str(time)})
        