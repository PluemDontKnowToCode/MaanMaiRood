from tqdm import tqdm

from Structure.AVLTree_recur import AVLTree  # -> around 70,000 room/sec when adding room
# from Structure.AVLTree import AVLTree  # -> around 90,000 room/sec can go above 100,000 room/sec when adding room 

from Room import Room

from Helper.track import *
from Helper.color import *

class Hotel:
    def __init__(self):
        self.tree = AVLTree()
        self.last_room = 0
        self.last_group = 0
        return
    
    #For requirement 1 requirement 2 and requirement 3
    @track
    def insert(self, channels):
        #temporaly
        passengers , cars , boats, walkins = channels

        total_rooms = passengers * cars * boats + walkins

        self.last_group += 1

        if self.last_room > 0:
            self.tree.update(total_rooms)

        room_count = 0 

        with tqdm(total=total_rooms, desc="Adding rooms", unit="room") as pbar:
            for boat in range(boats, 0, -1):
                for car in range(cars, 0, -1):
                    for passenger in range(passengers, 0, -1):
                        room_count += 1
                        self.tree.add(Room(f"{self.last_group}_{passenger}_{car}_{boat}_{0}", room_count))
                        pbar.update(1) 

            for walkin in range(walkins, 0, -1):
                room_count += 1
                self.add_room(self.last_group, 0,0,0,walkin, room=room_count)
                pbar.update(1) 

        self.last_room += room_count
        return
    

    #Set Guest format
    def add_room(self, group, passenger, car, boat,walkin, room):
        self.tree.add(Room(f"{group}_{passenger}_{car}_{boat}_{walkin}", room))
        return


    #For requirement 4
    @track  
    def manual_add(self, count):
        with tqdm(total=count, desc="Adding rooms", unit="room") as pbar:
            if self.last_room > 0:
                self.tree.update(count)
            for i in range(1, count + 1):
                self.tree.add(Room(f"manual", i))
                pbar.update(1) 
        return
    
    #For requirement 5
    @track  
    def manual_remove(self, room_number):
        self.tree.remove(int(room_number))
        return
    
    @track
    def get_all_available_room(self):
        data = self.tree.inorder()
        if data is None:
            print("\nNo Room\n")
            return 
        for item in data:
            print(item)
    

    #For requirement 7
    @track
    def search(self, room_number):
        result = self.tree.search(room_number)
        op = ""
        if result:
            op = f"{result}"
        else:
            op = "Room Not found"
        print()
        print(op)
       
    #For requirement 11
    @track
    def export_to_file(self):
        self.getCSV()
        return
    
    def getCSV(self):
        data = self.tree.inorder()
        if data is None:
            print("\nNo Room")
            return 
        

        with open("hotel.csv", "w") as f:
            for item in data:
                f.write(str(item) + "\n")
        print("\nExport Success")

