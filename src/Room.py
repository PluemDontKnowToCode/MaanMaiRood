class Room:

    number_offset = 0

    def __init__(self, channel, number):
        #format No. : car No. : boat No. : mannual
        self.__channel = channel
        self.__number = int(number)

    @property
    def number(self): return self.__number + Room.number_offset
    
    def __str__(self):
        #room format
        return f"{self.__number}_{self.__channel}"
    
    def __lt__(self, other):
        if isinstance(other, Room):
            print("compere by Room")
            return self.number < other.number
        elif isinstance(other, int):
            print("compere by int")
            return self.number < other
        print("Cannot compare Room with other type")
        return False

    def __gt__(self, other):
        if isinstance(other, Room):
            print("compere by Room")
            return self.number > other.number
        elif isinstance(other, int):
            print("compere by int")
            return self.number > other
        print("Cannot compare Room with other type")
        return False

    def __eq__(self, other):
        if isinstance(other, Room):
            print("compere by Room")
            return self.number == other.number
        elif isinstance(other, int):
            print("compere by int")
            return self.number == other
        print("Cannot compare Room with other type")
        return False
    
    def __int__(self):
        return int(self.number)
    @classmethod
    def increase_all_number(cls, amount):
        cls.number_offset += amount