#include "helpers.h"
#include <stdio.h>
#include <math.h>
#include <string.h>

// unit8_t tosix(int L)
// {
//     char xfin[4], x0[2], x1[2];
//     /*16進数の計算*/
//     xv0 = (int)(d/(pow(16,0)))%16; //16^0の位
//     xv1 = (int)(d/(pow(16,1)))%16; //16^1の位

//     for(L=0; L<16; L=L+1)
//     {
//         if(xv0==L)
//         {
//           strncpy(x0,x+L,1); //x0に、配列xのL番めからの値を1つ分代入する。
//         }
//         if(xv1==L)
//         {
//           strncpy(x1,x+L,1); //x1に、配列xのL番めからの値を1つ分代入する。
//         }
//     }

//     snprintf(xfin,6,"0x%s%s",x1,x0); //xfinにx4～x0を連結させたものを代入する
//     return

// }

// Convert image to grayscale

void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            uint8_t average;
            average = ((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0) + 0.5;
            image[i][j].rgbtBlue = image[i][j].rgbtGreen = image[i][j].rgbtRed = average;
            // printf("%u\n",average);
            // printf("0x%u\n", Blue);
        }
    }
    return;
}

double check_max(double n)
{
    if (n > 255) return 255;
    return n;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            uint8_t sepiaRed, sepiaGreen, sepiaBlue;

            sepiaRed = check_max((0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue) + 0.5);
            sepiaGreen = check_max((0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue) + 0.5);
            sepiaBlue = check_max((0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue) + 0.5);
            // sepiaBlue = printf("%x\n",sepiaBlue);

            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtRed = sepiaRed;
            // printf("0x%u\n", Blue);
        }
    }
    return;
}


// void reverse(RGBTRIPLE image[g_size], int size)
// {
//     uint8_t tmp;
//     for (int i = 0; i < size / 2; i++)
//     {
//         tmp = image[i];
//         image[i] = image[size - i - 1];
//         image[size - i - 1] = tmp;
//     }
//     return;
// }

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    uint8_t tmp;
    for (int j = 0; j < height; j++)
    {
        for (int i = 0; i < width / 2; i++)
        {
            tmp = image[j][i].rgbtBlue;
            image[j][i].rgbtBlue = image[j][width - i - 1].rgbtBlue;
            image[j][width - i - 1].rgbtBlue = tmp;

            tmp = image[j][i].rgbtGreen;
            image[j][i].rgbtGreen = image[j][width - i - 1].rgbtGreen;
            image[j][width - i - 1].rgbtGreen = tmp;

            tmp = image[j][i].rgbtRed;
            image[j][i].rgbtRed = image[j][width - i - 1].rgbtRed;
            image[j][width - i - 1].rgbtRed = tmp;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE image_[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (i == 0 && j == 0)
            {
                image_[i][j].rgbtRed = ((image[i][j].rgbtRed + image[i + 1][j + 1].rgbtRed + image[i][j + 1].rgbtRed + image[i + 1][j].rgbtRed) / 4.0) + 0.5;
                image_[i][j].rgbtGreen = ((image[i][j].rgbtGreen + image[i + 1][j + 1].rgbtGreen + image[i][j + 1].rgbtGreen + image[i + 1][j].rgbtGreen) / 4.0) + 0.5;
                image_[i][j].rgbtBlue = ((image[i][j].rgbtBlue + image[i + 1][j + 1].rgbtBlue + image[i][j + 1].rgbtBlue + image[i + 1][j].rgbtBlue) / 4.0) + 0.5;
            }
            else if (i == 0 && j == width - 1)
            {
                image_[i][j].rgbtRed = ((image[i][j].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed + image[i + 1][j].rgbtRed) / 4.0) + 0.5;
                image_[i][j].rgbtGreen = ((image[i][j].rgbtGreen + image[i + 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i + 1][j].rgbtGreen) / 4.0) + 0.5;
                image_[i][j].rgbtBlue = ((image[i][j].rgbtBlue + image[i + 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i + 1][j].rgbtBlue) / 4.0) + 0.5;
            }
            else if (i == height - 1 && j == width - 1)
            {
                image_[i][j].rgbtRed = ((image[i][j].rgbtRed + image[i - 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed + image[i - 1][j].rgbtRed) / 4.0) + 0.5;
                image_[i][j].rgbtGreen = ((image[i][j].rgbtGreen + image[i - 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i - 1][j].rgbtGreen) / 4.0) + 0.5;
                image_[i][j].rgbtBlue = ((image[i][j].rgbtBlue + image[i - 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i - 1][j].rgbtBlue) / 4.0) + 0.5;
            }
            else if (i == height - 1 && j == 0)
            {
                image_[i][j].rgbtRed = ((image[i][j].rgbtRed + image[i - 1][j + 1].rgbtRed + image[i][j + 1].rgbtRed + image[i + 1][j].rgbtRed) / 4.0) + 0.5;
                image_[i][j].rgbtGreen = ((image[i][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen + image[i - 1][j + 1].rgbtGreen + image[i][j + 1].rgbtGreen) / 4.0) + 0.5;
                image_[i][j].rgbtBlue = ((image[i][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue + image[i - 1][j + 1].rgbtBlue + image[i][j + 1].rgbtBlue) / 4.0) + 0.5;
            }

            else if (i == 0)
            {
                image_[i][j].rgbtRed = ((image[i][j].rgbtRed + image[i][j - 1].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i + 1][j + 1].rgbtRed + image[i + 1][j].rgbtRed + image[i][j + 1].rgbtRed) / 6.0) + 0.5;
                image_[i][j].rgbtGreen = ((image[i][j].rgbtGreen + image[i][j - 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen + image[i + 1][j].rgbtGreen + image[i][j + 1].rgbtGreen) / 6.0) + 0.5;
                image_[i][j].rgbtBlue = ((image[i][j].rgbtBlue + image[i][j - 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue + image[i + 1][j].rgbtBlue + image[i][j + 1].rgbtBlue) / 6.0) + 0.5;
            }
            else if (j == 0)
            {
                image_[i][j].rgbtRed = ((image[i][j].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed + image[i + 1][j + 1].rgbtRed + image[i][j + 1].rgbtRed + image[i + 1][j].rgbtRed) / 6.0) + 0.5;
                image_[i][j].rgbtGreen = ((image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen + image[i][j + 1].rgbtGreen + image[i + 1][j].rgbtGreen) / 6.0) + 0.5;
                image_[i][j].rgbtBlue = ((image[i][j].rgbtBlue + image[i - 1][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue + image[i][j + 1].rgbtBlue + image[i + 1][j].rgbtBlue) / 6.0) + 0.5;
            }
            else if (j == width - 1)
            {
                image_[i][j].rgbtRed = ((image[i][j].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed + image[i + 1][j].rgbtRed + image[i + 1][j - 1].rgbtRed) / 6.0) + 0.5;
                image_[i][j].rgbtGreen = ((image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen + image[i - 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i + 1][j].rgbtGreen + image[i + 1][j - 1].rgbtGreen) / 6.0) + 0.5;
                image_[i][j].rgbtBlue = ((image[i][j].rgbtBlue + image[i - 1][j].rgbtBlue + image[i - 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i + 1][j].rgbtBlue + image[i + 1][j - 1].rgbtBlue) / 6.0) + 0.5;
            }
            else if (j == height - 1)
            {
                image_[i][j].rgbtRed = ((image[i][j].rgbtRed + image[i][j - 1].rgbtRed + image[i - 1][j - 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed + image[i][j + 1].rgbtRed) / 6.0) + 0.5;
                image_[i][j].rgbtGreen = ((image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen + image[i - 1][j - 1].rgbtGreen + image[i - 1][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen + image[i][j + 1].rgbtGreen) / 6.0) + 0.5;
                image_[i][j].rgbtBlue = ((image[i][j].rgbtBlue + image[i - 1][j].rgbtBlue + image[i - 1][j - 1].rgbtBlue + image[i - 1][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue + image[i][j + 1].rgbtBlue) / 6.0) + 0.5;
            }

            else
            {
                image_[i][j].rgbtRed = ((image[i][j].rgbtRed + image[i - 1][j - 1].rgbtRed + image[i][j - 1].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed + image[i + 1][j + 1].rgbtRed + image[i + 1][j].rgbtRed + image[i][j + 1].rgbtRed) / 9.0) + 0.5;
                image_[i][j].rgbtGreen = ((image[i][j].rgbtGreen + image[i - 1][j - 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen + image[i - 1][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen + image[i + 1][j].rgbtGreen + image[i][j + 1].rgbtGreen) / 9.0) + 0.5;
                image_[i][j].rgbtBlue = ((image[i][j].rgbtBlue + image[i - 1][j - 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue + image[i - 1][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue + image[i + 1][j].rgbtBlue + image[i][j + 1].rgbtBlue) / 9.0) + 0.5;

            }
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = image_[i][j].rgbtBlue;
            image[i][j].rgbtGreen = image_[i][j].rgbtGreen;
            image[i][j].rgbtRed = image_[i][j].rgbtRed;
            // printf("%u\n",average);
            // printf("0x%u\n", Blue);
        }
    }


    return;
}
