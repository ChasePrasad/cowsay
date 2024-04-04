#used to inherit from dragon class
from dragon import Dragon

class IceDragon(Dragon):
    # used to initialize a new ice dragon object with a specified name and image
    def __init__(self, name, image):
        super().__init__(name, image)
    
    #used to determine if the dragon can breathe fire or not
    def can_breathe_fire(self):
        return False