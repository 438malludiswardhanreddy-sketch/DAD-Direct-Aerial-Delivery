import sqlite3
import os

DB_FILE = "dad_logistics.db"

class DatabaseManager:
    def __init__(self, db_path=DB_FILE):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create Drones table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS drones (
                id TEXT PRIMARY KEY,
                model TEXT NOT NULL,
                status TEXT NOT NULL,
                battery_capacity_mah REAL NOT NULL,
                last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create Missions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS missions (
                id TEXT PRIMARY KEY,
                drone_id TEXT NOT NULL,
                start_lat REAL NOT NULL,
                start_lon REAL NOT NULL,
                end_lat REAL NOT NULL,
                end_lon REAL NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (drone_id) REFERENCES drones (id)
            )
        ''')

        # Insert default fleet if empty
        cursor.execute("SELECT COUNT(*) FROM drones")
        if cursor.fetchone()[0] == 0:
            cursor.executemany('''
                INSERT INTO drones (id, model, status, battery_capacity_mah)
                VALUES (?, ?, ?, ?)
            ''', [
                ("drone_01", "Tarot 680Pro Hexacopter", "Active", 16000.0),
                ("drone_02", "Tarot 680Pro Hexacopter", "Charging", 16000.0),
                ("drone_03", "Tarot 680Pro Hexacopter", "Maintenance", 16000.0)
            ])
            conn.commit()

        conn.close()

    def get_all_drones(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM drones")
        drones = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return drones

if __name__ == "__main__":
    db = DatabaseManager()
    print(f"[DB] Initialized database. Registered drones: {db.get_all_drones()}")
