
from Structure.AVLTree import AVLTree
from Help.track import *
from Room import Room
class Hotel:
    def __init__(self):
        self.tree = AVLTree()
        self.last_room = 0
        return
    
    #For requirement 1 and requirement 3
    @track
    def insert(self, channels):
        #temporaly
        car , boat, helicopter, plane = channels
        return
    #For requirement 2
    @track
    def assign_room(self, channel):
        return
    
    def update_room_number(self, amount):
        Room.increase_all_number(amount)
        return
    
    #For requirement 4
    @track  
    def manual_add(self, count):
        return
    
    #For requirement 5
    @track
    def manual_remove(self, room_number):
        self.tree.remove(room_number)
        return
    
    @track
    def get_all_available_room(self):
        return
    

    #For requirement 7
    @track
    def search(self, room_number):
        return self.tree.search(room_number)
    
    #For requirement 11
    @track
    def export_to_csv(self):
        return
    

    
    
