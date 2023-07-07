# Import Flask to allow us to create our app
from flask import Flask, render_template, redirect, request
# Create a new instance of the Flask class called "app" 
app = Flask(__name__ )

# The "@" decorator associates this route with the function immediately following    
@app.route('/')          
def hello_world():
    # Return the string 'Hello World!' as a response
    return render_template('index.html')
# Ensure this file is being run directly and not from a different module  

@app.route('/users', methods=['POST','GET'])
def users():
    if (request.method == 'GET'):
        return "accessed thru gwet method"
    return render_template('success.html', tracking_num=123456)

if __name__=="__main__":       
    # Run the app in debug mode.
    app.run(debug=True)    