from flask_app import app #import app
from flask_app.controllers import controller_routes, controller_headshop

if __name__ == '__main__':
    app.run(debug=True)