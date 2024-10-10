import csv
from datetime import datetime

from database.connect import traffic_crashes_db, crashes, injuries


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row

def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)


def init_traffic_crashes():
   crashes.drop()
   injuries.drop()
   for row in read_csv('data/Traffic_Crashes.csv'):
       crash = {
           'crash_date': parse_date(row['CRASH_DATE']),
           'beat_of_occurrance': row['BEAT_OF_OCCURRENCE'],
           'prim_contributory_cause': row['PRIM_CONTRIBUTORY_CAUSE']

       }
       crash_id = crashes.insert_one(crash).inserted_id
       injury = {
           'crash_id': crash_id,
           'injuries_total': row['INJURIES_TOTAL'],
           'injuries_fatal': row['INJURIES_FATAL'],
           'injuries_incapcitating': row['INJURIES_INCAPACITATING'],
           'injuries_non_incapcitating': row['INJURIES_NON_INCAPACITATING']
       }
       injuries.insert_one(injury)
