from pandas import read_csv
import numpy
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


print ('Enter the file name')
file_name=raw_input();
dataset = read_csv(file_name, header=None)
print('you have '+str(len(dataset.columns))+' columns')
print('enter the column numbers of collumns where missing values are present')
str_arr = raw_input().split(' ') 
col_list = [int(num) for num in str_arr]
dataset[col_list] = dataset[col_list].replace(0, numpy.NaN)
print('enter what to do with the rows with missing values drop(d) replace with mean(me) replace with mode(mo) replace with median(md) replace with constant c')
choice=raw_input()
try:
    dataset=operate(choice,dataset)
except ValueError as e:
    print e
dataset.dropna(inplace=True)
print(dataset.shape)
print(dataset.head(20))