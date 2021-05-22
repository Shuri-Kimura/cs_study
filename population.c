#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int start_size, end_size;
    int years = 0;

    // TODO: Prompt for start size
    while (true)
    {
        start_size = get_int("type start size -> ");
        if (start_size >= 9)
        {
            break;
        }
        else
        {
            printf("Please type number of 9 or greater\n");
        }
    }

    // TODO: Prompt for end size
    while (true)
    {
        end_size = get_int("type end size -> ");
        if (end_size >= start_size)
        {
            break;
        }
        else
        {
            printf("Please type number of %i or greater\n",start_size);
        }
    }


    // TODO: Calculate number of years until we reach threshold
    while (true)
    {
        if (start_size >= end_size){
            break;
        }
        start_size += (start_size / 3) - (start_size / 4);
        years += 1;
    }

    // TODO: Print number of years
    printf("Years: %i\n",years);
}