#!/usr/bin/env python3

from pymongo import MongoClient
from writelog import Logging

client = MongoClient("mongodb://localhost:27017/")

class manageDB():
    def createDB (self):
        db = client['xyz']

    def insertMovies (self, item):
        with client:
            db = client.xyz
            item13 = [{'link': item}]
            db.Movies.insert(item13)

    def insertSeries (self, item):
        with client:
            db = client.xyz
            item13 = [{'link': item}]
            db.Series.insert(item13)