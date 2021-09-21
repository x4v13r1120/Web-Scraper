import json

txlist = {
    "blockNumber",
    "timeStamp",
    "hash",
    "nonce",
    "blockHash",
    "transactionsIndex",
    "from",
    "to",
    "value",
    "gas",
    "gasPrice",
    "isError",
    "txreceipt_status",
    "input",
    "contractAddress",
    "cumulativeGasUsed",
    "gasUsed",
    "confirmations"
}

def transform():
    with open("cleaned_data.json") as infile:
        txlist = json.load(infile)
        print(txlist)





