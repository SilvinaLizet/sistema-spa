from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect

from config import config

# * models
from models.ModelUser import ModelUser

# * entities
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db=MySQL(app) # * Conexion a la base de datos
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET',"POST"])
def login():
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        user = User(0, "", "", request.form['username'], request.form['password'], "",0,"", "")
        logged_user = ModelUser.login(db, user)
        print(user)
        print(logged_user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña inválida.")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/protected')
@login_required
def protected():
    return "<h1> Esta es una vista protegida, solo para usuarios autenticados</h1>"

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
