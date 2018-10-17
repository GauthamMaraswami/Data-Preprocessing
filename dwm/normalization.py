
	


 
# Normalize time series data
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize(array,req_min,req_max):
    curr_min=min(array)
    curr_max=max(array)
    print(curr_max,curr_min)
    for i in range(0,len(array)):
        array[i]=req_min+((array[i]-curr_min)*(req_max-req_min)/(curr_max-curr_min))
    return array



series = pd.read_csv('pima.csv', header=None)
fixerrange=pd.to_numeric(series[3],errors='coerce').astype(float)
print(fixerrange)
fixerrange=normalize(fixerrange,0,1)
print(fixerrange)
