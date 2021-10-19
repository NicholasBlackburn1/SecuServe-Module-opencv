"""
Simple Debuging Colorizer for the console uwu
"""
import imports
from datetime import datetime




def Debug(text):
    dmsgLayout("DEBUG",text)
    return


def Warning(text):
    dmsgLayout("WARNING",text)
    return


def Error(text):
    dmsgLayout("ERROR",text)
    return


def PipeLine_Ok(text):
    dmsgLayout("OK",text)
    return


def PipeLine_init(text):
    dmsgLayout("INIT",text)
    return


def PipeLine_Data(text):
    dmsgLayout("DATA",text)

    return


def dmsgLayout(type,message):
    print(imports.Fore.GREEN + "["+str(datetime.now())+"]"+" "+ imports.Fore.YELLOW + str(type)+":"+" "+imports.Fore.WHITE+str(message))
    print(imports.Style.RESET_ALL)

    