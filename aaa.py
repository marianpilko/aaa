# Abbreviations And Acronyms

import argparse
import json
from pathlib import Path
import requests

def get_json():
    url = 'https://raw.githubusercontent.com/marianpilko/aaa/main/aaa.json'
    r = requests.get(url)
    with open('aaa.json', 'w') as f:
        f.write(r.text)

def main():
    argparser = argparse.ArgumentParser(
        description='Abbreviations and Acronyms'
    )
    argparser.add_argument( # Positional argument [abbreviation or acronym]
        'a',
        help='abbreviation or acronym'
        )
    argparser.add_argument(
        '-j', '--json',
        action='store_true',
        dest='get_json',
        help='get current version of aaa.json'
    )
    args = argparser.parse_args()

    path = Path('aaa.json')
    if (not path.exists() or args.get_json):
        get_json()
    
    with open('aaa.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if 'abbreviation' in item:
                if item['abbreviation'] == args.a:
                    print(item['meaning'])
            if 'acronym' in item:
                if item['acronym'] == args.a:
                    print(item['meaning'])
                    if 'description' in item:
                        print(item['description'])

if __name__ == '__main__':
    main()