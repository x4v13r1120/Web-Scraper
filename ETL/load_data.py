import json
import sqlite3
from collections import Counter

conn = sqlite3.connect('data/ethData')
c = conn.cursor()


def load(command_choice):
    Keys = []
    Values = []
    with open("data/cleaned_data.json") as infile:
        rawdata = json.load(infile)
        ethdata = {}
        for raw in rawdata:
            ethdata.update(raw)
            for j in ethdata.values():
                Values.append(j)
        for i in ethdata.keys():
            Keys.append(i)
        for _ in ethdata:
            sql = SQLStatement().buildSqlStatement(command_choice, Keys, Values)
            #print(sql)
    conn.commit()
    conn.close()
    print("Data successfully loaded into database!!!")


class SQLStatement:
    PREFIX = "INSERT INTO"
    AccountModuleTableNames = [
        'Account',
        'TransactionsByAddress',
        'InternalTransactionsByAddress',
        'TransactionByHash',
        'TransferErc20',
        'TransferErc721',
        'BlocksMinedByAddress'

    ]
    SUFFIX = "VALUES"

    def __init__(self):
        self.sqlString = ''

    def buildSqlStatement(self, x, Keys, Values):
        self.sqlString = self.PREFIX + ' ' + get_choice(x) + \
                         '(' + ','.join(f"'{val}'" if val else '' for val in Keys) + ')' \
                         + self.SUFFIX + '(' \
                         + ','.join(f"'{val}'" if val else '' for val in Values) + ');'
        return self.sqlString


def get_choice(x):
    switcher1 = {
        1: SQLStatement.AccountModuleTableNames[0],
        3 or 5: SQLStatement.AccountModuleTableNames[2],
        2: SQLStatement.AccountModuleTableNames[1],
        4: SQLStatement.AccountModuleTableNames[3],
        6: SQLStatement.AccountModuleTableNames[4],
        7: SQLStatement.AccountModuleTableNames[5],
        8: SQLStatement.AccountModuleTableNames[6]
    }
    return switcher1.get(x, "invalid")
