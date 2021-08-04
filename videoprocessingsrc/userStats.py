"""
User stas this is where i have the seperate classes for the main opencv 
"""

import imports

class UserStats(object):

    # saves owner images and sends Frame
    def saveImage(self,imagepath, imagename, frame):
        imports.cv2.imwrite(imagepath + imagename + ".jpg", frame)


    # this is for Handling User Admin Stats
    def userAdmin(self,status,name,frame,font,imagename,imagePath,left,right,bottom,top,framenum):
        
            print(status)
            # Draw a box around the face
            imports.cv2.rectangle(frame, (left, top),
                        (right, bottom), (0, 255, 0), 2)


            imports.cv2.putText(frame, name, (left, top),
                        font, 0.5, (255, 255, 255), 1)
            imports.cv2.putText(
                frame, "Known Person..", (0,
                                        430), font, 0.5, (255, 255, 255), 1
            )
            imports.cv2.putText(frame, status, (0, 450),
                        font, 0.5, (255, 255, 255), 1)
            imports.cv2.putText(frame, name, (0, 470), font,
                        0.5, (255, 255, 255), 1)
                
            imports.cv2.putText(frame, "Frame num" + str(framenum), (0, 480), font,
                    0.5, (255, 255, 255), 1)

            self.saveImage(self,imagepath=imagePath+"Admin/",imagename=imagename,frame=frame)


    # User Grade Status
    # this is for Handling User Stats
    def userUser(self,status,name,frame,font,left,right,bottom,top,framenum,imagename,imagepath):

        # Draw a box around the face
        imports.cv2.rectangle(frame, (left, top),
                    (right, bottom), (255, 255, 0), 2)


        imports.cv2.putText(frame, name, (left, top),
                    font, 0.5, (255, 255, 255), 1)
        imports.cv2.putText(
            frame, "Known Person..", (0,
                                    430), font, 0.5, (255, 255, 255), 1
        )
        imports.cv2.putText(
            frame, status, (0,
                            450), font, 0.5, (255, 255, 255), 1
        )
        imports.cv2.putText(frame, name, (0, 470), font,
                    0.5, (255, 255, 255), 1)

        
        imports.cv2.putText(frame, "Frame num" + str(framenum), (0, 480), font,
                    0.5, (255, 255, 255), 1)

        # Distance info
        imports.cv2.putText(
            frame,
            "T&B" + str(top) + "," + str(bottom),
            (474, 430),
            font,
            0.5,
            (255, 255, 255),
            1,
        )
        self.saveImage(self,imagepath=imagepath+"User/",imagename=imagename,frame=frame)
      


    # Handles Unwanted Usr Stats
    def userUnwanted(self,status,name,frame,font,imagename,imagePath,left,right,bottom,top):
        
            imports.cv2.rectangle(frame, (left, top),
                        (right, bottom), (0, 0, 255), 2)
            imports.cv2.putText(frame, name, (left, top),
                        font, 0.5, (255, 255, 255), 1)
            imports.cv2.putText(frame, str(status), (left, top),
                    font, 0.5, (255, 255, 255), 1)

            self.saveImage(imagepath=imagePath+"Unwanted/",imagename=imagename,frame=frame)
            
            
            
    # Handles unKnown User
    def userUnknown(self,opencvconfig,name,frame,font,imagePath,imagename,left,right,bottom,top,framenum):

            imports.cv2.rectangle(frame, (left, top),
                        (right, bottom), (0, 0, 255), 2)
            imports.cv2.putText(frame, name, (left, top),
                        font, 0.5, (255, 255, 255), 1)
                    
            imports.cv2.putText(frame, "Frame num" + str(framenum), (0, 480), font,
                        0.5, (255, 255, 255), 1)

            # Distance info
            imports.cv2.putText(frame, opencvconfig['unreconizedPerson'], (0, 450),
                        font, 0.5, (255, 255, 255), 1)
            imports.cv2.putText(frame, name, (0, 470), font,
                        0.5, (255, 255, 255), 1)
            
            self.saveImage(self,imagepath=imagePath+"unknown/",imagename=imagename,frame=frame)
            

    # User Groups 
    def userGroup(self,frame,font,imagePath,imagename,left,right,bottom,top):
        
                imports.cv2.rectangle(
                    frame, (left, top), (right,
                                        bottom), (255, 0, 255), 2
                )
                imports.cv2.putText(frame, "Group", (left, top),
                            font, 0.5, (255, 255, 255), 1)

                # Distance info
                imports.cv2.putText(
                    frame,
                    "There's a group..",
                    (474, 430),
                    font,
                    0.5,
                    (255, 255, 255),
                    1,
                )
                imports.cv2.putText(
                    frame,
                    "be carfull now!",
                    (474, 450),
                    font,
                    0.5,
                    (255, 255, 255),
                    1,
                )
