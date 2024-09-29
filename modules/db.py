import sqlite3
class DB_Controller:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()

    def handle_user(self, user_id):
        is_exist = self.c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
        if is_exist is None:
            self.c.execute("INSERT INTO users VALUES (?, ?, ?)", (user_id, 0 ,0,))
            self.conn.commit()
            return True
        else:
            return False
        
    def handle_test(self, user_id):
        is_first_time = self.c.execute("SELECT is_test FROM users WHERE user_id = ?", (user_id,)).fetchone()
        if is_first_time[0] == 0:
            self.c.execute("UPDATE users SET is_test = 1 WHERE user_id = ?", (user_id,))
            self.conn.commit()
            return True
        else:
            return False
        
    def add_customer(self, user_id):
        self.c.execute("UPDATE users SET is_customer = 1 WHERE user_id = ?", (user_id,))
        self.conn.commit()
        
    def get_customers(self):
        return self.c.execute("SELECT user_id FROM users WHERE is_customer = 1").fetchall()