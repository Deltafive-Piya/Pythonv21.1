from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime


class Deal:
    def __init__(self, data):
        self.id=data['id']
        self.model=data['model']
        self.price=data['price']
        self.make=data['make']
        self.year=data['year']
        self.description=data['description']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        if 'seller_id' in data:
            self.seller=data['seller_id']


    @classmethod
    def create(cls, data):
        query="INSERT INTO deals (model, price, make, year, description, seller_id) VALUES (%(model)s, %(price)s, %(make)s, %(year)s, %(description)s, %(seller_id)s);"
        result=connectToMySQL('deals_db').query_db(query, data)
        return result


    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM deals;"
        result=connectToMySQL('deals_db').query_db(query, data)
        print(result)
        return cls(result[0])


    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM deals WHERE seller_id = %(seller_id)s;"
        results = connectToMySQL("deals_db").query_db(query, data)
        all_deals = []
        for row in results:
            all_deals.append(cls(row))
        return all_deals

    @classmethod
    def update(cls, data):
        query="UPDATE deals SET "\
            "description=%(description)s, model=%(model)s, price=%(price)s, make=%(make)s, year=%(year)s "\
            "WHERE id=%(id)s;"
        result=connectToMySQL('deals_db').query_db(query, data)
        return result


    @classmethod
    def delete(cls, data):
        query="DELETE FROM deals "\
            "WHERE id=%(id)s;"
        result=connectToMySQL('deals_db').query_db(query, data)
        return result


    @staticmethod
    def validate(data):
        is_valid=True

        #model
        if 'model' not in data:
            flash('*Please enter a model for your deal', 'create_errors')
            is_valid=False

        #model validator
        elif len(data['model'])<3:
            flash('*Name must be at least three characters', 'create_errors')
            is_valid=False

        #description validator-blank or less than 3
        if 'description' not in data:
            flash('*Please enter description for your deal', 'create_errors')
            is_valid=False
        elif len(data['description'])<3:
            flash('Description must be at least three characters', 'create_errors')
            is_valid=False

        #year validator-blank or less than 1
        if 'description' not in data:
            flash('*Please enter description for your deal', 'create_errors')
            is_valid=False
        elif len(data['description'])<1:
            flash('You werent born that far back ago', 'create_errors')
            is_valid=False

        if 'created_at' not in data:
            flash('*Please enter the date made for your deal', 'create_errors')
            is_valid=False
        elif len(data['created_at'])!=10:
            flash('*Please enter a valid date', 'create_errors')
            is_valid=False

        return is_valid