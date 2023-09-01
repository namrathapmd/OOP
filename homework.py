class Line:
    def __init__(self, coor1, coor2):
        self.coorx1, self.coory1 = coor1
        self.coorx2, self.coory2 = coor2
        self.coorxdiff = self.coorx2-self.coorx1
        self.coorydiff = self.coory2-self.coory1

    def distance(self):
        print(((self.coorxdiff**2)+(self.coorydiff**2))**(1/2))

    def slope(self):
        print(self.coorydiff/self.coorxdiff)


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
li.distance()
li.slope()
