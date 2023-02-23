# WAP to ask the number of lines from the user and print the following pattern:
#  1
#  AB
#  234
#  ABCD 
import string
alphabet = list(string.ascii_uppercase)
lines = int(input('enter the lines'))
if lines < 1:
    print('lines should be more than 0.')
    exit()
else:
    for i in range(1,lines+1):
        print()
        if( i%2 == 0 ):
            #chars
            for j in range(0,i):
                print(alphabet[j],end=" ")
            
        else:
            # numbers
            for j in range(1,i+1):
                print(j,end=" ")