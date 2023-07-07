from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to the Playground!'

@app.route('/play/<int:x>')                     #Adjustment from /play to /play/num_goes_here
def play(x):
    return render_template('play.html', x=x)    #Redundant Assignment

if __name__ == '__main__':
    app.run()