from tqdm import tqdm

from Structure.AVLTree_recur import AVLTree  # -> around 70,000 room/sec when adding room
# from Structure.AVLTree import AVLTree  # -> around 90,000 room/sec can go above 100,000 room/sec when adding room 

from Room import Room

from Helper.track import *
from Helper.color import *
from Helper.formula import *
class Hotel:
    def __init__(self):
        self.tree = AVLTree()
        self.last_group = 0 
        return
    
    def have_room(self):
        return self.tree.root is not None
    #For requirement 1,2 and 3
    @track
    def insert(self, channels):
        self.add_room(channels)
        self.last_group += 1

    #Set Guest format
    def add_room(self, channels):
        # channel_amount = len(channels) + int(self.have_room())
        
        if self.have_room():
            self.tree.update()

        total_rooms = 0

        for i in channels:
            channel_name , amount = i.strip().split()
            total_rooms += int(amount)
        with tqdm(total=total_rooms, desc="Adding rooms", unit="room") as pbar:
            for index ,channel in enumerate(channels):
                channel_name , amount = channel.strip().split()
                amount = int(amount)
                for j in range(1, amount + 1):
                    v = index + 1
                    n = Formula.triangular_accumulate(j, v)
                    #ชื่อช่องทาง_ลำดับของช่องทาง_ลำดับของคน_ลำดับของครั้งที่ใช้ function นี้ 
                    self.tree.add(Room(f"{channel_name}_{v}_{j}_{self.last_group}", n))
                    pbar.update(1)
        
        return


    #For requirement 4
    @track  
    def manual_add(self, count):
        # channel_amount = int(self.have_room()) + 1
        
        if self.have_room():
            self.tree.update()
        
        for index in range(1, count + 1):
            # v = 2
            # n = ((v + j) * (j + v - 1)) // 2 + j
            n = Formula.triangular_accumulate(index,1)
            self.tree.add(Room(f"manual", n))
        return
    

    #For requirement 5
    @track  
    def manual_remove(self, room_number):
        result = self.tree.search(room_number)
        if not result:
            print("Room not found")
            return
        self.tree.remove(int(room_number))
        print(f"Remove Room {room_number}")
        return
    
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
        if result:
            op = f"{result}"
        else:
            op = "Room Not found"
        print(f'\n{op}')
       

    #For requirement 11
    @track
    def export_to_file(self):
        data = self.tree.inorder()
        if data is None:
            print("\nNo Room\n")
            return 
        

        with open("hotel.csv", "w") as f:
            for item in data:
                f.write(str(item) + "\n")
        print("\nExport Success")
        return 
