import collections

import null as null

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

    # Returns the estimated time remaining, in seconds, until a certain block is mined.
    def GetEstimatedBlockCountdownTimeByBlockno(self):
        self.commandList[self.action] = 'getblockcountdown'
        self.commandList[self.blockNo] = str(input.getBlockNo())
        self.set_urlString()
        return self.get_urlString()

    # Returns the block number that was mined at a certain timestamp.
    def GetBlockNumberByTimestamp(self, closest="before"):
        self.commandList[self.action] = 'getblocknobytime'
        self.commandList[self.timestamp] = str(input.getTimeStamp())
        self.commandList[self.closest] = closest
        self.set_urlString()
        return self.get_urlString()

### START OF LOGS MODULE COMMANDS ###
class logs(command):

    def __init__(self):
        command.__init__(self)
        module.__init__(self)
        self.set_type(4)
        self.commandList[self.module] = module.get_type(self)

    # Get Event Logs from block number 000000 to 'latest'/000000 Block
    def SampleLogAPIQueries(self):
        self.commandList[self.action] = 'getLogs'
        self.commandList[self.from_block] = str(input.getFromBlock())
        # toblock can be used by inputting a block number to go to or 'latest'
        self.commandList[self.to_block] = str(input.getToBlock())
        self.commandList[self.address] = str(input.getEthAddress())
        # could put topic operator here but is not nessecary. I don't know what it would be used for so I left it out.
        self.set_urlString()
        return self.get_urlString()

### START OF GETH/PARITY PROXY MODULE COMMANDS ###
class proxy(command):

    def __init__(self):
        command.__init__(self)
        module.__init__(self)
        self.set_type(5)
        self.commandList[self.module] = module.get_type(self)

    # Returns the number of most recent block
    def Eth_BlockNumber(self):
        self.commandList[self.action] = 'eth_blockNumber'
        self.set_urlString()
        return self.get_urlString()

    # Returns information about a block by block number.
    def Eth_GetBlockByNumber(self):
        self.commandList[self.action] = 'eth_getBlockByNumber'
        self.commandList[self.tag] = str(input.getTag())
        # When true returns full transaction objects, when false only returns a list of transactions
        self.commandList[self.boolean] = "true"
        self.set_urlString()
        return self.get_urlString()

    # Returns information about a uncle by block number.
    def Eth_GetUncleByBlockNumberAndIndex(self):
        self.commandList[self.action] = 'eth_getUncleByBlockNumberAndIndex'
        self.commandList[self.tag] = str(input.getTag())
        self.commandList[self.index] = str(input.getIndex())
        self.set_urlString()
        return self.get_urlString()

    # Returns the number of transactions in a block.
    def Eth_GetBlockTransactionCountByNumber(self):
        self.commandList[self.action] = 'eth_getBlockTransactionCountByNumber'
        self.commandList[self.tag] = str(input.getTag())
        self.set_urlString()
        return self.get_urlString()

    # Returns the information about a transaction requested by transaction hash.
    def Eth_getTransactionByHash(self):
        self.commandList[self.action] = 'eth_getTransactionByHash'
        self.commandList[self.txHash] = str(input.getTxHash())
        self.set_urlString()
        return self.get_urlString()

    # Returns information about a transaction by block number and transaction index position.
    def Eth_GetTransactionByBlockNumberAndIndex(self):
        self.commandList[self.action] = 'eth_getTransactionByBlockNumberAndIndex'
        self.commandList[self.tag] = str(input.getTag())
        self.commandList[self.index] = str(input.getIndex())
        self.set_urlString()
        return self.get_urlString()

    # Returns the number of transactions performed by an address**.**
    def Eth_GetTransactionCount(self):
        self.commandList[self.action] = 'eth_getTransactionCount'
        self.commandList[self.address] = str(input.getEthAddress())
        self.commandList[self.tag] = str(input.getTag())
        self.set_urlString()
        return self.get_urlString()

    # *********DOES NOT WORK**********
    # Submits a pre-signed transaction for broadcast to the Ethereum network.
    # def Eth_SendRawTransaction(self):
    #    self.commandList[self.action] = 'Eth_sendRawTransaction'
    #    self.commandList[self.hex] = str(input.getHex())
    #    self.set_urlString()
    #    return self.get_urlString()

    # Returns the receipt of a transaction by transaction hash.
    def Eth_getTransactionReceipt(self):
        self.commandList[self.action] = 'eth_getTransactionReceipt'
        self.commandList[self.txHash] = str(input.getTxHash())
        self.set_urlString()
        return self.get_urlString()

    # Executes a new message call immediately without creating a transaction on the block chain.
    def Eth_Call(self):
        self.commandList[self.action] = 'eth_call'
        self.commandList[self.to] = str(input.getEthAddress())
        self.commandList[self.data] = str(input.getHashData())
        self.commandList[self.tag] = str(input.getTag())
        self.set_urlString()
        return self.get_urlString()

    # Returns code at a given address.
    def Eth_GetCode(self):
        self.commandList[self.action] = 'eth_getCode'
        self.commandList[self.address] = str(input.getEthAddress())
        self.commandList[self.tag] = str(input.getTag())
        self.set_urlString()
        return self.get_urlString()

    # Returns the value from a storage position at a given address.
    # EXPERIMENTAL
    def Eth_GetStorageAt(self):
        self.commandList[self.action] = 'eth_getStorageAt'
        self.commandList[self.address] = str(input.getEthAddress())
        self.commandList[self.position] = str(input.getPosition())
        self.commandList[self.tag] = str(input.getTag())
        self.set_urlString()
        return self.get_urlString()

    # Returns the current price per gas in wei.
    def Eth_GasPrice(self):
        self.commandList[self.action] = 'eth_gasPrice'
        self.set_urlString()
        return self.get_urlString()

    # Makes a call or transaction, which won't be added to the blockchain and returns the used gas.
    def Eth_EstimateGas(self):
        self.commandList[self.action] = 'eth_estimateGas'
        self.commandList[self.data] = str(input.getHashData())
        self.commandList[self.to] = str(input.getEthAddress())
        self.commandList[self.value] = str(input.getValueSentInTransaction())
        self.commandList[self.gas_price] = str(input.getGasPrice())
        self.commandList[self.gas] = str(input.getGasProvided())
        self.set_urlString()
        return self.get_urlString()

### START OF TOKENS MODULE COMMANDS ###
class tokens(command):

    def __init__(self):
        command.__init__(self)
        module.__init__(self)
        self.set_type(6)
        self.commandList[self.module] = module.get_type(self)

    # Returns the current amount of an ERC-20 token in circulation.
    def GetERC20TokenTotalSupplyByContractAddress(self):
        self.commandList[self.action] = 'tokensupply'
        self.commandList[self.contract_address] = str(input.getContractAddress())
        self.set_urlString()
        return self.get_urlString()

    # Returns the current balance of an ERC-20 token of an address.
    def GetERC20TokenAccountBalanceForTokenContractAddress(self):
        self.commandList[self.action] = 'tokenbalance'
        self.commandList[self.contract_address] = str(input.getContractAddress())
        self.commandList[self.address]= str(input.getEthAddress())
        self.set_urlString()
        return self.get_urlString()

### START OF GAS TRACKER MODULE COMMANDS ###
class gastracker(command):

    def __init__(self):
        command.__init__(self)
        module.__init__(self)
        self.set_type(7)
        self.commandList[self.module] = module.get_type(self)

    def GetEstimationOfConfirmationTime(self):
        self.commandList[self.action] = 'gasestimate'
        self.commandList[self.gas_price] = str(input.getGasPrice())
        self.set_urlString()
        return self.get_urlString()

    # Returns the current Safe, Proposed and Fast gas prices.
    def GetGasOracle(self):
        self.commandList[self.action] = 'gasoracle'
        self.set_urlString()
        return self.get_urlString()

### START OF STATS MODULE COMMANDS ###
class stats(command):

    def __init__(self):
        command.__init__(self)
        module.__init__(self)
        self.set_type(8)
        self.commandList[self.module] = module.get_type(self)

    # Returns the current amount of Ether in circulation.
    def GetTotalSupplyOfEther(self):
        self.commandList[self.action] = 'ethsupply'
        self.set_urlString()
        return self.get_urlString()

    # Returns the current amount of Ether in circulation, ETH2 Staking rewards and EIP1559 burnt fees statistics.
    def GetTotalSupplyOfEther2(self):
        self.commandList[self.action] = 'ethsupply2'
        self.set_urlString()
        return self.get_urlString()

    # Returns the latest price of 1 ETH.
    def GetEtherLastPrice(self):
        self.commandList[self.action] = 'ethprice'
        self.set_urlString()
        return self.get_urlString()

    # Returns the size of the Ethereum blockchain, in bytes, over a date range.
    def GetEthereumNodesSize(self, clienttype="geth", syncmode="default", sort="asc"):
        self.commandList[self.action] = 'chainsize'
        self.commandList[self.start_date] = str(input.getStartDate())
        self.commandList[self.end_date] = str(input.getEndDate())
        self.commandList[self.clienttype] = clienttype
        self.commandList[self.syncmode] = syncmode
        self.commandList[self.sort] = sort
        self.set_urlString()
        return self.get_urlString()

    # Returns the total number of discoverable Ethereum nodes.
    def GetTotalNodesCount(self):
        self.commandList[self.action] = 'nodecount'
        self.set_urlString()
        return self.get_urlString()
