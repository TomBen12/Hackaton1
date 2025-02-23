import psycopg2
import os
from dotenv import load_dotenv


class NeonDatabaseManager:
    def __init__(self):
        load_dotenv()
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        self.connection = None

    def connect_to_db(self):
        try:
            self.connection = psycopg2.connect(self.DATABASE_URL)
        except Exception as e:
            print("Error connecting to Neon DB:", e)
            self.connection = None

    def insert_questions(self, table, questions):
        if not self.connection:
            print("No database connection. Call connect_to_db() first.")
            return

        cursor = self.connection.cursor()
        query = f"""
        INSERT INTO {table} (question, answer_a, answer_b, answer_c, answer_d, answer_e, answer_f, correct_answer, difficulty, topic)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (question) DO NOTHING;
        """

        try:
            for q in questions:
                values = [
                    q["question"],
                    q["answers"].get("answer_a"),
                    q["answers"].get("answer_b"),
                    q["answers"].get("answer_c"),
                    q["answers"].get("answer_d"),
                    q["answers"].get("answer_e"),
                    q["answers"].get("answer_f"),
                    q.get("correct_answer"),
                    q["difficulty"],
                    q["topic"],
                ]
                cursor.execute(query, values)

            self.connection.commit()
            print(f"{len(questions)} questions inserted into '{table}' successfully.")

        except Exception as e:
            print("Error inserting questions:", e)

        finally:
            cursor.close()

    def retrieve_question_at_random(self, amount, table):
        if not self.connection:
            print("No database connection. Call connect_to_db() first.")
            return None

        cursor = self.connection.cursor()
        query = f"SELECT * FROM {table} ORDER BY RANDOM() LIMIT %s;"
        try:
            cursor.execute(query, (amount,))
            questions = cursor.fetchall()

            column_names = [desc[0] for desc in cursor.description]
            question_list = [dict(zip(column_names, row)) for row in questions]
            return question_list

        except Exception as e:
            print("Error", e)
            return None
        finally:
            cursor.close()

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
            except Exception as e:
                print("Error closing connection:", e)
        else:
            print("Nothing to close.")

# test = NeonDatabaseManager()
# test.connect_to_db()
# print(test.retrieve_question_at_random(10, "easy_questions"))
# test.close_connection()
