# p5 6 - Download a .csv file and WAP that extracts the columns indicating name, date, time, shares and price
import csv
data = list()
with open("d.csv") as f:
    reader = csv.reader(f)
    headers= next(reader)
    for i,row in enumerate(reader):
        if i == 11:
            break
        data.append(dict([('date',row[0]),("AAPL",dict([('Open',row[1]),('High',row[2]),('Low',row[3]),('Close',row[4]),('Volume',row[5]),('Adjusted',row[6])])),('more',dict([('dn',row[7]),('mavg',row[8]),('up',row[9]),('dicrection',row[10])]))]))
print(data)