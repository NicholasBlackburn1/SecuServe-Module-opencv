"""
Simple Debuging Colorizer for the console uwu
"""
import imports


def Debug(text):
    print(imports.Fore.LIGHTWHITE_EX + str(text))
    print(imports.Style.RESET_ALL)

    return


def Warning(text):
    print(imports.Fore.YELLOW + str(text))
    print(imports.Style.RESET_ALL)

    return


def Error(text):
    print(imports.Fore.RED + str(text))
    print(imports.Style.RESET_ALL)

    return


def PipeLine_Ok(text):
    print(imports.Fore.GREEN + str(text))
    print(imports.Style.RESET_ALL)

    return


def PipeLine_init(text):
    print(imports.Fore.LIGHTBLUE_EX + str(text))
    print(imports.Style.RESET_ALL)

    return


def PipeLine_Data(text):
    print(imports.Fore.LIGHTMAGENTA_EX + str(text))
    print(imports.Style.RESET_ALL)

    return
