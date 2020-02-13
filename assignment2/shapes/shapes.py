# file: shapes.py
# author: Reilly Parent
# polymorphic shape classes

import sys
import math

# parent shape class
class Shape:
    sides = []
    area = -1
    def __init__(self, sides):
        self.sides = sides

    def __str__(self): # print setups for triangles and rectangles
        out = ""
        if isinstance(self, Triangle):
            out = ("Triangle with sides " + str(self.sides[0]) + " " + str(self.sides[1]) + " " + str(self.sides[2]) + ": Area = " + str(self.area))
        elif isinstance(self, Rectangle):
            out = ("Rectangle with sides  " + str(self.sides[0]) + " " + str(self.sides[1]) + ": Area = " + str(self.area))
        return out

    def area(self):
        print("WhAT kiND oF sHApE?") # shouldn't happen

# triangle sub-class
class Triangle(Shape):

    def __init__(self, sides):
        super(Triangle, self).__init__(sides)

    # heron's area formula
    def area(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]

        p = (a+b+c) / 2
        self.area = math.sqrt(p*(p-a)*(p-b)*(p-c))

# rectangle sub-class
class Rectangle(Shape):

    def __init__(self, sides):
        super(Rectangle, self).__init__(sides)

    def area(self): # l x w
        self.area = self.sides[0]*self.sides[1]

# driver class for the program
class Driver:
    shapes = []
    shapeFile = open("shapes.txt")
    shapeLines = shapeFile.readlines()

    # needed an init function, basically useless
    def __init__(self):
        self.shapeFile = open("shapes.txt")
        self.shapeLines = self.shapeFile.readlines()

    # method to load shapes and calculate area
    def run(self):
        for line in self.shapeLines: # parse and store shapes
            shapeInfo = line.split()
            if shapeInfo[0]=="T":
                sides = [int(shapeInfo[1]), int(shapeInfo[2]), int(shapeInfo[3])]
                self.shapes.append(Triangle(sides))
            elif shapeInfo[0]=="R":
                sides = [int(shapeInfo[1]), int(shapeInfo[2])]
                self.shapes.append(Rectangle(sides))

        for shape in self.shapes: # get and print area for each side
            shape.area()
            print(shape)

# run
d = Driver()
d.run()
