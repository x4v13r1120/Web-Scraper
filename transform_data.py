import json

txlist = {
    "blockNumber",
    "timeStamp",
    "hash",
    "nonce",
    "blockHash",
    "transactionsIndex",
    "fromAddress",
    "toAddress",
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
wallet = {
    "address",
    "balance"
}
internaltxlist = {
  "blockNumber",
  "timeStamp",
  "hash",
  "fromAddress",
  "toAddress",
  "value",
  "contractAddress",
  "input",
  "type",
  "gas",
  "gasUsed",
  "traceId",
  "isError",
  "errCode"
}

internalhashlist = {
  "blockNumber",
  "timeStamp",
  "fromAddress",
  "toAddress",
  "value",
  "contractAddress",
  "input",
  "type",
  "gas",
  "gasUsed",
  "isError",
  "errCode"
}




def transform():
    with open("data/cleaned_data.json") as infile:
        txlist = json.load(infile)







