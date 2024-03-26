import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce
import socket
import os
import time

def addData(self):

        load_dotenv()
        ## connecting to supabase
        url: str = os.environ.get("REACT_APP_SUPABASE_URL")
        key: str = os.environ.get("REACT_APP_ANON_KEY")
        supabase: Client = create_client(url, key)

        ## adding id and name to supabase table 
        id = self.id.pop()
        name = self.codename.pop()
        print('id = ', id, ' name = ', name)
        fk_list = add_entries_to_vendor_table(supabase, id, name)

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