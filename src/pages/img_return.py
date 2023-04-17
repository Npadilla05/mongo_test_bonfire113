import streamlit as st
from PIL import Image
from io import BytesIO
import requests
import ast

# st.title('Image Return')

from pathlib import Path

import os
import sys

filepath = os.path.join(Path(__file__).parents[1])
sys.path.insert(0, filepath)

from to_mongo import ToMongo
c = ToMongo()

answer = st.text_input('Enter card name')
card = list(c.cards.find({'name': 'Sol Ring'}))[0]['image_uris']['normal']
for value in card:
    im = value['normal']
    st.image(Image.open(BytesIO(requests.get(im).content)))

# if __name__ == '__main__':
#     print(Base().get_data())