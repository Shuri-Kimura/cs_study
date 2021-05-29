#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int cal_coleman(string text)
{
    int char_num = 0;
    int sentence = 0;
    int word_num = 0;
    for (int i = 0, n = strlen(text); i < n; i++) //char by char from text
    {
        if ((text[i] >= 'a' && text[i] <= 'z') || (text[i] >= 'A' && text[i] <= 'Z')) //cal char_num
        {
            char_num += 1;
        }
        if (text[i] == ' ') //cal word_num
        {
            word_num += 1;
        }
        if (text[i] == '.' || text[i] == '!' || text[i] == '?') //cal sentence_num
        {
            sentence += 1;
        }
    }
    word_num += 1;
    double ave = 100 / (double) word_num; //cal average og 100
    double L = char_num * ave;
    double S = sentence * ave;
    double index = 0.0588 * L - 0.296 * S - 15.8;
    //near integer
    int result = (int)(index + 0.5);
    return result;
}

int main()
{
    //get input text
    string text = get_string("Text: ");
    int score;
    score = cal_coleman(text);
    if (score >= 16) //case score >= 16
    {
        printf("Grade 16+\n");
    }
    else if (score < 1) //case score < 1
    {
        printf("Before Grade 1\n");
    }
    else //case 1 <= score < 16
    {
        printf("Grade %d\n", score);
    }
}