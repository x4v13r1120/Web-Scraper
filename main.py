import classes
import input
from extract_data import extract
from transform_data import transform
from load_data import load

if __name__ == '__main__':
    command1 = classes.command()
    module1 = classes.account()

    x = (module1.GetEtherBalanceForSingleAddress())

    extract(x)





