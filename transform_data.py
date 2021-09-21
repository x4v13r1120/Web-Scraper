import json
import pandas as pd

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

with open("cleaned_data.json") as infile:
    txlist = json.load(infile)




