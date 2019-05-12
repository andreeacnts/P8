import pandas as pd
from pandas import DataFrame
import time
import multiprocessing as mp
from dask import delayed as delay
import dask
import dask.dataframe as dd


#read as pandas dataframe
#use only for naive and vectorized version
df = pd.read_csv(r"C:\Users\Bruger\Desktop\P8\NSCmp\smile_records.csv")

# MULTIPROCESSING VERSION
#read as dask dataframe 
#uncomment only for multiprocessing version
#df = dd.read_csv(r"C:\Users\Bruger\Desktop\P8\NSCmp\smile_records.csv")
start = time.time()

df_lazys =[]
df_fasts = []

#define computation but do not compute yet
df_lazy = dask.delayed( ((df['endx'] / df['startx']) + (df['endy'] / df['starty'])) / 2)
df_lazys.append(df_lazy)

df_lazys[0]

#compute here
df_fast = dask.compute(df_lazys)

df_fasts.append(df_fast)

print (df_fast)
end = time.time()
print (end-start)

# VECTORISED VERSION
startv = time.time()

#define computation in vector form
df['vectorized'] = ((df['endx'] / df['startx']) + (df['endy'] / df['starty'])) / 2

endv = time.time()
print (endv-startv)

# NAIVE VERSION
startn = time.time()

#create array to store values
smile_ratios = []

#go through the arrays and compute element by element
for i in range(0, len(df)):
    smile_ratio = ( (df.iloc[i]['endx'] / df.iloc[i]['startx']) + (df.iloc[i]['endy'] / df.iloc[i]['starty']) ) / 2
    #smile_ratio = ( (df.iloc[:,'endx'] / df.iloc[:,'startx']) + (df.iloc[:,'endy'] / df.iloc[:,'starty']) ) / 2
    smile_ratios.append(smile_ratio)

    startx = df.startx
    endx = df.endx
    starty = df.starty
    endy = df.endy

    startx.append(startx)
    endx.append(endx)
    starty.append(starty)
    endy.append(endy)

#create structure of the csv file to be saved
#r={'startx':startx, 'endx':endx, 'starty':starty, 'endy':endy,'vectorized':df['vectorized'],'naive':smile_ratios, 'multiprocessing':df_fasts}

r={'startx':startx, 'endx':endx, 'starty':starty, 'endy':endy,'naive':smile_ratios}

endn = time.time()
print (endn - startn)

#write values to csv
df=pd.DataFrame(r)
df.to_csv('processed_data.csv')