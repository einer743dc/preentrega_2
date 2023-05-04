'''
Creates diferent menus
'''

class Menu:

    ...

    def welcome_menu(self):
        print(f'BIEN VENIDO')
        print(f"1 --> Login\n2 --> Registrarse")
        welcome_response = input('>>')
        return int(welcome_response)
    

    def login_menu(self):
        print(f'LOGIN')
        name = input('Nombre: ')
        password = input('Password: ')
        return name,password
    
    
    def after_login_menu(self):
        print(f'QUE QUERES HACER?')
        options = {1 : 'Ver listado de clientes', 2 : 'Crear un cliente', 3 : 'Registrar una compra', 4 : 'Ver historia de compras', 5 : 'Salir'}
        for k,v in options.items():
            print(f"{k} --> {v}")
        response = input('>>')
        return response


'''
menu = Menu()
response = menu.after_login_menu()
print(response)
'''