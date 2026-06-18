import mysql.connector


class DB_connection:
    HOST = "127.0.0.1"
    PORT = 3306
    USER = "root"
    PASSWORD = "1234"
    DATABASE = "Intelligence_db"

    def _connect(self, with_database=True):
        params = {
            "host": self.HOST,
            "port": self.PORT,
            "user": self.USER,
            "password": self.PASSWORD,
        }
        if with_database:
            params["database"] = self.DATABASE
        return mysql.connector.connect(**params)

    def get_connection(self):
        return self._connect(with_database=True)

    def create_database(self):
        connection = self._connect(with_database=False)
        try:
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.DATABASE}")
            cursor.close()
        finally:
            connection.close()

    def create_tables(self):
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS agents ("
                "id INT AUTO_INCREMENT PRIMARY KEY, "
                "name VARCHAR(50) NOT NULL, "
                "specialty VARCHAR(50) NOT NULL, "
                "is_active BOOLEAN DEFAULT TRUE, "
                "completed_missions INT DEFAULT 0, "
                "failed_missions INT DEFAULT 0, "
                "agent_rank ENUM('Junior','Senior','Commander') NOT NULL"
                ")"
            )
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS missions ("
                "id INT AUTO_INCREMENT PRIMARY KEY, "
                "title VARCHAR(50) NOT NULL, "
                "description TEXT NOT NULL, "
                "location VARCHAR(50) NOT NULL, "
                "difficulty INT NOT NULL, "
                "importance INT NOT NULL, "
                "status VARCHAR(20) DEFAULT 'NEW', "
                "risk_level VARCHAR(20), "
                "assigned_agent_id INT DEFAULT NULL"
                ")"
            )
            cursor.close()
        finally:
            connection.close()


if __name__ == "__main__":
    db = DB_connection()
    db.create_database()
    # db.crea

