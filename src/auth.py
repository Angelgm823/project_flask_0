from flask import (Blueprint, render_template, request, redirect, flash, url_for)
from .models import User
from src import db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__, url_prefix='/auth')

# vistas de los HTML
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        
        user = User(nombre, generate_password_hash(password))
        
        user_name = User.query.filter_by(nombre = nombre).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('auth/login.html')