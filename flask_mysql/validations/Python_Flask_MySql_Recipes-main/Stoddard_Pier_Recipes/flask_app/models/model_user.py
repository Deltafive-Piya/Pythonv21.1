from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_recipe import Recipe
from flask import flash
import re
# [a-zA-Z0-9.+_-]+  -- Matches occurrences of characters that can be either (A-Z), (a-z), (0-9), or special characters ., +, _, and -.
# @ char that must exist in email addresses
# \. --Matches the period character in the email address. Since . is a regex special character, escape with a backslash to treat it as a literal period.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.recipes=[]


    @classmethod
    def create(cls, data):
        query="INSERT INTO users (first_name, last_name, email, password)"\
            "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result=connectToMySQL('recipes_schema').query_db(query, data)
        return result


    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM users "\
            "LEFT JOIN recipes ON users.id=recipes.user_id "\
            "WHERE users.id=%(id)s;"
        results=connectToMySQL('recipes_schema').query_db(query, data)
        user=cls(results[0])
        if results[0]['recipes.id']!=None:
            for row in results:
                row_data={
                    'id':row['recipes.id'],
                    'name':row['name'],
                    'directions':row['directions'],
                    'less_than_30':row['less_than_30'],
                    'instructions':row['instructions'],
                    'date_made':row['date_made'],
                    'created_at':row['recipes.created_at'],
                    'updated_at':row['recipes.updated_at']
                }
                user.recipes.append(Recipe(row_data))
        return user


    @classmethod
    def get_by_email(cls, data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        result=connectToMySQL('recipes_schema').query_db(query, data)
        print(result)
        if len(result)<1:
            return False
        return cls(result[0])


    @staticmethod
    def validate(data):
        is_valid=True

        if 'first_name' not in data:
            flash('Invalid first name', 'err_registration')
            is_valid=False
        elif len(data['first_name'])<2:
            flash('Invalid characters', 'err_registration')
            is_valid=False

        if 'last_name' not in data:
            flash('Invalid last name', 'err_registration')
            is_valid=False
        elif len(data['last_name'])<2:
            flash('Invalid characters', 'err_registration')
            is_valid=False

        if 'email' not in data:
            flash('Invalid address', 'err_registration')
            is_valid=False
        elif not EMAIL_REGEX.match(data['email']):
            flash('*Invalid email address', 'err_registration')
            is_valid=False
        elif User.get_by_email(data):
            flash(f"*{data['email']} already in use", 'err_registration')
            is_valid=False

        if 'password' not in data:
            flash('Invalid password', 'err_registration')
            is_valid=False
        elif 'confirm_password' not in data:
            flash('Invalid password', 'err_registration')
            is_valid=False
        elif len(data['password'])<8:
            flash('Invalid characters', 'err_registration')
            is_valid=False
        elif data['password']!=data['confirm_password']:
            flash('Invalid password confirmation', 'err_registration')
            is_valid=False

        return is_valid