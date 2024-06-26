from supabase import create_client
from dotenv import load_dotenv
import os
from typing import Dict
import python_udpserver

class Database:
    load_dotenv()
    url: str = os.environ.get("REACT_APP_SUPABASE_URL")
    key: str = os.environ.get("REACT_APP_ANON_KEY")
    supabase = create_client(url, key)

    @staticmethod
    def clearEquipmentIds():
        data = Database.supabase.table('player').update(
                {'equipment_id': 0, 'hasBase': bool(False), 'points': 0}).gt('prime_key', 0).execute()
        print("All equipment IDs cleared.")

    @staticmethod
    def removeB():
        # Fetch all player data
        all_players_data = Database.supabase.table('player').select('*').execute().data

        if all_players_data:
            for player_data in all_players_data:
                # Remove the '🅑' prefix from the code name
                codename = player_data.get('codename', '')
                if codename.startswith('🅑'):
                    new_codename = codename[2:]
                    # Update the database with the new code name
                    Database.supabase.table('player').update({'codename': new_codename}).eq('id', player_data['id']).execute()

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
                entries[id] = ''
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
        # Check if the equipment_id already exists for the given id
        existing_entry = supabase.table('player').select(
            '*').eq('id', id).execute()

        if existing_entry.data:
            # If the equipment_id exists, update the existing row
            data = supabase.table('player').update(
                {'equipment_id': equipment_id}
            ).eq('id', id).execute()
        else:
            # If the equipment_id doesn't exist, insert a new row
            data = supabase.table('player').insert(
                {'id': id, 'equipment_id': equipment_id}
            ).execute()
        python_udpserver.transmitCode(str(id))
        print(data)

    @staticmethod
    def update_data(id, codename, equipmentid, hasBase, points):
        data = Database.supabase.table('player').update({'codename': codename,
        'equipment_id': equipmentid, 'hasBase': hasBase, 'points': points}).eq('id', id).execute()
        print(data)

    @staticmethod
    def fetch_name(id):
        data = Database.supabase.table(
            'player').select('*').eq('equipment_id', id).execute()
        codename = data.data[0]['codename'] if data.data else None
        return codename

    @staticmethod
    def fetch_playerData(id):
        data = Database.supabase.table(
            'player').select('*').eq('equipment_id', id).execute()
        print(data)
        # checking if data exists, returns None if not
        return data.data if data.data else None

    @staticmethod
    def HID_fetch_playerData(hID):
        data = Database.supabase.table(
            'player').select('*').eq('equipment_id', hID).execute()
        print(data)
        # checking if data exists, returns None if not
        return data.data if data.data else None
