import os
import psycopg2
from dotenv import load_dotenv


class NeonDatabaseManager:
    def __init__(self):
        load_dotenv()
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        self.connection = None

    def connect_to_db(self):
        '''connect to Neon Bootcamp Survival database'''
        try:
            connection = psycopg2.connect(self.DATABASE_URL)
            self.connection = connection
        except Exception as e:
            print("Error while connecting to Neon DB:", e)
            return None 

    def insert_Questions(self, question):
        