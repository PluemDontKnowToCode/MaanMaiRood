
from Structure.AVLTree import AVLTree
from Helper.track import *
from Room import Room
from Download_csv import *
class Hotel:
    def __init__(self):
        self.tree = AVLTree()
        self.last_room = 0
        return
    
    #For requirement 1 and requirement 3
    @track
    def insert(self, channels):
        #temporaly
        passengers , cars , boats, walkins = channels
        # Room.increase_all_number(passengers * cars * boats + walkins)
        room_count = 0 
        for boat in range(1, boats + 1):
            for car in range(1 , cars + 1):
                for passenger in range(1, passengers + 1):
                    room_count += 1
                    self.tree.add(Room(f"{passenger}_{car}_{boat}_0", room_count))

        for walkin in range(1, walkins + 1):
            room_count += 1
            self.tree.add(Room(f"0_0_0_{walkin}",room_count))
        # self.last_room += room_count
        return
    
    # def add_room(self, ):
    #For requirement 2
    @track
    def assign_room(self, channel):
        return
    
    def update_room_number(self, amount):
        #change algorithm
        # Room.increase_all_number(amount)
        return
    
    #For requirement 4
    @track  
    def manual_add(self, count):
        return
    
    #For requirement 5
    @track
    def manual_remove(self, room_number):
        self.tree.remove(int(room_number))
        return
    
    @track
    def get_all_available_room(self):
        # Create CSV data in memory
        data = [
            ["Alice", 30, "New York"],
            ["Bob", 24, "London"],
            ["Charlie", 35, "Paris"]
        ]

        return data
    

    #For requirement 7
    @track
    def search(self, room_number):
        return self.tree.search(room_number)
    
    #For requirement 11
    @track
    def export_to_csv(self):
        all_room = self.get_all_available_room()
        auto_download(all_room)

        return
    def printTree(self):
        self.tree.printTree()
    

    
    
