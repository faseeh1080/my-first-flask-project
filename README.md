# My First Flask Project

## Setup

1. Run `python3 -m venv .venv` for Linux and `py -3 -m venv .venv` for Windows to create a Python virtual environment named `.venv`
2. Run `source .venv/bin/activate` or `. .venv/bin/activate` for Linux and `.venv\Scripts\activate` to activate the virtual environment in your terminal.
3. If you are using VS Code, select the interpreter from the virtual environment.
4. Run `pip install Flask` to install Flask.
5. Run `pip install flask-cors` to install Flask-CORS. This website uses Flask-CORS to enable cross-origin resource sharing, allowing *faseehapps.github.io* to retrieve reviews from the database.
6. Run `flask --app flaskr init-db` to initialize the SQLite database.

## Run the App

- Run: `flask --app flaskr run`
- Run with Debugging: `flask --app flaskr run --debug`

## More Information

- [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)