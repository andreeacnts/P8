import pandas as pd
from pandas import DataFrame
import time



df1 = pd.read_csv(r"C:\Users\Bruger\Desktop\P8\NSCmp\smile_records.csv")

#Vectorised pandas to calculate ratios
startv = time.time()

df1['vectorized'] = ((df1['endx'] / df1['startx']) + (df1['endy'] / df1['starty'])) / 2

endv = time.time()
print (endv-startv)

# naive pandas to calculate ratios
startn = time.time()

smile_ratios = []

for i in range(0, len(df1)):
    smile_ratio = ( (df1.iloc[i]['endx'] / df1.iloc[i]['startx']) + (df1.iloc[i]['endy'] / df1.iloc[i]['starty']) ) / 2
    smile_ratios.append(smile_ratio)

    startx = df1.startx
    endx = df1.endx
    starty = df1.starty
    endy = df1.endy

    startx.append(startx)
    endx.append(endx)
    starty.append(starty)
    endy.append(endy)

r={'startx':startx, 'endx':endx, 'starty':starty, 'endy':endy,'vectorized':df1['vectorized'],'naive':smile_ratios, }

endn = time.time()
print (endn - startn)

df2=pd.DataFrame(r)
df2.to_csv('processed_data.csv')
