import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

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


# Custom filter
app.jinja_env.filters["usd"] = usd
app.jinja_env.globals.update(usd=usd, lookup=lookup, int=int)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    cash = db.execute("SELECT cash FROM users WHERE id= ?", session["user_id"])[0]["cash"]

    transcations = db.execute("SELECT * FROM transcations WHERE user_id= ?", session["user_id"])
    if not transcations:
        return apology("you have no transcations")
    # (user_id, name, symbol, quantity, price)
    total = cash
    for trans in transcations:
        money = trans["quantity"] * trans["price"]
        total += money
    return render_template("index.html", transcations=transcations, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("There is no input1.")
        if int(request.form.get("shares")) <= 0:
            return apology("Share should be 1 or more.")
        quote = lookup(request.form.get("symbol").upper())
        if quote == None:
            return apology("No symbol in data.")
        money = int(request.form.get("shares")) * quote['price']
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        if money > cash:
            return apology("you don't have enough money.")
        db.execute("UPDATE users SET cash=cash - ? WHERE id= ?", money, session["user_id"]);

        cul_transcations = db.execute("SELECT quantity FROM transcations WHERE symbol = ? ", quote["symbol"])
        db.execute("INSERT INTO story (user_id, symbol, quantity, price, date) VALUES ( ?, ?, ?, ?, ?)", session["user_id"], quote["symbol"], int(request.form.get("shares")), quote['price'], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if not cul_transcations:
            db.execute("INSERT INTO transcations (user_id, name, symbol, quantity, price) VALUES (?, ?, ?, ?, ?)",session["user_id"], quote["name"], quote["symbol"], int(request.form.get("shares")), quote['price'])
        else:
            db.execute("UPDATE transcations SET quantity=quantity + ? WHERE symbol = ?", int(request.form.get("shares")), quote["symbol"]);
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    story = db.execute("SELECT * FROM story WHERE user_id= ? ", session["user_id"])
    if not story:
        return apology("you have no story")
    return render_template("history.html", story=story)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("There is no input.2")

        quote = lookup(request.form.get("symbol"))
        if quote == None:
            return apology("No symbol in data.")
        return render_template("quoted.html", quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if (not request.form.get("username")) or (not request.form.get("password")) or (not request.form.get("confirmation")):
            return apology("There is no input.3")

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("The password and the confirmation password are different.")

        usernames = db.execute("SELECT username FROM users WHERE username = ?", request.form.get("username"))
        if usernames:
            return apology("Already registered.", 200)
        else:
            password = generate_password_hash(request.form.get('password'))
            register_ = db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", request.form.get("username"), password)
            session["user_id"] = register_
            return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        if not request.form.get("symbol") or not request.form.get("shares"):
            return apology("There is no input.4")
        if int(request.form.get("shares")) <= 0:
                return apology("Share should be 1 or more.")

        have = db.execute("SELECT quantity FROM transcations WHERE symbol = ?", request.form.get("symbol"))
        print(have)
        if int(request.form.get("shares")) > have[0]['quantity']:
                return apology("They are not large enough.")
        quote = lookup(request.form.get("symbol"))
        if quote == None:
            return apology("You don't have this symbol.")
        money = int(request.form.get("shares")) * quote['price']
        db.execute("UPDATE users SET cash=cash+ ? WHERE id = ?", money, session["user_id"])
        add_transaction = db.execute("INSERT INTO story (user_id, symbol, quantity, price, date) VALUES ( ?, ?, ?, ?, ?)", session["user_id"], quote["symbol"], -int(request.form.get("shares")), quote['price'], datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        db.execute("UPDATE transcations SET quantity= quantity - ? WHERE symbol= ? ", int(request.form.get("shares")), quote["symbol"]);

        return redirect("/")

    else:
        aveil = db.execute("SELECT symbol FROM transcations")
        return render_template("sell.html", aveil = aveil)




def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
