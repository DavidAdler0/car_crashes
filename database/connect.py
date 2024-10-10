from pymongo import MongoClient





client = MongoClient('mongodb://localhost:27017')
traffic_crashes_db = client['traffic_crashes']

crashes = traffic_crashes_db['crashes']
injuries = traffic_crashes_db['injuries']