import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.Hotel import Hotel
from Helper.color import *
from Helper.track import *
BANNER =bcolors.GOLD +"""
============================================ welcome to ==================================================
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ ███╗   ███╗ █████╗  █████╗ ███╗   ██╗    ███╗   ███╗ █████╗ ██╗    ██████╗  ██████╗  ██████╗ ██████╗   │
│ ████╗ ████║██╔══██╗██╔══██╗████╗  ██║    ████╗ ████║██╔══██╗██║    ██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗  │
│ ██╔████╔██║███████║███████║██╔██╗ ██║    ██╔████╔██║███████║██║    ██████╔╝██║   ██║██║   ██║██║  ██║  │
│ ██║╚██╔╝██║██╔══██║██╔══██║██║╚██╗██║    ██║╚██╔╝██║██╔══██║██║    ██╔══██╗██║   ██║██║   ██║██║  ██║  │
│ ██║ ╚═╝ ██║██║  ██║██║  ██║██║ ╚████║    ██║ ╚═╝ ██║██║  ██║██║    ██║  ██║╚██████╔╝╚██████╔╝██████╔╝  │
│ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝   │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘

""" + bcolors.ENDC 


def main():
    hotel = Hotel()
    option = [
        "Check-in guests by channel",
        "Manually check-in guests",
        "Manually check-out guests",
        "Search room",
        "Export to CSV file",
        "Print Available Room",
        "Get Memory Usage",
        "Quit App"
    ]
    
    while True:
        print(BANNER)
        print("--------------------------------------------------------\n")
        print(f"{bcolors.BOLD}{bcolors.LIGHTRED}                 TYPE 1 - {len(option)}                   {bcolors.ENDC}")
        print()
        for i in range(len(option)):
            print(f"{bcolors.DRAKYELLOW}{i + 1} : {option[i]}{bcolors.ENDC}")

        print()
        print("--------------------------------------------------------")
        print()
        input_option = input("Select your option : ")

        if input_option == 'q':
            return
        try:
            input_option = int(input_option)
            
            match input_option:
                case 1: #add by channel
                    print(bcolors.LIGHTGREEN+"\nInput Format\nChannel Name : amount , Channel Name : amount , ...\nExample : Lopburi 10000, Home 1\n" + bcolors.ENDC)
                    channels = list(map(str, input("Input : ").split(",")))
                    hotel.insert(channels=channels)

                    pass
                case 2: # manual add
                    # inp = int(input("Enter guests amount : "))
                    inp = int(input("Enter Room Number : "))
                    hotel.manual_add(count=inp)
                    pass
                case 3: # manual remove
                    inp = int(input("Enter room number : "))
                    hotel.manual_remove(room_number=inp)
                    pass
                case 4: #search room
                    inp = int(input("Enter room number : "))
                    hotel.search(room_number=inp)
                    pass
                case 5: #export to csv
                    hotel.export_to_file()
                    pass
                case 6: #print tree
                    hotel.get_all_available_room()
                    pass
                case 7: #get memory usage
                    memory = get_process_memory()
                    print("=============memory used stat==============")
                    print(f"Function : {bcolors.LIGHTGREEN}Program Memory Used{bcolors.ENDC}")
                    print(f"memory consumed: {bcolors.LIGHTGREEN}{memory:,}{bcolors.ENDC} bytes")
                    print("===========================================")
                case 8: #Quit App
                    return
                case _:
                    raise SyntaxError("Invalid Input Option")
        except:
            print("Invalid Input")
        input("Press enter to continue")
        clear_screen()

def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()


if __name__ == "__main__":
    main()
else:
    raise ImportError("This script cannot be imported as a module")
