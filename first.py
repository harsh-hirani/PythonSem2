val = int(input('enter a number of lines : '))
def literator(intial,counts):
    for i in range(0,counts):
        print(intial - 2*i,end=' ')
for kk in range(1,int((val+1)/2)+1):
    literator(val,kk)
    print()