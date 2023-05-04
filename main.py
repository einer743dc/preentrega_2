'''
Que deberia hacer la app?
Deberia registrar clientes y permitir guardar "carritos de compra" despues de agregarle a estos items y guardar este carrito en la base de datos.

NOTA: 
Desarrolle las clases, todas funcionan bien y cumplen su proposito cuando se les ejecuta por separado, pero hay un problema cuando las importo al main...

bug:
Traceback (most recent call last):
  File "/Users/mavors/Library/Mobile Documents/com~apple~CloudDocs/CoderHouse/Preentrega_2/main.py", line 18, in <module>
    from Apps.Others.Client import Client
  File "/Users/mavors/Library/Mobile Documents/com~apple~CloudDocs/CoderHouse/Preentrega_2/Apps/Others/Client.py", line 6, in <module>
    from DB_Handler import DB_Handler as DB
ModuleNotFoundError: No module named 'DB_Handler'

Esto pasa con los modulos que requieren de la importacion de otros para funcionar, por ejempo ahi al importart la clase "Client" que a su vez importa en su 
estructura el modulo DB_Handler, pero si vas y ejecutas el archivo Client.py funciona normal

Una solucion es reescribir en cada modulo las funciones que se llaman de otros... pero pues creo que esa no es la idea de los modulos...

Esta consulta la tengo para el afterclass del vienes, yo ya comente a Esteban que no podria entregarlo, pero agradezco si me puedes decir como debo hacer 
la importacion para poder escribir el main..

MUCHAS GRACIAS!

'''

# Imports
from Apps.Others.DB_Handler import DB_Handler as DB
from Apps.Others.Client import Client
from Apps.Others.Cart import Cart
from Apps.Others.Item import Item
from Apps.Viewer.Menu import Menu
