import json
import requests
from commands import command

action = str(input("Please enter action you'd like to perform."))  # balance, balancemulti, txlist, txlistinternal,
# tokentx, tokennfttx, getminedblocks, balancehistory,
address = str(input("Please enter Ether Address.")) # 0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
tag = str(input("Please enter tag."))  # latest

commandList = {
    0: command.command0(command.api_key, command.module[0], command.website,
                        action, address, tag),  # Get Ether
    # Balance for a Single Address

    1: command.command1(command.api_key, command.module[0], command.website,
                        action, address, tag),  # Get Ether
    # Balance for Multiple Addresses in a Single Call

    2: command.command2(command.api_key,command.website,command.module[0],
                        action, address, startBlock = 0, endBlock = 99999999,
                        page = 1, offset = 10,sort = "asc") # Get a list of
    # 'Normal' Transactions By Address


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
                        outfile.write(f"{line}")
