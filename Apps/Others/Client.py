'''
Class Client defines client info and actions could a client do
'''

# Imports
from DB_Handler import DB_Handler as DB

# Class definition
class Client:
    ''''''
    ID = 0
    client_list = []

    def __init__(self,name,password,client_ID=0,carts_list=[]) -> None:
        self.client_ID = Client.ID
        self.name = name
        self.password = password
        self.carts_list = carts_list
        Client.ID += 1
        Client.client_list.append(self.__dict__)

    # Registar cliente
    @staticmethod
    def client_register():
        name = input('Nombre: ')
        password = input('Password: ')
        Client(name=name,password=password)
        print(f'{name} fue registrado exitosamente')

    # Guardar los clientes en el Json
    @staticmethod
    def client_writer():
        DB.DB_updater(Client.client_list)

    # Cargar clientes
    def client_loader():
        DB_loaded_list = DB.DB_loader()
        for client in DB_loaded_list:
            Client(**client)
        return Client.client_list

    # Login estatus
    @staticmethod
    def client_login_status(name,password)->bool:
        for client in Client.client_list:
            if client['name'] == name and client['password'] == password:
                return True
            return False
        
    # Mostrar listado de clientes
    @staticmethod
    def display_client_list():
        for client in Client.client_list:
            print(f"{client['client_ID']} {client['name']}")

'''
Client.client_register()
print(Client.client_list)
print(Client.client_login_status('Einer','1234'))
Client.client_loader()

DB.DB_creator()
Client.client_register()
Client.client_register()
print(Client.client_list)
Client.client_writer()

loaded_list = Client.client_loader()
print(loaded_list)

loaded_list = Client.client_loader()
print(loaded_list)
Client.display_client_list()
'''