from database.db_connection import DB_connection
from mysql.connector import Error
from logs.setup_logger import logger


def _compute_risk_level(difficulty, importance):
    score = difficulty * 2 + importance
    if score <= 9:
        return "LOW"
    if score <= 17:
        return "MEDIUM"
    if score <= 24:
        return "HIGH"
    return "CRITICAL"


class MissionDB:
    def __init__(self):
        self.db = DB_connection()

    def create_mission(self, data):
        risk_level = _compute_risk_level(data["difficulty"], data["importance"])
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "INSERT INTO missions "
                "(title, description, location, difficulty, importance, risk_level) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    data["title"],
                    data["description"],
                    data["location"],
                    data["difficulty"],
                    data["importance"],
                    risk_level,
                ),
            )
            connection.commit()
            new_id = cursor.lastrowid
            cursor.execute("SELECT * FROM missions WHERE id = %s", (new_id,))
            row = cursor.fetchone()
            cursor.close()
            return row
        except Error as e:
            logger.error(e)
            return None
        finally:
            connection.close()

    def get_all_missions(self):
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM missions")
            rows = cursor.fetchall()
            cursor.close()
            return rows if rows else []
        except Error as e:
            logger.error(e)
            return []
        finally:
            connection.close()

    def get_mission_by_id(self, id):
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM missions WHERE id = %s", (id,))
            row = cursor.fetchone()
            cursor.close()
            return row
        except Error as e:
            logger.error({"message":str(e)})
            return None
        finally:
            connection.close()

    def update_mission_status(self, id, status):
        connection = self.db.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE missions SET status = %s WHERE id = %s",
                (status, id),
            )
            connection.commit()
            cursor.close()
            return {"message": "success"}
        except Error as e:
            return {"message": str(e)}
        finally:
            connection.close()













