import json
import requests
from commands import commands, getEthAdress, getContractAdress, getTxHash, getBlockNo, getTimeStamp

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
        accountCommandsList = {
            0: commands.accountCommand0(getEthAdress()),  # Get Ether Balance for a Single Address

            1: commands.accountCommand1(getEthAdress()),
            # Get Ether Balance for Multiple Addresses in a Single Call

            2: commands.accountCommand2(getEthAdress()),
            # Get a list of'Normal' Transactions By Address

            3: commands.accountCommand3(getEthAdress()),
            # get a list of 'internal transactions by address'

            4: commands.accountCommand4(getEthAdress()),
            # Get 'Internal Transactions' by Transaction Hash

            5: commands.accountCommand5(),  # get "internal transactions" by block range

            6: commands.accountCommand6(getEthAdress(), getContractAdress()),
            # Get a list of 'ERC20 - Token Transfer Events' by Address

            7: commands.accountCommand7(getEthAdress(), getContractAdress()),
            # Get a list of 'ERC721 - Token Transfer Events' by Address

            8: commands.accountCommand8(getEthAdress())  # Get list of Blocks Mined by Address
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
        contractCommandsList = {
            0: commands.contractCommand0(commands.getEthAdress()),
            # Get Contract ABI for Verified Contract Source Code

            1: commands.contractCommand1(commands.getEthAdress())  # Get Contract Source Code for Verified
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
        transactionCommandsList = {
            0: commands.transactionCommand0(commands.getTxHash()),
            # Check Contract Execution Status
            1: commands.transactionCommand1(commands.getTxHash())
            # Check Transaction Receipt Status
        }
        passthrough = transactionCommandsList.get(command_choice-1)

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









