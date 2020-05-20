# Google trends help.

import pytrends
from pytrends.request import TrendReq

pytrend = TrendReq() # this connects to google.

# google hot trends data, daily search trends..
pytrend.trending_searches(pn = 'australia') (could put it in a dataframe)

worldwide, you wouldnt put a parameter. so get rid of 'pn'

# todays trending search..
pytrend.today_searches

# get suggestions for keywords..
pytrend.suggestions(keyword='Mercedes benz')
