class Rectangle:
    def __inti__(self):
        self.length = 0
        self.width = 0

    def setdimension(self, newlength, newwidth):
        self.length = newlength
        self.width = newwidth

    def __str__(self):
        return "length is: %s, width is: %s" % (self.length, self.width)

    def area(self):
        a = self.length * self.width
        return "area is %i" % a



if (__name__ == "__main__"):

    r1 = Rectangle()
    r1.setdimension(9, 5)
    print(r1)
    print(r1.area())



