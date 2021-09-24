import json
import requests
from commands import commands

module_choice = int(input(f"What module do u wish to utilize:\n1.{commands.module[0]}\n2.{commands.module[1]}\n"
                      f"3.{commands.module[2]}\n4.{commands.module[3]}\n5.{commands.module[4]}\n"
                      f"6.{commands.module[5]}\n7.{commands.module[6]}\n8.{commands.module[7]}\n"
                      f"9.{commands.module[8]}\n"))

accountCommandsList = {
    "etherBalanceSingle": commands.accountCommand0(),  # Get Ether Balance for a Single Address

    "etherBalanceMultiple": commands.accountCommand1(),  # Get Ether Balance for Multiple Addresses in a Single Call

    "listNormalTransactions": commands.accountCommand2(),  # Get a list of'Normal' Transactions By Address

    "listInternalTransactions": commands.accountCommand3(),  # get a list of 'internal transactions by address'

    "txhashInternalTransactions": commands.accountCommand4(),
    # Get 'Internal Transactions' by Transaction Hash

    "blockRangeInternalTx": commands.accountCommand5(),  # get "internal transactions" by block range

    "listErc20Transfer": commands.accountCommand6(), # Get a list of 'ERC20 - Token Transfer Events' by Address

    "listErc721Transfer": commands.accountCommand7(), # Get a list of 'ERC721 - Token Transfer Events' by Address

    "listBlocksMined": commands.accountCommand8(), # Get list of Blocks Mined by Address

}
contractCommandsList = {
    "getAbiContract": commands.contractCommand0(), # Get Contract ABI for Verified Contract Source Code

    "getContractSource": commands.contractCommand1() # Get Contract Source Code for Verified
    # Contract Source Codes
}
transactionCommandsList = {
    "checkContractStatus": commands.transactionCommand0(), #Check Contract Execution Status
    "checkTransactionStatus":commands.transactionCommand1() # Check Transaction Receipt Status
}
blockCommandsList = {
    "getBlockRewards": commands.blockCommand0(), # Get Block And Uncle Rewards by BlockNo
    "getBlockCountdown": commands.blockCommand1(), # Get Estimated Block Countdown Time by BlockNo
    "getBlockNumber": commands.blockCommand2() # Get Block Number by Timestamp
}

module_command_list = [
    accountCommandsList,
    contractCommandsList,
    transactionCommandsList,
    blockCommandsList
]

passthrough = ""

if module_choice == 1:
    command_choice = int(input(f"which command you like to use:\n1.{list(accountCommandsList.keys())[0]}\n"
          f"2.{list(accountCommandsList.keys())[1]}\n3.{list(accountCommandsList.keys())[2]}\n"
          f"4.{list(accountCommandsList.keys())[3]}\n5.{list(accountCommandsList.keys())[4]}\n"
          f"6.{list(accountCommandsList.keys())[5]}\n7.{list(accountCommandsList.keys())[6]}\n"
          f"8.{list(accountCommandsList.keys())[7]}\n"))
    coversion_dict = {
        0:"etherBalanceSingle",
        1:"etherBalanceMultiple",
        2:"listNormalTransactions",
        3:"listInternalTransactions",
        4:"txhashInternalTransactions",
        5:"blockRangeInternalTx",
        6:"listErc20Transfer",
        7:"listErc721Transfer",
        8:"listBlocksMined"
    }
    passthrough = module_command_list[module_choice-1][coversion_dict[command_choice-1]]
elif module_choice == 2:
    command_choice = int(input(f"which command you like to use:\n1.{list(contractCommandsList.keys())[0]}\n"
                               f"2.{list(contractCommandsList.keys())[1]}\n"))
    coversion_dict = {
        0: "getAbiContract",
        1: "getContractSource",
    }
    passthrough = module_command_list[module_choice - 1][coversion_dict[command_choice - 1]]
elif module_choice == 3:
    command_choice = int(input(f"which command you like to use:\n1.{list(transactionCommandsList.keys())[0]}\n"
                               f"2.{list(transactionCommandsList.keys())[1]}\n"))
    coversion_dict = {
        0: "checkContractStatus",
        1: "checkTransactionStatus",
    }
    passthrough = module_command_list[module_choice - 1][coversion_dict[command_choice - 1]]
elif module_choice == 4:
    command_choice = int(input(
        f"which command you like to use:\n1."
        f"{list(blockCommandsList.keys())[0]}\n"
        f"2.{list(blockCommandsList.keys())[1]}\n"
        f"3.{list(blockCommandsList.keys())[2]}"))
    coversion_dict = {
        0: "getBlockRewards",
        1: "getBlockCountdown",
        2: "getBlockNumber"
    }
    passthrough = module_command_list[module_choice - 1][
        coversion_dict[command_choice - 1]]

def extract():
    # make request using command
    response = requests.get(passthrough)
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
                        print("Data Extracted & Cleaned!!! Ready for transformation!!!")


