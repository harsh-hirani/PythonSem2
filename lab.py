# Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.
f = [int(input('enter x1 :')),int(input('enter y1 :'))]
s = [int(input('enter x2 :')),int(input('enter y1 :'))]
t = [int(input('enter x3 :')),int(input('enter y1 :'))]

if (f[0]==s[0] and s[0]==t[0]) or (f[1]==s[1] and s[1]==t[1]):
    print("in lines")
else:
    if (f[0]-s[0])/(f[1] - s[1]) == (s[0] - t[0])/(s[1] - t[1]):
        print("in lines")
    else:
        print('not in lines')