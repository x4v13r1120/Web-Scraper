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
        ethdata = []
        for keys in rawdata:
            for value in keys.values():
                ethdata.append(value)
        for value in keys.keys():
            table.append(value)
        sql = SQLStatement().buildSqlStatement(command_choice)
        print(sql)
        for keys in rawdata:
            conn.execute(sql)
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

    def buildSqlStatement(self, x):
        self.sqlString = self.PREFIX + ' ' + get_choice(x) + \
                         '(' + ','.join(f"'{val}'" if val else '' for val in table) + ')' \
                         + self.SUFFIX + '(' \
                         + ','.join('?' for val in table) + ');'
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
