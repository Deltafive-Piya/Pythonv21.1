from flask import flash, session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt

class Vendor:
    def __init__(self, data: dict):
        # Initialize attributes for all the columns in the markets_db.markets table
        self.id = data['id']
        self.f_name = data['f_name']
        self.l_name = data['l_name']
        self.email = data['email']
        self.password = data['password']
        self.market_id = data['market_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data: dict):
        # Query [ Study %()s- parameterized queries are used to securely pass data to DB w/o directly inserting the values into SQL query string.]
        query = "INSERT INTO vendors (f_name, l_name, email, password, market_id) VALUES (%(f_name)s, %(l_name)s, %(email)s, %(password)s, %(market_id)s);"
        # Contact to db(brought to you by ln 5) and RUN!DAT! data! Specifically, here is where we correct the 'markets" nomenclature ->to "vendor"
        vendor_id = connectToMySQL(DATABASE).query_db(query, data)
        # Return - Now that we have previously created the path to send and retrieve, let's make it work
        return vendor_id

    # Read
    @classmethod
    def get_one(cls, data: dict):
        query = "SELECT * FROM vendors WHERE id = %(id)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        #convert the results into instance and return
        return cls( results[0] )
    
    @classmethod
    def get_one_by_name(cls, data: dict):
        query = "SELECT * FROM vendors WHERE f_name = %(f_name)s AND l_name = %(l_name)s;"

        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return False
        # Convert the results into an instance and return
        return cls(results[0])
    
    # Update
    # Delete

    @staticmethod
    def validate(data: dict):
        is_valid = True

        if len(data['f_name']) < 1:
            is_valid = False
            flash("Invalid First Name", "err_vendor_f_name")
        else:
            # Delete the flashed message from the session if it exists
            if 'err_vendor_f_name' in session:
                del session['err_vendor_f_name']

        if len(data['l_name']) < 1:
            is_valid = False
            flash("Invalid Last Name", "err_vendor_l_name")
        else:
            # Delete the flashed message from the session if it exists
            if 'err_vendor_l_name' in session:
                del session['err_vendor_l_name']

        # Additional validation for password (at least 1 number and 1 uppercase letter)
        if len(data['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters", "err_vendor_password")

        if not any(char.isdigit() for char in data['password']):
            is_valid = False
            flash("Password must contain at least 1 number", "err_vendor_password")

        if not any(char.isupper() for char in data['password']):
            is_valid = False
            flash("Password must contain at least 1 uppercase letter", "err_vendor_password")

        # Check if the email already exists in the database (including the current request data)
        if is_valid:
            potential_vendor = Vendor.get_one_by_name({'email': data['email']})
            if potential_vendor:
                is_valid = False
                flash("Email already exists", "err_vendor_email")

        return is_valid
    
    @staticmethod
    def validate_login(data: dict):
        is_valid = True

        if len(data['f_name']) < 1:
            is_valid = False
            flash("Invalid credentials", "err_vendor_f_name")

        if len(data['password']) < 8:
            is_valid = False
            flash("Invalid credentials", "err_vendor_password")

        if is_valid:
            potential_vendor = Vendor.get_one_by_name({'f_name': data['f_name']})

            if not potential_vendor:
                is_valid = False
                flash("Invalid Credentials", "err_vendor_f_name")
            else:
                # Use the correct hashed password from the potential_vendor object
                hashed_password = potential_vendor.password
                # Check if the provided password matches the hashed password
                has_passed = bcrypt.check_password_hash(hashed_password, data['password'])
                if not has_passed:
                    flash("Invalid Credentials", "err_vendor_f_name")
                else:
                    session['vendor_id'] = potential_vendor.id

        return is_valid