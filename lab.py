# WAP to read two text files and merge their contents into a third file.


file1 = open("t.txt", "r")
file2 = open("w.txt", "r")
file3 = open("z.txt", "w")
data1 = file1.read()
data2 = file2.read()
print(data1)
print(data2)
file3.write(data1+data2)

file1.close()
file2.close()
file3.close()

file3 = open("z.txt", "r")
print(file3.read())
file3.close()