from flask_app import app #import app
from flask_app.controllers import controller_routes, controller_headshop #this line targets and imports all controller files

if __name__ == '__main__':
    app.run(debug=True)