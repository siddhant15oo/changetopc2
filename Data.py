import csv
import pandas as pd 
import plotly.figure_factory as ff
import random
import statistics

df=pd.read_csv('IceCreamShop.csv')
data=df['Temperature'].tolist()

#fig=ff.create_distplot([data],['temperature'],show_hist=False)
#fig.show()


temp=statistics.mean(data)

#print(temp)

temp1=statistics.mode(data)

#print(temp1)

temp2=statistics.median(data)

#print(temp2)

temp3=statistics.stdev(data)

#print(temp3)

data_set=[]
for i in range(0,10):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    data_set.append(float(value))

mean=statistics.mean(data_set)
print(mean)


stdev=statistics.stdev(data_set)
print(stdev)


