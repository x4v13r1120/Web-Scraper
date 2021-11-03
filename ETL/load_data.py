import json
import sqlite3
from input import module_choice

conn = sqlite3.connect('data/ethData')
c = conn.cursor()

table = []

def buildTableArguments(*args):
    argument = ''
    for x in args:
        argument = x
    table.append(argument)


def load():
    rawdata = {}
    with open("data/cleaned_data.json") as infile:
        rawdata = json.load(infile)
    for keys in rawdata:
        ethdata = []
        for value in keys.values():
            ethdata.append(value)
    for value in keys.keys():
        table.append(value)
    print(SQLStatement().buildSqlStatement())
    #conn.execute(SQLStatement().buildSqlStatement())
    conn.commit()
    conn.close()
    print("Data successfully loaded into database!!!")


class SQLStatement:
    PREFIX = 'INSERT INTO'
    AccountModuleTableNames = [
        'account',
        'BlocksMinedByAddress',
        'TransactionByHash',
        'InternalTransactionsByAddress',
        'TransferErc20',
        'TransferErc721',
        'TransactionsByAddress'
    ]
    SUFFIX = 'VALUES'

    def __init__(self):
        self.sqlString = ''

    def buildSqlStatement(self):
        self.sqlString = self.PREFIX + ' ' + self.AccountModuleTableNames[module_choice] + \
                         '(' + ','.join(val if val else '' for val in table) + ')' + self.SUFFIX + '(' \
                         + ','.join('?' for val in table) + ')'
        return self.sqlString
