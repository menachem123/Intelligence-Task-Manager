from .db_connection import DB_connection
from mysql.connector import Error
from logs.setup_logger import logger
class AgentDB:
    def __init__(self):
        self.db = DB_connection()

    def create_agent(self, data):
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "INSERT INTO agents (name, specialty, agent_rank) "
                "VALUES (%s, %s, %s)",
                (data["name"], data["specialty"], data["agent_rank"]),
            )
            connection.commit()
            new_id = cursor.lastrowid
            cursor.execute("SELECT * FROM agents WHERE id = %s", (new_id,))
            row = cursor.fetchone()
            cursor.close()
            return row
        except Error as e:
            print(e)
            return None
        finally:
            connection.close()

    def get_all_agents(self):
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM agents")
            rows = cursor.fetchall()
            cursor.close()
            if rows:
                return rows
            else:
                return []
        except Error as e:
            logger.error(e)
            return []
        finally:
            connection.close()

    def get_agent_by_id(self, id):
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM agents WHERE id = %s", (id,))
            row = cursor.fetchone()
            cursor.close()
            return row
        except Error as e:
            logger.error(e)
            return None
        finally:
            connection.close()

    def deactivate_agent(self, id):
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE agents SET is_active = FALSE WHERE id = %s", (id,))
            connection.commit()
            cursor.close()
            return {"message": "success"}
        except Error as e:
            return {"message": str(e)}
        finally:
            connection.close()

 







  