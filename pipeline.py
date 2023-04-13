from base import Base # from file import class
from dotenv import load_dotenv
import pymongo
import os # operating system

load_dotenv()
mongo_url = os.getenv('MONGO_URL')
client = pymongo.MongoClient(mongo_url)
db = client.db
cards = db.cards
base = Base()
df = base.df
df.set_index('id', inplace=True)

for i in df.index: # iterating thru each item inside df index
    cards.insert_one(df.loc[i].to_dict()) # For each item we will insert one or w/e we are iterating thru. iterate thru that using index