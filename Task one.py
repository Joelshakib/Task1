import calendar
import yfinance as yf
import GoogleNews as gn
import pandas as pd
import numpy as np
from datetime import datetime, timedelta 

#datetime range

start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 12, 2)
set_date_range1=pd.date_range(start_date,end_date-timedelta(days=1),freq='d')
set_date_range2=[]
for l1 in set_date_range1.tolist():
   l2=l1.to_pydatetime()
   l3=l2.date()
   set_date_range2.append(l3)
   
#dataset in yfinance

Crude_Oil =yf.download("CL=F", start="2021-01-01", end="2023-12-02")
Gold= yf.download("GC=F", start="2021-01-01", end="2023-12-02")
uxdx=yf.download("DX-Y.NYB", start="2021-01-01", end="2023-12-02")
Crude_Oil.drop('Adj Close',axis=1,inplace=True)
Gold.drop('Adj Close',axis=1,inplace=True)
uxdx.drop('Adj Close',axis=1,inplace=True)

#change timestamp to datetime

Gt=[]
for i in Gold.index.tolist():
   timestamp_to_datetime=i.to_pydatetime()
   remove_time=i.date()
   Gt.append(remove_time)


Cot=[]
for j in Crude_Oil.index.tolist():
    timestamp_to_datetime=j.to_pydatetime()
    remove_time=j.date()
    Cot.append(remove_time)
    
uxdxt=[]
for  k in uxdx.index.tolist():
    timestamp_to_datetime=k.to_pydatetime()
    remove_time=k.date()
    uxdxt.append(remove_time)

#change index

Gt_array=np.array(Gt)
Gold['Date']=Gt_array
Gold.index=Gold.Date
Gold.drop('Date',axis=1,inplace=True)

Cot_array=np.array(Cot)
Crude_Oil['Date']=Cot_array
Crude_Oil.index=Crude_Oil.Date
Crude_Oil.drop('Date',axis=1,inplace=True)

Cuxdxt_array=np.array(uxdxt)
uxdx['Date']=Cuxdxt_array
uxdx.index=uxdx.Date
uxdx.drop('Date',axis=1,inplace=True)

#set Gold dataset
notinformation_Gold=[]
for i in set_date_range2:
    if i not in Gold.index:
        notinformation_Gold.append(i)

Gold_null={'Open':['null' for i in range(len(notinformation_Gold))], 'High':['null' for i in range(len(notinformation_Gold))], 'Low':['null' for i in range(len(notinformation_Gold))], 'Close':['null' for i in range(len(notinformation_Gold))], 'Volume':['null' for i in range(len(notinformation_Gold))]}
Gold_null_Data=pd.DataFrame(Gold_null)

no_information_Gold=np.array(notinformation_Gold)
Gold_null_Data['Date']=no_information_Gold
Gold_null_Data.index=Gold_null_Data.Date
Gold_null_Data.drop('Date',axis=1,inplace=True)
final_Gold_Data = pd.concat([Gold_null_Data,Gold])
final_Gold_Data.sort_values(by='Date',ascending=True,inplace=True)


#set Crude_Oil dataset

notinformation_Crude_Oil=[]
for i in set_date_range2:
    if i not in Crude_Oil.index:
        notinformation_Crude_Oil.append(i)



Crude_Oil_null={'Open':['null' for i in range(len(notinformation_Crude_Oil))], 'High':['null' for i in range(len(notinformation_Crude_Oil))], 'Low':['null' for i in range(len(notinformation_Crude_Oil))], 'Close':['null' for i in range(len(notinformation_Crude_Oil))], 'Volume':['null' for i in range(len(notinformation_Crude_Oil))]}
Crude_null_Data=pd.DataFrame(Crude_Oil_null)
not_information_Crude_Oil=np.array(notinformation_Crude_Oil)
Crude_null_Data['Date']=not_information_Crude_Oil

Crude_null_Data.index=Crude_null_Data.Date
Crude_null_Data.drop('Date',axis=1,inplace=True)
final_Crude_Oil_Data = pd.concat([Crude_Oil,Crude_null_Data])
final_Crude_Oil_Data.sort_values(by='Date',ascending=True,inplace=True)


#set uxdx dataset

notinformation_uxdx=[]
for i in set_date_range2:
    if i not in uxdx.index:
        notinformation_uxdx.append(i)



uxdx_null={'Open':['null' for i in range(len(notinformation_uxdx))], 'High':['null' for i in range(len(notinformation_uxdx))], 'Low':['null' for i in range(len(notinformation_uxdx))], 'Close':['null' for i in range(len(notinformation_uxdx))], 'Volume':['null' for i in range(len(notinformation_uxdx))]}
uxdx_null_Data=pd.DataFrame(uxdx_null)
not_information_uxdx=np.array(notinformation_uxdx)
uxdx_null_Data['Date']=not_information_uxdx

uxdx_null_Data.index=uxdx_null_Data.Date
uxdx_null_Data.drop('Date',axis=1,inplace=True)
final_uxdx_null_Data = pd.concat([uxdx,uxdx_null_Data])
final_uxdx_null_Data.sort_values(by='Date',ascending=True,inplace=True)

#merg all data set
concat_all_dataset=(pd.concat([final_Gold_Data, final_Crude_Oil_Data,final_uxdx_null_Data],keys=['Gold', 'Crude','uxdx']))
print(concat_all_dataset)
#Now its time for news
googlenews=gn.GoogleNews()
googlenews.set_lang('en')
googlenews.set_time_range('02/01/2020','01/12/2023')
googlenews.set_encode('utf-8')
googlenews.search('apple')






    



   
   
   
  


 









