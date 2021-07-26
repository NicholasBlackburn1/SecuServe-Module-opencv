"""
this class is for handling the User data 
Passes data into class validate class data
like if the user daya is empty i test the data if its 

"""

import dataclasses
import validators

@dataclasses.dataclass
class UserData(object):
    user: str = ""
    status: str= ""
    image: str = ""
    downloadUrl: str= ""
    phoneNum: str   = ""
    
    
    # sets user name in structure
    def setUserName(self,name):
        Username = str(name)
        
        if(Username == "" or  None ):
            raise(TypeError("Cant have No Name the user name"))
        if (Username.isnumeric):
              raise(TypeError("Cant have a number user name "))
        else:
            self.user = Username.lower()
         
         
        # sets user status in structure
    def setUserStatus(self,status):
        stat = str(status)
        
        if(stat == "" or  None ):
            raise(TypeError("Cant have No Name status"))
        if (stat.isnumeric):
              raise(TypeError("Cant have a number in the status "))
        else:
            self.status = stat 
         
            
       
        # sets user image in structure
    def setUserImg(self,img):
        imgage = str(img)
        
        if(imgage == "" or  None ):
            raise(TypeError("Cant have No Image"))
        else:
            self.image = imgage 
            
    
    # checks url to see if tis formatted correctly   
    def setUserUrl(self,url):
        checkyurl = str(url)
       
        if(checkyurl == "" or None):
            raise(TypeError("Cant have No URL"))
    
        else:
            self.downloadUrl = str(url)
           
           
           
            
      
    # checks url to see if tis formatted correctly   
    def setUserPhoneNumber(self,phonenumber):
        checkyurl = str(phonenumber)
       
        if(checkyurl == "" or None):
            raise(TypeError("Cant have No PhoneNumber"))
        
        if(checkyurl.isnumeric() and checkyurl.index(0) == 0):
          self.downloadUrl = 4123891615
          
        else:
            self.downloadUrl = checkyurl
           
           
           
            
        
    
    
