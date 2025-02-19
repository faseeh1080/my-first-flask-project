# My First Flask Project

## Setup

- Run `python3 -m venv .venv` for Linux and `py -3 -m venv .venv` for Windows to create a Python virtual environment named `.venv`
- Run `source .venv/bin/activate` or `. .venv/bin/activate` for Linux and `.venv\Scripts\activate` to activate the virtual environment in your terminal.
- If you are using VS Code, select the interpreter from the virtual environment.
- Run `pip install Flask` to install Flask. **Ensure the virtual environment is activated on your terminal beore working with the app.**

## How to Run the App

- Run: `flask --app flaskr run`
- Run with Debugging: `flask --app flaskr run --debug`

## Initialize the SQLite Database

- `flask --app flaskr init-db`

## More Information

- [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Flask Tutorial](https://flask.palletsprojects.com/en/stable/tutorial/)