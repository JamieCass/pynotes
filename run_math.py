import numpy as np
import pandas as pd
import os
os.getcwd()



# #Change directory (copy the path of where the file is)
# os.chdir()


os.getcwd()
# def double_number(x, verbose=0, name='David'):
#     if verbose>0:
#         print('multiplying by 2')
#     if verbose>1:
#         print('number being multipled',x)
#         #print('number being multipled'+str(x))
#     print(name)
#     return x*2
#
#
# def half_number(x, verbose=0):
#     return x/2


import TEST.trial

import dbs_math as db

dir(db)


import imp
imp.reload(db)
print(db.double_number.__doc__)



# # Running with defaul
db.double_number(4)

# # Running without default
db.double_number(4, verbose=2,  name='Jamie')




# Building a Class
class math_functions():

    def __init__(self):
        self.name='math-function'

    def double_number(self, x, verbose=0, name='David'):
        """
            Explain what my function does

            Input Params
            ----------------
            x: Number
            verbose: Level of print detail [0,1,2]
            name: str
        """
        if verbose>0:
            print('multiplying by 2')
        if verbose>1:
            print('number being multipled',x)
            #print('number being multipled'+str(x))
        print(name)
        self.original_number=x
        return x*2

    def half_number(self, x, verbose=0):
        return x/2


db.half_number(8)



# mf = math_functions()
# mf.name
#
#
# mf.double_number(2)
# mf.original_number



# Data FRame insides
dbsdict = {'name':['David','jamie'],
           'Age':[30,27]}

dbsdf = pd.DataFrame(dbsdict, index=[0,1])
dbsdf

dbsdict['name']

print(pd.DataFrame.__doc__)
dir(pd.DataFrame)
dir(pd)
