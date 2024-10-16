from flask import Flask, render_template

app = Flask(__name__)

@app.route("/mainpage")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/usluga1")
def usluga1():
    return render_template('usluga1.html')

@app.route("/usluga2")
def usluga2():
    return render_template('usluga2.html')

@app.route("/usluga3")
def usluga3():
    return render_template('usluga3.html')

if __name__ == '__main__':
        app.run(debug=True)