from flask_app import app
#The DB "Books" is being imported from HERE
from flask_app.controllers import authors, books


if __name__ == "__main__":
    app.run(host="localhost", port=5555, debug=True)