
	


 
# Normalize time series data
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    """Calculates the population standard deviation
    by default; specify ddof=1 to compute the sample
    standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5

def normalize(array,req_min,req_max):
    curr_min=min(array)
    curr_max=max(array)
    print(curr_max,curr_min)
    for i in range(0,len(array)):
        array[i]=req_min+((array[i]-curr_min)*(req_max-req_min)/(curr_max-curr_min))
    return array

def zScore(array):
    arrmean=mean(array)
    stddevval=stddev(array)
    for i in range(0,len(array)):
        array[i]=(array[i]-arrmean)/stddevval
    return array

def decimalNormalization(array):
    maxele=max(array)
    i = 1;
    while((i * 10) < maxele):
        i *= 10;
    for i1 in range(0,len(array)):
        array[i1]=(array[i1]/(i*10));
    return array

series = pd.read_csv('pima.csv', header=None)
fixerrange=pd.to_numeric(series[3],errors='coerce').astype(float)
print max(fixerrange)
fixerrange=decimalNormalization(fixerrange)
print max(fixerrange)
