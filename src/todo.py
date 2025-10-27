from flask import Blueprint, render_template, request, redirect, url_for,g
from .models import Todo, User

from src import db
bp = Blueprint('todo', __name__, url_prefix='/todo')

@bp.route('/lista')
def index():
    todos = Todo.query.all()
    return render_template('todo/index.html', todos = todos)

@bp.route('/create', methods=('GET', 'POST'))
def crear():
    if request.method == 'POST':
        titulo = request.form['titulo']
        desc = request.form['desc']
        
        todo = Todo(titulo, desc)
        
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')

def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo

@bp.route('/update/<id>', methods=('GET', 'POST'))
def update(id):
    
    todo = get_todo(id)
    
    if request.method == 'POST':
        todo.titulo = request.form['titulo']
        todo.desc = request.form['desc']
        todo.state = True if request.form.get('state') == 'on' else  False
        
        
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/update.html' , todo = todo)

@bp.route('/delete/<id>')
def delete(id):
    todo = get_todo(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index'))