
from Structure.AVLTree import AVLTree
from Helper.track import *
from Room import Room
from Download_csv import *
from tqdm import tqdm

class Hotel:
    def __init__(self):
        self.tree = AVLTree()
        self.last_room = 0
        self.last_group = 0
        return
    
    #For requirement 1 and requirement 3
    @track
    def insert(self, channels):
        #temporaly
        passengers , cars , boats, walkins = channels

        total_rooms = passengers * cars * boats + walkins

        self.last_group += 1

        if self.last_room > 0:
            self.update_room_number(total_rooms)

        room_count = 0 

        with tqdm(total=total_rooms, desc="Adding rooms", unit="room") as pbar:
            for boat in range(1, boats + 1):
                for car in range(1 , cars + 1):
                    for passenger in range(1, passengers + 1):
                        room_count += 1
                        self.add_room(self.last_group, passenger, car,boat, 0, room_count)
                        pbar.update(1) 

            for walkin in range(1, walkins + 1):
                room_count += 1
                self.add_room(self.last_group, 0,0,0,walkin, room=room_count)
                pbar.update(1) 

        self.last_room += room_count
        return
    

    #Set Guest format
    def add_room(self, group, passenger, car, boat,walkin, room):
        self.tree.add(Room(f"{group}_{passenger}_{car}_{boat}_{walkin}", room))
        return


    #For requirement 2
    @track
    def assign_room(self, channel):
        return
    
    def update_room_number(self, amount):
        self.tree.update(amount)
        #change algorithm
        # Room.increase_all_number(amount)
        return
    
    #For requirement 4
    @track  
    def manual_add(self, count):
        if self.last_room > 0:
            self.update_room_number(count)
        for i in range(1, count + 1):
            self.tree.add(Room(f"mannual", i))
        return
    
    #For requirement 5
    @track
    def manual_remove(self, room_number):
        self.tree.remove(int(room_number))
        return
    
    @track
    def get_all_available_room(self):
        self.tree.printTree()
    

    #For requirement 7
    @track
    def search(self, room_number):
        result = self.tree.search(room_number)
        return f"Room : {result}" if result else "Room Not found"
    
    #For requirement 11
    @track
    def export_to_file(self):
        self.getCSV()
        # all_room = self.get_all_available_room()
        # auto_download(all_room)
        return
    
    def getCSV(self):
        data = self.data

        with open("hotel.txt", "w") as f:
            for item in data:
                f.write(str(item) + "\n")
    
