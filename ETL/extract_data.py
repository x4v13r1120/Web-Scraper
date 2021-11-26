import json
from requests import get


def extract(x):
    # make request using command from user input
    response = get(x)
    address_content = response.json()
    result = address_content.get("result")
    # dump data
    with open("data/jsondata.json", "w") as outfile:
        json.dump(result, outfile)
        print("Extraction Complete.")
