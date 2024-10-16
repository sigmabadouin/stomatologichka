from flask import Flask, render_template

app = Flask(__name__)

@app.route("/mainpage")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/terapevticheskaya_stomatologiya")
def usluga1():
    return render_template('usluga1.html')


@app.route("/usluga_2")
def usluga2():
    return render_template('usluga2.html')


@app.route("/usluga_3")
def usluga3():
    return render_template('usluga3.html')


@app.route("/nashi_uslugi")
def uslugi():
    return render_template('nashi_uslugi.html')


@app.route("/price_list")
def price_list():
    return render_template('price_list.html')


@app.route("/specialists")
def specialists():
    return render_template('specialists.html')


if __name__ == '__main__':
        app.run(debug=True)