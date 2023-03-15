# House down payment planner 
import csv
csvFile=open('test.csv','w')
writer = csv.writer(csvFile)
writer.writerow(['uid','pass'])
s = True
while s:
    uid = input("Uid: ")
    pas = input("Pass: ")
    writer.writerow([uid,pas])
    if(input('want to add more? y/n: ') == 'n'):
        s=False
        break

csvFile.close()
csvFile = open('test.csv','r')
csvReader = csv.reader(csvFile)
uid = input('uid: ')
indexii = 0
for row in csvReader:
    if(indexii%2==1):
        indexii = indexii +1
        continue
    indexii = indexii + 1
    # print(row)
    if row[0] == uid:
        pas = input('Pass: ')
        if pas == row[1]:
            print('You can login')
            exit(0)
        else:
            pas = input('incorect pass try again: ')
            if pas == row[1]:
                print('You can login')
                exit(0)
            else:
                print('system locked.')
                exit(0)
print("wrong uid")
csvFile.close()