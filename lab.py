# Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the
# circle or outside the circle. (Hint: Use sqrt( ), pow( ) ) 
from math import sqrt


circle = [5,5,10]#[x,y,radius]
x = float(input('enter x cordinate:'))
y = float(input('enter y cordinate:'))
diff = sqrt((circle[0] - x)**2 +(circle[1] - y)**2)
print('given point is ',end='')
if diff < circle[2]:
    print('INSIDE a ',end='')
elif(diff>circle[2]):
    print('OUTSIDE a ',end='')
else:
    print('ON a ',end='')
print('circle.')