import json
import sqlite3


def load():
    ethData = []
    with open("../data/cleaned_data.json") as infile:
        ethData = json.load(infile)
        sql = "INSERT INTO table_name () VALUES ()"

        print("paulllllll is sus!!!!!!")
