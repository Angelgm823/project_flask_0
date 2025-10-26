from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# extencion de base de datos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root0300@localhost:3306/test'
    )

    # inicializar conexión de base de datos
    db.init_app(app)

    # Registro de Blueprint rutas de componentes
    from . import todo
    app.register_blueprint(todo.bp)
    
    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    

    with app.app_context():
        db.create_all()
    
    return app