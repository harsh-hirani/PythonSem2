# p4 3 - WAP program to print a specified list after removing the 0th, 2nd, 4th and 5th elements
test_list = [0,1,3,4,5,6,7,8,9]
test_list = [e for count,e in enumerate(test_list) if count not in [0,2,4,5] ]
# test_list.pop(5)
# test_list.pop(4)
# test_list.pop(2)
# test_list.pop(0)
print(test_list)