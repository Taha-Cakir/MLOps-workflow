# import statements
import os
from dotenv import load_dotenv, find_dotenv

#default directory for .env file is the current directory
#if you set .env in different directory, put the directory address load_dotenv("directory_of_.env)
load_dotenv()

private_key=os.getenv("URI")
load_dotenv(find_dotenv())


import pandas as pd
import requests
from datetime import datetime
from sqlalchemy import create_engine
import os
#uri = os.environ.get('URI')

#os.environ["URI"] = "sqlite:///testDb.db"
#print(os.environ["URI"])


#engine = create_engine("sqlite:///testDb.db")

# obtaining the data
url = 'https://api.blockchain.info/charts/transactions-per-second?timespan=all&sampled=false&metadata=false&cors=true&format=json'
resp = requests.get(url)
data = pd.DataFrame(resp.json()['values'])

#data.head()

# parsing the date
data['x'] = [datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S') for x in data['x']]
data['x'] = pd.to_datetime(data['x'])


# rounding hours to get hourly data
data['x'] = data['x'].dt.round('H')

# getting the number of transactions per hour
data_grouped = data.groupby('x').sum().reset_index()

# getting the data from the last data available in the database
#data_grouped = data_grouped.loc[data_grouped['x'] >= date_extract,:]

# preparing the data to upload it to the database


data.head()
data.columns = ["reality_date","reality"]
data.to_sql("Reality",con=engine,if_exists='replace')

engine.execute("""Select * from Reality""")
"""
#git remote add origin https://github.com/Taha-Cakir/MLOps-workflow.git
# git add . && git commit -m "initial commit"
#git push https://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@github.com/Taha-Cakir/MLOps-workflow.git/
"""