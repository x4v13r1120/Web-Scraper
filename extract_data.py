import json
import requests
from commands import commands, getEthAddress, getContractAddress, getTxHash, \
    getBlockNo, getTimeStamp, getTag, getHex,getToAddress, getHashData, \
    getGasProvided, getGasPricePaid, getValueSentInTransaction, getGasPrice


def userinput():
    passthrough = ""

    module_choice = int(input(f"What module do u wish to utilize:\n1.{commands.module[0]}\n2.{commands.module[1]}\n"
                              f"3.{commands.module[2]}\n4.{commands.module[3]}\n5.{commands.module[4]}\n"
                              f"6.{commands.module[5]}\n7.{commands.module[6]}\n8.{commands.module[7]}\n"
                              f"9.{commands.module[8]}\n"))

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
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n3.{conversion_dict[2]}\n"
                  f"4.{conversion_dict[3]}\n5.{conversion_dict[4]}\n"
                  f"6.{conversion_dict[5]}\n7.{conversion_dict[6]}\n"
                  f"8.{conversion_dict[7]}\n9.{conversion_dict[0]}\n"))
        if command_choice == 1:
            ethaddress = getEthAddress()
            accountCommand = commands.accountCommand0(ethaddress)
        elif command_choice == 2:
            ethaddress = getEthAddress()
            accountCommand = commands.accountCommand1(ethaddress)
        elif command_choice == 3:
            ethaddress = getEthAddress()
            accountCommand = commands.accountCommand2(ethaddress)
        elif command_choice == 4:
            ethaddress = getEthAddress()
            accountCommand = commands.accountCommand3(ethaddress)
        elif command_choice == 5:
            txhash = getTxHash()
            accountCommand = commands.accountCommand4(txhash)
        elif command_choice == 6:
            accountCommand = commands.accountCommand5()
        elif command_choice == 7:
            ethaddress = getEthAddress()
            contractaddress = getContractAddress()
            accountCommand = commands.accountCommand6(ethaddress, contractaddress)
        elif command_choice == 8:
            ethaddress = getEthAddress()
            contractaddress = getContractAddress()
            accountCommand = commands.accountCommand7(ethaddress, contractaddress)
        elif command_choice == 9:
            ethaddress = getEthAddress()
            accountCommand = commands.accountCommand8(ethaddress)
        return accountCommand
    elif module_choice == 2:
        conversion_dict = {
            0: "Get Contract ABI for Verified Contract Source Code",
            1: "Get Contract Source Code for Verified Contract Source Codes",
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n"))
        ethaddress = getEthAddress()
        contractCommandsList = {
            0: commands.contractCommand0(ethaddress),
            # Get Contract ABI for Verified Contract Source Code

            1: commands.contractCommand1(ethaddress)  # Get Contract Source Code for Verified
            # Contract Source Codes
        }
        passthrough = contractCommandsList.get(command_choice - 1)
    elif module_choice == 3:
        conversion_dict = {
            0: "Check Contract Execution Status",
            1: "Check Transaction Receipt Status",
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n"))
        txhash = getTxHash()
        transactionCommandsList = {
            0: commands.transactionCommand0(txhash),
            # Check Contract Execution Status
            1: commands.transactionCommand1(txhash)
            # Check Transaction Receipt Status
        }
        passthrough = transactionCommandsList.get(command_choice - 1)
    elif module_choice == 4:
        conversion_dict = {
            0: "Get Block And Uncle Rewards by Block Number",
            1: "Get Estimated Block Countdown Time by Block Number",
            2: "Get Block Number by Timestamp"
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n3.{conversion_dict[2]}"))
        if command_choice == 1:
            blockno = getBlockNo()
            blockCommand = commands.blockCommandn0(blockno)
        elif command_choice == 2:
            blockno = getBlockNo()
            blockCommand = commands.blockCommandn1(blockno)
        elif command_choice == 3:
            timestamp = getTimeStamp()
            blockCommand = commands.blockCommand2(timestamp)
        passthrough = blockCommand
    elif module_choice == 5:
        conversion_dict = {
            0: "Get Event Logs from block number ____ to 'latest' Block",
            1: "Get Event Logs from block number ____ to block ____"
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n"))
        ethaddress = getEthAddress()
        logCommandsList = {
            0: commands.logCommand0(ethaddress),
            # Get Block And Uncle Rewards by BlockNo
            1: commands.logCommand1(ethaddress)
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
            7: "Submits a pre-signed transaction for broadcast to the Ethereum"
               " network",  # Error: returns null  BAN THIS COMMAND
            8: "Returns the receipt of a transaction by transaction hash",
            9: "Executes a new message call immediately without creating a "
               "transaction on the block chain",
            10: "Returns code at a given address",
            11: "Returns the value from a storage position at a given address",
            12: "Returns the current price per gas in gwei",
            13: "Makes a call or transaction, which won't be added to the "
                "blockchain and returns the used gas",
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n3.{conversion_dict[2]}\n"
                  f"4.{conversion_dict[3]}\n5.{conversion_dict[4]}\n"
                  f"6.{conversion_dict[5]}\n7.{conversion_dict[6]}\n"
                  f"8.{conversion_dict[7]}\n9.{conversion_dict[8]}\n"
                  f"10.{conversion_dict[9]}\n11.{conversion_dict[10]}\n"
                  f"12.{conversion_dict[11]}\n13.{conversion_dict[12]}\n"
                  f"14.{conversion_dict[13]}\n"))

        # ethaddress = getEthaddress()
        # tag = getTag()
        # txhash = getTxHash()
        if command_choice == 1:
            proxy = commands.proxyCommand0()
        elif command_choice == 2:
            tag = getTag()
            proxy = commands.proxyCommand1(tag)
        elif command_choice == 3:
            tag = getTag()
            proxy = commands.proxyCommand2(tag)
        elif command_choice == 4:
            tag = getTag()
            proxy = commands.proxyCommand3(tag)
        elif command_choice == 5:
            txhash = getTxHash()
            proxy = commands.proxyCommand4(txhash)
        elif command_choice == 6:
            tag = getTag()
            proxy = commands.proxyCommand5(tag)
        elif command_choice == 7:
            ethaddress = getEthAddress()
            proxy = commands.proxyCommand6(ethaddress)  # address = 0x4bd5900Cb274ef15b153066D736bf3e83A9ba44e
        elif command_choice == 8:
            hex = getHex()
            proxy = commands.proxyCommand7()  # Error: returns null hex = 0xf904808000831cfde080
        elif command_choice == 9:
            txhash = getTxHash()
            proxy = commands.proxyCommand8(
                txhash)  # hash =0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170
        elif command_choice == 10:
            toaddress = getToAddress()  # address = 0xAEEF46DB4855E25702F8237E8f403FddcaF931C0
            data = getHashData()
            proxy = commands.proxyCommand9(toaddress,
                                           data)  # Error: returns null  data = 0x70a08231000000000000000000000000e16359506c028e51f16be38986ec5746251e9724
        elif command_choice == 11:
            ethaddress = getEthAddress()
            proxy = commands.proxyCommand10(
                ethaddress)  # Error: returns error  data  = 0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd
        elif command_choice == 12:
            ethaddress = getEthAddress()
            proxy = commands.proxyCommand11(ethaddress)
        elif command_choice == 13:
            proxy = commands.proxyCommand12()
        elif command_choice == 14:
            hashData = getHashData()
            toaddress = getToAddress()
            gasProvided = getGasProvided()
            gasPricePaid = getGasPricePaid()
            valueSent = getValueSentInTransaction()
            proxy = commands.proxyCommand13(hashData, toaddress, gasProvided, gasPricePaid, valueSent)
        passthrough = proxy
    elif module_choice == 7:
        conversion_dict = {
            0: "Returns the current amount of an ERC-20 token in circulation",
            1: "Returns the current balance of an ERC-20 token of an address",
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}"))

        if command_choice == 1:
            contractAddress = getContractAddress()
            tokens = commands.tokensCommand0(contractAddress)
        elif command_choice == 2:
            contractAddress = getContractAddress()
            address = getEthAddress()
            tag = getTag()
            tokens = commands.tokensCommand1(contractAddress, address, tag)

        passthrough = tokens
    elif module_choice == 8:
        conversion_dict = {
            0: "Get Estimation of Confirmation Time",
            1: "Returns the current Safe, Proposed and Fast gas prices",
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n"))
        if command_choice == 1:
            gasPrice = getGasPrice()
            gasTracker = commands.gasTrackerCommand0(gasPrice)
        elif command_choice == 2:
            gasTracker = commands.gasTrackerCommand1()

        passthrough = gasTracker
    elif module_choice == 9:
        conversion_dict = {
            0: "Get total supply of ether",
            1: "Get ether last price",
            2: "Get ether nodes size",
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n3.{conversion_dict[2]}\n"))
        if command_choice == 1:
            # returns the current amount of ether in circulation
            stats = commands.statsCommand0()
        elif command_choice == 2:
            # returns the latest price of 1 ETH
            stats = commands.statsCommand1()
        elif command_choice == 3:
            # Returns the size of the ethereum  blockchain, in bytes, over date range
            stats = commands.statsCommand2()
        passthrough = stats
    return passthrough


def extract():
    # make request using command
    response = requests.get(userinput())
    address_content = response.json()
    result = address_content.get("result")
    # dump data
    with open("data/jsondata.json", "w") as outfile:
        json.dump(result, outfile)

    # starting cleaning process
    comment = False
    with open("data/jsondata.json", 'r') as infile, open("data/cleaned_data.json", 'w') as \
            outfile:
        for line in infile:
            if line.startswith("/*"):
                comment = True
                continue
            elif line.startswith("*/"):
                comment = False
                continue
            elif comment:
                continue
            if len(line.strip()) > 0:
                if not line.strip().startswith("//"):
                    if not comment:
                        outfile.write(f"{line}\n")
                        print("Data has been extracted and cleaned!!!")
