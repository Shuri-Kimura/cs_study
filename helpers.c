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
            uint8_t Blue, Green, Red, average;
            Blue = image[i][j].rgbtBlue;
            Green = image[i][j].rgbtGreen;
            Red = image[i][j].rgbtRed;
            average = ((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0) + 0.5;
            image[i][j].rgbtBlue = image[i][j].rgbtGreen = image[i][j].rgbtRed = average;
            printf("%u\n",average);
            // printf("0x%u\n", Blue);
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            uint8_t Blue, Green, Red, sepiaRed, sepiaGreen, sepiaBlue;
            Blue = image[i][j].rgbtBlue;
            Green = image[i][j].rgbtGreen;
            Red = image[i][j].rgbtRed;

            sepiaRed = 0.393 * Red + 0.769 * Green + 0.189 * Blue;
            sepiaGreen = 0.349 * Red + 0.686 * Green + 0.168 * Blue;
            sepiaBlue = 0.272 * Red + 0.534 * Green + 0.131 * Blue;
            if (sepiaBlue > 255) sepiaBlue = 255;
            if (sepiaGreen > 255) sepiaGreen = 255;
            if (sepiaRed > 255) sepiaRed = 255;
            // sepiaBlue = printf("%x\n",sepiaBlue);
            // break;

            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtRed = sepiaRed;
            // printf("0x%u\n", Blue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
