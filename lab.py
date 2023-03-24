# p5 1 - WAP to remove multiple elements from a list.
def removeListElements(ulist,sets,type='n'):
    if isinstance(ulist, list) and isinstance(sets,list):
        for i in sets[::-1]:
            if type == 'n':#normal type by index
                if i < len(ulist):    
                    ulist.pop(i)
            elif type == 'ele':#element type by elements
                if i in ulist:
                    ulist.remove(i)
    else:
        print('not perfect use of func')

testlist1 = [1,2,3,4,5,6,7,8,9,0]
removeListElements(testlist1,[0,5,8,8536])
print(testlist1)

testlist2 = [1,2,3,4,5,6,7,8,9,0]
removeListElements(testlist2,[0,5,8,1111],'ele')
print(testlist2)
