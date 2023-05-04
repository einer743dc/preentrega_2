'''
Class Item creates items that can be added to a shoping cart

'''
from os import getcwd
import json

class Item:
    ID = 0
    item_list:list = []

    def __init__(self,item_id,name:str,item_price:float,available=True)-> None:
        self.item_id = Item.ID
        self.name:str = name
        self.item_price:float = item_price
        self.available:bool = available
        Item.item_list.append(self.__dict__)
        Item.ID += 1

    def __repr__(self) -> str:
        return f'"ID":{self.item_id} "name":{self.name} "price":{self.item_price} "available":{self.available}'

    def create_product(self):
        ...

    @staticmethod
    def write_products():
        with open('Item_list.json','w') as product_info:
            json.dump(Item.item_list,product_info,indent=4)

    @staticmethod
    def load_item_list():
        with open('Item_list.json','r') as items:
            loaded_item_list:list = json.load(items)
            for item in loaded_item_list:
                Item(**item)
            return Item.item_list
            #return loaded_item_list
            # list_info_items = [Item(x) for x in loaded_item_list]


'''
PROBANDO:

pera= Item('pera',500)
naranja = Item('naranja',300)

print(pera.__dict__)
print(naranja.__dict__)
print(Item.item_list)
print(type(Item.item_list[0]))

print(Item.item_list)
print(Item.item_list[0])
Item.write_products()

print(type(Item.load_item_list()[0]))
x = Item(**Item.load_item_list()[0])
print(x)

loaded_items = Item.load_item_list()
print(loaded_items)
'''