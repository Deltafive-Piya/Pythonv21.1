from ..config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        self.weapon_of_choice = data['weapon_of_choice']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos_and_ninjas.ninjas;"
        ninjas = []
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        for row in results:
            ninjas.append(cls(row))
        return ninjas

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos_and_ninjas.ninjas (first_name, last_name, age, dojo_id, weapon_of_choice) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, %(weapon_of_choice)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM dojos_and_ninjas.ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return cls(result[0])