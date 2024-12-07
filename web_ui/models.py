from django.db import models
from neomodel import StructuredNode, StringProperty, ArrayProperty, RelationshipTo, StructuredRel

class Item(StructuredNode):
    name = StringProperty(unique_index=True)
    categories = ArrayProperty()
    ingredients = RelationshipTo('Material', 'INGREDIENT')


class Material(StructuredNode):
    name = StringProperty(unique_index=True)
    categories = ArrayProperty()
    ingredients = RelationshipTo('Material', 'INGREDIENT')

class Ingredients(StructuredRel):
    meeting_id = StringProperty(unique_index=True)


class Ryza1(StructuredNode):
    name = StringProperty(unique_index=True)
    ingredients = RelationshipTo('Ryza1', 'INGREDIENT', model=Ingredients)
    categories = StringProperty()
