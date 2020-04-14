## Pandas help

#Start with these IMPORTS

import pandas as pd
import numpy as np
import sqlite3
import os
import matplotlib.pyplot as plt



#(Allows you to see all columns and 200 rows in a df)

pd.set_option('display.max_rows', 200)
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', -1)


'''
Simple linear models...

Y: Response variable e.g (price) 
X: Predictor variable e.g (highway-mpg)
a: value of intercept.. using (''.intercept_)
b: coefficient of variable.. using (''.coef_)

So the Yhat would look like this::
Yhat = a+bX or a+b*X

e.g
Price = 38423.31 - 821.73*highway-mpg 

#####################################

Multiple linear models... 
Y: Response variable e.g (price)
X1: Predictor variable 1 e.g (horsepower)
X2: Predictor variable 2 e.g (curb-weight)
X3: Predictor variable 3 e.g (engine-size)
X4: Predictor variable 4 e.g (highway-mpg)

a: intercept
b1: coefficients of Variable 1
b2: coefficients of Variable 2
b3: coefficients of Variable 3
b4: coefficients of Variable 4

So the Yhat would look like this:
Yhat = a + b1*X1 + b2*X2 + b3*X3 + b4*X4

code would look like this..

lm2 = LinearRegression()
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm2.fit(Z, df['price'])

lm2.intercept_ gives you (-15678.74) (a)

lm2.coef_ give you ([53.50, 4.71, 81.53, 36,06]) (b1, b2, b3, b4)

example of the final equation..

Price = -15678.74 + 53.50 x 'horsepower' + 4.71 x 'curb-weight' + 
81.53 x 'engine-size + 36.06' x 'highway-mpg'


'''