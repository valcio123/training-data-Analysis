import pandas as pd
import numpy as np
from IPython.display import display

list = []
a = int(input("Size of array:"))
for i in range(a):
    list.append(float(input("insert Element:")))
list = np.array(list)
print(np.floor(list))


def calculate(list):
    if len(list)!=9:
        return print('aceito array somente com 9 elementos')
    else:
        lista= list.reshape(3,3)
        row1=np.mean(lista,axis=0)
        row2=np.mean(lista,axis=1)
        row3=np.mean(lista)
        vrow1=np.var(lista,axis=0)
        vrow2=np.var(lista,axis=1)
        vrow3=np.var(lista)
        srow1=np.std(lista,axis=0)
        srow2=np.std(lista,axis=1)
        srow3=np.std(lista)
        mrow1=np.max(lista,axis=0)
        mrow2=np.max(lista,axis=1)
        mrow3=np.max(lista)
        minrow1=np.min(lista,axis=0)
        minrow2=np.min(lista,axis=1)
        minrow3=np.min(lista)
        sumrow1=np.sum(lista,axis=0)
        sumrow2=np.sum(lista,axis=1)
        sumrow3=np.sum(lista)                        
        df1=pd.DataFrame(index=['mean','variance','standard deviation','max','min','sum'],columns=['1','2','3'])
        df1.loc['mean'] = pd.Series({'1':row1,'2':row2,'3':row3})
        df1.loc['variance'] = pd.Series({'1':vrow1,'2':vrow2,'3':vrow3})
        df1.loc['standard deviation'] = pd.Series({'1':srow1,'2':srow2,'3':srow3})
        df1.loc['max'] = pd.Series({'1':mrow1,'2':mrow2,'3':mrow3})
        df1.loc['min'] = pd.Series({'1':minrow1,'2':minrow2,'3':minrow3})    
        df1.loc['sum'] = pd.Series({'1':sumrow1,'2':sumrow2,'3':sumrow3})              
        return df1

display(calculate(list))