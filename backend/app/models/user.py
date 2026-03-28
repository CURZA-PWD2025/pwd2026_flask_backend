from app.models import db

class User(db.Model):
    
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique = True)
    email = db.Column(db.String(200), unique =True)
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    def __init__(self, nombre, email):
      self.nombre = nombre
      self.email = email
    
    def __repr__(self):
       return f"usuario {self.nombre}, email {self.email} , fecha de creacion {self.created_at} " 
     
    def to_dict(self):
      return {
        'id':self.id,
        'nombre':self.nombre,
        'email':self.email,
        'created_at':self.created_at,
        'updated_at': self.updated_at
      }