import json

def json_parser(result):
#    for transaction in result:
#        print(transaction)
    with open("data/jsondata.json", "w") as outfile:
        json.dump(result, outfile)