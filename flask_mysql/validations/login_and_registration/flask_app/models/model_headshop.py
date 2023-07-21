class Dispensary:
    def __init__(self, data:dict):
        #for all the columns in the db
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