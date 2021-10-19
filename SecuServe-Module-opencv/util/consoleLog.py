"""
Simple Debuging Colorizer for the console uwu
"""
import imports
from datetime import datetime


def Debug(text):
    dmsgLayout("DEBUG", imports.Fore.LIGHTBLUE_EX, text)
    return


def Warning(text):
    dmsgLayout("WARNING", imports.Fore.YELLOW, text)
    return


def Error(text):
    dmsgLayout("ERROR", imports.Fore.RED, text)
    return


def PipeLine_Ok(text):
    dmsgLayout("OK", imports.Fore.LIGHTGREEN_EX, text)
    return


def PipeLine_init(text):
    dmsgLayout("INIT", imports.Fore.LIGHTMAGENTA_EX, text)
    return


def PipeLine_Data(text):
    dmsgLayout("DATA", imports.Fore.LIGHTCYAN_EX, text)

    return


def dmsgLayout(type, color, message):
    print(
        imports.Fore.GREEN
        + "["
        + str(datetime.now())
        + "]"
        + " "
        + color
        + str(type)
        + ":"
        + " "
        + imports.Fore.WHITE
        + str(message)
    )
    print(imports.Style.RESET_ALL)
