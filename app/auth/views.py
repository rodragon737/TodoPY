from flask import render_template, session, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user

from werkzeug.security import generate_password_hash, check_password_hash #Hash

from . import auth

from app.forms import LoginForm
from app.firestore_service import get_user, user_put, get_users
from app.models import UserData, UserModel

# verpass = check_password_hash(get_user(password))

# print(verpass)

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():          
        username = login_form.username.data
        password = login_form.username.data

        user_doc = get_user(username)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict() ['password']

            #if check_password_hash(password_from_db, password):
            if password == password_from_db:
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)

                flash('Bienvenido {{username}}')

                redirect(url_for('hello'))
            else:
                flash('Usuario ó password NO encontrado')
        else:
            flash('Usuario NO registrado')
          
        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('signup', methods=['GET','POST'])
def signup():
    signup_form = LoginForm()
    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            user_put(user_data)

            user = UserModel(user_data)

            login_user(user)
            flash("Ya se creo tu usuario")

            return redirect(url_for('hello'))
        
        else:
            flash('El usario ya existe')
            return redirect(url_for('auth.login'))
            
    return render_template('signup.html', **context)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Hasta la proxima!!!')

    return redirect(url_for('auth.login'))