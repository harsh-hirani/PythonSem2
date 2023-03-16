# p4 5 - Formulate a problem of your own and demonstrate list mutability in python.
testlist = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
testlist.append('hii')
print('testlist ->',testlist)
testlist.pop()
print('testlist ->',testlist)
testlist.append([14, 15, 16])
print('testlist ->',testlist)
testlist.extend([14, 15, 16])
print('testlist ->',testlist)
# delet
del testlist[-1]
print('testlist ->',testlist)
testlist.pop()
testlist.pop()
testlist.pop()
print('testlist ->',testlist)
print('testlist[::-1] ->',testlist[::-1])
print('testlist[5:8:] ->',testlist[5:8:])

newlist = list()
newlist.extend(testlist)
testlist.append(['new1','new2'])
print('testlist ->',testlist)
print('newlist ->',newlist)
testlist.pop()

newlist = testlist
testlist.append(['new1','new2'])
print('testlist ->',testlist)
print('newlist ->',newlist)
newlist.pop()
print('testlist ->',testlist)
print('newlist ->',newlist)
newlist.clear()
print('testlist ->',testlist)
print('newlist ->',newlist)