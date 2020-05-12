class Map:
    map = []


    # Define constructor
    def __init__(self, height, width):
        self.dimensions = (height,width)
        for i in range(height*width):
            self.map.append(Cell())
    #self.map = [Cell() for i in range(height*width) ]
class Cell:
    id = None
    neighbors = []
    type = None
    def __init__(self):
        id