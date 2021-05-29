#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

void changer(string text, string key) //change from char to key
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


bool check_dup(string text, int size) //check duplication
{
    bool flag = true;
    for (int i = 0; i < size - 1; i++)
    {
        flag = flag && (text[i] != text[i+1]);
        if (flag == false)
        {
            return false;
        }
    }
    return true;
}

void selectionSort(string data, int left, int right) //sort alphabet
{
    int start;
    int i;
    char min;
    int i_min;
    char tmp;

    /* データ数が１の場合はソート済みなのでソート終了 */
    if (left == right)
    {
        return;
    }

    /* ソート範囲（開始点）の初期化 */
    start = left;

    /* ソート範囲を狭めながらソート処理 */
    for (start = left; start < right; start++)
    {

        /* ひとまずソート範囲の先頭を最小値とみなす */
        i_min = start;
        min = data[i_min];

        /* ソート範囲の中から最小値を探索 */
        for (i = start; i <= right; i++)
        {
            if (min > data[i])
            {
                /* 最小値とその値を持つインデックスを更新 */
                min = data[i];
                i_min = i;
            }
        }

        if (start != i_min)
        {

            /* ソート範囲の先頭と最小値を交換 */
            tmp = data[start];
            data[start] = data[i_min];
            data[i_min] = tmp;
        }
    }
}


int main(int argc, string argv[])
{
    if (argc == 2)
    {
        int counter = 0;
        bool flag;
        int  n = strlen(argv[1]);
        char check_key[n];
        for (int i = 0; i < n; i++) //char by char from key
        {
            if ((argv[1][i] >= 'a' && argv[1][i] <= 'z') || (argv[1][i] >= 'A' && argv[1][i] <= 'Z')) //check and transform char
            {
                argv[1][i] = toupper(argv[1][i]);
                check_key[i] = argv[1][i];
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


        selectionSort(check_key, 0, n - 1); //check_key sort
        flag = flag && check_dup(check_key, n);

        if (flag == true)
        {
            string text = get_string("plaintext: ");
            changer(text, argv[1]);
            printf("ciphertext: %s\n", text);
            return 0;
        }
        else //key error
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
    }
    else //argument error
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
}