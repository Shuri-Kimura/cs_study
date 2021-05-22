#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    //set number
    float change;
    int q_num = 0;
    int d_num = 0;
    int n_num = 0;
    int p_num = 0;
    int res = 0;
    //inpput change
    while (true)
    {
        change = get_float("Change owed: ");
        if (change >= 0)
        {
            break;
        }
    }
    //from doll to cent
    int cents = round(change * 100);
    res = cents;

    //calculate quoter number
    if (cents >= 25)
    {
        q_num = cents / 25;
        res = cents % 25;
    }

    //calculate dime number
    if (res >= 10)
    {
        d_num = res / 10;
        res %= 10;
    }

    //calculate nickel number
    if (res >= 5)
    {
        n_num = res / 5;
        res %= 5;
    }

    //calculate peny number
    p_num = res;

    //output number
    printf("%i\n", q_num + d_num + n_num + p_num);
}