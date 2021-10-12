import json
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

"""
accountmodule = {
    "balance",
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
    "txreceipt_status",
    "input",
    "contractAddress",
    "cumulativeGasUsed",
    "gasUsed",
    "confirmations",
    "type",
    "gasUsed",
    "traceId",
    "isError",
    "errCode",
    "tokenName",
    "tokenSymbol",
    "tokenDecimal",
    "transactionIndex",
    "tokenID"
}
"""


n = {}

def load():
    conn = sqlite3.connect('data/ethdata')
    c = conn.cursor()
    with open("data/cleaned_data.json") as infile:
        print("paulllllll is sus!!!!!!")

def insertmodChoicecomChoice(module_choice, command_choice):
    conn = sqlite3.connect('data/ethdata')
    c = conn.cursor()
    c.execute("INSERT INTO moduleCommand(module_choice, command_choice) VALUES ('module_choice', 'command_choice')")




