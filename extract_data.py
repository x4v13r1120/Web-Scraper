import json
import requests
from commands import commands

address = str(input("Please enter Ether Address."))  # 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae

accountCommandsList = {
    "etherBalanceSingle": commands.command0(address),  # Get Ether Balance for a Single Address

    "etherBalanceMultiple": commands.command1(address),  # Get Ether Balance for Multiple Addresses in a Single Call

    "listNormalTransactions": commands.command2(address),  # Get a list of'Normal' Transactions By Address

    "listInternalTransactions": commands.command3(address),  # get a list of 'internal transactions by address'

    "txhashInternalTransactions": commands.command4(txhash = 0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170),
    # Get 'Internal Transactions' by Transaction Hash

    "blockRangeInternalTx": commands.command5(),  # get "internal transactions" by block range

    "listErc20Transfer": commands.command6(address), # Get a list of 'ERC20 - Token Transfer Events' by Address

    "listErc721Transfer": commands.command7(address), # Get a list of 'ERC721 - Token Transfer Events' by Address

    "listBlocksMined": commands.command8(address), # Get list of Blocks Mined by Address

}
# contractCommandsList{ }

# module_choice = input("What module do u wish to utilize:"}

command_choice = input(f"which command from the {module_choice} would you like to use:\n1.{list(accountCommandsList.keys())[0]}\n"
      f"2.{list(accountCommandsList.keys())[1]}\n3.{list(accountCommandsList.keys())[2]}\n"
      f"4.{list(accountCommandsList.keys())[3]}\n5.{list(accountCommandsList.keys())[4]}\n"
      f"6.{list(accountCommandsList.keys())[5]}\n7.{list(accountCommandsList.keys())[6]}\n"
      f"8.{list(accountCommandsList.keys())[7]}\n")


def extract():
    # make request using command
    response = requests.get(accountCommandsList[command_choice - 1])
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
