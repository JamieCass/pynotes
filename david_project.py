import requests
from bs4 import BeautifulSoup
from time import sleep
import sqlite3

base_url = 'https://www.kingsoopers.com'
dairy = '/pl/dairy-eggs/18007'

https://www.kingsoopers.com/pl/dairy-eggs/18007

res = requests.get('https://www.kingsoopers.com/pdp-sitemap/kingsoopers-product-details-sitemap-1.xml',timeout=3)
soup = BeautifulSoup(res.text, 'html.parser')

url='http://www.google.com/blahblah'
try:
    r = requests.get('https://www.kingsoopers.com/pdp-sitemap/kingsoopers-product-details-sitemap-1.xml',timeout=3)
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

def verify_ssl(proxy_info, target):
   print('Attempting to verify SSL Cert on %s:443' % target)
   try:
       if proxy_info is None:
          response = requests.get('https://%s' % target)
       else:
          response = requests.get('https://%s' % target, proxies=proxy_info)
   except requests.exceptions.SSLError as g:
      print('SSL Verification Error %s' % g)
      return 'Got SSL error'
   return 'Successfully Verified SSL Cert: HTTP 200 received.\n'

verify_ssl(, 'https://www.kingsoopers.com/pdp-sitemap/kingsoopers-product-details-sitemap-1.xml')

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
r = requests.get('https://www.kingsoopers.com/pdp-sitemap/kingsoopers-product-details-sitemap-1.xml', headers=headers, timeout=3)
