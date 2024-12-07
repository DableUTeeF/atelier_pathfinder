import pandas as pd
import json

if __name__ == '__main__':
    df = pd.read_excel('xlsxs/ryza.xlsx', sheet_name='Item Recipe Data')
    items = {}
    item = {'name': ''}
    for i, row in df.iterrows():
        if row['Item'] != item['name']:
            if i > 0:
                items[item['name']] = item
            item = {'name': row['Item'], 'ingredients': [], 'categories': []}
        item['ingredients'].append(row['Ingredient'])


    df = pd.read_excel('xlsxs/ryza.xlsx', sheet_name='Items')
    for i, row in df.iterrows():
        if row['Name'] not in items:
            items[row['Name']] = {'name': row['Name']}
        cats = []
        for j in range(4):
            if isinstance(row[f'Cat {j+1}'], str):
                cats.append(row[f'Cat {j+1}'])
        items[row['Name']]['categories'] = cats

    src1 = 'Uni'
    dst = 'Prosthetic Arm'
    json.dump(items, open('jsons/ryza.json', 'w'))
    print()
