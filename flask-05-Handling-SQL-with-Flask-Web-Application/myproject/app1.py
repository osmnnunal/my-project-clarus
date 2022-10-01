from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy   # https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#installation


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///email.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods=["GET","POST"])
def user_add():
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password=request.form.get("password")

        if request.form['submit_button']=='add-button':
            new_user = User(username=username, email=email,password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)


