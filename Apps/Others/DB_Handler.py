'''
DB_Handler handel the BD operations
'''

# Import requeriments:
from os import getcwd,listdir
import json

class DB_Handler:
    current_dir = getcwd()
    db_file_name = 'DB_app.json'

    @staticmethod
    def DB_checker()->bool:
        if DB_Handler.db_file_name not in listdir(DB_Handler.current_dir):
            return True
        return False

    @staticmethod
    def DB_creator()->None:
        if DB_Handler.DB_checker():
            print('entro')
            with open(DB_Handler.db_file_name,'w') as file:
                json.dump([],file)

    @staticmethod
    def DB_loader()->list:
        if DB_Handler.DB_checker() == False:
            with open(DB_Handler.db_file_name,'r') as info:
                DB_loaded_list = json.load(info)
                return DB_loaded_list
            
    @staticmethod
    def DB_updater(updated_DB_list:list)->None:
        with open(DB_Handler.db_file_name,'w') as info:
            json.dump(updated_DB_list,info,indent=4)

'''
print(DB_Handler.current_dir)
response = DB_Handler.DB_checker()
print(response)
DB_Handler.DB_creator()

loaded = DB_Handler.DB_loader()
print(loaded)
'''