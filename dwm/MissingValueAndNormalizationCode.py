from pandas import read_csv,to_numeric
import pandas as pd
import numpy as np
from scipy.stats import stats
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
def normalize(array,req_min,req_max):
    curr_min=min(array)
    curr_max=max(array)
    for i in range(0,len(array)):
        array[i]=req_min+((array[i]-curr_min)*(req_max-req_min)/(curr_max-curr_min))
    print(array.head())
    return array

def fillByLinearRegression(array,x,y):
    initlen=array[x].count()
    dataset1=array.dropna(subset=[y])
    dataset1=dataset1.dropna(subset=[x])
   # df1=pd.DataFrame({'X': dataset1[x], 'Y': dataset1[y]}, index=index)
    from sklearn import linear_model
    regr=linear_model.LinearRegression()
    len1=dataset1[x].count()
    print(len1)
    print (initlen)
    la=np.array(dataset1[y]).reshape(len1,1)
    ai=np.array(dataset1[x]).reshape(len1,1)
    mod1=regr.fit(ai,la)
    Rsquare=regr.score(ai,la)
    Intercept=regr.intercept_
    Coeff=regr.coef_
    print("Rsquare:%f" % Rsquare)
    print("Intercept:%f" % Intercept)
    print("Coeff:%f" % Coeff)
    test=array[x][array[y].isnull()]
    predict=regr.predict(test.values.reshape((initlen-len1),1))
    test.replace(to_replace=test.values,value=predict,inplace=True)
    array[y].fillna(value=test,inplace=True)
    return array

def operate(choice,dataset,col_list):
    if choice=='d':
        dataset.dropna(inplace=True)
    elif choice=='me':
        dataset.fillna(dataset.mean(), inplace=True)
    elif choice=='md':
        dataset.fillna(dataset.median(), inplace=True)
    elif choice=='mo':
        dataset.fillna(dataset.mode(), inplace=True)
    elif choice=='c':
        print('Enter the number to fill the empty spaces')
        const=float(raw_input())
        dataset.fillna(const, inplace=True)
    elif choice=='g':
        grouping_attr = raw_input('Enter the Grouping Attribute :')
        for col in col_list:
            dataset[col] = dataset.groupby([int(grouping_attr)])[col]\
                .transform(lambda x: x.fillna(x.mean()))
    elif choice=='lr':
        X_attr = raw_input('Enter the X Attribute :')
        Y_attr = raw_input('Enter the Y Attribute :')
        dataset=fillByLinearRegression(dataset,int(X_attr),int(Y_attr))
    else:
        raise ValueError('Invalid Input')
    return dataset

def replace(dataset,col_list,choice):
    dataset[col_list] = dataset[col_list].replace(0, np.NaN)
    dataset.to_csv('I.csv', sep='\t')
    dataset=operate(choice,dataset,col_list)
    return dataset

print ('Enter the file name')
file_name=raw_input()
dataset = read_csv(file_name, header=None)
print('you have '+str(len(dataset.columns))+' columns')
ch='y'
while(ch=='y'):
    print('enter the column numbers of collumns where missing values are present')
    str_arr = raw_input().split(' ') 
    col_list = [int(num) for num in str_arr]
    print('enter what to do with the rows with missing values drop(d) replace with mean(me) replace with mode(mo) replace with median(md) replace with constant (c) linear regression(lr) class wise mean (g)')
    choice=raw_input()
    try:
        dataset=replace(dataset,col_list,choice)
    except ValueError as e:
        print e
    print('Do you want to replace more?')
    ch=raw_input()
print('do you want to normalize')
ch=raw_input()
while(ch=='y'):
    print('enter type of normalization 1.min/max 2.zscore 3.DecimalScale')
    option=raw_input()
    if option=='1':
        print('enter the column number min and max values')
        col,minval,maxval=raw_input().split(' ')
        dataset[int(col)]=to_numeric(dataset[int(col)],errors='coerce').astype(float)
        dataset[int(col)]=normalize(dataset[int(col)],float(minval),float(maxval))
    elif option=='2':
        col=raw_input()
        dataset[int(col)]=to_numeric(dataset[int(col)],errors='coerce').astype(float)
        dataset[int(col)]=zScore(dataset[int(col)])
    elif option=='3':
        col=raw_input()
        dataset[int(col)]=to_numeric(dataset[int(col)],errors='coerce').astype(float)
        dataset[int(col)]=decimalNormalization(dataset[int(col)])
    else:
        continue
    print('do you want to normalize again')
    ch=raw_input()
dataset.dropna(inplace=True)
print(dataset.head())
dataset.to_csv('O.csv', sep='\t')
