# For selenium code / stuff to go online with
# Use these IMPORTS!!

import requests
import json
import sys
import urllib
import webbrowser
import requests
from io import BytesIO
import numpy as np
from random import randint
from time import sleep
import random
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import lxml

########### Files that are useful ############

# HTML_Scraping_demo_jc.py (has a fair bit of info for bs4 and other bits and bobs)

# pandas_test.py (has a lot of info on pandas)

##############################

# change jupyter theme

jt -t 'theme' # run in terminal, then select a theme

# Use this to make jupyter notebok wider

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))




# Change window size and position of browser

browser.set_window_position(720, 0)
browser.set_window_size(720,1160)


# To preview a md file in atom.. ctrl, shift, m.


##############################

GITHUB (terminal)

git init (initiates the connection)

pull, add, commit, push. (in order.. use status to see what the new things are you need to upload
	then add the new/updated files, commit -m 'then comment', finally push them to'origin master')

status ( shows the status of files that are new or have a chnage..)

##############################

# Date and time!!

import time
import datetime
datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')




from pytrends.request import TrendReq
pytrend = TrendReq()
driver_list = ['Lewis Hamilton','Valtteri Bottas','Sebastian Vettel','Charles Leclerc','Pierre Gasly','Max Verstappen','Daniel Ricardo','Nico Hulkenberg','Romain Grosjean','Kevin Magnussen','Lando Norris','Carlos Sainz','Sergio Perez','Lance Stroll','Kimi Raikkonen','Antonio Giovinazzi','Alexander Albon','Daniil Kvyat','George Russel','Robert Kubica']
total_drivers = len(driver_list)
max_google_request=5
# Number of times we need to loop over
iter = int(total_drivers/max_google_request)
# Difference we need to add every time
diff = int(total_drivers/iter)
# Set an empty df
full_results_region = pd.DataFrame()
counter = 0
for i in range(iter):
    iter_drivers = driver_list[counter:counter+diff]
    print('COMPLETE:',print(iter_drivers))
    counter+=diff
    pytrend.build_payload(kw_list=iter_drivers)
    df_region = pytrend.interest_by_region()
    ## Can add other things to the payload
    #df_interest_over_time = pytrend.interest_over_time()
    # APPEND TO FULL RESULTS
    full_results_region = full_results_region.append(df.T)
    full_results_region['datetime'] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
    print('full_results len',len(full_results_region))
    # CHECK
    print('COMPLETE:',print(iter_drivers))



##################################

#Not used at the minute, just something im playing around with
groupkeywords = list(zip(*[iter(driver_list)]*1))
groupkeywords = [list(x) for x in groupkeywords]

dicti = {}
dic_overtime = {}
i = 1
for trending in groupkeywords[0:2]:
	pytrend.build_payload(kw_list=trending)
	print(trending)
	dicti[i] = pytrend.interest_by_region()
	dic_overtime[i] = pytrend.interest_over_time().drop(['isPartial'],axis=1)
	i+=1

dicti[1]
import pandas as pd

result = pd.concat(dicti, axis=1)ß

overtime_result=pd.concat(dic_overtime, axis=1)

result

overtime_result[1]

##################################################
# SHOWING JOINS
##################################################
pytrend.build_payload(kw_list=driver_list[0:0+diff])
df_interest_over_time_A = pytrend.interest_over_time().drop(['isPartial'],axis=1)
df_interest_over_time_A.head()
pytrend.build_payload(kw_list=driver_list[5:5+diff])
df_interest_over_time_B = pytrend.interest_over_time().drop(['isPartial'],axis=1)
df_interest_over_time_B.head()
# Join them instead of transpose and append
# df_joined = pd.merge(df_interest_over_time_A, df_interest_over_time_B, left_on='colname', right_on='colname', how='inner')
df_joined = pd.merge(df_interest_over_time_A, df_interest_over_time_B, left_index=True, right_index=True, how='inner')
df_joined.head()
# Check they are the same length
len(df_interest_over_time_A), len(df_interest_over_time_B)
