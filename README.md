# MaanMaiRood
KMITL-OOD Project
Project 

---

## Team Members

| Name         | Student ID   |
|--------------|--------------|
| Teerawat Lappanich        | 67010448 |
| Nethitorn Suthumwaraporn  | 67010497 |
| Paramed Rojlorsakul       | 67010534 |
| Teepob Mahasuk            | 67011464 |

---

> **KMITL-OOD Project**  
> 

---
## Project Overview

This Python code defines a Hotel class that serves as a management system for hotel rooms. The core of this system is an AVL Tree, a self-balancing binary search tree. This choice of data structure is crucial as it ensures that operations like adding, removing, and searching for rooms are very efficient (typically with a time complexity of $O(\log n)$), even with a large number of rooms.

Key Methods and Functionality

insert(channels): This is the primary method for adding rooms in bulk. It takes a list of channels (sources, e.g., "Online_Booking", "Walk-in") and the number of rooms for each, then populates the AVL tree. It uses a helper method, add_room, to perform the actual insertion.
add_room(channels): This internal method iterates through the provided channels and amounts. For each room, it generates a unique name (e.g., channelName_channelIndex_roomIndex_batchNumber) and calculates a unique room number using a custom formula (Formula.triangular_accumulate).
manual_add(count): Allows for the manual addition of a single room with a specific room number (count). It first checks if the room number is already occupied before adding it.
manual_remove(room_number): Removes a specific room from the hotel system by its room number. It includes a check to see if the room exists before attempting removal.
search(room_number): Searches for a room by its number and prints its details if found, or a "Room Not Found" message otherwise.get_all_available_room(): Retrieves and prints a list of all currently occupied rooms in sorted order (due to the inorder traversal of the AVL tree).
export_to_file(): Exports the list of all occupied rooms into a CSV file named hotel.csv.

Important Implementation Details

tqdm Progress Bar: During bulk room additions, the code uses the tqdm library to provide a user-friendly progress bar, which is helpful for long-running operations.
@track Decorator: The methods for adding, removing, searching, and exporting are decorated with @track. This suggests the decorator is likely used for performance tracking, such as measuring how long each operation takes to complete.


---

## Dependencies

- [`psutil`](https://pypi.org/project/psutil/) — for querying memory usage from the OS.

---

## Getting Started
To run this project locally, ensure you have Python installed. Then, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PluemDontKnowToCode/MaanMaiRood.git
   ```
2. **Set Up Project**:

   For Windows:
   ```bash
   cd MaanMaiRood
   python -m venv venv
   venv/bin/activate
   pip install -r requirements.txt
   ```
   For Linux/ macOS
   ```bash
   cd MaanMaiRood
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run Project**
   ```bash
   cd MaanMaiRood
   python -u src/main.py
   ```
   or use **run.bat** for Windows.
