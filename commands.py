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
        "token",
        "gastracker",
        "stats"
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
    def accountCommand2(address, startBlock, endBlock):
        action = "txlist"
        page = 1
        offset = 10
        sort = "asc"
        return f"{commands.website}&module={commands.module[0]}&action={action}&address={address}" \
               f"&startblock={startBlock}&endblock={endBlock}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={commands.api_key}"

    # get a list of 'internal transactions by address'
    @staticmethod
    def accountCommand3(address, startBlock, endBlock):
        action = "txlistinternal"
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

    # get "internal transactions" by block range # need user input for endblock
    @staticmethod
    def accountCommand5(startBlock, endBlock):
        action = "txlistinternal"
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
        return f"{commands.website}&module={commands.module[0]}&action={action}&address={address}" \
               f"&=blocktype={blocktype}&page={page}&offset={offset}&apikey={commands.api_key}"

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

    # Check Contract Execution Status
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

    # Get Block And Uncle Rewards by Block Number
    @staticmethod
    def blockCommand0(blockno):
        action = "getblockreward"
        return f"{commands.website}&module={commands.module[3]}" \
               f"&action={action}&blockno={blockno}&apikey={commands.api_key}"

    # Get Estimated Block Countdown Time by Block Number
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
    def logCommand0(address, fromBlock, toBlock):
        action = "getLogs"
        topic0 = "0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545"  # test hash
        return f"{commands.website}&module={commands.module[4]}&action={action}&fromBlock={fromBlock}" \
               f"&toBlock={toBlock}&address={address}&topic0={topic0}&apikey={commands.api_key}"

    # Get Event Logs from block number 379224 to block 400000 ,
    # where log address = 0x33990122638b9132ca29c723bdf037f1a891a70c,
    # topic[0] = 0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545
    # 'AND' topic[1] = 0x72657075746174696f6e00000000000000000000000000000000000000000000
    @staticmethod
    def logCommand1(address, fromBlock, toBlock):
        action = "getLogs"
        topic0 = "0xf63780e752c6a54a94fc52715dbc5518a3b4c3c2833d301a204226548a2a8545"  # test hash
        topic0_1_opr = "and"
        topic1 = "0x72657075746174696f6e00000000000000000000000000000000000000000000"
        return f"{commands.website}&module={commands.module[4]}&action={action}&fromBlock={fromBlock}" \
               f"&toBlock={toBlock}&address={address}&topic0={topic0}" \
               f"&topic0_1_opr={topic0_1_opr}&topic1={topic1}&apikey={commands.api_key}"

    ### START OF GETH/PARITY/PROXY MODULE COMMANDS ###

    # Returns the number of most recent block
    @staticmethod
    def proxyCommand0():
        action = "eth_blockNumber"
        return f"{commands.website}&module={commands.module[5]}&action={action}" \
               f"&apikey={commands.api_key}"

    # Returns information about a block by block number.
    @staticmethod
    def proxyCommand1(tag):
        action = "eth_getBlockByNumber"
        # tag = 0x10d4f
        boolean = 'true'
        return f"{commands.website}&module={commands.module[5]}&action={action}&tag={tag}" \
               f"&boolean={boolean}&apikey={commands.api_key}"

    # Returns information about a uncle by block number.
    @staticmethod
    def proxyCommand2(tag):
        action = "eth_getUncleByBlockNumberAndIndex"
        index = 0x0
        return f"{commands.website}&module={commands.module[5]}&action={action}&tag={tag}" \
               f"&index={index}&apikey={commands.api_key}"

    # Returns the number of transactions in a block.
    @staticmethod
    def proxyCommand3(tag):
        action = "eth_getBlockTransactionCountByNumber"
        return f"{commands.website}&module={commands.module[5]}&action={action}&tag={tag}" \
               f"&apikey={commands.api_key}"

    # Returns the information about a transaction requested by transaction hash.
    @staticmethod
    def proxyCommand4(txhash):
        action = "eth_getTransactionByHash"
        return f"{commands.website}&module={commands.module[5]}&action={action}&txhash{txhash}" \
               f"&apikey={commands.api_key}"

    # Returns information about a transaction by block number and transaction index position.
    @staticmethod
    def proxyCommand5(tag):
        action = "eth_getTransactionByBlockNumberAndIndex"
        index = 0x11A
        return f"{commands.website}&module={commands.module[5]}&action={action}&tag{tag}" \
               f"&index{index}&apikey={commands.api_key}"

    # Returns the number of transactions performed by an address.
    @staticmethod
    def proxyCommand6(address, tag):  # Error: returns null
        action = "eth_getTransactionCount"
        return f"{commands.website}&module={commands.module[5]}&action={action}&address{address}" \
               f"&tag{tag}&apikey={commands.api_key}"

    # Submits a pre-signed transaction for broadcast to the Ethereum network.
    #    @staticmethod
    #    def proxyCommand7():  # Error: returns null
    #        action = "eth_sendRawTransaction"
    #        hex = 0xf904808000831cfde080
    #        return f"{commands.website}&module={commands.module[5]}&action={action}&hex{hex}&apikey={commands.api_key}"

    # Returns the receipt of a transaction by transaction hash.
    @staticmethod
    def proxyCommand7(txhash):
        action = "eth_getTransactionReceipt"
        return f"{commands.website}&module={commands.module[5]}&action={action}&txhash{txhash}" \
               f"&apikey={commands.api_key}"

    # Executes a new message call immediately without creating a transaction on the block chain.
    @staticmethod
    def proxyCommand8(tag, toAddress, hashData):
        action = "eth_call"
#        to = 0xAEEF46DB4855E25702F8237E8f403FddcaF931C0 # to address
#        data = 0x70a08231000000000000000000000000e16359506c028e51f16be38986ec5746251e9724 # hash of method signature
        return f"{commands.website}&module={commands.module[5]}&action={action}&to{to}&data{data}" \
               f"&tag{tag}&apikey={commands.api_key}"

    # Returns code at a given address.
    @staticmethod
    def proxyCommand9(address, tag):
        action = "eth_getCode"
        return f"{commands.website}&module={commands.module[5]}&action={action}&address{address}" \
               f"&tag{tag}&apikey={commands.api_key}"

    # Returns the value from a storage position at a given address.
    @staticmethod  # experimental endpoint
    def proxyCommand10(address, tag):
        action = "eth_getStorageAt"
        position = 0x0
        return f"{commands.website}&module={commands.module[5]}&action={action}&address{address}" \
               f"&position{position}&tag{tag}&apikey={commands.api_key}"

    # Returns the current price per gas in gwei.
    @staticmethod
    def proxyCommand11():
        action = "eth_gasPrice"
        return f"{commands.website}&module={commands.module[5]}&action={action}" \
               f"&apikey={commands.api_key}"

    # Makes a call or transaction, which won't be added to the blockchain and returns the used gas.
    @staticmethod
    def proxyCommand12(hashData, toAddress, valueSent, gasPricePaid, gasProvided):
        action = "eth_estimateGas"
#        data = 0x4e71d92d
#        to = 0xf0160428a8552ac9bb7e050d90eeade4ddd52843
#        value = 0xff22
#        gasPrice = 0x51da038cc
#        gas = 0x5f5e0ff
        return f"{commands.website}&module={commands.module[5]}&action={action}&data{data}&to{to}" \
               f"&value{value}&gasPrice{gasPrice}&gas{gas}&apikey={commands.api_key}"

    ### START OF TOKENS MODULE COMMANDS ###

    # Returns the current amount of an ERC-20 token in circulation.
    @staticmethod
    def tokensCommand0(contractaddress):
        action = "tokensupply"
        return f"{commands.website}&module={commands.module[8]}&action={action}" \
               f"&contractaddress={contractaddress}&apikey={commands.api_key}"

    # Returns the current balance of an ERC-20 token of an address.
    @staticmethod
    def tokensCommand1(contractaddress, address, tag):
        action = "tokenbalance"
        return f"{commands.website}&module={commands.module[0]}&action={action}" \
               f"&contractaddress={contractaddress}&address={address}&apikey={commands.api_key}"

    ### START OF GAS TRACKER MODULE COMMANDS ###

    # Get Estimation of Confirmation Time
    @staticmethod
    def gasTrackerCommand0(gasPrice):
        action = "gasestimate"
        return f"{commands.website}&module={commands.module[7]}&action={action}&gasprice={gasPrice}&apikey={commands.api_key}"

    # Returns the current Safe, Proposed and Fast gas prices.
    @staticmethod
    def gasTrackerCommand1():
        action = "gasoracle"
        return f"{commands.website}&module={commands.module[7]}&action={action}&apikey={commands.api_key}"

    ### START OF STATS MODULE COMMANDS ###

    # Get total supply of ether
    @staticmethod
    def statsCommand0():
        action = "ethsupply"
        return f"{commands.website}&module={commands.module[8]}&action={action}&apikey={commands.api_key}"

    # Get ether last price
    @staticmethod
    def statsCommand1():
        action = "ethprice"
        return f"{commands.website}&module={commands.module[8]}&action={action}&apikey={commands.api_key}"

    # get ether nodes size
    @staticmethod
    def statsCommand2(startDate, endDate):
        action = "chainsize"
        clientType = "geth"
        syncMode = "default"
        sort = "asc"
        return f"{commands.website}&module={commands.module[8]}&action={action}&startdate={startDate}" \
               f"&enddate={endDate}&clienttype={clientType}&syncmode={syncMode}&sort={sort}&apikey={commands.api_key}"

    # Returns the total number of discoverable Ethereum nodes.
    @staticmethod
    def statsCommand3():
        action = "nodecount"
        return f"{commands.website}&module={commands.module[8]}&action={action}&apiKey={commands.api_key}"