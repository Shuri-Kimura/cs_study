#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

typedef uint8_t BYTE;
#define FILE_SIZE 8
#define BLOCK_SIZE 512

bool is_start_new_jpeg(BYTE buffer[])
{
    bool flag;
    flag = (buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0);
    return flag;
}

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: correct argument");
        return (1);
    }
    FILE * input_file = fopen(argv[1], "r");
    if (input_file == NULL)
    {
        printf("NO FILE!!");
        return (1);
    }

    BYTE buffer[BLOCK_SIZE];
    int file_index = 0;

    bool check_jpg = false;
    FILE * output_file;
    while (fread(buffer, BLOCK_SIZE, 1, input_file))
    {
        if (is_start_new_jpeg(buffer))
        {
            if (!check_jpg)
            {
                check_jpg = true;
            }
            else
            {
                fclose(output_file);
            }
            char file[FILE_SIZE];
            sprintf(file, "%03i.jpg", file_index++);
            output_file = fopen(file, "w");
            if (output_file == NULL)
            {
                return (1);
            }
            fwrite(buffer, BLOCK_SIZE, 1, output_file);
        }
        else if (check_jpg)
        {
            fwrite(buffer, BLOCK_SIZE, 1, output_file);
        }
    }
    fclose(output_file);
    fclose(input_file);

}