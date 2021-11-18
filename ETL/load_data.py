import json
import sqlite3
from collections import Counter

conn = sqlite3.connect('data/ethData')
c = conn.cursor()


def load(command_choice):
    with open("data/cleaned_data.json") as infile:
        rawdata = json.load(infile)
        ethdata = {}
        for raw in rawdata:
            ethdata.update(raw)
            sql = SQLStatement().buildSqlStatement(command_choice, ethdata)
            print(sql)
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

    def buildSqlStatement(self, x, ethdata):
        self.sqlString = self.PREFIX + ' ' + get_choice(x) + \
                         '(' + ','.join(f"'{val}'" if val else '' for val in ethdata.keys()) + ')' \
                         + self.SUFFIX + '(' \
                         + ','.join(f"{val}" if val else '' for val in ethdata.values()) + ');'
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
