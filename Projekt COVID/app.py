from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Email %r>' % self.email

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    first_name = db.Column(db.String(70), nullable=False)
    last_name = db.Column(db.String(90), nullable=False)
    city = db.Column(db.String(70), nullable=False)
    goraczka = db.Column(db.Boolean)
    suchy_kaszel = db.Column(db.Boolean)
    nudnosci = db.Column(db.Boolean)
    bol_miesni = db.Column(db.Boolean)
    katar = db.Column(db.Boolean)
    dreszcze = db.Column(db.Boolean)
    agree_data = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.first_name


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/formularz', methods=["POST", "GET"])
def formularz():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        city = request.form.get("city")
        goraczka = request.form.get("goraczka")
        suchy_kaszel = request.form.get("suchy_kaszel")
        nudnosci = request.form.get("nudnosci")
        bol_miesni = request.form.get("bol_miesni")
        katar = request.form.get("katar")
        dreszcze = request.form.get("dreszcze")
        agree_data = request.form.get("agree_data")
        if not email or not password or not first_name or not last_name or not city or not agree_data:
            error = "Proszę uzupełnić i zatwierdzić wszystkie dane."
            return render_template("forms.html",
                                   error=error,
                                   email=email,
                                   password=password,
                                   first_name=first_name,
                                   last_name=last_name,
                                   city=city,
                                   goraczka=goraczka,
                                   suchy_kaszel=suchy_kaszel,
                                   nudnosci=nudnosci,
                                   bol_miesni=bol_miesni,
                                   katar=katar,
                                   dreszcze=dreszcze)


    return render_template("forms.html")


@app.route('/info')
def informacje():
    return render_template("info.html")

@app.route('/login')
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
