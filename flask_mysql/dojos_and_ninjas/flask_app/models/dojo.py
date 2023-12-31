from ..config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos_and_ninjas.dojos;"
        dojos = []
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        for row in results:
            dojos.append(cls(row))
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        dojo = cls(results[0])
        for row in results:
            if row['ninjas.id'] is not None:
                data = {
                    "id": row['ninjas.id'],
                    "first_name": row['first_name'],
                    "last_name": row['last_name'],
                    "age": row['age'],
                    "created_at": row['ninjas.created_at'],
                    "updated_at": row['ninjas.updated_at'],
                    "dojo_id": row['dojo_id'],
                    "weapon_of_choice": row['weapon_of_choice'],
                }
                dojo.ninjas.append(Ninja(data))
        return dojo