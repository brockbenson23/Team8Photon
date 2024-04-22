from supabase import create_client
from dotenv import load_dotenv
import os
#import python_udpserver
from typing import Dict
from typing import List

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
            existing_entry = Database.check_existing_entry(Database.supabase, id)
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
    def add_entry_to_player_table(id, codename):
        data = Database.supabase.table('player').insert(
            {'id': id, 'codename': codename}).execute()
        print(data)

    @staticmethod
    def add_hardware(supabase, id, equipment_id):
        data = supabase.table('player').update(
            {'equipment_id': equipment_id}).eq('id', id).execute()
        #python_udpserver.transmitID(equipment_id)
        print(data)
        
    @staticmethod
    def update_data(id, codename, equipmentid, hasBase, points):
        data = Database.supabase.table('player')
        data.upsert({'id' : id, 'name' : codename})
        print(data)

    @staticmethod
    def fetch_name(id):
        data = Database.supabase.table('player').select('*').eq('id', id).execute()
        codename = data.data[0]['codename'] if data.data else None
        return codename
    
    @staticmethod
    def fetch_playerData(id):
        data = Database.supabase.table('player').select('*').eq('id', id).execute()
        print(data)
        return data.data if data.data else None # checking if data exists, returns None if not
    

