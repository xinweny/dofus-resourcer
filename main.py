import json
import pandas as pd

txt_file = input('Path to .txt file: ')
category = input("Select a category (weapons/equipments): ")
output_dir = input('Output directory: ')

def main(txt_file, category, output_dir):
    with open(txt_file) as file:
        crafts = [line.rstrip('\n').lower() for line in file]

    ## load json file
    with open ('./dofus.en.json') as json_file:
        data = json.load(json_file)

    ## initialise resource counter
    counter = {}

    ## iterate over each txt, search in json
    for craft in crafts:
        if not any(item['name'].lower() == craft for item in data[category]):
            print(f"'{craft}' not found in {category}.")
        else:
            resources = [item for item in data[category] if item['name'].lower() == craft][0]['craft']

            for resource in resources:
                name = ' '.join(resource['url'].split('-')[1:])
                quantity = int(resource['quantity'])

                if name in counter.keys():
                    counter[name] += quantity
                else:
                    counter[name] = quantity

    counter_df = pd.DataFrame.from_dict(counter, orient='index', columns=['quantity'])
    counter_df.to_csv(f"{output_dir}/resources.csv")

if __name__ == "__main__":
    main(txt_file, category, output_dir)
