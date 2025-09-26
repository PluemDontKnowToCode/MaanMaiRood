import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.Hotel import Hotel

BANNER = """

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
    return

if __name__ == "__main__":
    main()
else:
    raise ImportError("This script cannot be imported as a module")