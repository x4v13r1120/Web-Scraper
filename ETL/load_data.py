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
    AccountModuleTableNames = {
        'Account',
        'TransactionsByAddress',
        'InternalTransactionsByAddress',
        'TransactionByHash',
        'TransferErc20',
        'TransferErc721',
        'BlocksMinedByAddress'

}
    SUFFIX = 'VALUES'

    def __init__(self):
        self.sqlString = ''

    def buildSqlStatement(self, command_choice):
        self.sqlString = self.PREFIX + ' ' + self.AccountModuleTableNames[command_choice] + \
                         '(' + ','.join(val if val else '' for val in table) + ')' + self.SUFFIX + '(' \
                         + ','.join('?' for val in table) + ')'
        return self.sqlString
