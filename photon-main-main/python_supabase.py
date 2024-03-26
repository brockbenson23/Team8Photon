import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce
import socket
import os
import time

class Database():
    ## initializing lists
    id = [0]
    codename = [""]

    def getName(self, sv, entry, names, entry2):
            with open("player.sql", "r") as f:
                index = 0
                for line in f:
                    word = f.readline()
                    if f"VALUES ({names.get()}," in word:
                        code = word[10:-2]
                        index += 1
                        entry.setvar(names, code)
                        sv.set(code)
                    else:
                        break
            with open("player.sql", "a") as f:
                nam = sv.get()
                idd = names.get()
                if nam != '':
                    print('nam = ', nam)
                    self.codename.append(nam)
                if idd is not None:
                    if idd == '':
                        idd = -1
                    self.id.append(int(idd))
                f.write(f"\nVALUES ({names.get()}, {sv.get()});")
        
    def addData():
            print("submitting id...")
            load_dotenv()
            ## connecting to supabase
            url: str = os.environ.get("REACT_APP_SUPABASE_URL")
            key: str = os.environ.get("REACT_APP_ANON_KEY")
            supabase: Client = create_client(url, key)

            ## adding id and name to supabase table 
            id = Database.id.pop()
            name = Database.codename.pop()
            print('id = ', id, ' name = ', name)
            fk_list = Database.add_entries_to_vendor_table(supabase, id, name)

    def add_entries_to_vendor_table(supabase, name, codename):
        fake = Faker()
        foreign_key_list = []
        fake.add_provider(faker_commerce.Provider)
        main_list = []
        value = {'id': name, 'codename': codename}
        main_list.append(value)
        data = supabase.table('player').insert(main_list).execute()
        print(data)
        data_dict = data.dict()
        data_entries = data_dict['data']
        for entry in data_entries:
            foreign_key_list.append(int(entry['id']))
        return foreign_key_list


    def add_entries_to_product_table(supabase, vendor_id):
        fake = Faker()
        fake.add_provider(faker_commerce.Provider)
        main_list = []
        iterator = fake.random_int(1, 15)
        for i in range(iterator):
            value = {'id': vendor_id, 'codename': fake.ecommerce_name()}
            main_list.append(value)
        data = supabase.table('Product').insert(main_list).execute()