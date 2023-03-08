# Write a program in Python to create a CSV file by entering user-id and password, read and search the password for given user-id.
import csv
file = open('csvtest.csv','w')
fileobj = csv.writer(file)
fileobj.writerow(["User Id", "password"])
user_id = input("enter user id: ")
password = input("enter user password: ")
record = [user_id, password]
fileobj.writerow(record)
file.close()
file = open('csvtest.csv', 'r')
print(file.read())
file.close()