# p4 2 - WAP that takes two lists and returns True if they have at least one common member.
l1_size = int(input('size of First list: '))
l1 = []
for i in range(0,l1_size):
    l1.append(input(f"member{i}:"))
l2_size = int(input("---------------\nsize of Second list: "))
l2 = []
for i in range(0,l2_size):
    l2.append(input(f"member{i}:"))
for e in l1:
    if e in l2:
        print(f"yes it has '{e}' common in both")
        exit(0)
print('not at least one member is common')