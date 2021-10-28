import json
import sqlite3

conn = sqlite3.connect('data/ethData')
c = conn.cursor()


def load():
    ethData = {}
    with open("data/cleaned_data.json") as infile:
        ethData = json.load(infile)

        sql = "INSERT INTO test(blockNumber,timeStamp,hash,nonce,blockHash," \
              "transactionIndex,fromAddress,toAddress,value,gas,gasPrice,isError," \
              "txreceipt_status,input,contractAddress,cumulativeGasUsed,gasUsed)" \
              "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    for value in ethData:
        c.execute(sql,)

        conn.commit()
        conn.close()
        print("paulllllll is sus!!!!!!")
