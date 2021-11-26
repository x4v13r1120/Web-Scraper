import input
from ETL.extract_data import extract
from ETL.transform_data import transform
from ETL.load_data import load
from input import userInput

if __name__ == '__main__':
    extract(userInput())
    transform()
    load(input.command_choice)














