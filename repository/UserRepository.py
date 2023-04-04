from repository.DBRepository import DBRepository
from fastapi import HTTPException


class UserRepository(DBRepository):
    def __init__(self):
        super().__init__()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user
                (id INTEGER PRIMARY KEY, email TEXT NOT NULL, password TEXT NOT NULL, username TEXT NOT NULL, bio TEXT, image TEXT)""")
        self.conn.commit()

    def create_user(self, user_dict):
        self.conn.execute("INSERT INTO user (email, username, password) VALUES (?, ?, ?)",
                   (user_dict['email'], user_dict['username'], user_dict['password']))
        user_id = self.cursor.lastrowid
        self.conn.commit()
        return user_id

    def login(self, email, password):
        self.cursor.execute("SELECT * FROM user WHERE email=? AND password=?", (email, password))
        user = self.cursor.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        return user

    def get_user(self, user_id):
        self.cursor.execute("SELECT * FROM user WHERE id=?", (user_id,))
        user = self.cursor.fetchone()
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        return user

    def update_user(self, user_id, user_dict):
        self.cursor.execute("SELECT * FROM user WHERE id=?", (user_id,))
        existing_user = self.cursor.fetchone()
        if not existing_user:
            raise HTTPException(status_code=404, detail="user not found")
        self.cursor.execute("UPDATE user SET email=:email, password=:password, username=:username, bio=:bio, image=:image WHERE id=:id",
                            (user_dict['email'], user_dict['username'], user_dict['password'], user_dict['bio'],
                             user_dict['image'], user_id))
        self.conn.commit()
        return user_id

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM user")
        users = self.cursor.fetchall()
        return users
