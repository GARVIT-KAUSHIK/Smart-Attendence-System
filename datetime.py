import datetime
import pandas as pd
df=pd.read_csv("C:/Users/Administrator/Desktop/at1.csv")
date=datetime.datetime.now().strftime("%d/%m/20%y")
df[date]='A'  #add new date column
df.to_csv("C:/Users/Administrator/Desktop/at1.csv",index=False)