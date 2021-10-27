import json
import requests
import input


def extract():
    # make request using command from user input
    response = requests.get(input.userInput())
    address_content = response.json()
    result = address_content.get("result")
    # dump data
    with open("data/jsondata.json", "w") as outfile:
        json.dump(result, outfile)
        print("Extraction Complete.")
