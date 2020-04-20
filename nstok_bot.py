import requests
import argparse
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--link', type=str)
parser.add_argument('-k', '--keyword', type=str)
parser.add_argument('-t', '--delay', default=60,type=int)

args = parser.parse_args()


if __name__ == "__main__":
    url = args.link
    keyword = args.keyword
    t = args.delay
    
    while True:
        r = requests.get(url)
        s = keyword in r.text
        print(s)
        sleep(t)