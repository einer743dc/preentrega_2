'''
Class Cart creates a shoping cart where a client could registre product items
'''
# imports
from Item import Item
from datetime import date

class Cart:
    cart_item_list = []
    loaed_items = Item.load_item_list()
    
    def __init__(self) -> None:
        self.time = date.today()
        self.cart_item_list:list = Cart.cart_item_list
        self.total = 0

    def add_item(self):
        while True:
            print('AGREGAR PRODUCTOS AL CARRITO')
            for item in Cart.loaed_items:
                print(f"{item['item_id']} --> {item['name']} : {item['item_price']}")
            print(f"9 --> Terminar compra")
            response = int(input('>>>'))
            if response == 0:
                self.cart_item_list.append(Cart.loaed_items[0])
            elif response == 1:
                self.cart_item_list.append(Cart.loaed_items[1])
            elif response == 2:
                self.cart_item_list.append(Cart.loaed_items[2])
            elif response == 3:
                self.cart_item_list.append(Cart.loaed_items[3])
            elif response == 9:
                self.view_cart()
                return self.cart_item_list
            else:
                print('Elige una opcion valida')
      

    def view_cart(self):
        print('CARRITO DE COMPRAS')
        print(f'Fecha : {self.time}')
        for item in self.cart_item_list:
            print(f" {item['name']} --> {item['item_price']}")
            self.total += item['item_price']
        print(f"TOTAL PAGADO --> {self.total}")
        

'''
cart = Cart()
print(Cart.loaed_items)
#print(cart.__dict__)

compra = cart.add_item()

#cart.view_cart()
#print(cart.__dict__)
print(compra)
'''