from flask import flash

class Headshop:
    def __init__(self, data:dict):
        #for all the columns in the headshops_db.dispensaries table 
        self.id = data['id']
        self.name = data['name']
        self.city = data['city']
        self.cbd_only = data['cbd_only']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        #classsmethods
        #Create
        #Read
        #Update
        #Delete

        #validations
        @staticmethod
        def validate(data):
            is_valid = True

            if len(data['name']) < 1:
                is_valid = False
                flash("Invalid Name", "err_dispensary_name")

            if len(data['city']) < 1:
                is_valid = False
                flash("Invalid Name", "err_dispensary_city")
            
            if data['cbd_only'] > 1:
                is_valid = False
                flash("Please enter either '0' for no or '1' for yes", "err_dispensary_cbd_only")

            if len(data['password']) < 1:
                is_valid = False
                
            return is_valid