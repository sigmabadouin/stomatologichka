from flask import Flask, render_template

app = Flask(__name__)

@app.route("/mainpage")
@app.route("/")
def mainpage():
    return render_template('index.html')


@app.route("/usluga1")
def usluga1():
    return render_template('usluga1.html')

@app.route("/usluga2")
def usluga2():
    return render_template('usuluga2.html')

    

if __name__ == '__main__':
        app.run(debug=True)