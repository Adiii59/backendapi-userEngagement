from flask import Flask

app = None
def create_app():
    app = Flask(__name__)
    app.app_context().push()
    return app

app = create_app()
if __name__ == "__main__":
    from api import *
    from database import *
    print("Running")
    app.run(debug = True)