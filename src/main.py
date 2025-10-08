import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.Hotel import Hotel

BANNER = """
███╗   ███╗ █████╗  █████╗ ███╗   ██╗███╗   ███╗ █████╗ ██╗██████╗  ██████╗  ██████╗ ██████╗ 
████╗ ████║██╔══██╗██╔══██╗████╗  ██║████╗ ████║██╔══██╗██║██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗
██╔████╔██║███████║███████║██╔██╗ ██║██╔████╔██║███████║██║██████╔╝██║   ██║██║   ██║██║  ██║
██║╚██╔╝██║██╔══██║██╔══██║██║╚██╗██║██║╚██╔╝██║██╔══██║██║██╔══██╗██║   ██║██║   ██║██║  ██║
██║ ╚═╝ ██║██║  ██║██║  ██║██║ ╚████║██║ ╚═╝ ██║██║  ██║██║██║  ██║╚██████╔╝╚██████╔╝██████╔╝
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ 
""" 
CHANNEL_ENTRY = [
    "passenger in a car",
    "car in a boat",
    "boat",
    "walkin passenger"
]
def clear_screen():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()
def main():
    hotel = Hotel()
    option = [
        "Check-in guests by channel",
        "Manully check-in guests",
        "Manully check-out guests",
        "Search room",
        "Export to CSV file",
        "Print All Room",
        "Quit App"
    ]
    
    while True:
        print(BANNER)
        print()
        print("------------------------------------------------")
        print()
        print(f"                 TYPE 1 - {len(option)}                   ")
        print()
        for i in range(len(option)):
            print(f"{i + 1} : {option[i]}")
        print()
        input_option = input("Select your option : ")

        if input_option == 'q':
            return
        try:
            input_option = int(input_option)
            
            match input_option:
                case 1: #add by channel
                    channels = []
                    for i in range(len(CHANNEL_ENTRY)):
                        channels.append(int(input(f"{CHANNEL_ENTRY[i]} : ")))
                    hotel.insert(channels=channels)
                    pass
                case 2: # manual add
                    inp = int(input("Enter guests amount : "))
                    hotel.manual_add(count=inp)
                    pass
                case 3: # manual remove
                    inp = int(input("Enter room number : "))
                    hotel.manual_remove(room_number=inp)
                    pass
                # case 4: #rearrange room
                #     pass
                case 4: #search room
                    inp = int(input("Enter room number : "))
                    print(hotel.search(room_number=inp))
                    pass
                case 5: #export to csv
                    hotel.export_to_csv()
                    pass
                case 6: #print tree
                    hotel.printTree()
                    pass
                case 7: #Quit App
                    return
                case _:
                    raise SyntaxError("Invalid Input Option")
        except:
            print("Invalid Input")
        input("Press enter to continue")
        clear_screen()


if __name__ == "__main__":
    main()
else:
    raise ImportError("This script cannot be imported as a module")