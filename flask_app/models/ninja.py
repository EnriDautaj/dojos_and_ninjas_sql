from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db_name = 'dojos_ninjas_SQL'
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['first_name']
        self.content = data['last_name']
        self.content = data['age']
        self.user_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #READ
    @classmethod
    def get_ninjas_of_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.dojo_id = %(dojo_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        ninjas = []
        if results:
            for ninja in results:
                ninjas.append(ninja)
            return ninjas
        return ninjas
    
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (dojo_id, first_name, last_name, age) VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);'
        return connectToMySQL(cls.db_name).query_db(query, data)
    