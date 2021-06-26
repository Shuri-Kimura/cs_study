
def main():
    # set number
    q_num = 0;
    d_num = 0;
    n_num = 0;
    p_num = 0;
    res = 0;
    # inpput change
    while (True):
        change = float(input("Change owed: "))
        if (change >= 0):
            break
    # from doll to cent
    cents = round(change * 100)
    res = cents

    # calculate quoter number
    if (cents >= 25):
        q_num = int(cents / 25)
        res = cents % 25

    # calculate dime number
    if (res >= 10):
        d_num = int(res / 10)
        res %= 10

    # calculate nickel number
    if (res >= 5):
        n_num = int(res / 5)
        res %= 5

    # calculate peny number
    p_num = res

    # output number
    print(q_num + d_num + n_num + p_num)

if __name__ == "__main__":
    main()