import sys
import math

class Shape:
    sides = []
    area = -1
    def __init__(self, sides):
        self.sides = sides

    def __str__(self):
        out = ""
        if isinstance(self, Triangle):
            out = ("Triangle with sides " + str(self.sides[0]) + " " + str(self.sides[1]) + " " + str(self.sides[2]) + ": Area = " + str(self.area))
        elif isinstance(self, Rectangle):
            out = ("Rectangle with sides  " + str(self.sides[0]) + " " + str(self.sides[1]) + ": Area = " + str(self.area))
        return out

    def area(self):
        print("WhAT kiND oF sHApE?")

class Triangle(Shape):

    def __init__(self, sides):
        super(Triangle, self).__init__(sides)

    def area(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]

        p = (a+b+c) / 2
        self.area = math.sqrt(p*(p-a)*(p-b)*(p-c))

class Rectangle(Shape):

    def __init__(self, sides):
        super(Rectangle, self).__init__(sides)

    def area(self):
        self.area = self.sides[0]*self.sides[1]

class Driver:
    shapes = []
    shapeFile = open("shapes.txt")
    shapeLines = shapeFile.readlines()

    def __init__(self):
        self.shapeFile = open("shapes.txt")
        self.shapeLines = self.shapeFile.readlines()

    def run(self):
        for line in self.shapeLines:
            shapeInfo = line.split()
            if shapeInfo[0]=="T":
                sides = [int(shapeInfo[1]), int(shapeInfo[2]), int(shapeInfo[3])]
                self.shapes.append(Triangle(sides))
            elif shapeInfo[0]=="R":
                sides = [int(shapeInfo[1]), int(shapeInfo[2])]
                self.shapes.append(Rectangle(sides))

        for shape in self.shapes:
            shape.area()
            print(shape)

d = Driver()
d.run()
