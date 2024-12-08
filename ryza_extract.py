import pandas as pd
import json

sorted_names = """Explosive Uni
Ice Caltrop
Craft
Bomb
Ice Bomb
Plajig
Luft
Norden Brand
Lightning Bell
Bubble Bullet
Rose Bomb
Kleid Ice Bomb
Strahl Plajig
Ratsel Luft
Fire Bottle
Genesis Hammer
Vanish Siegel
Lunar Lamp
Eternal Fear
Philosopher's Book
Grass Beans
Dry Biscuit
Blessing Ointment
Puni Jelly
Rasen Pudding
Trickling Breeze
Restoration Bottle
Nectar
Healing Ball
Dynamic Syrup
Cocktail Leb
Goddess Cup
Elixir
Fish Oil
War Powder
Thorny Embrace
Energianica
Sundry Remedy
Poison Smoke
Mystic Robe
Miracle Ebonyal
Heroic Geist
Astronomical Clock
Reaper's Scythe
Woodcutter's Axe
Hammer
Bomb Rod
Fishing Rod
Bug Net
Compass
Wind Shoes
Knapsack
Mirage Loupe
Scythe Axe
Bomb Hammer
Fishing Rod Net
Loupe Compass
Exploration Set
Red Supplement
Blue Supplement
Yellow Supplement
Green Supplement
Polish Powder
Zettel
Delicious Bait
Alchemy Paint
Delphi Rose Incense
Ingot
Bronze Eisen
Staltium
Criminea
Goldoterion
Cloth
Natural Cloth
Beastial Air
Sorcery Rose
Eldrocode
Pearl Crystal
Amberlite
Spirinite
Saint's Diamond
Arc en Ciel
Honey
Eltz Sugar
Traveler's Water Orb
Super Pure Water
Healing Chip
Holy Drop
Poison Cube
Taboo Drop
Lightning Sand
Marblestone
Gunpowder Base
Blue Flame Ember
Mixing Oil
Meltstone
Flour
Gelatin Powder
Alchemy Fibers
Heaven's String
Composite Plate
Holy Nut
Mist Liquid
Feather Draft
Puni Leather
Master Leather
Glass Flower
Spirit Bottle
Crystal Element
Philosopher's Stone
Plant Seed
Stone Seed
Fire Seed
Water Seed
Mystic Seed""".split('\n')

if __name__ == '__main__':
    df = pd.read_excel('xlsxs/ryza.xlsx', sheet_name='Item Recipe Data')
    items = {n: {} for n in sorted_names}
    item = {'name': ''}
    for i, row in df.iterrows():
        if not isinstance(row['Item'], str):
            continue
        if row['Item'] != item['name']:
            if i > 0:
                items[item['name']] = item
            item = {'name': row['Item'], 'ingredients': [], 'categories': []}
        item['ingredients'].append(row['Ingredient'])


    df = pd.read_excel('xlsxs/ryza.xlsx', sheet_name='Items')
    for i, row in df.iterrows():
        if not isinstance(row['Name'], str):
            continue
        if row['Name'] not in items:
            items[row['Name']] = {'name': row['Name']}
        cats = []
        for j in range(4):
            if isinstance(row[f'Cat {j+1}'], str):
                cats.append(row[f'Cat {j+1}'])
        items[row['Name']]['categories'] = cats
        items[row['Name']]['cost'] = 1.1 - row['LV'] * 0.002

    src1 = 'Uni'
    dst = 'Prosthetic Arm'
    json.dump(items, open('jsons/ryza.json', 'w'))
    print()
