from supabase import create_client
from dotenv import load_dotenv
import os
from typing import Dict
import udp_files.python_udpclient.py


class Database:

    load_dotenv()
    url: str = os.environ.get("REACT_APP_SUPABASE_URL")
    key: str = os.environ.get("REACT_APP_ANON_KEY")
    supabase = create_client(url, key)

    @staticmethod
    def addData(values: Dict[int, str]) -> Dict[int, str]:
        print("submitting id...")

        entries = {}

        for id, name in values.items():
            print('id = ', id, ' name = ', name)

            # Check if the ID already exists in the table
            existing_entry = Database.check_existing_entry(
                Database.supabase, id)
            if existing_entry is not None:
                print(
                    f"ID {id} already exists in the table. Codename: {existing_entry['codename']}")
                entries[id] = existing_entry['codename']
            else:
                if name != '':
                    Database.add_entry_to_player_table(id, name)
        return entries

    @staticmethod
    def addHardware(values: Dict[int, int]):
        load_dotenv()

        for id, name in values.items():
            print('id = ', id, ' name = ', name)
            Database.add_hardware(Database.supabase, id, name)

    @staticmethod
    def check_existing_entry(supabase, id):
        data = supabase.table('player').select('*').eq('id', id).execute()
        if 'error' in data:
            print(f"Error fetching data: {data['error']}")
            return None
        else:
            return data.data[0] if data.data else None

    @staticmethod
    def add_entry_to_player_table(supabase, id, codename):
        data = supabase.table('player').insert(
            {'id': id, 'codename': codename}).execute()
        print(data)

    @staticmethod
    def add_hardware(supabase, id, equipment_id):
        data = supabase.table('player').update(
            {'equipment_id': equipment_id}).eq('id', id).execute()
        udp_files.python_udpclient.transmitEquipmentCode(equipment_id)
        print(data)

    @staticmethod
    def fetch_data(id):
        data = Database.supabase.table('player')
        codename = data.select(id).execute()
        print("codename = {}".format(codename))
        return codename

    @staticmethod
    def fetch_data():
        data = Database.supabase.table('player').select("*").execute()
        print(data)
        return data
