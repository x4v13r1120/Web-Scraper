class commands:
    api_key = "F6KD4YVEAVT9P6M2U3TPCGZCXT4PRQG4U9"
    website = "https://api.etherscan.io/api?"
    module = [
        "account",
        "contract",
        "transaction",
        "block",
        "logs",
        "proxy",
        "stats",
        "gastracker",
        "token"
    ]

    ### DEFAULT CONSTRUCTOR ###
    def __init__(self, api_key, website, module):
        api_key = api_key
        website = website
        module = module

### START OF ACCOUNT MODULE COMMANDS ###
    # Get Ether Balance for a Single Address
    @staticmethod
    def accountCommand0(address):
        action = "balance"
        tag = "latest"
        return f"{commands.website}&module={commands.module[0]}" \
               f"&action={action}&address={address}&tag={tag}&apikey={commands.api_key}"

    # Get Ether Balance for Multiple Addresses in a Single Call
    @staticmethod
    def accountCommand1(address):
        action = "balancemulti"
        tag = "latest"
        return f"{commands.website}&module={commands.module[0]}" \
               f"&action={action}&address={address}&tag={tag}&apikey={commands.api_key}"

    # Get a list of 'Normal' Transactions By Address
    @staticmethod
    def accountCommand2(address):
        action = "txlist"
        start_block = 0
        end_block = 99999999
        page = 1
        offset = 10
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}&address={address}" \
               f"&startblock={start_block}&endblock={end_block}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # get a list of 'internal transactions by address'
    @staticmethod
    def accountCommand3(address):
        action = "txlistinternal"
        start_block = 0
        end_block = 99999999
        page = 1
        offset = 10
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}&address={address}" \
               f"&startblock={start_block}&endblock={end_block}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # Get 'Internal Transactions' by Transaction Hash
    @staticmethod
    def accountCommand4(txhash):
        action = "txlistinternal"
        return f"{commands.website}&module={commands.module[0]}" \
               f"&action={action}&txhash={txhash}&apikey={commands.api_key}"

    # get "internal transactions" by block range
    @staticmethod
    def accountCommand5():
        action = "txlistinternal"
        startBlock = 0
        endBlock = 99999999
        page = 1
        offset = 10
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}" \
               f"&startblock={startBlock}&endblock={endBlock}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # Get a list of 'ERC20 - Token Transfer Events' by Address
    @staticmethod
    def accountCommand6(address, contractaddress):
        action = "tokentx"
        page = 1
        offset = 100
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}" \
               f"&=contractaddress={contractaddress}&=address{address}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # Get a list of 'ERC721 - Token Transfer Events' by Address
    @staticmethod
    def accountCommand7(address, contractaddress):
        action = "tokennfttx"
        page = 1
        offset = 100
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}" \
               f"&=contractaddress={contractaddress}&address{address}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # Get list of Blocks Mined by Address
    @staticmethod
    def accountCommand8(address):
        action = "getminedblocks"
        blocktype = "blocks"
        page = 1
        offset = 100
        return f"{commands.website}&module={commands.module[0]}&action={action}&address={address}&=blocktype={blocktype}&page={page}" \
               f"&offset={offset}&apikey={commands.api_key}"

### START OF CONTRACT MODULE COMMANDS ###

# Get Contract ABI for Verified Contract Source Code
    @staticmethod
    def contractCommand0(address):
        action = "getabi"
        return f"{commands.website}&module={commands.module[1]}" \
               f"&action={action}&address={address}&apikey={commands.api_key}"

# Get Contract Source Code for Verified Contract Source Codes
    @staticmethod
    def contractCommand1(address):
        action = "getsourcecode"
        return f"{commands.website}&module={commands.module[1]}" \
               f"&action={action}&address={address}&apikey={commands.api_key}"

### START OF TRANSACTIONS MODULE COMMANDS ###

#Check Contract Execution Status
    @staticmethod
    def transactionCommand0(txhash):
        action = "getstatus"
        return f"{commands.website}&module={commands.module[2]}" \
               f"&action={action}&txhash={txhash}&apikey={commands.api_key}"

# Check Transaction Receipt Status
    @staticmethod
    def transactionCommand1(txhash):
        action = "gettxreceiptstatus"
        return f"{commands.website}&module={commands.module[2]}" \
               f"&action={action}&txhash={txhash}&apikey={commands.api_key}"

### START OF BLOCK MODULE COMMANDS ###

# Get Block And Uncle Rewards by BlockNo
    @staticmethod
    def blockCommand0(blockno):
        action = "getblockreward"
        return f"{commands.website}&module={commands.module[3]}" \
               f"&action={action}&blockno={blockno}&apikey={commands.api_key}"

# Get Estimated Block Countdown Time by BlockNo
    @staticmethod
    def blockCommand1(blockno):
        action = "getblockcountdown"
        return f"{commands.website}&module={commands.module[3]}" \
               f"&action={action}&blockno={blockno}&apikey={commands.api_key}"

# Get Block Number by Timestamp
    @staticmethod
    def blockCommand2(timestamp):
        action = "getblocknobytime"
        closest = "before"
        return f"{commands.website}&module={commands.module[3]}&action={action}" \
               f"&timestamp={timestamp}&closest={closest}&apikey={commands.api_key}"

### START OF LOGS MODULE COMMANDS ###

# Sample Log API Queries

    # Get Event Logs from block number 379224 to 'latest' Block,
    # where log address = 0x33990122638b9132ca29c723bdf037f1a891a70c
    # and topic[0] = 0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545
    @staticmethod
    def logCommand0(address):
        action = "getLogs"
        fromBlock = 379224
        toBlock = "latest"
        topic0 = "0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545" # test hash
        return f"{commands.website}&module={commands.module[4]}&action={action}&fromBlock={fromBlock}" \
               f"&toBlock={toBlock}&address={address}&topic0={topic0}&apikey={commands.api_key}"

    #Get Event Logs from block number 379224 to block 400000 ,
    # where log address = 0x33990122638b9132ca29c723bdf037f1a891a70c,
    # topic[0] = 0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545
    # 'AND' topic[1] = 0x72657075746174696f6e00000000000000000000000000000000000000000000
    @staticmethod
    def logCommand1(address):
        action = "getLogs"
        fromBlock = 379224
        toBlock = "latest"
        topic0 = "0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545" # test hash
        topic0_1_opr = "and"
        topic1 = "0x72657075746174696f6e00000000000000000000000000000000000000000000"
        return f"{commands.website}&module={commands.module[4]}&action={action}&fromBlock={fromBlock}" \
               f"&toBlock={toBlock}&address={address}&topic0={topic0}" \
               f"&topic0_1_opr={topic0_1_opr}&topic1={topic1}&apikey={commands.api_key}"

### START OF GETH/PARITY/PROXY MODULE COMMANDS ###5

    # Returns the number of most recent block
    @staticmethod
    def proxyCommand0():
        action = "eth_blockNumber"
        return f"{commands.website}&module={commands.module[5]}&action={action}&apikey={commands.api_key}"

    # Returns information about a block by block number.
    @staticmethod
    def proxyCommand1(tag):
        action = "eth_getBlockByNumber"
        tag = 0x10d4f
        boolean = 'true'
        return f"{commands.website}&module={commands.module[5]}&action={action}&tag={tag}&boolean={boolean} " \
               f"&apikey={commands.api_key}"

    # Returns information about a uncle by block number.
    @staticmethod
    def proxyCommand2(tag):
        action = "eth_getUncleByBlockNumberAndIndex"
        index = 0x0
        return f"{commands.website}&module={commands.module[5]}&action={action}&tag={tag}&index={index}"\
               f"&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand3(tag):
        action = "eth_getBlockTransactionCountByNumber"
        return f"{commands.website}&module={commands.module[5]}&action={action}&tag={tag}&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand4(txhash):
        action = "eth_getTransactionByHash"
        #txhash = 0x1e2910a262b1008d0616a0beb24c1a491d78771baa54a33e66065e03b1f46bc1
        return f"{commands.website}&module={commands.module[5]}&action={action}&txhash={txhash}&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand5(tag):
        action = "eth_getTransactionByBlockNumberAndIndex"
        index = 0x11A
        tag = tag
        return f"{commands.website}&module={commands.module[5]}&action={action}&tag{tag}&index{index}&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand6(ethaddress):
        action = "eth_getTransactionCount"
        tag = 'latest'
        address = str (ethaddress)
        return f"{commands.website}&module={commands.module[5]}&action={action}&address={address}&tag={tag}" \
               f"&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand7(hex):
        action = "eth_sendRawTransaction"
        #hex = 0xf904808000831cfde080
        return f"{commands.website}&module={commands.module[5]}&action={action}&hex={hex}" \
               f"&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand8(txhash):
        action = "eth_getTransactionReceipt"
        hash = txhash
        return f"{commands.website}&module={commands.module[5]}&action={action}&txhash={txhash}&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand9(toAddress,hashData):
        action = "eth_call"
        to = toAddress
        data = hashData
        tag = "latest"
        return f"{commands.website}&module={commands.module[5]}&action={action}&to={to}&data={data}&tag={tag}&apikey={commands.api_key}"

    def proxyCommand10(ethaddress):
        action = "eth_getCode"
        address = ethaddress
        tag = "latest"
        return f"{commands.website}&module={commands.module[5]}&action={action}&address={address}&tag={tag}" \
               f"&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand11(ethaddress):
        action = "eth_getStorageAt"
        address = ethaddress
        tag = "latest"
        position = 0x0
        return f"{commands.website}&module={commands.module[5]}&action={action}&address={address}&tag={tag}" \
               f"&position={position}&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand12():
        action = "eth_gasPrice"
        return f"{commands.website}&module={commands.module[5]}&action={action}&apikey={commands.api_key}"

    @staticmethod
    def proxyCommand13(hashData, toAddress, gasProvided, gasPricePaid, valueSent):
        action = "eth_estimateGas"
        data = hashData
        to = toAddress
        value = valueSent
        gas = gasProvided
        gasPrice = gasPricePaid
        return f"{commands.website}&module={commands.module[5]}&action={action}&data={data}&to={to}&value={value}&gas={gas}&gasPrice={gasPrice}&apikey={commands.api_key}"

    #@staticmethod
    #def proxyCommand():

### START OF TOKENS MODULE COMMANDS ###
### START OF GAS TRACKER MODULE COMMANDS ###
### START OF STATS MODULE COMMANDS ###



## USER INPUT ###
def getValueSentInTransaction():
    valueSent = str(input(
        "Please enter value sent in transaction."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
    return valueSent

def getGasPricePaid():
    gasPricePaid = str(input(
        "Please enter gas price paid."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
    return gasPricePaid

def getGasProvided():
    gasProvided = str(input(
        "Please enter gas provided."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
    return gasProvided

def getToAddress():
    toAddress = str(input(
        "Please enter address to interact with."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
    return toAddress

def getHashData():
    hashData = str(input(
        "Please enter hash of method signature"))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
    return hashData

def getEthAdress():
    address = str(input(
        "Please enter Ether Address."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
    return address

def getHex():
    hex = str(input(
        "Please enter Hex."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
    return hex

def getTag():
    tag = str(input(
        "Please enter the tag."))  # tag for testing = 0x10d4f
    return tag

def getTxHash():
    txhash = str(input(
        "Please enter Transaction Hash."))  # address for testing =
    # 0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170
    return txhash

def getContractAdress():
    contractaddress = str(input(
        "Please enter Contract Address."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
    return contractaddress

def getBlockNo():
    blockno = int(input("Please enter Block Number."))  # block for testing = 216540
    return blockno

def getTimeStamp():
    timestamp = int(input("Please enter Timestamp."))  # timestamp for testing 1578638524
    return timestamp