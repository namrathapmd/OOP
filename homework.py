class Line:
    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2
        self.xdiff = self.x2-self.x1
        self.ydiff = self.y2-self.y1

    def distance(self):
        return ((self.xdiff ** 2) + (self.ydiff ** 2)) ** (1/2)

    def slope(self):
        return self.ydiff / self.xdiff


coordinate1 = (3, 2)
coordinate2 = (8, 10)
li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = self.pi * (self.radius ** 2) * self.height
        return vol

    def surface_area(self):
        area = (2 * self.pi * self.radius * self.height) + \
            (2 * self.pi * self.radius ** 2)
        return area


cylin = Cylinder(2, 3)

print(cylin.volume())
print(cylin.surface_area())
