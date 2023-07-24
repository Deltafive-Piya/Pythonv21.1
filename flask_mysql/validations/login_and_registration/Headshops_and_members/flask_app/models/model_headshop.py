from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt

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
    @classmethod
    def get_one(cls, data: dict):
        query = "SELECT * FROM dispensaries WHERE id = %(id)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        #convert the results into instance and return
        return cls( results[0] )
    
    @classmethod
    def get_one_by_name(cls, data: dict):
        query = "SELECT * FROM dispensaries WHERE name = %(name)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        #convert the results into instance and return
        return cls( results[0] )
    
    # Update
    # Delete

    @staticmethod
    def validate(data: dict):
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
            flash("Invalid City", "err_dispensary_city")

        cbd_only_value = data.get('cbd_only')
        if cbd_only_value not in ('0', '1'):
            is_valid = False
            flash("Please enter either '0' for no or '1' for yes", "err_dispensary_cbd_only")

        if len(data['password']) < 1:
            is_valid = False

        # Check if the name already exists in the database (including the current request data)
        if is_valid:
            potential_dispensary = Headshop.get_one_by_name({'name': data['name']})
            if potential_dispensary:
                is_valid = False
                flash("Name already exists", "err_dispensary_name")

        return is_valid
    
    @staticmethod
    def validate_login(data:dict):
        is_valid = True

        if len(data['name']) < 1:
            is_valid = False
            flash("Invalid credentials", "err_dispensary_name")

        if len(data['password']) < 1:
            is_valid = False
            flash("Invalid credentials", "err_dispensary_password")

        if is_valid:
            potential_dispensary = Headshop.get_one_by_name({'name': data['name']})

            if not potential_dispensary:
                is_valid = False
                flash("Invalid Credentials", "err_dispensary_name")
            else:
                # Use the correct hashed password from the potential_dispensary object
                hashed_password = potential_dispensary.password
                # Check if the provided password matches the hashed password
                has_passed = bcrypt.check_password_hash(hashed_password, data['password'])
                if not has_passed:
                    flash("Invalid Credentials", "err_dispensary_name")
                else:
                    session['dispensary_id'] = potential_dispensary.id

        return is_valid