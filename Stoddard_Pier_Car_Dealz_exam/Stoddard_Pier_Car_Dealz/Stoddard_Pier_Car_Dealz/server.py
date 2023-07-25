from flask_app import app

from flask_app.controllers import controller_sellers
from flask_app.controllers import controller_deals

if __name__=='__main__':
    app.run(debug=True)