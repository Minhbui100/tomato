'''
Project 1: Implement a class Triangle

This class should be able to differentiate between isosceles, right, and obtuse triangles. 
Class should be initialized with the angles or sides, then from there, the class should be able to determine whether the triangle is isosceles, right, obtuse, or none of the above.

Example initialization:

triangle = triangle(a=3, b=4, C=60)
triangle = triangle(a=3, b=4, c=5)
triangle = triangle(c=30, B=60, C=90)


'''
import math
class tester():
    def __init__(self,a=None,b=None,c=None,A=None,B=None,C=None):
        self.a=a
        self.b=b
        self.c=c
        self.A=A
        self.B=B
        self.C=C
        self.sides=[self.a,self.b,self.c]
        self.angles=[self.A,self.B,self.C]
        
        self.sides_copy=[]
        self.angles_copy=[]

        for side in self.sides:
            if side != None:
                self.sides_copy.append(side)

        for angle in self.angles:
            if angle != None:
                self.angles_copy.append(angle)          
    
    def cos_rule(self,a,b,c):
        return math.degrees(math.acos((math.pow(b,2)+math.pow(c,2)-math.pow(a,2))/(2*b*c)))

    def three_sides(self, a, b, c):
        A=self.cos_rule(a,b,c)
        B=self.cos_rule(b,a,c)
        C=self.cos_rule(c,b,a)
        angles=[A,B,C]
        return angles
    
    def side_angle_side(self, a, b, C):
        c=math.sqrt(math.pow(b,2)+math.pow(a,2)-2*a*b*math.cos(math.radians(C)))
        A=self.cos_rule(a,b,c)
        B=self.cos_rule(b,a,c)
        angles=[A,B,C]
        return angles

    def side_side_angle(self, a, b, A):
        B=math.degrees(math.asin(b*math.sin(math.radians(A))/a))
        C=180-A-B
        angles=[A,B,C]
        return angles    
    
    def two_angles(self, a, A, B):
        C=180-A-B
        angles=[A,B,C]
        return angles
    
    def three_angles(self, A, B, C):
        angles=[A,B,C]
        return angles

    def convert_to_angles(self):
        if len(self.sides_copy) == 3:
            return self.three_sides(self.a, self.b, self.c)
        elif len(self.sides_copy) == 2:
            determine=0
            for i in range (3):
                if self.sides[i] == None and self.angles[i] == None:
                    determine=1
            if determine == 0:
                return self.side_angle_side(self.sides_copy[0],self.sides_copy[1],self.angles_copy[0])
            else:
                return self.side_side_angle(self.sides_copy[0],self.sides_copy[1],self.angles_copy[0])
        elif len(self.sides_copy) == 1:
            return self.two_angles(self.sides_copy[0],self.angles_copy[0],self.angles_copy[1])
        else:
            return self.three_angles(self.angles_copy[0],self.angles_copy[1],self.angles_copy[2])
        
    def what_triangle(self):
        angles_final=self.convert_to_angles()
        if round(angles_final[0]+angles_final[1]+angles_final[2])!=180:
            return "None of above"
        elif angles_final[0] == 90 or angles_final[1] == 90 or angles_final[2] == 90:
            return "Right triangle"
        elif angles_final[0] == angles_final[1] or angles_final[2] == angles_final[1] or angles_final[0] == angles_final[2]:
            return "Isosceles triangle"
        elif angles_final[0] > 90 or angles_final[1] > 90 or angles_final[2] > 90:
            return "Obtuse triangle"
        else:
            return "None of above"
 
         
newTriangle=tester(C=70,a=2,A=55)
print(newTriangle.convert_to_angles())    
print(newTriangle.what_triangle())       