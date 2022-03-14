from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB, bcrypt
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at'] 
    #C
    @classmethod
    def create_user(cls, data):
            query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
            plain_pass = data['password']
            pw_hash = bcrypt.generate_password_hash(plain_pass)

            data = {
            **data,
            'password':pw_hash,
        }

            results = connectToMySQL(DB).query_db(query, data)
            print('this is the user id -----> ', results)
            return results
    #R
    @classmethod
    def get_one(cls, **data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])
    
    # @classmethod
    # def get_painting_by_maker(cls, data):
    #     query = '''
    #         SELECT * FROM users
    #         LEFT JOIN paintings ON users.id = user_id
    #         WHERE users.id = %(id)s;
    #         '''
    #     results = connectToMySQL(DB).query_db(query, data)
    #     print(results)
    #     if results:
    #         one_user = cls(results[0])
    #         one_user.paintings_created = []
    #         for row in results:
    #             painting_data = {
    #                 "id" : row['painting.id'],
    #                 "created_at" : row['painting.created_at'],
    #                 "updated_at" : row['painting.updated_at'],
    #                 "title" : row['title'],
    #                 "description" : row['description'],
    #                 "price" : row['price'],
    #                 "description" : row['description']
    #             }
    #             painting = Painting(painting_data)
    #             one_user.paintings_created.append(painting)
    #         print(one_user)
    #         return one_user

    @staticmethod
    def login_user(data):
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid Email/Password")
            return False
        
        if len(data['password']) < 7:
            flash("Invalid Email/Password")
            return False

        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query,data)

        if not result:
            flash("Invalid Email/Password")
            return False

        user_in_db = User(result[0])
        print(user_in_db)
        if not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash("Invalid Email/Password", "login")
            return False

        return user_in_db

    @staticmethod
    def validate_user(data):
        is_valid = True
        
        if len(data['first_name'])<3:
            flash('First name must be at least 4 characters!')
            is_valid = False
        elif len(data['first_name']) == 0:
            flash('All fields required!')
            is_valid = False
        
        if len(data['last_name'])<3:
            flash('Full name must be at least 4 characters!')
            is_valid = False
        elif len(data['last_name']) == 0:
            flash('All fields required!')
            is_valid = False
        # maybe we need users to be unique

        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Invalid email address!')

        if len(data['password'])<7:
            is_valid = False
            flash('Password must be at least 8 characters!')

        if data['password'] != data['confirm_password']:
            is_valid = False
            flash('Passwords must match!!')

        return is_valid