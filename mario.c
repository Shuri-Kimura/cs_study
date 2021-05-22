#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    //input number
    while (true)
    {
        height = get_int("Height: ");
        if (height <= 8 && height >= 1)
        {
            break;
        }
    }
    //output block number:8
    if (height == 8)
    {
        printf("       #  #\n      ##  ##\n     ###  ###\n    ####  ####\n   #####  #####\n  ######  ######\n #######  #######\n########  ########\n");
    }
    //output block number:7
    else if (height == 7)
    {
        printf("      #  #\n     ##  ##\n    ###  ###\n   ####  ####\n  #####  #####\n ######  ######\n#######  #######\n");
    }
    //output block number:6
    else if (height == 6)
    {
        printf("     #  #\n    ##  ##\n   ###  ###\n  ####  ####\n #####  #####\n######  ######\n");
    }
    //output block number:5
    else if (height == 5)
    {
        printf("    #  #\n   ##  ##\n  ###  ###\n ####  ####\n#####  #####\n");
    }
    //output block number:4
    else if (height == 4)
    {
        printf("   #  #\n  ##  ##\n ###  ###\n####  ####\n");
    }
    //output block number:3
    else if (height == 3)
    {
        printf("  #  #\n ##  ##\n###  ###\n");
    }
    //output block number:2
    else if (height == 2)
    {
        printf(" #  #\n##  ##\n");
    }
    //output block number:1
    else
    {
        printf("#  #\n");
    }
}