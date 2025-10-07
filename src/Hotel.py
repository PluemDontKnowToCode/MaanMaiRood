
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
        if self.last_room > 0:
            self.update_room_number(passengers * cars * boats + walkins)
        room_count = 0 
        for boat in range(1, boats + 1):
            for car in range(1 , cars + 1):
                for passenger in range(1, passengers + 1):
                    room_count += 1
                    self.tree.add(Room(f"{passenger}_{car}_{boat}_0", room_count))

        for walkin in range(1, walkins + 1):
            room_count += 1
            self.tree.add(Room(f"0_0_0_{walkin}",room_count))
        self.last_room += passengers * cars * boats + walkins
        return
    
    # def add_room(self, ):
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
        # Create CSV data in memory
        data = self.tree.inorder()
        return data
    

    #For requirement 7
    @track
    def search(self, room_number):
        result = self.tree.search(room_number)
        return f"Room : {result}" if result else "Room Not found"
    
    #For requirement 11
    @track
    def export_to_csv(self):
        self.getCSV()
        # all_room = self.get_all_available_room()
        # auto_download(all_room)

        return
    def printTree(self):
        self.tree.printTree()
    
    def getCSV(self):
        data = self.tree.inorder()

        with open("fruits.csv", "w") as f:
            for item in data:
                f.write(str(item) + "\n")
    
    
