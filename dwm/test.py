from pandas import read_csv,to_numeric
import numpy

def normalize(array,req_min,req_max):
    curr_min=min(array)
    curr_max=max(array)
    for i in range(0,len(array)):
        array[i]=req_min+((array[i]-curr_min)*(req_max-req_min)/(curr_max-curr_min))
    print(array.head())
    return array

def operate(choice,dataset):
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
    else:
        raise ValueError('Invalid Input')
    return dataset

def replace(dataset,col_list,choice):
    dataset[col_list] = dataset[col_list].replace(0, numpy.NaN)
    dataset=operate(choice,dataset)
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
    print('enter what to do with the rows with missing values drop(d) replace with mean(me) replace with mode(mo) replace with median(md) replace with constant c')
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
    print('enter the column number min and max values')
    col,minval,maxval=raw_input().split(' ')
    dataset[int(col)]=to_numeric(dataset[int(col)],errors='coerce').astype(float)
    dataset[int(col)]=normalize(dataset[int(col)],float(minval),float(maxval))
    print('do you want to normalize')
    ch=raw_input()
dataset.dropna(inplace=True)
print(dataset.head())