from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombre = db.Column(db.String(20), unique=True)
    password = db.Column(db.Text, nullable = False)
    
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
        
    def __repr__(self):
        return f'<User: (self.nombre)>'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = True)
    titulo = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.Boolean, default= False)
    
    def __init__(self,created_by, titulo, desc, state):
        self.created_by = created_by
        self.titulo = titulo
        self.desc = desc
        self.state = state
        
        
    def __repr__(self):
        return f'<User: (self.titulo)>'