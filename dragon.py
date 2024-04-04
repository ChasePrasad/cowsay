#used to inherit from cow class
from cow import Cow

class Dragon(Cow):
    # used to initialize a new dragon object with a specified name and image
    def __init__(self, name, image):
        super().__init__(name)
        self.image = image
    
    #used to determine if the dragon can breathe fire or not
    def can_breathe_fire(self):
        return True