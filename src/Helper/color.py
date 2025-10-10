import random

class bcolors:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    WARNING   = '\033[38;2;255;255;102m'   # yellowish
    FAIL      = '\033[38;2;255;51;51m'     # red
    BLACK     = '\033[38;2;0;0;0m'
    RED       = '\033[38;2;255;0;0m'
    GREEN     = '\033[38;2;0;128;0m'
    LIGHTGREEN= '\033[38;2;102;255;102m'
    YELLOW    = '\033[38;2;255;255;0m'
    DRAKYELLOW= '\033[38;2;204;204;100m'
    BLUE      = '\033[38;2;0;0;255m'
    MAGENTA   = '\033[38;2;255;0;255m'
    CYAN      = '\033[38;2;0;255;255m'
    WHITE     = '\033[38;2;255;255;255m'
    GREY      = '\033[38;2;128;128;128m'
    SKYBLUE   = '\033[38;2;135;206;235m'
    ORANGE    = '\033[38;2;255;165;0m'
    GOLD      = '\033[38;2;240;215;0m'
    LIGHTRED  = '\033[38;2;255;75;75m'

    BG_BLACK   = '\033[48;2;0;0;0m'
    BG_RED     = '\033[48;2;255;0;0m'
    BG_GREEN   = '\033[48;2;0;128;0m'
    BG_YELLOW  = '\033[48;2;255;255;0m'
    BG_BLUE    = '\033[48;2;0;0;255m'
    BG_MAGENTA = '\033[48;2;255;0;255m'
    BG_CYAN    = '\033[48;2;0;255;255m'
    BG_WHITE   = '\033[48;2;255;255;255m'

    def getRandomFrontColor():
        return f'\033[38;2;{random.randint(0,255)};{random.randint(0,255)};{random.randint(0,255)}m'

#how to use
#print(f"{bcolors.OKGREEN}This is green text{bcolors.ENDC}")
#print(f"{bcolors.WARNING}This is yellow text{bcolors.ENDC}") 
#print(f"{bcolors.FAIL}This is red text{bcolors.ENDC}")
#print(f"{bcolors.BOLD}This is bold text{bcolors.ENDC}")
#print(f"{bcolors.UNDERLINE}This is underlined text{bcolors.ENDC}")
#print(f"{bcolors.HEADER}This is header text{bcolors.ENDC}")
#print(f"{bcolors.GREY}This is grey text{bcolors.ENDC}")
#print(f"{bcolors.BG_GREEN}This is with green background{bcolors.ENDC}")
