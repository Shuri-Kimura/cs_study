#include <cs50.h>
#include <stdio.h>

int main(void){
    int height;
    while (true){
        height = get_int("Height: ");
        if (height <= 8 && height >= 1)break;
    }
    if (height == 8){
        printf("       #  #\n      ##  ##\n     ###  ###\n    ####  ####\n   #####  #####\n  ######  ######\n #######  #######\n########  ########\n");
    }else if(height == 7){
        printf("      #  #\n     ##  ##\n    ###  ###\n   ####  ####\n  #####  #####\n ######  ######\n#######  #######\n");
    }else if(height == 6){
        printf("     #  #\n    ##  ##\n   ###  ###\n  ####  ####\n #####  #####\n######  ######\n");
    }else if(height == 5){
        printf("    #  #\n   ##  ##\n  ###  ###\n ####  ####\n#####  #####\n");
    }else if(height == 4){
        printf("   #  #\n  ##  ##\n ###  ###\n####  ####\n");
    }else if(height == 3){
        printf("  #  #\n ##  ##\n###  ###\n");
    }else if(height == 2){
        printf(" #  #\n##  ##\n");
    }else{
        printf("#  #\n");
    }
}