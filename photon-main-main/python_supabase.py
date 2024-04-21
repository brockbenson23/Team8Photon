from supabase import create_client
from dotenv import load_dotenv
import os
from typing import Dict

class Database:
    load_dotenv()
    url: str = os.environ.get("REACT_APP_SUPABASE_URL")
    key: str = os.environ.get("REACT_APP_ANON_KEY")
    supabase = create_client(url, key)

    @staticmethod
    def addData(values: Dict[int, str]) -> Dict[int, str]:
        print("submitting id...")
        for id, name in values.items():
            print('id = ', id, ' name = ', name)

            # Check if the ID already exists in the table
            existing_entry = Database.check_existing_entry(Database.supabase, id)
            if existing_entry is not None:
                print(
                    f"ID {id} already exists in the table. Codename: {existing_entry['codename']}")
                return {id: existing_entry['codename']}
            else:
                Database.add_entry_to_player_table(id, name)
                return {0: ''}

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
    def update_data(id, newname):
        data = Database.supabase.table('player')
        data.upsert({'id' : id, 'name' : newname})
        print(data)

    @staticmethod
    def fetch_name(id):
        data = Database.supabase.table('player').select('*').eq('id', id).execute()
        codename = data.data[0]['codename'] if data.data else None
        return codename
    
    @staticmethod
    def fetch_data():
        data = Database.supabase.table('player').select("*").execute()
        print(data)
        return data

