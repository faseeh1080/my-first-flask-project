# My First Flask Project

## Setup

- Run `python3 -m venv .venv` for Linux and `py -3 -m venv .venv` for Windows to create a Python virtual environment named `.venv`
- Run `source .venv/bin/activate` or `. .venv/bin/activate` for Linux and `.venv\Scripts\activate` to activate the virtual environment in your terminal.
- If you are using VS Code, select the interpreter from the virtual environment.
- Run `pip install Flask` to install Flask. **Ensure the virtual environment is activated on your terminal beore working with the app.**

## How to Run the App

To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is with the --app option. Type the command `$ flask --app hello run` in your terminal.

If the file is named `app.py` or `wsgi.py`, you don’t have to use `--app`.

## More Information

Check out the [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/) documentation.