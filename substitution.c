#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

void changer (string text, string key)
{
    for (int i = 0, n = strlen(text); i < n; i++) //char by char from key
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            int idx = text[i] - 97;
            char tmp = key[idx];
            text[i] = tolower(tmp);
        }
        else if (text[i] >= 'A' && text[i] <= 'Z')
        {
            int idx = text[i] - 65;
            text[i] = key[idx];
        }
    }
}


bool check_dup(string text, int size){
    bool flag = true;
    for (int i = 0; i < size-1; i++)
    {
        for (int j = 0; j < size; j++)
        {
            flag = flag && (text[i] != text[i+1]);
            if (flag == false){
                return false;
            }
        }
    }
    return true;
}


int main(int argc, string argv[])
{
    if (argc == 2)
    {
        int counter = 0;
        bool flag;
        int  n = strlen(argv[1]);
        for (int i = 0; i < n; i++) //char by char from key
        {
            if ((argv[1][i] >= 'a' && argv[1][i] <= 'z') || (argv[1][i] >= 'A' && argv[1][i] <= 'Z')) //check and transform char
            {
                argv[1][i] = toupper(argv[1][i]);
                counter += 1;
            }
            else
            {
                flag = false;
                break;
            }
        }
        if (counter == 26)
        {
            flag = true;
        }

        flag = flag && check_dup(argv[1], n);

        if (flag == true)
        {
            string text = get_string("plaintext: ");
            changer(text, argv[1]);
            printf("ciphertext: %s\n",text);
            return 0;
        }
        else
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
    }
    else
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
}