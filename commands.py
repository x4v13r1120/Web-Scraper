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
    address = str(
        input("Please enter Ether Address."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae

    txhash = str(input("Please enter Transaction Hash."))  # address for
    # testing = 0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170

    contractAddress = str(input("Please enter Contract address."))  #
    # address for testing = 0x06012c8cf97bead5deae237070f9587f8e7a266d

    blockno = int(input("Please enter block."))  # block for testing = 216540

    timestamp = int(input("Please enter timestamp."))  # timestamp for testing 1578638524

    ### DEFAULT CONSTRUCTOR ###
    def __init__(self, api_key, website, module):
        api_key = api_key
        website = website
        module = module

### START OF ACCOUNT MODULE COMMANDS ###
    # Get Ether Balance for a Single Address
    @staticmethod
    def accountCommand0():
        action = "balance"
        tag = "latest"
        return f"{commands.website}&module={commands.module[0]}" \
               f"&action={action}&address={commands.address}&tag={tag}&apikey={commands.api_key}"

    # Get Ether Balance for Multiple Addresses in a Single Call
    @staticmethod
    def accountCommand1():
        action = "balancemulti"
        tag = "latest"
        return f"{commands.website}&module={commands.module[0]}" \
               f"&action={action}&address={commands.address}&tag={tag}&apikey={commands.api_key}"

    # Get a list of 'Normal' Transactions By Address
    @staticmethod
    def accountCommand2():
        action = "txlist"
        start_block = 0
        end_block = 99999999
        page = 1
        offset = 10
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}&address={commands.address}" \
               f"&startblock={start_block}&endblock={end_block}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # get a list of 'internal transactions by address'
    @staticmethod
    def accountCommand3():
        action = "txlistinternal"
        start_block = 0
        end_block = 99999999
        page = 1
        offset = 10
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}&address={commands.address}" \
               f"&startblock={start_block}&endblock={end_block}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # Get 'Internal Transactions' by Transaction Hash
    @staticmethod
    def accountCommand4():
        action = "txlistinternal"
        return f"{commands.website}&module={commands.module[0]}" \
               f"&action={action}&txhash={commands.txhash}&apikey={commands.api_key}"

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
    def accountCommand6():
        action = "tokentx"
        page = 1
        offset = 100
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}" \
               f"&=contractaddress={commands.contractaddress}&=address{commands.address}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # Get a list of 'ERC721 - Token Transfer Events' by Address
    @staticmethod
    def accountCommand7():
        action = "tokennfttx"
        page = 1
        offset = 100
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}" \
               f"&=contractaddress={commands.contractaddress}&address{commands.address}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # Get list of Blocks Mined by Address
    @staticmethod
    def accountCommand8():
        action = "getminedblocks"
        blocktype = "blocks"
        page = 1
        offset = 100
        return f"{commands.website}&module={commands.module[0]}&action={action}&address={commands.address}&=blocktype={blocktype}&page={page}" \
               f"&offset={offset}&apikey={commands.api_key}"

### START OF CONTRACT MODULE COMMANDS ###

# Get Contract ABI for Verified Contract Source Code
    @staticmethod
    def contractCommand0():
        action = "getabi"
        return f"{commands.website}&module={commands.module[1]}" \
               f"&action={action}&address={commands.address}&apikey={commands.api_key}"

# Get Contract Source Code for Verified Contract Source Codes
    @staticmethod
    def contractCommand1():
        action = "getsourcecode"
        return f"{commands.website}&module={commands.module[1]}" \
               f"&action={action}&address={commands.address}&apikey={commands.api_key}"

### START OF TRANSACTIONS MODULE COMMANDS ###

#Check Contract Execution Status
    @staticmethod
    def transactionCommand0():
        action = "getstatus"
        return f"{commands.website}&module={commands.module[2]}" \
               f"&action={action}&txhash={commands.txhash}&apikey={commands.api_key}"

# Check Transaction Receipt Status
    @staticmethod
    def transactionCommand1():
        action = "gettxreceiptstatus"
        return f"{commands.website}&module={commands.module[2]}" \
               f"&action={action}&txhash={commands.txhash}&apikey={commands.api_key}"

### START OF BLOCK MODULE COMMANDS ###

# Get Block And Uncle Rewards by BlockNo
    @staticmethod
    def blockCommand0():
        action = "getblockreward"
        return f"{commands.website}&module={commands.module[3]}" \
               f"&action={action}&blockno={commands.blockno}&apikey={commands.api_key}"

# Get Estimated Block Countdown Time by BlockNo
    @staticmethod
    def blockCommand1():
        action = "getblockcountdown"
        return f"{commands.website}&module={commands.module[3]}" \
               f"&action={action}&blockno={commands.blockno}&apikey={commands.api_key}"

# Get Block Number by Timestamp
    @staticmethod
    def blockCommand2():
        action = "getblocknobytime"
        closest = "before"
        return f"{commands.website}&module={commands.module[3]}&action={action}" \
               f"&timestamp={commands.timestamp}&closest={closest}&apikey={commands.api_key}"

### START OF LOGS MODULE COMMANDS ###

# Sample Log API Queries

    # Get Event Logs from block number 379224 to 'latest' Block,
    # where log address = 0x33990122638b9132ca29c723bdf037f1a891a70c
    # and topic[0] = 0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545
    @staticmethod
    def logCommand0():
        action = "getLogs"
        fromBlock = 379224
        toBlock = "latest"
        topic0 = "0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545" #test hash
        return f"{commands.website}&module={commands.module[4]}&action={action}&fromBlock={fromBlock}" \
               f"&toBlock={toBlock}&address={commands.address}&topic0={topic0}&apikey={commands.api_key}"

### START OF GETH/PARITY/PROXY MODULE COMMANDS ###
### START OF TOKENS MODULE COMMANDS ###
### START OF GAS TRACKER MODULE COMMANDS ###
### START OF STATS MODULE COMMANDS ###