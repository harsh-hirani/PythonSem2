# p5 2 - Write a Python script to concatenate following dictionaries to create a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

sumdic=dict()

for i in dic1.keys():
    sumdic[i]=dic1[i]
for i in dic2.keys():
    sumdic[i]=dic2[i]
for i in dic3.keys():
    sumdic[i]=dic3[i]
print(sumdic)
