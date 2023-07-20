from flask_app import app
#The DB "Books" is being imported from HERE
from flask_app.controllers import dojos, ninjas


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)