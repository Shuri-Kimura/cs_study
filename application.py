import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import pandas as pd

from helpers import apology, login_required, toList, make_shift

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///users.db")



@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/inquire")
@login_required
def inquire():
    """Show portfolio of stocks"""
    possible = {}
    required = {}
    each_require = {'ランチ': 3, 'ディナー': 4}
    not_same_group = []
    for day in range(1, 32):
        d = ('0' + str(day))[-2:]
        for k, v in each_require.items():
            required[d + k] = v
        not_same_group.append((('0' + str(day))[-2:]+list(each_require.keys())[0] ,('0' + str(day))[-2:]+list(each_require.keys())[1]))

    data_list = db.execute("SELECT username, shift FROM personal")
    for data_dict in data_list:
        if data_dict["shift"] != None:
            possible[data_dict["username"]] = data_dict["shift"].split(",")
    shift, all = toList(make_shift(required, possible, not_same_group)[0][2])
    name_list = db.execute("SELECT username FROM personal")
    array1 = [["従業員名","出勤回数"]]
    for name_dict in name_list:
        name = name_dict["username"]
        array1.append([name, all.count(name)])

    return render_template("inquire.html", array=shift, array1=array1)


@app.route("/shift", methods=["GET", "POST"])
@login_required
def shift():
    if request.method == "POST":
        if "the_file" not in request.files:
            flash('ファイルがありません。')
            return redirect(request.url)
        file = request.files["the_file"]
        if file.filename == "":
            flash('ファイルがありません。')
            return redirect(request.url)
        filename = file.filename
        if filename.split(".")[1] != "xlsx":
            flash('ファイルの形式が正しくありません。')
            return redirect(request.url)
        df = pd.read_excel(file)
        if 3 != len(df.columns.tolist()) or 31 != len(df):
            flash('ファイルフォーマットを参考にしてください。')
            return redirect(request.url)

        shift_list = []
        df_ = df.isnull()
        for day, lan, din in zip(df["日程"], df_["ランチ"], df_["ディナー"]):
            day_ = ('0'+str(day))[-2:]
            if not lan:
                shift_list.append(day_ + "ランチ")
            if not din:
                shift_list.append(day_ + "ディナー")

        db.execute("UPDATE personal SET shift= ? WHERE id = ?", ",".join(shift_list), session["user_id"])
        return redirect("/")
    else:
        shift = db.execute("SELECT shift FROM personal WHERE id = ? ", session["user_id"])[0]["shift"]
        if not shift:
            text = "まだアップロードされていません。"
        else:
            text = "既にシフトが登録されています。"
        array = [["日程","ランチ", "ディナー"]]
        for day in range(1,32):
            array.append([day,"",""])
        return render_template("shift.html", text=text, array=array)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash('名前を入力してください。')
            return redirect(request.url)

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash('パスワードを入力してください。')
            return redirect(request.url)

        # Query database for username
        rows = db.execute("SELECT * FROM personal WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash('名前かパスワードが間違えています。')
            return redirect(request.url)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        print(rows[0]["id"])

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/delete", methods=["GET", "POST"])
def delete():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            flash('入力してください。')
            return redirect(request.url)

        name_list = db.execute("SELECT username FROM personal")
        flag = True
        for name_dict in name_list:
            if name_dict["username"] == request.form.get("username"):
                flag = False
        if flag:
            flash('名前が登録されていません。')
            return redirect(request.url)

        db.execute("DELETE FROM personal WHERE username = ?", request.form.get("username"))
        return redirect("/")
    else:
        return render_template("delete.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if (not request.form.get("username")) or (not request.form.get("password")) or (not request.form.get("confirmation")):
            flash('入力してください。')
            return redirect(request.url)

        elif request.form.get("password") != request.form.get("confirmation"):
            flash('パスワードと確認パスワードが一致しません。')
            return redirect(request.url)

        usernames = db.execute("SELECT username FROM personal WHERE username = ?", request.form.get("username"))
        if usernames:
            flash('その名前は既に使われています。')
            return redirect(request.url)
        else:
            password = generate_password_hash(request.form.get('password'))
            register_ = db.execute("INSERT INTO personal(username, hash) VALUES(?, ?)", request.form.get("username"), password)
            session["user_id"] = register_
            return redirect("/")
    else:
        return render_template("register.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
