"""
This class is for the required opencv
parts 
State machine -> Discreet Finite States of of operations and clear transitions of states, seperation of states, trigger signals

TODO: work on getting the total of reconized and unreconized peole there are in the group
TODO: NEED TO REMOVE ANY FOLDER ROM THE TRANING DIR AFTER MODEL BEEN TRAINED
TODO: Check to see if any Users were added to the database so then we can see if the model needs retrained or not


TODO: Need to add model only being trained on adding or removeing of user from database 

TODO: Need to check too see if running on a jetson nano or dev pc so i can run pipeline on dev pc without crassing 

"""


from enum import Enum
from os import stat

#from Jetson.GPIO.gpio import UNKNOWN
import imports
from util import const
import pipeline.pipelineStates as pipelineStates
import pipeline.knnClasifiyer as knnClasifiyer
import pipeline.videoThread as videoThread
import pipeline.userStats as userStats

class Status():
    # enums for the user status 
    ADMIN = 0
    USER = 1
    UNWANTED = 2
    UNKNOWN = None
class RequiredCode(object):

    
    i = 0
    
    # these are vars for storing the num faces that are seen
    Total = 0
    Reconized = 0
    Unreconized = 0
    
    # this allows me to set up pipe line easyerly  but for the cv module
    def setupPipeline(self,sender):
        const.watchdog = 0 
        pipeline_start_setup = imports.datetime.now()
        self.sendProgramStatus(sender,"SETUP_PIPELINE","Starting to run pipleline",imports.datetime.now()-pipeline_start_setup)
        #this sends a stats message back to the main controller and to the messaging and webserver module
        self.setUpIndicatorLight()
        
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
         # updates stats message 
        self.sendProgramStatus(sender,"SETUP_PIPELINE","finishes setup pipeline to run",imports.datetime.now()-pipeline_start_setup)
        return
        
            
    # This trains the face model for the  pipeline
    def trainPipeLine(self,sender):
        
        pipeline_train_knn = imports.datetime.now()
         # updates stats message 
        self.sendProgramStatus(sender,"TRAIN_MODEL","starting  to train model",imports.datetime.now() - pipeline_train_knn)
       
       
        imports.consoleLog.Warning("Training Model Going to take a while UwU..... ")
        knnClasifiyer.train(train_dir=const.imagePathusers,
                  model_save_path=const.Modelpath, n_neighbors=2)
        
        imports.consoleLog.PipeLine_Ok("Done Train Knn pipeline timer" + str(imports.datetime.now() - pipeline_train_knn))
        imports.consoleLog.Warning("Done Training Model.....")
        self.sendProgramStatus(sender,"STAGE_COMPLETE","done training model",imports.datetime.now() - pipeline_train_knn)
        return
    
    def reconitionPipeline(self,sender):
        
        
        self.sendProgramStatus(sender,"SETUP_PIPELINE","Starting Face rec",imports.datetime.now())
         # cleans mess as we keep prosessing
        imports.gc.collect()
    
          # Camera Stream gst setup
        gst_str = ("rtspsrc location={} latency={}  ! rtph264depay  ! nvv4l2decoder ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert !appsink".format(
            str(const.opencvconfig['Stream_intro']+const.opencvconfig['Stream_ip']+":"+const.opencvconfig['Stream_port']), 400, 720, 480))

        imports.consoleLog.Warning("Looking for Faces...")

        
        face_index = 0
        process_this_frame = 5
        status = None
        pipeline_video_prossesing =  imports.datetime.now()

        cap =  videoThread.ThreadingClass("pc")

        pipe = pipelineStates.PipeLine()
        
        #TODO: GET RECONITION TO IDLE when it sees no faces so it does not waste time waiting for faces
        while True:
            process_this_frame = process_this_frame + 1
            
            self.setProcessingLed(True)
            
            if(const.watchdog == 10):
                print("WATCHDOG OVERRAIN")
                self.sendProgramStatus(sender,"ERROR","WATCHDOG OVERRRAN",imports.datetime.now())
                break
                
            if process_this_frame % 10 == 0:
                #frame=imports.cv2.imread("/home/nick/Face-Door_Moudles/Video-processing/data/images/test.jpg")
                #cap.read()
                frame = cap.read()
                img =  imports.cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                predictions =  knnClasifiyer.predict(
                    img, knn_clf= knnClasifiyer.loadTrainedModel(knn_clf =None, model_path=const.Modelpath), distance_threshold=const.faceTolorace
                    )
                # print(process_this_frame)

                """
                    This Section is Dedicated to dealing with user Seperatation via the User Stats data tag
                """
                font =  imports.cv2.FONT_HERSHEY_DUPLEX
                sent = False
                
                userstat =  userStats.UserStats

                # runs like an idle stage so program can wait for face to be recived 
                if(self.getAmmountOfFaces(frame) <= 0):
                    
                    imports.time.sleep(.5)
                    self.setProcessingLed(False)
                    pipe.on_event(pipelineStates.States.IDLE,sender)
                    
                    
                #processes faces when seen
                if(self.getAmmountOfFaces(frame) > 0):
                    face_processing_pipeline_timer =  imports.datetime.now()
                    
                      # allows total var to incrament All Seen Faces
                    self.Total += self.getAmmountOfFaces(frame)
                    self.setProcessingLed(True)
                    # Display t he results
                    for name, (top, right, bottom, left) in predictions:
                    
                        
                        
                        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                        top *= 2
                        right *= 2
                        bottom *= 2
                        left *= 2
                    

                        if(name != None):
                            
                              
                                if name not in const.userList[self.i]:
                                    
                                                    
                                    if(status == Status.UNKNOWN):
                                        userstat.userUnknown(self = userstat,opencvconfig= const.opencvconfig, name=name, frame=frame, font=font, imagename=imports.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%f"), imagepath=const.imagePath,
                                                        left=left, right=right, bottom=bottom, top=top, framenum=process_this_frame,recperesntage=const.facepredict)
                                        imports.logging.info("unknowns Here UwU!")
                                        self.sendUserInfoToSocket(sender=sender,status="Unknown`",user=name,image=const.unknown_pic_url,time= imports.datetime.now(),phonenumber=4123891615)
                                        imports.consoleLog.PipeLine_Ok("stop face prossesing timer unknown" +str( imports.datetime.now()-face_processing_pipeline_timer))
                                        
                                        self.sendFaceCount(sender,self.Total,self.Unreconized,self.Reconized,imports.datetime.now())
                            
                                    if(self.i > len(const.userList[self.i])):
                                        self.i+=1
                                    

                                    
                                if  name in const.userList[self.i]:
                                    
                                    userinfo = const.userList[self.i][name]
                                    
                                    status= userinfo[1]
                                    usrname = userinfo[0]
                                    phone = userinfo[4]
                                    
                                    status = int(status)
                                    
                                
                                    if phone == None or 0000000000:
                                        phone = int(const.phoneconfig['default_num'])

                                    if (status == Status.ADMIN):
                                        self.sendUserInfoToSocket(sender=sender,status=status,user=usrname,image=const.admin_pic_url ,time= imports.datetime.now(),phonenumber=phone)
                                       # imports.logging.info("got an Admin The name is"+str(usrname))
                                        userstat.userAdmin(self=userstat,status="Admin", name=str(usrname), frame=frame, font=font, imagename=imports.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%f"),imagepath=const.imagePath, left=left, right=right, bottom=bottom, top=top, recperesntage=const.facepredict)
                                        imports.consoleLog.PipeLine_Ok(const.StopingMess+"admin" + str(imports.datetime.now()-face_processing_pipeline_timer))
                                 

                                    if (status == Status.USER):
                                        self.sendUserInfoToSocket(sender=sender,status=status,user=usrname,image=const.user_pic_url,time=imports.datetime.now(),phonenumber=phone)
                                        imports.logging.info(
                                            "got an User Human The name is"+str(name))
                                        userstat.userUser(self=userstat,status="User", name=usrname, frame=frame, font=font, imagename=imports.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%f"),imagepath=const.imagePath, left=left, right=right, bottom=bottom, top=top, recperesntage=const.facepredict)
                                        
                                        imports.consoleLog.Warning("eeeep there is an User They Might be evil so um let them in"+"  `"+"There Name is:" + str(name))
                                        imports.consoleLog.PipeLine_Ok(
                                        const.StopingMess +"user" + str(imports.datetime.now()-face_processing_pipeline_timer))
                                

                                    if (status == Status.UNWANTED):
                                        self.sendUserInfoToSocket(sender=sender,status=status,user=usrname,image=const.unwanted_pic_url,time=imports.datetime.now(),phonenumber=phone)
                                        imports.logging.info(
                                            "got an Unwanted Human The name is"+str(usrname))
                                        userstat.userUnwanted(self=userstat,status="Unwanted", name=usrname, frame=frame, font=font, imagename=imports.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%f"),
                                                        imagepath=const.imagePath, left=left, right=right, bottom=bottom, top=top, recperesntage=const.facepredict)
                                        
                                        imports.consoleLog.PipeLine_Ok(const.StopingMess +"unwanted" + str(
                                        imports.datetime.now()-face_processing_pipeline_timer))
                                        

                                    if(self.getAmmountOfFaces(frame) > 2):
                                        self.sendUserInfoToSocket(sender=sender,status="Group",user=name,image=const.group_pic_url,time= imports.datetime.now(),phonenumber=4123891615)
                                        userStats.UserStats.userGroup(self=userstat,frame=frame, font=font, imagename=imports.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%f"), imagepath=const.imagePath, left=left, right=right, bottom=bottom, top=top)
                                        imports.consoleLog.PipeLine_Ok(const.StopingMess +"Group" + str(imports.datetime.now()-face_processing_pipeline_timer))
                                     
                               
                                    

                        else:
                           
                            imports.consoleLog.PipeLine_Ok("Time For non Face processed frames" + str(imports.datetime.now()-face_processing_pipeline_timer))

                            return

                
                if const.watchdog == 10:
                    self.sendProgramStatus(sender,"ERROR","WATCHDOG OVERRRAN",imports.datetime.now())
                    return pipelineStates.States.ERROR

        
               
               

    
    # returns ammount of seenfaces
    def getAmmountOfFaces(self,image):
        return len(imports.face_recognition.face_locations(image, model="cnn",number_of_times_to_upsample=0))
    
    # Makes startup dirs

    def makefiledirs(self):
        imports.consoleLog.Warning("Creating Folder Dirs")
        # sets up base file structure
        imports.Path(const.rootDirPath).mkdir(parents=True, exist_ok=True)
        imports.Path(const.imagePath).mkdir(parents=True, exist_ok=True)
        imports.Path(const.configPath).mkdir(parents=True, exist_ok=True)
        imports.Path(const.plateImagePath).mkdir(parents=True, exist_ok=True)
        imports.Path(const.imagePathusers).mkdir(parents=True, exist_ok=True)

        # the captured images sorted by status path
        imports.Path(const.adminPath).mkdir(parents=True, exist_ok=True)
        imports.Path(const.usrPath).mkdir(parents=True, exist_ok=True)
        imports.Path(const.unknownPath).mkdir(parents=True, exist_ok=True)
        imports.Path(const.unwantedPath).mkdir(parents=True, exist_ok=True)

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
        
            i += 1

            # Checks to see if i == the database amount hehe
            if(i == imports.mydb.getAmountOfEntrys()):
                return
            
   
        
    # saves downloaded Image 

    def downloadFacesAndProssesThem(self, data, filepath):
        # pulls right info from data
        filename = str(data[2])
        url = str(data[3])
        print(url)
        
        imports.Path(filepath+"/").mkdir(parents=True, exist_ok=True)
        
        if(not imports.os.path.exists(filepath+filename)):
            imports.wget.download(url, str(filepath))

    # Fully Downloades USer Images
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
      imports.consoleLog.Warning("sending Program status to zmq socket")
      sender.send_string("PIPELINE")
      sender.send_json({"status":str(status),"pipelinePos":str(pipelinePos),"time": str(time)})
      imports.time.sleep(.5)
      imports.consoleLog.PipeLine_Ok("Sent Program status to zmq socket")
        
        
      
    # Sends Face count to the web server to create database entryies
    def sendFaceCount(self,sender,total,unknown,reconized,time):
      imports.consoleLog.Warning("sending Face count to zmq")
      sender.send_string("FACECOUNT")
      sender.send_json({"total": int(total),"unknown":int(unknown),"reconized":str(reconized),"time": str(time)})
      imports.time.sleep(.5)
      imports.consoleLog.PipeLine_Ok("sent Face Count to zmq socket")
        
        
        
        
     # Sends Seen Users Info to Socket
    def sendUserInfoToSocket(self,sender,status,user,image,time,phonenumber):
        imports.consoleLog.Warning("sending User indo to zmq")
        sender.send_string("USERS")
        sender.send_json({"usr":str(user),"status":str(status),"image":str(image),"phone":str(phonenumber),"Accuracy":str(const.facepredict),"time": str(time)})
        imports.time.sleep(.5)
        imports.consoleLog.PipeLine_Ok("sent User info to zmq socket")
        
    # this sets up the gpio pinout and system light 
    def setUpIndicatorLight(self):
        '''
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(const.system_on_led, GPIO.OUT)  # system on pin set as output
        GPIO.setup(const.processing_led, GPIO.OUT)  # system on pin set as output
   
        GPIO.output(const.system_on_led, 1)
        '''
        pass
        
    # simply controls status lef of program to show user its working / processing
    def setProcessingLed(self,processing):
        '''
        if processing:
            GPIO.output(const.processing_led, 1)
            GPIO.output(const.processing_led, 0)
            GPIO.output(const.processing_led, 1)
            GPIO.output(const.processing_led, 0)
        else:
            GPIO.output(const.processing_led, 0)
        '''
        pass
            
     
     
