'''
Return information about an item from a database to a user in a friendly format.

Query the database based off a user input, the display the information back to them

Why is this important?
When a user wants to search information, and we don't have a local file to reference to,
We can use a query function to return the data instead

How do we go about this?
First, we will test it in a notebook environment
We will use our database to return the information
use a .find() function to grab that information
'''

from pathlib import Path
import streamlit as st

import os
import sys

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from to_mongo import ToMongo
c = ToMongo()

answer = st.text_input('Enter Name', value = 'Sol Ring')
st.write(list(c.cards.find({})))

