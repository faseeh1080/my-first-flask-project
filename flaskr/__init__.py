import os

from flask import Flask, render_template,  request, redirect, url_for, session

from .db import get_db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # the main page
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if 'logged_in' not in session:
            return redirect(url_for('login'))

        return render_template("index.html")
    
    # the login page
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            entered_password = request.form['password']
            
            if entered_password == "You didn't see anything.":
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                error_message = "Invalid password. Please try again."
                return render_template('login.html', error_message=error_message)
        
        return render_template('login.html')

    # review submission page
    @app.route('/submit-review', methods=['POST'])
    def submit_review():
        entered_name = request.form['name']
        entered_review = request.form['review']

        if entered_name == "" or entered_review == "":
            return 'Entries cannot be empty'
        
        db = get_db()
        db.execute(
            "INSERT INTO reviews (name, review) VALUES (?, ?)",
            (entered_name, entered_review)
        )
        db.commit()
        return 'success'

    # the logout page
    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))

    from . import db
    db.init_app(app)

    return app