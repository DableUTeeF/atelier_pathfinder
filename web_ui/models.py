from django.db import models
from neomodel import StructuredNode, StringProperty, ArrayProperty, RelationshipTo

class Item(StructuredNode):
    name = StringProperty(unique_index=True)
    categories = ArrayProperty()
    ingredients = RelationshipTo('Material', 'INGREDIENT')


class Material(StructuredNode):
    name = StringProperty(unique_index=True)
    categories = ArrayProperty()
    ingredients = RelationshipTo('Material', 'INGREDIENT')
