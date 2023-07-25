from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_deal import Deal
from flask import flash
import re
# [a-zA-Z0-9.+_-]+  -- Matches occurrences of characters that can be either (A-Z), (a-z), (0-9), or special characters ., +, _, and -.
# @ char that must exist in email addresses
# \. --Matches the period character in the email address. Since . is a regex special character, escape with a backslash to treat it as a literal period.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Seller:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.deals=[]


    @classmethod
    def create(cls, data):
        query="INSERT INTO sellers (first_name, last_name, email, password)"\
            "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result=connectToMySQL('deals_db').query_db(query, data)
        return result


    @classmethod
    def get_one(cls, data):
        query="SELECT * FROM sellers "\
            "LEFT JOIN deals ON sellers.id=deals.seller_id "\
            "WHERE sellers.id=%(id)s;"
        results=connectToMySQL('deals_db').query_db(query, data)
        seller=cls(results[0])
        if results:
            for row in results:
                row_data={
                    'id':row['deals.id'],
                    'model':row['model'],
                    'price':row['price'],
                    'make':row['make'],
                    'year':row['year'],
                    'description':row['description'],
                    'created_at':row['deals.created_at'],
                    'updated_at':row['deals.updated_at']
                }
                seller.deals.append(Deal(row_data))
        return seller


    @classmethod
    def get_by_email(cls, data):
        query="SELECT * FROM sellers WHERE email=%(email)s;"
        result=connectToMySQL('deals_db').query_db(query, data)
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
            #first name length validation
        elif len(data['first_name'])<2:
            flash('Invalid characters', 'err_registration')
            is_valid=False

        if 'last_name' not in data:
            flash('Invalid last name', 'err_registration')
            is_valid=False
            #last name length validation
        elif len(data['last_name'])<2:
            flash('Invalid characters', 'err_registration')
            is_valid=False

        if 'email' not in data:
            flash('Invalid address', 'err_registration')
            is_valid=False
            #email entry validation
        elif not EMAIL_REGEX.match(data['email']):
            flash('*Invalid email address', 'err_registration')
            is_valid=False
        elif Seller.get_by_email(data):
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