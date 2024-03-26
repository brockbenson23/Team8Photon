import json
from dotenv import load_dotenv
from supabase import create_client, Client
from faker import Faker
import faker_commerce


## this file will send and retrieve data to/from the supabase
url: str = os.environ.get("https://rqavdtetomzeacidtuys.supabase.co")
key: str = s.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJxYXZkdGV0b216ZWFjaWR0dXlzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDc0MjM3ODAsImV4cCI6MjAyMjk5OTc4MH0.K12hAvUWChQdhKlUJaLwpcaXIovaEoOnWXR2nhWP-wc")
f.open("supabaseClient.py")
response = supabase.table