class Cow:
    # used to initialize a new cow object with a specified name and no image
    def __init__(self, name):
        self.name = name
        self.image = None
    
    # used to get the name of the cow object
    def get_name(self):
        return self.name
    
    # used to get the image of the cow object
    def get_image(self):
        return self.image
    
    # used to set the image of the cow object to a specified image
    def set_image(self, image):
        self.image = image