

class command:
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

    @staticmethod
    def __init__(api_key, website, module):
        api_key = api_key
        website = website
        module = module

    # Get Ether Balance for a Single Address
    @staticmethod
    def command0(api_key, website, module, action, address, tag):
        apikey = command.api_key
        website = command.website
        module = command.module[0]  # account module
        action = action
        address = address
        tag = tag
        return f"{website}&module={module}&action={action}&address={address}&tag={tag}&apikey={api_key}"

    # Get Ether Balance for Multiple Addresses in a Single Call
    @staticmethod
    def command1(api_key, website, module, action, address, tag):
        website = command.website
        apikey = command.api_key
        action = action
        module = command.module[0]
        address = address
        tag = tag
        return f"{website}&module={module}&action={action}&address={address}&tag={tag}&apikey={api_key}"

    # Get a list of 'Normal' Transactions By Address
    @staticmethod
    def command2(api_key, website, module, action, address):
        website = command.website
        apikey = command.api_key
        action = action
        module = command.module[0]
        address = address
        startBlock = 0
        endBlock = 99999999
        page = 1
        offset = 10
        sort = "asc"
        return f"{website}&module={module}&action={action}&address={address}" \
               f"&startblock={startBlock}&endblock={endBlock}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={api_key}"

    @staticmethod
    # get a list of 'internal transactions by address'
    def command3(api_key, website, module, action, address):
        website = command.website
        apikey = command.api_key
        module = command.module[0]
        action = action
        address = address
        startBlock = 0
        endBlock = 99999999
        page = 1
        offset = 10
        sort = "asc"
        return f"{website}&module={module}&action={action}&address={address}" \
               f"&startblock={startBlock}&endblock={endBlock}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={api_key}"

    @staticmethod
    # Get 'Internal Transactions' by Transaction Hash
    def command4(apikey, website, module, action, txhash):
        website = website
        apikey = command.api_key
        action = action
        module = command.module[0]
        txhash = txhash
        return  f"{website}&module={module}&action={action}&txhash={txhash}&apikey={apikey}"

    @staticmethod
    # get "internal transactions" by block range
    def command5(apikey, website, module, action):
        website = command.website
        module = command.module[0]
        apikey = command.api_key
        action = action
        startBlock = 0
        endBlock = 99999999
        page = 1
        offset = 10
        sort = "asc"
        return f"{website}&module={module}&action={action}&startblock={startBlock}&endblock={endBlock}&page={page}" \
               f"&offset={offset}&sort={sort}&apikey={apikey}"


"""
    # Get a list of 'ERC20 - Token Transfer Events' by Address
    def command7(command7):
        command7.website = website
        command7.apikey = api_key
        command7.action = "tokentx"
        command7.module = module_account
        command7.address = ""
        command7.page = 1
        command7.offset = 100
        command7.sort = "asc"
        command7.contractaddress = ""

    # Get a list of 'ERC721 - Token Transfer Events' by Address
    def command8(command8):
        command8.website = website
        command8.module = module_account
        command8.action = "tokennfttx"
        command8.contractAddress = ""
        command8.address = ""
        command8.page = 1
        command8.offset = 100
        command8.sort = "asc"
        command8.apikey = api_key

    # Get list of Blocks Mined by Address
   def command9(command9):
       command9.website = website
       command9.module = module_account
       command9.action = "getminedblocks"
       command9.blocktype = "blocks"
       command9.address = ""
       command9.page = 1
        command9.offset = 100
"""
