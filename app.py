from flask import Flask, url_for, render_template, redirect, request,session
from flask_session import Session
import flask_settings
from lantu import blue

app = Flask(__name__)
app.config.from_object(flask_settings.FlaskSet)
Session(app)
app.register_blueprint(blue.bp)

@app.route('/index', methods=["GET","POST"],endpoint="helloworld", strict_slashes=True,)
def index():
    # print(url_for("hello_world"))
    # return 'Hello World!'
    # return render_template('index.html')
    # request.form
    return redirect("/login")

@app.route('/login', methods=["GET","POST"])
def login():
    session["user"]=123123
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

