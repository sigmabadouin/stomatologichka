from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('mainpage.html')


@app.route('/uslugi')
def uslugi():
    return render_template('mainpage.html')

if __name__ == "__main__":
    app.run(debug=True)