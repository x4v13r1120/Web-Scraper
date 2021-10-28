import json
import sqlite3

conn = sqlite3.connect('data/ethData')
c = conn.cursor()


def load():
    rawdata = {}
    with open("data/cleaned_data.json") as infile:
        rawdata = json.load(infile)

        sql = "INSERT INTO test(blockNumber,timeStamp,hash,nonce,blockHash," \
              "transactionIndex,fromAddress,toAddress,value,gas,gasPrice,isError," \
              "txreceipt_status,input,contractAddress,cumulativeGasUsed,gasUsed,confirmations)" \
              "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    for keys in rawdata:
        ethdata = []
        for value in keys.values():
            ethdata.append(value)
        c.execute(sql, ethdata)
    conn.commit()
    conn.close()
    print("Data successfully loaded into database!!!")

