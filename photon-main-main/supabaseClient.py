import os
from supabase import create_client, Client

url: str = os.environ.get("REACT_APP_SUPABASE_URL")
key: str = os.environ.get("RECT_APP_ANON_KEY")
supabase: Client = create_client(url, key)
