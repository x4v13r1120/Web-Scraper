import classes


### GETTERS ###
def getValueSentInTransaction():
    while True:
        valueSent = str(input(
            "Please enter value sent in transaction."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
        try:
            if valueSent.isalnum():
                return valueSent
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(valueSent)


def getGasPricePaid():
    while True:
        gasPricePaid = str(input(
            "Please enter gas price paid."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
        try:
            if gasPricePaid.isalnum():
                return gasPricePaid
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(gasPricePaid)


def getGasProvided():
    while True:
        gasProvided = str(input(
            "Please enter gas provided"))  # address for testing = 0x5f5e0ff
        try:
            if gasProvided.isalnum():
                return gasProvided
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(gasProvided)


def getToAddress():
    while True:
        toAddress = str(input(
            "Please enter address to interact with."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
        try:
            if toAddress.isalnum():
                return toAddress
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(toAddress)


def getHashData():
    while True:
        hashData = str(input(
            "Please enter hash of method signature"))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
        try:
            if hashData.isalnum():
                return hashData
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(hashData)


def getMultipleEthAddress():
    while True:
        address = str(input(
            "Please enter each Ether address followed by a ',':"))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
        try:
            if address.find('0x', 0, 1000) != -1:
                return address
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(address)


def getEthAddress():
    while True:
        address = str(input(
            "Please enter Ether Address."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
        try:
            if address.isalnum():
                return address
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(address)


def getHex():
    while True:
        hex = str(input(
            "Please enter hex Address."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
        try:
            if hex.isalnum():
                return hex
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(hex)


def getTag():
    while True:
        tag = str(input(
            "Please enter the tag."))  # tag for testing = 0x10d4f
        try:
            if tag.isalnum():
                return tag
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(tag)


def getTxHash():
    while True:
        txhash = str(input(
            "Please enter Transaction Hash."))  # address for testing =
        # 0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170
        try:
            if txhash.isalnum():
                return txhash
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(txhash)


def getContractAddress():
    while True:
        contractAddress = str(input(
            "Please enter Contract Address."))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
        try:
            if contractAddress.isalnum():
                return contractAddress
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(contractAddress)


def getBlockNo():
    while True:
        blockno = str(input("Please enter Block Number."))  # block for testing = 216540
        try:
            if blockno.isdecimal():
                return blockno
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return blockno


def getTimeStamp():
    try:
        timestamp = int(input("Please enter Timestamp."))  # timestamp for testing 1578638524
    except ValueError:
        print("Unacceptable input. Please try again.")
    return timestamp


def getIndex():
    try:
        index = int(input("Please enter index."))  # index for testing can be 0x0 or 0x5 anything of that sort.
    except ValueError:
        print("Unacceptable input. Please try again.")
        return index


def getPosition():
    try:
        position = int(input("Please enter hex code of the position in storage"))  # 0x0, 0x5, or 0x11C
    except ValueError:
        print("Unacceptable input. Please try again.")
        return position


def getGasPrice():
    gasPrice = ''
    try:
        gasPrice = int(input("Please enter gas price."))  # $0
    except ValueError:
        print("Unacceptable input. Please try again.")
    return gasPrice


def getStartBlock():
    startBlock = ''
    try:
        startBlock = int(input("Enter the starting block."))  # 0
    except ValueError:
        print("Unacceptable input. Please try again.")
    return startBlock


def getEndBlock():
    endBlock = ''
    try:
        endBlock = int(input("Enter the ending block."))  # 99999
    except ValueError:
        print("Unacceptable input. Please try again.")
    return endBlock


def getFromBlock():
    while True:
        fromBlock = str(input("Enter the block the transaction is going to."))  # 'latest'
        try:
            if fromBlock.isalnum():
                return fromBlock
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
        return str(fromBlock)


def getToBlock():
    while True:
        toBlock = str(input("Enter the block the transaction is going to."))  # 'latest'
        try:
            if toBlock.isalpha() | toBlock.isalnum():
                return toBlock
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
        return str(toBlock)


def getStartDate():
    while True:
        startDate = str(input(
            "Please enter the starting data of the query."))  #
        try:
            if startDate.isalnum():
                return startDate
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(startDate)


def getEndDate():
    while True:
        endDate = str(input(
            "Please enter the end date of the query."))
        try:
            if endDate.isalnum():
                return endDate
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return str(endDate)


### COMMAND SELECTION ###
def getModuleChoice():
    # exception handling for when users input wrong type or number
    module = classes.module()
    while True:
        module_choice = input(f"What module do u wish to utilize:\n1.{module.types[0]}\n2.{module.types[1]}\n"
                              f"3.{module.types[2]}\n4.{module.types[3]}\n5.{module.types[4]}\n"
                              f"6.{module.types[5]}\n7.{module.types[6]}\n8.{module.types[7]}\n"
                              f"9.{module.types[8]}\n")
        try:
            val = int(module_choice)
            if 1 <= val <= 9:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(module_choice)


def getM0CommandChoice(module_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{module_dict[0]}\n"
                               f"2.{module_dict[1]}\n3.{module_dict[2]}\n"
                               f"4.{module_dict[3]}\n5.{module_dict[4]}\n"
                               f"6.{module_dict[5]}\n7.{module_dict[6]}\n"
                               f"8.{module_dict[7]}\n")
        try:
            val = int(command_choice)
            if val >= 1 and val <= 9:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)


def getM1CommandChoice(module_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{module_dict[0]}\n"
                               f"2.{module_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <= 2:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)


def getM2CommandChoice(module_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{module_dict[0]}\n"
                               f"2.{module_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <= 2:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)


def getM3CommandChoice(module_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{module_dict[0]}\n"
                               f"2.{module_dict[1]}\n3.{module_dict[2]}\n")
        try:
            val = int(command_choice)
            if val >= 1 and val <= 3:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)


def getM4CommandChoice(module_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{module_dict[0]}\n"
                               f"2.{module_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <= 2:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)


def getM5CommandChoice(module_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{module_dict[0]}\n"
                               f"2.{module_dict[1]}\n3.{module_dict[2]}\n"
                               f"4.{module_dict[3]}\n5.{module_dict[4]}\n"
                               f"6.{module_dict[5]}\n7.{module_dict[6]}\n"
                               f"8.{module_dict[7]}\n9.{module_dict[8]}\n"
                               f"10.{module_dict[9]}\n11.{module_dict[10]}\n"
                               f"12.{module_dict[11]}\n13.{module_dict[12]}\n")
        try:
            val = int(command_choice)
            if val >= 1 and val <= 12:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)


def getM6CommandChoice(module_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{module_dict[0]}\n"
                               f"2.{module_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <= 9:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)


def getM7CommandChoice(module_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{module_dict[0]}\n"
                               f"2.{module_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <= 9:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)


def getM8CommandChoice(module_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{module_dict[0]}\n"
                               f"2.{module_dict[1]}\n3.{module_dict[2]}\n4.{module_dict[3]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <= 9 and val:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)


module_choice = getModuleChoice()


def getCommandChoice():
    command_choice = None
    module_dict1 = {
        0: "Get Ether Balance for a Single or Multiple Addresses in a Single Call",
        1: "Get a list of Normal Transactions By Address",
        2: "Get a list of internal transactions by address",
        3: "Get 'Internal Transactions' by Transaction Hash",
        4: "Get internal transactions by block range",
        5: "Get a list of 'ERC20 - Token Transfer Events' by Address",
        6: "Get a list of 'ERC721 - Token Transfer Events' by Address",
        7: "Get list of Blocks Mined by Address"
    }
    module_dict2 = {
        0: "Get Contract ABI for Verified Contract Source Code",
        1: "Get Contract Source Code for Verified Contract Source Codes",
    }
    module_dict3 = {
        0: "Get Block And Uncle Rewards by Block Number",
        1: "Get Estimated Block Countdown Time by Block Number",
        2: "Get Block Number by Timestamp"
    }
    module_dict4 = {
        0: "Get Event Logs from block number ____ to 'latest' Block",
    }
    module_dict5 = {
        0: "Returns the number of most recent block",
        1: "Returns information about a block by block number",
        2: "Returns information about a uncle by block number",
        3: "Returns the number of transactions in a block",
        4: "Returns the information about a transaction requested by "
           "transaction hash",
        5: "Returns information about a transaction by block number and "
           "transaction index position",
        6: "Returns the number of transactions performed by an address",
        7: "Returns the receipt of a transaction by transaction hash",
        8: "Executes a new message call immediately without creating a "
           "transaction on the block chain",
        9: "Returns code at a given address",
        10: "Returns the value from a storage position at a given address",
        11: "Returns the current price per gas in gwei",
        12: "Makes a call or transaction, which won't be added to the "
            "blockchain and returns the used gas",
    }
    module_dict6 = {
        0: "Returns the current amount of an ERC-20 token in circulation",
        1: "Returns the current balance of an ERC-20 token of an address",
    }
    module_dict7 = {
        0: "Get Estimation of Confirmation Time",
        1: "Returns the current Safe, Proposed and Fast gas prices",
    }
    module_dict8 = {
        0: "Get total supply of ether",
        1: "Get total supply of ether, ETH2 staking rewards and EIP1559 burnt fees stats",
        2: "Get ether last price",
        3: "Get ether nodes size",
        4: "Get total node count",
    }
    if module_choice == 1:
        command_choice = getM0CommandChoice(module_dict1)
    elif module_choice == 2:
        command_choice = getM1CommandChoice(module_dict2)
    elif module_choice == 3:
        command_choice = getM2CommandChoice(module_dict3)
    elif module_choice == 4:
        command_choice = getM3CommandChoice(module_dict4)
    elif module_choice == 5:
        command_choice = getM5CommandChoice(module_dict5)
    elif module_choice == 6:
        command_choice = getM6CommandChoice(module_dict6)
    elif module_choice == 7:
        command_choice = getM7CommandChoice(module_dict7)
    elif module_choice == 8:
        command_choice = getM8CommandChoice(module_dict8)

    return command_choice


command_choice = getCommandChoice()


def userInput():
    passthrough = ""

    if module_choice == 1:
        module0 = classes.account()
        if command_choice == 1:
            passthrough = module0.GetEtherBalanceForAddresses()
        elif command_choice == 2:
            passthrough = module0.GetlistNormalTransactionsByAddress()
        elif command_choice == 3:
            passthrough = module0.GetListInternalTransactionsByAddress()
        elif command_choice == 4:
            passthrough = module0.GetInternalTransactionsByHash()
        elif command_choice == 5:
            passthrough = module0.GetInternalTransactionsByBlockRange()
        elif command_choice == 6:
            passthrough = module0.GetListOfERC20TokenTransferEventsByAddress()
        elif command_choice == 7:
            passthrough = module0.GetListOfERC721TokenTransferEventsByAddress()
        elif command_choice == 8:
            passthrough = module0.GetListOfBlocksMinedByAddress()

    elif module_choice == 2:
        module1 = classes.contracts()

        if command_choice == 1:
            passthrough = module1.GetContractABIForVerifiedContractSourceCodes()
        elif command_choice == 2:
            passthrough = module1.GetContractSourceCodeForVerifiedContractSourceCodes()

    elif module_choice == 3:
        module2 = classes.transactions()

        if command_choice == 1:
            passthrough = module2.CheckContractExecutionStatus()
        elif command_choice == 2:
            passthrough = module2.CheckTransactionReceiptStatus()

    elif module_choice == 4:
        module3 = classes.blocks()

        if command_choice == 1:
            passthrough = module3.GetBlockAndUncleRewardsByBlockno()
        elif command_choice == 2:
            passthrough = module3.GetEstimatedBlockCountdownTimeByBlockno()
        elif command_choice == 3:
            passthrough = module3.GetBlockNumberByTimestamp()

    elif module_choice == 5:
        module4 = classes.logs()

        if command_choice == 1:
            passthrough = module4.SampleLogAPIQueries()

    elif module_choice == 6:
        module5 = classes.proxy()

        if command_choice == 1:
            passthrough = module5.Eth_BlockNumber()
        elif command_choice == 2:
            passthrough = module5.Eth_GetBlockByNumber()
        elif command_choice == 3:
            passthrough = module5.Eth_GetUncleByBlockNumberAndIndex()
        elif command_choice == 4:
            passthrough = module5.Eth_GetBlockTransactionCountByNumber()
        elif command_choice == 5:
            passthrough = module5.Eth_getTransactionByHash()
        elif command_choice == 6:
            passthrough = module5.Eth_GetUncleByBlockNumberAndIndex()
        elif command_choice == 7:
            passthrough = module5.Eth_GetTransactionCount()
        elif command_choice == 8:
            passthrough = module5.Eth_getTransactionReceipt()
        elif command_choice == 9:
            passthrough = module5.Eth_Call()
        elif command_choice == 10:
            passthrough = module5.Eth_GetCode()
        elif command_choice == 11:
            passthrough = module5.Eth_GetStorageAt()
        elif command_choice == 12:
            passthrough = module5.Eth_GasPrice()
        elif command_choice == 13:
            passthrough = module5.Eth_EstimateGas()

    elif module_choice == 7:
        module6 = classes.tokens()

        if command_choice == 1:
            passthrough = module6.GetERC20TokenTotalSupplyByContractAddress()
        elif command_choice == 2:
            passthrough = module6.GetERC20TokenAccountBalanceForTokenContractAddress()

    elif module_choice == 8:
        module7 = classes.gastracker()

        if command_choice == 1:
            passthrough = module7.GetEstimationOfConfirmationTime()
        elif command_choice == 2:
            passthrough = module7.GetGasOracle()

    elif module_choice == 9:
        module8 = classes.stats()

        if command_choice == 1:
            passthrough = module8.GetTotalSupplyOfEther()
        elif command_choice == 2:
            passthrough = module8.GetTotalSupplyOfEther2()
        elif command_choice == 3:
            passthrough = module8.GetEtherLastPrice()
        elif command_choice == 4:
            passthrough = module8.GetEthereumNodesSize()
        elif command_choice == 5:
            passthrough = module8.GetTotalNodesCount()

    return passthrough
