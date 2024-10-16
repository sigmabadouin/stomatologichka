from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/pultimos')
def pultimos():
    return render_template('about_us.html')

if __name__ == "__main__":
    app.run(debug=True)