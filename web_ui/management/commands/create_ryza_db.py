from web_ui.models import Ryza1
from django.utils import timezone
import json


class Command:
    def run_from_argv(self, *args, **kwargs):
        pass


data = json.load(open('jsons/ryza.json'))

categories = {}
item2idx = {}
for name, item in data.items():
    item2idx[name] = len(item2idx)
    for cat in item['categories']:
        if cat.startswith('('):
            if cat not in categories:
                categories[cat] = {'items': []}
            categories[cat]['items'].append(name)

edges = []
names = []
for name, item in data.items():
    names.append(name)
    if 'ingredients' in item:
        for ing in item['ingredients']:
            if ing.startswith('('):
                for cat in categories[ing]['items']:
                    edges.append((item2idx[cat], item2idx[name]))
            else:
                edges.append((item2idx[ing], item2idx[name]))


for i, (name, item) in enumerate(data.items()):
    a = Ryza1(
        name=name,
        categories=item['categories'][0]
    )
    a.save()

for edge in edges:
    node1 = Ryza1.nodes.get(
        name=names[edge[0]]
    )
    node2 = Ryza1.nodes.get(
        name=names[edge[1]]
    )
    rel = node1.ingredients.connect(node2)
    rel.save()

# a = Material(
#     name='Uni'
# )
# a.save()
a = Ryza1.nodes.all()
now = timezone.now()
print(a)
