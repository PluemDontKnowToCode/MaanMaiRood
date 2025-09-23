class Room:
    def __init__(self, guest, number):
        self.__guest = guest
        self.__number = number

    @property
    def guest(self): return self.__guest

    @property
    def number(self): return self.__number

    @guest.setter
    def guest(self, value):
        self.__guest = value

    def isEmpty(self):
        return self.guest is None