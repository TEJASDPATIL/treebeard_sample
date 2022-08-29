from operator import mod
from django.db import models

# Create your models here.
from treebeard.mp_tree import MP_Node

class Category(MP_Node):
    name = models.CharField(max_length=100)

    node_order_by = ['name']

    def __str__(self):
        return 'Category: {}'.format(self.name)


class TreeB(models.Model):
    name = models.CharField(max_length=50)
    layout = models.JSONField()

    def __str__(self):
        return self.name