class Map:
    map = []


    # Define constructor
    def __init__(self, height, width):
        self.dimensions = {height,"width":width}
        for i in range(height*width):
            self.map.append(Cell())
    #self.map = [Cell() for i in range(height*width) ]
    def cartesian_to_index(self, x, y):

    def index_to_cartesian(self, id):
        x = id%self.dimensions[1]
        y = id//self.dimensions[0]

        return {x,y]


class Cell:
    # Id of the cell
    id = None
    # Neighbors of the current cell
    neighbors = []
    ''' Type of cell that can be: 
    '''
    type = None
    def __init__(self, id):
        self.id = id
        self.neighbors = self.getneighbors(height,width)

    def get_neighbors(self):

