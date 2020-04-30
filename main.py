import json
import pandas as pd

txt_file = './carver.txt'

def main(txt_file):
    with open(txt_file) as file:
        crafts = [line.rstrip('\n').lower() for line in file]

    ## load json file
    with open ('./dofus.en.json') as json_file:
        data = json.load(json_file)

    ## iterate over each txt, search in json
    for craft in crafts:
        data[]

if __name__ == "__main__":
    main(txt_file)
