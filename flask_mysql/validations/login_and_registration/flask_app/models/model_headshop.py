from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Headshop:
    def __init__(self, data: dict):
        # Initialize attributes for all the columns in the headshops_db.dispensaries table
        self.id = data['id']
        self.name = data['name']
        self.city = data['city']
        self.cbd_only = data['cbd_only']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data: dict):
        # Query [ Study %()s- parameterized queries are used to securely pass data to DB w/o directly inserting the values into SQL query string.]
        query = "INSERT INTO dispensaries (name, city, cbd_only, password) VALUES (%(name)s,%(city)s,%(cbd_only)s,%(password)s);" 
        # Contact to db(brought to you by ln 5) and RUN!DAT! data! Specifically, here is where we correct the 'Headshops" nomenclature ->to "Dispensary"
        dispensary_id = connectToMySQL(DATABASE).query_db(query, data)
        # Return - Now that we have previously created the path to send and retrieve, let's make it work
        return dispensary_id

    # Read
    # Update
    # Delete

    @staticmethod
    def validate(data):
        is_valid = True

        # --- Change 1: Removed unnecessary parentheses ---
        if data['name'] == 'Snoop Dogg':
            is_valid = False
            flash("Nice try", "err_dispensary_name")

        if len(data['name']) < 1:
            is_valid = False
            flash("Invalid Name", "err_dispensary_name")

        if len(data['city']) < 1:
            is_valid = False
            flash("Invalid Name", "err_dispensary_city")

        cbd_only_value = data.get('cbd_only')
        if cbd_only_value not in ('0', '1'):
            is_valid = False
            flash("Please enter either '0' for no or '1' for yes", "err_dispensary_cbd_only")

        if len(data['password']) < 1:
            is_valid = False
            
        return is_valid