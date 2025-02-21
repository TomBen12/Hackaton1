import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

def connect_to_db():
    try:
        conection = psycopg2.connect(DATABASE_URL)
        return conection
    except:
        print('Error while connecting to Neon db...')
        