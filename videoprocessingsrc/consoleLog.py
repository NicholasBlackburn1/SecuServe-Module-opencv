"""
Simple Debuging Colorizer for the console uwu
"""
import __init__

def Debug(text):
    print(__init__.Fore.LIGHTWHITE_EX+str(text))
    print(__init__.Style.RESET_ALL)
  
    return 


def Warning(text):
    print(__init__.Fore.YELLOW+str(text))
    print(__init__.Style.RESET_ALL)
    
    return


def Error(text):
    print(__init__.Fore.RED+str(text))
    print(__init__.Style.RESET_ALL)
  
    return

def PipeLine_Ok(text):
    print(__init__.Fore.GREEN+str(text))
    print(__init__.Style.RESET_ALL)
   
    return

def PipeLine_init(text):
    print(__init__.Fore.LIGHTBLUE_EX + str(text))
    print(__init__.Style.RESET_ALL)
  
    return

def PipeLine_Data(text):
    print(__init__.Fore.LIGHTMAGENTA_EX + str(text))
    print(__init__.Style.RESET_ALL)
 
    return