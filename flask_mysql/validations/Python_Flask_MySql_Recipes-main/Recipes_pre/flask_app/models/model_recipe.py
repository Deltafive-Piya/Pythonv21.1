from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime


class Recipe:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.directions=data['directions']
        self.less_than_30=data['less_than_30']
        self.instructions=data['instructions']
        self.date_made=data['date_made'].date()
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        if 'user_id' in data:
            self.user=data['user_id']


    @classmethod
    def create(cls, data):
        query="INSERT INTO recipes (name, directions, instructions, less_than_30, date_made, user_id, created_at, updated_at)"\
            "VALUES (%(name)s, %(directions)s, %(instructions)s, %(less_than_30)s, %(date_made)s, %(user_id)s, NOW(), NOW())"
        result=connectToMySQL('recipes_schema').query_db(query, data)
        return result


    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM recipes WHERE id=%(id)s;"
        result=connectToMySQL('recipes_schema').query_db(query, data)
        print(result)
        return cls(result[0])


    @classmethod
    def get_all(cls):       #method does not need 'data'
        query = "SELECT * FROM recipes;"
        results =  connectToMySQL("recipes_schema").query_db(query)
        all_recipes = []
        for row in results:
            print(row['date_made'])
            all_recipes.append( cls(row) )
        return all_recipes


    @classmethod
    def update(cls, data):
        query="UPDATE recipes "\
            "SET name=%(name)s, directions=%(directions)s, "\
            "instructions=%(instructions)s, less_than_30=%(less_than_30)s, "\
            "date_made=%(date_made)s, updated_at=NOW() "\
            "WHERE id=%(id)s;"
        result=connectToMySQL('recipes_schema').query_db(query, data)
        return result


    @classmethod
    def delete(cls, data):
        query="DELETE FROM recipes "\
            "WHERE id=%(id)s;"
        result=connectToMySQL('recipes_schema').query_db(query, data)
        return result


    @staticmethod
    def validate(data):
        is_valid=True

        if 'name' not in data:
            flash('*Please enter a name for your recipe', 'create_errors')
            is_valid=False
        elif len(data['name'])<3:
            flash('*Name must be at least three characters', 'create_errors')
            is_valid=False

        if 'directions' not in data:
            flash('*Please enter a directions for your recipe', 'create_errors')
            is_valid=False
        elif len(data['directions'])<3:
            flash('*directions must be at least three characters', 'create_errors')
            is_valid=False

        if 'instructions' not in data:
            flash('*Please enter instructions for your recipe', 'create_errors')
            is_valid=False
        elif len(data['instructions'])<3:
            flash('*Instructions must be at least three characters', 'create_errors')
            is_valid=False

        if 'less_than_30' not in data:
            flash('*Must select a valid checkbox', 'create_errors')
            is_valid=False
        elif data['less_than_30']!='0' and data['less_than_30']!='1':
            flash('*Must select a valid checkbox', 'create_errors')
            is_valid=False

        if 'date_made' not in data:
            flash('*Please enter the date made for your recipe', 'create_errors')
            is_valid=False
        elif len(data['date_made'])!=10:
            flash('*Please enter a valid date', 'create_errors')
            is_valid=False

        return is_valid