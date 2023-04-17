from base import Base # from file import class
from dotenv import load_dotenv
import pymongo
import os # operating system

class ToMongo(Base):
    '''
    Class to handle the connection between my data and MongoDB
    Define methods to create a database, upload data one by one,
    and upload all at once. We will also define a drop collection method
    '''

    def __init__(self):
        # Initializing instance of an inherited class
        Base.__init__(self)

        # Load in enviornment variables
        load_dotenv()
        self.mongo_url = os.getenv('MONGO_URL')
        
        # Connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)

        # Create a databse
        self.db = self.client.decklist

        # Create a table/collection
        self.cards = self.db.cards

        # Set DataFrame index to ID column
        self.df.set_index('id', inplace=True)

    # Upload cards
    def upload_one_by_one(self):
        ''' Uploads an item to mongoDB one by one '''
        for i in self.df.index: # iterating thru each item inside df index
            self.cards.insert_one(self.df.loc[i].to_dict()) # For each item we will insert one or w/e we are iterating thru. iterate thru that using index

    def upload_collection(self):
        ''' Uploads an entire list of items to MongoDB 
            BE WARNED THERE IS A MAXIMUM SIZE 
            Limitations to the amount of data you can upload'''
        self.cards.insert_many([self.df.to_dict()])

    def delete_cards(self):
        ''' Drop Database '''
        self.db.drop_collection('cards')
if __name__ == '__main__':
    c = ToMongo()
    print(c.client)
    #c.upload_one_by_one()
    # c.upload_collection()
    c.delete_cards()
    print('delete complete')