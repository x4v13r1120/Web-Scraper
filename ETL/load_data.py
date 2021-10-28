import json
import sqlite3

conn = sqlite3.connect('data/ethData')
c = conn.cursor()


def load():
    ethdata = {}
    with open("data/cleaned_data.json") as infile:
        ethdata = json.load(infile)

        sql = "INSERT INTO test(blockNumber,timeStamp,hash,nonce,blockHash," \
              "transactionIndex,fromAddress,toAddress,value,gas,gasPrice,isError," \
              "txreceipt_status,input,contractAddress,cumulativeGasUsed,gasUsed,confirmations)" \
              "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    for x in ethdata:
        for keys in x:
            print(x.values())



    conn.commit()
    conn.close()

