#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

class plant:
    def __init__(self,
                 name,
                 latin_name,
                 plant_type,
                 flowers,
                 colour,
                 surface,
                 height,
                 smell,
                 leaf_structure,
                 leaf_margins,
                 leaf_venation,
                 leaf_stem,
                 is_invasive,
                 is_eu_invasive):
        self.name = name
        self.latin_name = latin_name
        self.plant_type = plant_type
        self.flowers = flowers
        self.colour = colour
        self.height = height
        self.smell = smell
        self.leaf_structure = leaf_structure
        self.leaf_structure = leaf_margins
        self.leaf_venation = leaf_venation
        self.leaf_stem = leaf_stem
        self.is_invasive = is_invasive
        self.is_eu_invasive = is_eu_invasive


#oak = plant('oak', 'oak but in a latin', 'tree', 'no','no', 'no', 'smooth', 'tall', 'whole', 'oblate','palmated', 'single', False, False)




