import os
from getjson import getjson
from microprediction import MicroWriter

write_key = os.environ.get('write_key')    # GitHub action needs to set env variable. You need to create a GitHub secret called WRITE_KEY
mw = MicroWriter(write_key=write_key)
assert mw.key_difficulty(mw.write_key)>=12, "You need a key of difficulty 12 to create a stream"

REPOS = ['microprediction','neuralprophet','deepecho','auto_ts','pykalman','filterpy',
         'pydlm','simdkalman','fbprophet','pmdarima','pyflux',
         'divinity','tigramite']

if __name__=='__main__':
  # Intended to be run once a day
  for repo in REPOS:
     value = getjson('https://pypistats.org/api/packages/'+repo+'/recent')['data']['last_day']
     name  = 'downloads_'+repo+'.json'
     mw.write(name=name,value=value)
     
     
  
