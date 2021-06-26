
def main():
    height = -1
    # input number
    while (True):
        try:
            height = int(input("Height: "))
        except:
            continue
        if (height <= 8 and height >= 1):
            break

    # output block number:8
    if (height == 8):
        print("       #  #\n      ##  ##\n     ###  ###\n    ####  ####\n   #####  #####\n  ######  ######\n #######  #######\n########  ########")
    # output block number:7
    elif (height == 7):
        print("      #  #\n     ##  ##\n    ###  ###\n   ####  ####\n  #####  #####\n ######  ######\n#######  #######")
    # output block number:6
    elif (height == 6):
        print("     #  #\n    ##  ##\n   ###  ###\n  ####  ####\n #####  #####\n######  ######")
    # output block number:5
    elif (height == 5):
        print("    #  #\n   ##  ##\n  ###  ###\n ####  ####\n#####  #####")
    # output block number:4
    elif (height == 4):
        print("   #  #\n  ##  ##\n ###  ###\n####  ####")
    # output block number:3
    elif (height == 3):
        print("  #  #\n ##  ##\n###  ###")
    # output block number:2
    elif (height == 2):
        print(" #  #\n##  ##")
    # output block number:1
    else:
        print("#  #")


if __name__ == "__main__":
    main()