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
    timestamp = "&timestamp="
    closest = "&closest="
    from_block = "&fromBlock="
    to_block = "&toBlock="
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
    start_date = '&startdate='
    end_date = '&enddate='
    clienttype = '&clienttype'
    syncmode = '&syncmode='
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
            (self.timestamp, ''),
            (self.closest, ''),
            (self.from_block, ''),
            (self.to_block, ''),
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
            (self.start_date, ''),
            (self.end_date, ''),
            (self.clienttype, ''),
            (self.blockNo, ''),
            (self.syncmode, ''),
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

    # Returns the Ether balance of a given address.
    def GetEtherBalanceForSingleAddress(self):
        self.commandList[self.action] = 'balance'
        self.commandList[self.tag] = 'latest'
        self.commandList[self.address] = input.getEthAddress()
        self.set_urlString()
        return self.get_urlString()

    # Returns the balance of the accounts from a list of addresses.
    def GetEtherBalanceForMultipleAddresses(self):
        self.commandList[self.action] = 'balancemulti'
        self.commandList[self.tag] = 'latest'
        self.commandList[self.address] = input.getMultipleEthAddress()
        self.set_urlString()
        return self.get_urlString()

    # Returns the list of transactions performed by an address, with optional pagination.
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

    # Returns the list of internal transactions performed by an address, with optional pagination.
    def GettListInternalTransactionsByAddress(self, page="1", offset="10000", sort="asc"):
        self.commandList[self.action] = 'txlistinternal'
        self.commandList[self.address] = str(input.getEthAddress())
        self.commandList[self.start_block] = str(input.getStartBlock())
        self.commandList[self.end_block] = str(input.getEndBlock())
        self.commandList[self.page] = page
        self.commandList[self.offset] = offset
        self.commandList[self.sort] = sort
        self.set_urlString()
        return self.get_urlString()

    # Returns the list of internal transactions performed within a transaction.
    def GetInternalTransactionsByHash(self):
        self.commandList[self.action] = 'txlistinternal'
        self.commandList[self.txHash] = str(input.getTxHash())
        self.set_urlString()
        return self.get_urlString()

    # is this even needed? This is the same action and params as GetListInternalTransactionsByAddress
    # Returns the list of internal transactions performed within a block range, with optional pagination.
    def GetInternalTransactionsByBlockRange(self, page="1", offset="10", sort="asc"):
        self.commandList[self.action] = 'txlistinternal'
        self.commandList[self.address] = str(input.getEthAddress())
        self.commandList[self.start_block] = str(input.getStartBlock())
        self.commandList[self.end_block] = str(input.getEndBlock())
        self.commandList[self.page] = page
        self.commandList[self.offset] = offset
        self.commandList[self.sort] = sort
        self.set_urlString()
        return self.get_urlString()

    # Returns the list of ERC-20 tokens transferred by an address, with optional filtering by token contract.
    def GetListOfERC20TokenTransferEventsByAddress(self, page="1", offset="10", sort="asc"):
        self.commandList[self.action] = 'tokentx'
        self.commandList[self.contract_address] = str(input.getContractAddress())
        self.commandList[self.address] = str(input.getEthAddress())
        self.commandList[self.page] = page
        self.commandList[self.offset] = offset
        self.commandList[self.sort] = sort
        self.set_urlString()
        return self.get_urlString()

    # Returns the list of ERC-721 ( NFT ) tokens transferred by an address, with optional filtering by token contract.
    def GetListOfERC721TokenTransferEventsByAddress(self, page="1", offset="10", sort="asc"):
        self.commandList[self.action] = 'tokennfttx'
        self.commandList[self.contract_address] = str(input.getContractAddress())
        self.commandList[self.address] = str(input.getEthAddress())
        self.commandList[self.page] = page
        self.commandList[self.offset] = offset
        self.commandList[self.start_block] = str(input.getStartBlock())
        self.commandList[self.end_block] = str(input.getEndBlock())
        self.commandList[self.sort] = sort
        self.set_urlString()
        return self.get_urlString()

    # Returns the list of blocks mined by an address.
    def GetListOfBlocksMinedByAddress(self, page="1", offset="10", block_type="blocks"):
        self.commandList[self.action] = 'getminedblocks'
        self.commandList[self.address] = str(input.getEthAddress())
        self.commandList[self.block_type] = block_type
        self.commandList[self.page] = page
        self.commandList[self.offset] = offset
        self.set_urlString()
        return self.get_urlString()

### START OF CONTRACTS MODULE COMMANDS ###
class contracts(command):

    def __init__(self):
        command.__init__(self)
        module.__init__(self)
        self.set_type(1)
        self.commandList[self.module] = module.get_type(self)

    # Returns the Contract Application Binary Interface ( ABI ) of a verified smart contract.
    def GetContractABIForVerifiedContractSourceCodes(self):
        self.commandList[self.action] = 'getabi'
        self.commandList[self.address] = str(input.getEthAddress())
        self.set_urlString()
        return self.get_urlString()

    # Returns the Solidity source code of a verified smart contract.
    def GetContractSourceCodeForVerifiedContractSourceCodes(self):
        self.commandList[self.action] = 'getsourcecode'
        self.commandList[self.address] = str(input.getEthAddress())
        self.set_urlString()
        return self.get_urlString()

### START OF TRANSACTIONS MODULE COMMANDS ###
class transactions(command):

    def __init__(self):
        command.__init__(self)
        module.__init__(self)
        self.set_type(2)
        self.commandList[self.module] = module.get_type(self)

    # Returns the status code of a contract execution.
    def CheckContractExecutionStatus(self):
        self.commandList[self.action] = 'getstatus'
        self.commandList[self.txHash] = str(input.getTxHash())
        self.set_urlString()
        return self.get_urlString()

    # Returns the status code of a transaction execution.
    def CheckTransactionReceiptStatus(self):
        self.commandList[self.action] = 'gettxreceiptstatus'
        self.commandList[self.txHash] = str(input.getTxHash())
        self.set_urlString()
        return self.get_urlString()

### START OF BLOCKS MODULE COMMANDS ###
class blocks(command):

    def __init__(self):
        command.__init__(self)
        module.__init__(self)
        self.set_type(3)
        self.commandList[self.module] = module.get_type(self)

    # Returns the block reward and 'Uncle' block rewards.
    def GetBlockAndUncleRewardsByBlockno(self):
        self.commandList[self.action] = 'getblockreward'
        self.commandList[self.blockNo] = str(input.getBlockNo())
        self.set_urlString()
        return self.get_urlString()


    def GetTotalNodesCount(self):
        self.commandList[self.action] = 'nodecount'
        self.set_urlString()
        return self.get_urlString()
