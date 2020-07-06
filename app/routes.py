from flask import render_template, flash, redirect, url_for
from app import app
from app.form import LoginForm


@app.route("/")
@app.route("/index")
def index():
     user = {"name":"Pham Viet Anh"}
     posts = [
          {
               "author": {"username":"anhpv"},
               "content": "Flask hoc rat de"
          },
          {
               "author": {"username":"chienthang"},
               "content": "Flask hoc rat kho"
          },
          {
               "author": {"username":"hieunm"},
               "content": "Flask hoc binhthuong"
          },
     ]
     return render_template('index.html', title="home", user=user, posts=posts)


@app.route("/login", methods = ['GET', 'POST'])
def login():
     form = LoginForm()
     # validate_on_submit : Xu ly moi su kien cho form
     if form.validate_on_submit():
          flash("Yeu cau dang nhap tu user {}, remmember_me {}".format(form.username.data,form.remember_me.data))
          return redirect(url_for('index'))
     return render_template("login.html", title="Sign In", form=form)
