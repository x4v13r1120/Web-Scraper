import classes
import transform_data
import sqlite3
import load_data



def userInput():
    passthrough = ""

    module_choice = getModuleChoice()

    if module_choice == 1:
        conversion_dict = {
            0: "Get Ether Balance for a Single Address",
            1: "Get Ether Balance for Multiple Addresses in a Single Call",
            2: "Get a list of Normal Transactions By Address",
            3: "Get a list of internal transactions by address",
            4: "Get 'Internal Transactions' by Transaction Hash",
            5: "Get internal transactions by block range",
            6: "Get a list of 'ERC20 - Token Transfer Events' by Address",
            7: "Get a list of 'ERC721 - Token Transfer Events' by Address",
            8: "Get list of Blocks Mined by Address"
        }

        command_choice = getM1CommandChoice(conversion_dict)

        if command_choice == 1:
            ethaddress = getEthAddress()
            accountCommand = commands.accountCommand0(ethaddress)
            load_data.insertmodChoicecomChoice(module_choice,command_choice)

    elif module_choice == 2:
        conversion_dict = {
            0: "Get Contract ABI for Verified Contract Source Code",
            1: "Get Contract Source Code for Verified Contract Source Codes",
        }

    elif module_choice == 3:
        conversion_dict = {
            0: "Check Contract Execution Status",
            1: "Check Transaction Receipt Status",
        }

    elif module_choice == 4:
        conversion_dict = {
            0: "Get Block And Uncle Rewards by Block Number",
            1: "Get Estimated Block Countdown Time by Block Number",
            2: "Get Block Number by Timestamp"
        }

    elif module_choice == 5:
        conversion_dict = {
            0: "Get Event Logs from block number ____ to 'latest' Block",
            1: "Get Event Logs from block number ____ to block ____"
        }

    elif module_choice == 6:
        conversion_dict = {
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

    elif module_choice == 7:
        conversion_dict = {
            0: "Returns the current amount of an ERC-20 token in circulation",
            1: "Returns the current balance of an ERC-20 token of an address",
        }

    elif module_choice == 8:
        conversion_dict = {
            0: "Get Estimation of Confirmation Time",
            1: "Returns the current Safe, Proposed and Fast gas prices",
        }

    elif module_choice == 9:
        conversion_dict = {
            0: "Get total supply of ether",
            1: "Get ether last price",
            2: "Get ether nodes size",
            3: "Get total node count",
        }

    return passthrough

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
            "Please enter gas provided"))  # address for testing = 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
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
    try:
        blockno = int(input("Please enter Block Number."))  # block for testing = 216540
    except ValueError:
        print("Unacceptable input. Please try again.")
    return blockno

def getTimeStamp():
    try:
        timestamp = int(input("Please enter Timestamp."))  # timestamp for testing 1578638524
    except ValueError:
        print("Unacceptable input. Please try again.")
    return timestamp

def getGasPrice():
    try:
        gasPrice = int(input("Please enter gas price.")) # $0
    except ValueError:
        print("Unacceptable input. Please try again.")
    return gasPrice

def getStartBlock():
    try:
        startBlock = int(input("Enter the starting block.")) #0
    except ValueError:
        print("Unacceptable input. Please try again.")
    return startBlock

def getEndBlock():
    try:
        endBlock = int(input("Enter the ending block.")) #99999
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
            if toBlock.isalnum():
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
        module_choice = input(f"What module do u wish to utilize:\n1.{classes.module[0]}\n2.{classes.module[1]}\n"
                              f"3.{classes.module[2]}\n4.{classes.module[3]}\n5.{classes.module[4]}\n"
                              f"6.{classes.module[5]}\n7.{classes.module[6]}\n8.{classes.module[7]}\n"
                              f"9.{classes.module[8]}\n")
        try:
            val = int(module_choice)
            if val >= 1 and val <= 9:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(module_choice)

def getM1CommandChoice(conversion_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n3.{conversion_dict[2]}\n"
                  f"4.{conversion_dict[3]}\n5.{conversion_dict[4]}\n"
                  f"6.{conversion_dict[5]}\n7.{conversion_dict[6]}\n"
                  f"8.{conversion_dict[7]}\n9.{conversion_dict[8]}\n")
        try:
            val = int(command_choice)
            if val >= 1 and val <=9:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)

def getM2CommandChoice(conversion_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <=2:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)

def getM3CommandChoice(conversion_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <=2:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)

def getM4CommandChoice(conversion_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n3.{conversion_dict[2]}\n")
        try:
            val = int(command_choice)
            if val >= 1 and val <=3:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)

def getM5CommandChoice(conversion_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <=2:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)

def getM6CommandChoice(conversion_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n3.{conversion_dict[2]}\n"
                  f"4.{conversion_dict[3]}\n5.{conversion_dict[4]}\n"
                  f"6.{conversion_dict[5]}\n7.{conversion_dict[6]}\n"
                  f"8.{conversion_dict[7]}\n9.{conversion_dict[8]}\n"
                  f"10.{conversion_dict[9]}\n11.{conversion_dict[10]}\n"
                  f"12.{conversion_dict[11]}\n13.{conversion_dict[12]}\n")
        try:
            val = int(command_choice)
            if val >= 1 and val <=12:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)

def getM7CommandChoice(conversion_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <=9:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)

def getM8CommandChoice(conversion_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <=9:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)

def getM9CommandChoice(conversion_dict):
    # exception handling for when users input wrong type or number
    while True:
        command_choice = input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n3.{conversion_dict[2]}\n4.{conversion_dict[3]}")
        try:
            val = int(command_choice)
            if val >= 1 and val <=9 and val:
                return val
            else:
                print("Unacceptable input. Please try again.")
        except ValueError:
            print("Unacceptable input. Please try again.")
    return int(command_choice)

