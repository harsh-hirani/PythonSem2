# p5 5 - 
'''
Given a list of elements, perform grouping of similar elements, as different key-value list in dictionary.
Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] -> Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
Input : test_list = [7, 7, 7, 7] -> Output : {7 : [7, 7, 7, 7]} 
'''
test_list1 = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
test_list2 = [7, 7, 7, 7]

def itreter(l):
    returndict = dict()
    for i in l:
        if i in returndict:
            returndict[i].append(i)
        else:
            returndict[i]= list((i,))#add coma to make it list or it will be int
    return returndict
print(itreter(test_list1))
print(itreter(test_list2))