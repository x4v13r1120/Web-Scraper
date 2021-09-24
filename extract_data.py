import json
import requests
from commands import commands, getEthAdress, getContractAdress, getTxHash, getBlockNo, getTimeStamp

accountCommandsList = {
    "etherBalanceSingle": commands.accountCommand0(getEthAdress()),  # Get Ether Balance for a Single Address

    "etherBalanceMultiple": commands.accountCommand1(getEthAdress()),  # Get Ether Balance for Multiple Addresses in a Single Call

    "listNormalTransactions": commands.accountCommand2(getEthAdress()),  # Get a list of'Normal' Transactions By Address

    "listInternalTransactions": commands.accountCommand3(getEthAdress()),  # get a list of 'internal transactions by address'

    "txhashInternalTransactions": commands.accountCommand4(getEthAdress()), # Get 'Internal Transactions' by Transaction Hash

    "blockRangeInternalTx": commands.accountCommand5(),  # get "internal transactions" by block range

    "listErc20Transfer": commands.accountCommand6(getEthAdress(),getContractAdress()), # Get a list of 'ERC20 - Token Transfer Events' by Address

    "listErc721Transfer": commands.accountCommand7(getEthAdress(),getContractAdress()), # Get a list of 'ERC721 - Token Transfer Events' by Address

    "listBlocksMined": commands.accountCommand8(getEthAdress()), # Get list of Blocks Mined by Address

}
contractCommandsList = {
    "getAbiContract": commands.contractCommand0(commands.getEthAdress()), # Get Contract ABI for Verified Contract Source Code

    "getContractSource": commands.contractCommand1(commands.getEthAdress()) # Get Contract Source Code for Verified
    # Contract Source Codes
}
transactionCommandsList = {
    "checkContractStatus": commands.transactionCommand0(commands.getTxHash()), #Check Contract Execution Status
    "checkTransactionStatus":commands.transactionCommand1(commands.getTxHash()) # Check Transaction Receipt Status
}

module_command_list = [
    accountCommandsList,
    contractCommandsList,
    transactionCommandsList
]

def userinput():
    passthrough = ""

    module_choice = int(input(f"What module do u wish to utilize:\n1.{commands.module[0]}\n2.{commands.module[1]}\n"
                              f"3.{commands.module[2]}\n4.{commands.module[3]}\n5.{commands.module[4]}\n"
                              f"6.{commands.module[5]}\n7.{commands.module[6]}\n8.{commands.module[7]}\n"
                              f"9.{commands.module[8]}\n"))

    if commands.module_choice == 1:
        command_choice = int(
            input(f"which command you like to use:\n1.{list(commands.accountCommandsList.keys())[0]}\n"
                  f"2.{list(commands.accountCommandsList.keys())[1]}\n3.{list(commands.accountCommandsList.keys())[2]}\n"
                  f"4.{list(commands.accountCommandsList.keys())[3]}\n5.{list(commands.accountCommandsList.keys())[4]}\n"
                  f"6.{list(commands.accountCommandsList.keys())[5]}\n7.{list(commands.accountCommandsList.keys())[6]}\n"
                  f"8.{list(commands.accountCommandsList.keys())[7]}\n9.{list(commands.accountCommandsList.keys())[8]}\n"))
        coversion_dict = {
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
        passthrough = commands.module_command_list[commands.module_choice - 1][coversion_dict[command_choice - 1]]
    elif commands.module_choice == 2:
        command_choice = int(
            input(f"which command you like to use:\n1.{list(commands.contractCommandsList.keys())[0]}\n"
                  f"2.{list(commands.contractCommandsList.keys())[1]}\n"))
        coversion_dict = {
            0: "getAbiContract",
            1: "getContractSource",
        }
        passthrough = commands.module_command_list[commands.module_choice - 1][coversion_dict[command_choice - 1]]
    elif commands.module_choice == 3:
        command_choice = int(
            input(f"which command you like to use:\n1.{list(commands.transactionCommandsList.keys())[0]}\n"
                  f"2.{list(commands.transactionCommandsList.keys())[1]}\n"))
        coversion_dict = {
            0: "checkContractStatus",
            1: "checkTransactionStatus",
        }
        passthrough = commands.module_command_list[commands.module_choice - 1][coversion_dict[command_choice - 1]]

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









