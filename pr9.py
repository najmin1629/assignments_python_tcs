import sys
import math
 
a = int(input('Please enter the first side of a triangle: '))
b = int(input('Please enter the second side of a triangle: '))
c = int(input('Please enter the third side of a triangle: '))
class triangle():
   def __init__(self,a,b,c):
       self.a = a
       self.b = b
       self.c = c
   def area(self):
       s=(a + b + c)/2
       area=math.sqrt(s*(s-a)*(s-b)*(s-c))
       return area
t = triangle(a, b, c)
print(t.area())