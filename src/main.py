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
    "passenger in a car"
    "car in a boat"
    "boat"
    "passenger in a plane"
    "walkin passenger"
]

def main():
    hotel = Hotel()
    option = [
        "Check-in guests by channel",
        "Manully check-in guests",
        "Manully check-out guests",
        "Rearrange room number",
        "Search room",
        "Export to CSV file"
    ]
    print(BANNER)
    while True:
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
                    pass
                case 2: # manual add
                    inp = int(input("Enter guests amount"))
                    hotel.manual_add(inp)
                    pass
                case 3: # manual remove
                    pass
                case 4: #rearrange room
                    pass
                case 5: #search room
                    pass
                case 6: #export to csv
                    pass
                case _:
                    raise SyntaxError("Invalid Input Option")
        except:
            print("Invalid Input")


if __name__ == "__main__":
    main()
else:
    raise ImportError("This script cannot be imported as a module")