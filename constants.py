
attribute_names = ['name',
                 'latin_name',
                 'is_tree',
                 'is_grass',
                 'is_creeper',
                 'is_swamp_plant',
                 'has_flowers',
                 'has_single_flowers',
                 'has_florets',
                 'flowers_blue',
                 'flowers_red',
                 'flowers_yellow',
                 'flowers_white',
                 'other_colour',
                 'stem_smooth',
                 'stem_rough',
                 'is_creeping',
                 'is_short',
                 'is_medium_tall',
                 'is_tall',
                 'smells_good',
                 'smells_bad',
                 'smells_mildly',
                 'leaves_whole',
                 'leaves_lobed',
                 'leaves_divided',
                 'leaves_dissected',
                 'leaves_margins_entire',
                 'leaves_margins_serrate',
                 'leaves_margins_undulate',
                 'leaves_margins_lobed',
                 'venation_parallel',
                 'venation_palmated',
                 'venation_pinnately_net',
                 'stem_opposite',
                 'stem_alternate',
                 'stem_whorled',
                 'no_stem_arrangement',
                 'is_invasive',
                 'is_eu_invasive',
                 'image_link',
                 'description']
questions_to_index = {i:x for i,x in enumerate(attribute_names[2:-4])}
feature_names = attribute_names[2:-4]
class_to_target = {i+1:name for i,name in enumerate(['oak','maple','birch','jug','ryabina'])}
questions_dict = {"is_tree": 'Is this plant a tree/bush?',
"is_grass": 'Is this plant a grass/herb?',
"is_creeper": 'Is this plant a creeper?',
"is_swamp_plant": 'Is this a swamp or water plant?',
"has_flowers": 'Does this plant have visible blossoms or flowers?',
"has_single_flowers": 'Does it have single flowers?',
"has_florets": 'Does it have floret flowers?',
"flowers_blue": 'Are the flowers blue?',
"flowers_red": 'Are the flowers pink or red?',
"flowers_yellow": 'Are the flowers yellow?',
"flowers_white": 'Are the flowers white?',
"other_colour": 'Are the flowers of a different colour?',
"stem_smooth": 'Is the plant\'s stem smooth?',
"stem_rough": 'Is the plant\'s stem rough?',
"is_creeping": 'Does this plant grows close to land, i.e. horizontally on the surface?',
"is_short": 'Is this plant less than 0.5m tall?',
"is_medium_tall": 'Is this plant 0.5-1m tall?',
"is_tall": 'Is this plant taller than 1m?',
"smells_good": 'Does it have a strong pleasant smell?',
"smells_bad": 'Does it have a strong unpleasant smell?',
"smells_mildly": 'Does it smell mildly?',
"leaves_whole": 'Is the leaf structure whole?',
"leaves_lobed": 'Are the leaves lobed?',
"leaves_divided": 'Are the leaves divided?',
"leaves_dissected": 'Are the leaves dissected?',
"leaves_margins_entire": 'Are leaves\' margins smooth?',
"leaves_margins_serrate": 'Are leaves\' margins serrate?',
"leaves_margins_undulate": 'Are leaves\' margins undulate?',
"leaves_margins_lobed": 'Are leaves\' margins lobed?',
"venation_parallel": 'Do the leaves have parallel venation?',
"venation_palmated": 'Do the leaves have palmated venation?',
"venation_pinnately_net": 'Are the leaves pinnately net-veined?',
"stem_opposite": 'Are the leaf stem arrangements opposite?',
"stem_alternate": 'Are the leaf stem arrangements alternate?',
"stem_whorled": 'Are the leaf stem arrangements whorled?',
"no_stem_arrangement": 'Is this no stem leaf arrangement (just single leaves)?'}

name_dict = {1:'Common milkweed',
             2:'Giant hogweed',
             3:'Floating pennywort',
             4:'Himalayan balsam',
             5:'Water-primrose',
             6:'English oak',
             7:'Sycamore maple',
             8:'European mountain ash',
             9:'Ryegrass',
             10:'Common daisy'}
latin_name_dict = {1:'Asclepias syriaca',
             2:'Heracleum mantegazzianum',
             3:'Hydrocotyle ranunculoides',
             4:'Impatiens glandulifera',
             5:'Ludwigia grandiflora',
             6:'Quercus robur',
             7:'Acer pseudoplatanus',
             8:'Sorbus aucuparia',
             9:'Lolium',
             10:'Bellis perennis'}

