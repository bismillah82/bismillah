#program to calculate get area and perimeter of circle

class Circle:
    def CalculateArea(self):
        print("Enter radius:")
        self.s=float(input())   #to get input and place in current object
        area=3.14*self.s*self.s
        print("Area of circle is = %f"%(area))
        
    def CalculatePerimeter(self):
        perimeter=2*3.14*self.s
        print("Perimeter of circle is = %f"%(perimeter))

#program to calculate get area and perimeter of ellipse

class Ellipse:
    def CalculateArea(self):
        print("Enter major axis:")
        self.s=float(input())
        print("Enter minor axis:")
        self.c=float(input())
        area=self.s*self.c  #it calculate area of ellipse
        print("Area of ellipse is = %f"%(area))

    def CalculatePerimeter(self):
        perimeter=2*3.14**(self.s+self.c/2)
        print("Perimeter of ellipse is =%f"%(perimeter))
        

#here we create object and call the function
c=Circle()
c.CalculateArea()
c.CalculatePerimeter()

print("\n")

c=Ellipse()
c.CalculateArea()
c.CalculatePerimeter()
