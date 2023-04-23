# p8 1
from numpy import *
from pylab import*
a=linspace(-4,2,6)
print(a)
print(a.shape)
print(type(a))
b=a**2
print(b.shape)
print(b)
print(type(b))
plot(a,b)
show()
'''
Explanation :	“a” is a array consisting the values -4 and 2 and other 4 with equal difference.
And “b” is another array of the square of all elements in “a”
And by plot it takes x as a points and y as b points 
And x=y2 funtion like graph is optaind but is has only six points connected by lines on the actual curve.
'''