import json
import requests
from commands import command


action = str(input("Please enter action you'd like to perform."))  # balance, balancemulti, txlist, txlistinternal,
# tokentx, tokennfttx, getminedblocks, balancehistory,
address = str(input("Please enter Ether Address."))  # 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
tag = str(input("Please enter tag."))  # latest

commandList = {
    0: command.command0(command.api_key, command.module[0], command.website,
                        action, address, tag),  # Get Ether
    # Balance for a Single Address

    1: command.command1(command.api_key, command.module[0], command.website,
                        action, address, tag),  # Get Ether
    # Balance for Multiple Addresses in a Single Call

    2: command.command2(command.api_key, command.website, command.module[0],
                        action, address),  # Get a list of
    # 'Normal' Transactions By Address

    3: command.command3(command.api_key, command.website, command.module[0],
                        action, address), # get a list of 'internal transactions by address'

    4: command.command4(command.api_key, command.website, command.module[0],action,
                        txhash= 0x40eb908387324f2b575b4879cd9d7188f69c8fc9d87c901b9e2daaea4b442170),
    # Get 'Internal Transactions' by Transaction Hash

    5:  command.command5(command.api_key, command.website, command.module[0], action), # get
    # "internal transactions" by block range

}


def extract():
    # make request using command
    response = requests.get(commandList[2])
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
