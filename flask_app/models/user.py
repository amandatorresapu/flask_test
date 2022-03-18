from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def make_user(cls,data):
        mysql = connectToMySQL("users_schema")
        query = "INSERT INTO users (first_name, last_name, email) Values (%(first_name)s, %(last_name)s, %(email)s);"
        return mysql.query_db(query, data)
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_schema").query_db(query, data)
        if results: 
            return cls(results[0])
    
    @classmethod
    def update_user(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        connectToMySQL("users_schema").query_db(query, data)

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL("users_schema").query_db(query, data)