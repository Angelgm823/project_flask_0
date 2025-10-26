from flask import Blueprint

bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/lista')
def index():
    return 'Lista de tareas'

@bp.route('/create')
def crear():
    return 'Crear nueva tarea'