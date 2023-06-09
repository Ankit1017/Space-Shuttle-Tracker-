# -*- coding: utf-8 -*-
"""Copy of deep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17TOkgZNH7LeZUV-m-_-OCcF2d9w5Nnur
"""

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import time
def transpose(l1, l2):
     
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row =[]
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2
def result(path):
    dataset = pd.read_csv('./rocket_data.csv')
    dr=pd.read_csv(path)
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    Xt = dr.iloc[:, :].values
    yt = dr.iloc[:, -1].values
    st=[]
    xmat=[]
    tim=[]
    tt=1
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
    regressor.fit(X_train, y_train)

    from sklearn.svm import SVR
    regresso = SVR(kernel = 'rbf')
    regresso.fit(X_train, y_train)

    from sklearn.linear_model import LinearRegression
    regress = LinearRegression()
    regress.fit(X_train, y_train) 

    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    for xinp in Xt:
        gg=[]
        y_pred=regressor.predict(X_test)
        yt=regressor.predict([xinp])
        a=r2_score(y_test,y_pred)
        gg.append([a,yt[0]])

        y_pred=regresso.predict(X_test)
        yt=regresso.predict([xinp])
        a=r2_score(y_test,y_pred)
        gg.append([a,yt[0]])


        y_pred=regress.predict(X_test)
        a=r2_score(y_test,y_pred)
        yt=regress.predict([xinp])
        gg.append([a,yt[0]])


        y_pred=reg.predict(X_test)
        a=r2_score(y_test,y_pred)
        yt=reg.predict([xinp])
        gg.append([a,yt[0]])
        tim.append(tt)
        tt+=1
        gg.sort(reverse=True)
        ans=gg[0][1]
        
        xmat.append(ans)
        xl=xinp.tolist()
        xl.append(ans)
        st.append(xl)
    l2=[]
    transpose(st,l2)
    return l2



