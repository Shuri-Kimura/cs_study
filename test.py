from cs50 import SQL

db = SQL("sqlite:///users.db")

def main():
    cash = db.execute("SELECT username, cash FROM users")
    print(cash)

if __name__ == '__main__':
    main()