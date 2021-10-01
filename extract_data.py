import json
import requests
from commands import commands, getEthAdress, getContractAdress, getTxHash, getBlockNo, getTimeStamp, getTag, getHex,\
    getToAddress, getHashData, getGasProvided, getGasPricePaid, getValueSentInTransaction

def userinput():

    passthrough = ""

    module_choice = int(input(f"What module do u wish to utilize:\n1.{commands.module[0]}\n2.{commands.module[1]}\n"
                              f"3.{commands.module[2]}\n4.{commands.module[3]}\n5.{commands.module[4]}\n"
                              f"6.{commands.module[5]}\n7.{commands.module[6]}\n8.{commands.module[7]}\n"
                              f"9.{commands.module[8]}\n"))

    if module_choice == 1:
        conversion_dict = {
            0: "etherBalanceSingle",
            1: "etherBalanceMultiple",
            2: "listNormalTransactions",
            3: "listInternalTransactions",
            4: "txhashInternalTransactions",
            5: "blockRangeInternalTx",
            6: "listErc20Transfer",
            7: "listErc721Transfer",
            8: "listBlocksMined"
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n3.{conversion_dict[2]}\n"
                  f"4.{conversion_dict[3]}\n5.{conversion_dict[4]}\n"
                  f"6.{conversion_dict[5]}\n7.{conversion_dict[6]}\n"
                  f"8.{conversion_dict[7]}\n9.{conversion_dict[0]}\n"))
        ethaddress = getEthAdress()
        txhash = getTxHash()
        contractaddress = getContractAdress()
        if command_choice == 1:
            ethaddress = getEthAdress()
            accountCommand = commands.accountCommand0(ethaddress)
        elif command_choice == 2:
            ethaddress == getEthAdress()
            accountCommand = commands.accountCommand1(ethaddress)
        elif command_choice == 3:
            ethaddress = getEthAdress()
            accountCommand = commands.accountCommand2(ethaddress)
        elif command_choice == 4
            ethaddress = getEthAdress()
            accountCommand = commands.accountCommand3(ethaddress)
        elif command_choice == 5
            txhash = getTxHash()
            accountCommand = commands.accountCommand4(txhash)
        elif command_choice == 6
            accountCommand = commands.accountCommand5()
        elif command_choice == 7
            ethaddress = getEthAdress()
            contractaddress = getContractAdress()
            accountCommand = commands.accountCommand6(ethaddress, contractaddress)
        elif command_choice == 8
            ethaddress = getEthAdress()
            contractaddress = getContractAdress()
            accountCommand = commands.accountCommand7(ethaddress, contractaddress)
        elif command_choice == 9
            ethaddress = getEthAdress()
            accountCommand = commands.accountCommand8(ethaddress)

        accountCommandsList = {
         #   0: commands.accountCommand0(ethaddress),  # Get Ether Balance for a Single Address

         #   1: commands.accountCommand1(ethaddress),
            # Get Ether Balance for Multiple Addresses in a Single Call

         #   2: commands.accountCommand2(ethaddress),
            # Get a list of'Normal' Transactions By Address

         #   3: commands.accountCommand3(ethaddress),
            # get a list of 'internal transactions by address'

         #   4: commands.accountCommand4(txhash),
            # Get 'Internal Transactions' by Transaction Hash

         #   5: commands.accountCommand5(),  # get "internal transactions" by block range

         #   6: commands.accountCommand6(ethaddress, contractaddress),
            # Get a list of 'ERC20 - Token Transfer Events' by Address

        #    7: commands.accountCommand7(ethaddress, contractaddress),
            # Get a list of 'ERC721 - Token Transfer Events' by Address

       #     8: commands.accountCommand8(ethaddress)  # Get list of Blocks Mined by Address
       # }
        #return accountCommandsList.get(command_choice-1)
        return accountCommand
    elif module_choice == 2:
        conversion_dict = {
            0: "getAbiContract",
            1: "getContractSource",
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{conversion_dict[0]}\n"
                  f"2.{conversion_dict[1]}\n"))
        ethaddress = getEthAdress()
        contractCommandsList = {
            0: commands.contractCommand0(ethaddress),
            # Get Contract ABI for Verified Contract Source Code

            1: commands.contractCommand1(ethaddress)  # Get Contract Source Code for Verified
            # Contract Source Codes
        }
        passthrough = contractCommandsList.get(command_choice-1)
    elif module_choice == 3:
        coversion_dict = {
            0: "checkContractStatus",
            1: "checkTransactionStatus",
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{coversion_dict[0]}\n"
                  f"2.{coversion_dict[1]}\n"))
        txhash = getTxHash()
        transactionCommandsList = {
            0: commands.transactionCommand0(txhash),
            # Check Contract Execution Status
            1: commands.transactionCommand1(txhash)
            # Check Transaction Receipt Status
        }
        passthrough = transactionCommandsList.get(command_choice-1)
    elif module_choice == 4:
        coversion_dict = {
            0: "GetBlockRewards",
            1: "GetEstimatedBlockCountdown",
            2: "GetBlockNumber"
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{coversion_dict[0]}\n"
                  f"2.{coversion_dict[1]}\n3.{coversion_dict[2]}"))
        blockno = getBlockNo()
        timestamp = getTimeStamp()
        blockCommandsList = {
            0: commands.blockCommand0(blockno),
            # Get Block And Uncle Rewards by BlockNo
            1: commands.blockCommand1(blockno),
            # Get Estimated Block Countdown Time by BlockNo
            2: commands.blockCommand2(timestamp)
            # Get Block Number by Timestamp
        }
        passthrough = blockCommandsList.get(command_choice-1)
    elif module_choice == 5:
        coversion_dict = {
            0: "GetEventLogs",
            1: "GetEventLogsBetweenBlocks"
        }
        command_choice = int(
            input(f"which command you like to use:\n1.{coversion_dict[0]}\n"
                  f"2.{coversion_dict[1]}\n"))
        ethaddress = getEthAdress()
        logCommandsList = {
            0: commands.logCommand0(ethaddress),
            # Get Block And Uncle Rewards by BlockNo
            1: commands.logCommand1(ethaddress)
        }
    elif module_choice == 6:
        conversion_dict = {
            0: "GetMostRecentBlock",
            1: "GetBlockByNumber",
            2: "GetUncleByBlockAndIndex",
            3: "GetBlockTransactionCountByNumber",
            4: "GetTransactionByHash",
            5: "GetTransactionByBlockNumberAndIndex",
            6: "GetTransactionCount",
            7: "GetRawTransaction",                # Error: returns null  BAN THIS COMMAND
            8: "getTransactionReceipt",
            9: "getCall",
            10: "GetCode",
            11: "GetStorageAt",
            12: "getGasPrice",
            13: "getEstimatedGas",
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

        #ethaddress = getEthAdress()
        #tag = getTag()
        #txhash = getTxHash()
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
            ethaddress = getEthAdress()
            proxy = commands.proxyCommand6(ethaddress)  # address = 0x4bd5900Cb274ef15b153066D736bf3e83A9ba44e
        elif command_choice == 8:
            hex = getHex()
            proxy = commands.proxyCommand7()  # Error: returns null hex = 0xf904808000831cfde080
        elif command_choice == 9:
            txhash = getTxHash()
            proxy = commands.proxyCommand8(txhash) # hash =0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170
        elif command_choice == 10:
            toAddress = getToAddress() # address = 0xAEEF46DB4855E25702F8237E8f403FddcaF931C0
            data = getHashData()
            proxy = commands.proxyCommand9(toAddress, data)  # Error: returns null  data = 0x70a08231000000000000000000000000e16359506c028e51f16be38986ec5746251e9724
        elif command_choice == 11:
            ethaddress = getEthAdress()
            proxy = commands.proxyCommand10(ethaddress)  # Error: returns error  data  = 0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd
        elif command_choice == 12:
            ethaddress = getEthAdress()
            proxy = commands.proxyCommand11(ethaddress)
        elif command_choice == 13:
            proxy = commands.proxyCommand12()
        elif command_choice == 14:
            hashData = getHashData()
            toAddress = getToAddress()
            gasProvided = getGasProvided()
            gasPricePaid = getGasPricePaid()
            valueSent = getValueSentInTransaction()
            proxy = commands.proxyCommand13(hashData,toAddress,gasProvided,gasPricePaid,valueSent)



       # proxyCommandsList = {
       #     0: commands.proxyCommand0(),
       #     1: commands.proxyCommand1(tag),
       #     2: commands.proxyCommand2(tag),
       #     3: commands.proxyCommand3(tag),
       #     4: commands.proxyCommand4(txhash),
        #    5: commands.proxyCommand5(tag),
       #     6: commands.proxyCommand6(ethaddress),
       #     7: commands.proxyCommand7()
     #       8: commands.proxyCommand8(),
      #      9: commands.proxyCommand9(),
       #     10: commands.proxyCommand10(),
        #    11: commands.proxyCommand11(),
         #  13: commands.proxyCommand13(),
          #  14: commands.proxyCommand14()
        #}
        #passthrough = proxyCommandsList.get(command_choice - 1)
        passthrough = proxy
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