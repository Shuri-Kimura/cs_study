
def cal_coleman(text):
    char_num = 0
    sentence = 0
    word_num = 0
    for i in range(0,len(text)): #char by char from text
        if ((text[i] >= 'a' and text[i] <= 'z') or (text[i] >= 'A' and text[i] <= 'Z')): #cal char_num
            char_num += 1
        if (text[i] == ' '): #cal word_num
            word_num += 1;
        if (text[i] == '.' or text[i] == '!' or text[i] == '?'): #cal sentence_num
            sentence += 1;
    word_num += 1
    ave = 100 / word_num #cal average og 100
    L = char_num * ave
    S = sentence * ave
    index = 0.0588 * L - 0.296 * S - 15.8
    # near integer
    result = int(index + 0.5);
    return result;

def main():
    # get input text
    text = input("Text: ")
    score = cal_coleman(text)
    if (score >= 16): #case score >= 16
        print("Grade 16+")
    elif (score < 1): # case score < 1
        print("Before Grade 1")
    else: # case 1 <= score < 16
        print("Grade "+ str(score))

if __name__ == "__main__":
    main()