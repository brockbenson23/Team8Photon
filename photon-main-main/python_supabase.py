from supabase import create_client
from dotenv import load_dotenv
import os
from typing import Dict

class Database:
    @staticmethod
    def addData(values: Dict[int, str]) -> Dict[int, str]:
        print("submitting id...")
        load_dotenv()

        url: str = os.environ.get("REACT_APP_SUPABASE_URL")
        key: str = os.environ.get("REACT_APP_ANON_KEY")
        supabase = create_client(url, key)

        for id, name in values.items():
            print('id = ', id, ' name = ', name)

            # Check if the ID already exists in the table
            existing_entry = Database.check_existing_entry(supabase, id)
            if existing_entry is not None:
                print(
                    f"ID {id} already exists in the table. Codename: {existing_entry['codename']}")
                return {id: existing_entry['codename']}
            else:
                Database.add_entry_to_player_table(supabase, id, name)
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
    def add_entry_to_player_table(supabase, id, codename):
        data = supabase.table('player').insert(
            {'id': id, 'codename': codename}).execute()
        print(data)

