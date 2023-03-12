from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/uppercase', methods=['POST'])
def uppercase():
    username = request.form['username']
    username_upper = username.upper()
    return render_template('uppercase.html', username=username_upper)

if __name__ == '__main__':
    app.run(debug=True)