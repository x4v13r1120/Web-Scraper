import json
import sqlite3

conn = sqlite3.connect('data/ethData')
c = conn.cursor()

table = []


def buildTableArguments(*args):
    argument = ''
    for x in args:
        argument = x
    table.append(argument)


def load(command_choice):
    rawdata = {}
    with open("data/cleaned_data.json") as infile:
        rawdata = json.load(infile)
    for keys in rawdata:
        ethdata = []
        for value in keys.values():
            ethdata.append(value)
    for value in keys.keys():
        table.append(value)
    print(SQLStatement().buildSqlStatement(command_choice))
    # conn.execute(SQLStatement().buildSqlStatement())
    conn.commit()
    conn.close()
    print("Data successfully loaded into database!!!")


class SQLStatement:
    PREFIX = 'INSERT INTO'
    AccountModuleTableNames = [
        'Account',
        'TransactionsByAddress',
        'InternalTransactionsByAddress',
        'TransactionByHash',
        'TransferErc20',
        'TransferErc721',
        'BlocksMinedByAddress'

    ]
    SUFFIX = 'VALUES'

    def __init__(self):
        self.sqlString = ''

    def buildSqlStatement(self, x):
        self.sqlString = self.PREFIX + ' ' + get_choice(x) + \
                         '(' + ','.join(val if val else '' for val in table) + ')' + self.SUFFIX + '(' \
                         + ','.join('?' for val in table) + ')'
        return self.sqlString


def get_choice(x):
    switcher = {
        1 or 2: SQLStatement.AccountModuleTableNames[0],
        4 or 6: SQLStatement.AccountModuleTableNames[2],
        3: SQLStatement.AccountModuleTableNames[1],
        5: SQLStatement.AccountModuleTableNames[3],
        7: SQLStatement.AccountModuleTableNames[4],
        8: SQLStatement.AccountModuleTableNames[5],
        9: SQLStatement.AccountModuleTableNames[6]
    }
    return switcher.get(x, "invalid")
