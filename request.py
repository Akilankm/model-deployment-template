import argparse
import requests
import pandas as pd
from urls import list_urls

parser = argparse.ArgumentParser()
parser.add_argument("-d","--data",type=list,default=None)
args = parser.parse_args()
    

if __name__=="__main__":
    r = requests.post(url=list_urls["predict"],json=args.data)
    print(r.json())