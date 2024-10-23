from flask import Flask, render_template

app = Flask(__name__)

@app.route("/mainpage")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/uslugi/terapevticheskaya_stomatologiya")
def usluga1():
    return render_template('usluga1.html')


@app.route("/uslugi/usluga_2")
def usluga2():
    return render_template('usluga2.html')


@app.route("/uslugi/usluga_3")
def usluga3():
    return render_template('usluga3.html')


@app.route("/uslugi")
def uslugi():
    return render_template('nashi_uslugi.html')


@app.route("/specialists")
def specialists():
    return render_template('specialists.html')


@app.route("/contactu")
def contactu():
    return render_template('contactu.html')

@app.route("/m")
def mversion():
    return render_template('mobileversion.html')


if __name__ == '__main__':
        app.run(debug=True)