import json
import requests

# Should make this into some sort of structure so we can have different types of calls we can make
website = "http://api.etherscan.io/api?"
api_key = "F6KD4YVEAVT9P6M2U3TPCGZCXT4PRQG4U9"
address = "0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a"
action = "txlist"
module = "account"
startBlock = 0
endBlock = 99999999
page = 1
offset = 10
sort = "asc"

# Should change these to actual variables and use concatenation to perform tasks

# commandTest1 = "http://api.etherscan.io/api?module=account&action=balance&address" \
#               "=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae&tag=latest&apikey=F6KD4YVEAVT9P6M2U3TPCGZCXT4PRQG4U9 "

# commandTest2 = "http://api.etherscan.io/api?module=account&action=txlist&address" \
#               "=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&startblock=0&endblock=99999999&page=1&offset=10&sort=asc" \
#                "&apikey=F6KD4YVEAVT9P6M2U3TPCGZCXT4PRQG4U9 "

# commandTest3 = website + "module=" + module + "&action=" + action + "&address=" \
# x- broke this           + address + "&startblock=" + startBlock + "&endblock=" + endBlock + \
# one sorry               "&page=" + page + "&offset=" + offset + "&sort=" + sort + "&apikey=" + api_key


# using f string i  made a concatenation of string and ints for modularization
commandTest4 = (f"{website}module={module}&action={action}&address={address}"
                f"&startblock={startBlock}&endblock={endBlock}&page={page}"
                f"&offset={offset}&sort={sort}&apikey={api_key}")


#    for transaction in result:
#        print(transaction)

def extract():
    # make request using command
    response = requests.get(commandTest4)
    address_content = response.json()
    result = address_content.get("result")
    # dump data
    with open("jsondata.json", "w") as outfile:
        json.dump(result, outfile)

    # starting cleaning process
    comment = False
    with open("jsondata.json", 'r') as infile, open("cleaned_data.json", 'w') as \
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
