from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session security

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Save form data into session
        session['name'] = request.form['name']
        session['dojo_location'] = request.form['dojo_location']
        session['favorite_language'] = request.form['favorite_language']
        session['comments'] = request.form['comments']
        return redirect('/result')

    return render_template('form.html')

@app.route('/result')
def result():
    # Retrieve data from session
    name = session.get('name')
    dojo_location = session.get('dojo_location')
    favorite_language = session.get('favorite_language')
    comments = session.get('comments')

    return render_template('result.html', name=name, dojo_location=dojo_location, favorite_language=favorite_language, comments=comments)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)