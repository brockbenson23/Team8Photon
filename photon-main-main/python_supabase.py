import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce
import socket
import os
import time

class Database:
    ## initializing lists
    id = [0]
    codename = [""]

    @staticmethod
    def addData(ids: list[int], codenames):
        print("submitting id...")
        load_dotenv()
        ## connecting to supabase
        url: str = os.environ.get("REACT_APP_SUPABASE_URL")
        key: str = os.environ.get("REACT_APP_ANON_KEY")
        supabase: Client = create_client(url, key)

        ## adding id and name to supabase table
        while ids and codenames:
            id = ids.pop()
            name = codenames.pop()
            print('id = ', id, ' name = ', name)
            fk_list = Database.add_entries_to_vendor_table(supabase, id, name)

    @staticmethod
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
