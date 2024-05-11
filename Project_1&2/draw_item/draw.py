import json
from draw_item.draw_item import *

with open("data.json") as f:
    data = json.load(f)

def draw_item (name_list,item):
    for data_item in data[name_list]:
        for sub_item in item:
            if (sub_item == data_item['name'] & data_item['apple']):
                draw_apple(sub_item)
            if (sub_item == data_item['name'] & data_item['banana']):
                draw_banana(sub_item)
            if (sub_item == data_item['name'] & data_item['orange']):
                draw_orange(sub_item)