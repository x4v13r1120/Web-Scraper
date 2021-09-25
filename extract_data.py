import json
import requests
from commands import commands, getEthAdress, getContractAdress, getTxHash, getBlockNo, getTimeStamp, getTag

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
        accountCommandsList = {
            0: commands.accountCommand0(ethaddress),  # Get Ether Balance for a Single Address

            1: commands.accountCommand1(ethaddress),
            # Get Ether Balance for Multiple Addresses in a Single Call

            2: commands.accountCommand2(ethaddress),
            # Get a list of'Normal' Transactions By Address

            3: commands.accountCommand3(ethaddress),
            # get a list of 'internal transactions by address'

            4: commands.accountCommand4(txhash),
            # Get 'Internal Transactions' by Transaction Hash

            5: commands.accountCommand5(),  # get "internal transactions" by block range

            6: commands.accountCommand6(ethaddress, contractaddress),
            # Get a list of 'ERC20 - Token Transfer Events' by Address

            7: commands.accountCommand7(ethaddress, contractaddress),
            # Get a list of 'ERC721 - Token Transfer Events' by Address

            8: commands.accountCommand8(ethaddress)  # Get list of Blocks Mined by Address
        }
        return accountCommandsList.get(command_choice-1)
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
        passthrough = logCommandsList.get(command_choice - 1)
    elif module_choice == 6:
        conversion_dict = {
            0: "GetMostRecentBlock",
            1: "GetBlockByNumber",
            2: "GetUncleByBlockAndIndex",
            3: "GetBlockTransactionCountByNumber",
            4: "GetTransactionByHash",
            5: "GetTransactionByBlockNumberAndIndex",
            6: "GetTransactionCount",
            7: "GetRawTransaction",
            8: "getTransactionReceipt",
            9: "getCall",
            10: "getCall",
            11: "GetCode",
            12: "GetStorageAt",
            13: "getGasPrice",
            14: "getEstimatedGas",
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
        tag = getTag()
        proxyCommandsList = {
            0: commands.proxyCommand0(),
            1: commands.proxyCommand1(tag),
            2: commands.proxyCommand2(tag),
            3: commands.proxyCommand3(tag)#,
 #          4: commands.proxyCommand4(),
  #          5: commands.proxyCommand5(),
   #         6: commands.proxyCommand6(),
    #        7: commands.proxyCommand7(),
     #       8: commands.proxyCommand8(),
      #      9: commands.proxyCommand9(),
       #     10: commands.proxyCommand10(),
        #    11: commands.proxyCommand11(),
         #  13: commands.proxyCommand13(),
          #  14: commands.proxyCommand14()
        }
        passthrough = proxyCommandsList.get(command_choice - 1)
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









