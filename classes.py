import collections

import input


class module:
    types = [
        "account",
        "contract",
        "transaction",
        "block",
        "logs",
        "proxy",
        "token",
        "gastracker",
        "stats"
    ]

    def __init__(self):
        pass

    def get_type(self):
        return self.types

    def set_type(self, x):
        self.types = self.types[x]


class command(module):
    website = "https://api.etherscan.io/api?"
    module = "&module="
    action = '&action='
    contract_address = '&contractaddress='
    address = '&address='
    offset = '&offset='
    page = '&page='
    sort = '&sort='
    block_type = '&blocktype='
    to = '&to='
    value = '&value='
    data = '&data='
    position = '&position='
    hex = '&hex='
    gas_price = '&gasPrice='
    gas = '&gas='
    start_block = '&startblock='
    end_block = '&endblock='
    blockNo = '&blockno='
    txHash = '&txhash='
    tag = '&tag='
    boolean = '&boolean='
    index = '&index='
    api_key = "&apikey=F6KD4YVEAVT9P6M2U3TPCGZCXT4PRQG4U9"

    commandList = {}

    def __init__(self):
        self.urlString = None

        self.commandList = collections.OrderedDict([
            (self.module, ''),
            (self.address, ''),
            (self.offset, ''),
            (self.page, ''),
            (self.sort, ''),
            (self.block_type, ''),
            (self.to, ''),
            (self.value, ''),
            (self.data, ''),
            (self.position, ''),
            (self.hex, ''),
            (self.gas_price, ''),
            (self.gas, ''),
            (self.start_block, ''),
            (self.end_block, ''),
            (self.blockNo, ''),
            (self.txHash, ''),
            (self.tag, ''),
            (self.boolean, ''),
            (self.index, ''),
            (self.api_key, '')])

    def get_urlString(self):
        return self.urlString

    def set_urlString(self):
        self.urlString = self.get_website() + ''.join(
            [param + val if val else '' for param, val in
             self.commandList.items()]) + self.get_apiKey()

    def get_apiKey(self):
        return self.api_key

    def get_website(self):
        return self.website


### START OF ACCOUNT MODULE COMMANDS ###
class account(command):

    def __init__(self):
        command.__init__(self)
        module.__init__(self)
        self.set_type(0)
        self.commandList[self.module] = module.get_type(self)

    # Get Ether Balance for a Single Address
    def GetEtherBalanceForSingleAddress(self):
        self.commandList[self.action] = 'balance'
        self.commandList[self.tag] = 'latest'
        self.commandList[self.address] = input.getEthAddress()
        self.set_urlString()
        return self.get_urlString()

    def GetlistNormalTransactionsByAddress(self, page="1", offset="10000", sort="asc"):
        self.commandList[self.action] = 'txlist'
        self.commandList[self.address] = str(input.getEthAddress())
        self.commandList[self.start_block] = str(input.getStartBlock())
        self.commandList[self.end_block] = str(input.getEndBlock())
        self.commandList[self.page] = page
        self.commandList[self.offset] = offset
        self.commandList[self.sort] = sort
        self.set_urlString()
        return self.get_urlString()
