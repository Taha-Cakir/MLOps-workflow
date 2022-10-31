# import statements
import pandas as pd
import requests
from datetime import datetime
from sqlalchemy import create_engine
import os

#uri = os.environ.get('URI')
#uri = os.environ["URI"] = "sqlite:///testDb.db"

from dotenv import load_dotenv,dotenv_values

load_dotenv()
config = dotenv_values(".env")
print(config)

uri = os.environ.get('URI')


engine = create_engine(uri)


#query = engine.execute("""SELECT * FROM Reality;""")

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
data.columns = ["reality_date","reality"]

# getting the number of transactions per hour
data_grouped = data.groupby('reality_date').sum().reset_index()


#data.head()
data.to_sql("Taha_Real",con=engine,if_exists='replace')



# reading the last prediction from the database

"""
first_prediction_date = prediction_date[0]
last_prediction_date = prediction_date[1]
if last_reality_date is None:
    date_extract = first_prediction_date
elif  last_reality_date <= last_prediction_date:
    date_extract = last_reality_date
else:
    date_extract = last_reality_date
# rounding hours to get hourly data
data['x'] = data['x'].dt.round('H')
# getting the number of transactions per hour
data_grouped = data.groupby('x').sum().reset_index()
# getting the data from the last data available in the database
data_grouped = data_grouped.loc[data_grouped['x'] >= date_extract,:]
# preparing the data to upload it to the database
upload_data = list(zip(data_grouped['x'], round(data_grouped['y'],4)))
upload_data[:3]
# inserting the data in the database
for upload_day in upload_data:
    timestamp, reality= upload_day
    result = engine.execute(f"INSERT INTO reality(reality_date, reality) VALUES('{timestamp}', '{reality}') ON CONFLICT (reality_date) DO UPDATE SET reality_date = '{timestamp}', reality= '{reality}';")
    result.close()
"""


"""
#git remote add origin https://github.com/Taha-Cakir/MLOps-workflow.git
# git add . && git commit -m "initial commit"
#git push https://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@github.com/Taha-Cakir/MLOps-workflow.git/
"""
