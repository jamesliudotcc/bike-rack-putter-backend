"""
Mostly cribbed from the Yelp Fusion API code sample.

"""

# Yelp API imports
import argparse

import json
import requests
import sys
import urllib

from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

# Keep our API key secret
from dotenv import load_dotenv
import os

load_dotenv()

import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.bikerackputter
collection = db.restaurants


API_KEY = os.getenv("YELP_API_KEY")

headers = {"Authorization": f"Bearer {API_KEY}"}

for offset in range(0, 1000, 50):
    response = requests.request(
        "GET",
        f"https://api.yelp.com/v3/businesses/search?term=restaurants&latitude=47.6062&longitude=-122.3321&limit=50&offset={offset}",
        headers=headers,
        params=None,
    )

    for restaurant in response.json()["businesses"]:
        collection.insert_one(restaurant)

