import sys
from csv import reader, DictReader

def count_str(line, name):
    line_ = line.replace(name,"0")
    # print(line)
    count = 0
    for i in range(0, len(line_) - 1):
        if line_[i] == line_[i + 1] and line_[i] == "0":
            count += 1
        if line_[i] != line_[i + 1] and line_[i - 1] == line_[i] and line_[i - 1] == "0":
            count += 1
    if count == 0 and "0" in line_:
        count = 1
    return count


def judge(answer, dict_):
    for k in dict_.keys():
        flag = 0
        for an, n in zip(answer, k.split(":")):
            if an >= int(n):
                flag += 1
        if flag >= len(answer):
            return dict_[k]
    return "No match"



    key = ":".join([str(n) for n in answer])
    if key in dict_.keys():
            return dict_[key]
    # answer_ = answer
    print(answer)
    # for i, ans in enumerate(answer):
    #     tmp = ans
    #     answer_[i] = ans - 1
    #     key = ":".join([str(n) for n in answer_])
    #     if key in dict_.keys():
    #         return dict_[key]
    #     answer_[i] = ans
    # return answer
    return "No match"


def search(list_name, dict_, line):
    answer = []

    for name in list_name:
        num = count_str(line, name)
        answer.append(num)
    return judge(answer, dict_)


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")
    # read the dna sequence from the file
    with open(argv[2]) as DNAfile:
        DNAreader = reader(DNAfile)
        for row in DNAreader:
            DNAlist = row
    #store in string
    DNA = DNAlist[0]
    #create a dictionary
    sequences = {}
    with open(argv[1]) as peoplefile:
        people = reader(peoplefile)
        for row in people:
            DNASequences = row
            DNASequences.pop(0)
            break

    for item in DNASequences:
        sequences[item] = 1

    # if repetitions of the values from sequence dictionary are found, count
    for key in sequences:
        l = len(key)
        tempMax = 0
        temp = 0
        for i in range(len(DNA)):
            # after having counted a sequence
            # skip at the end of it to avoid counting again
            while temp > 0:
                temp -= 1
                continue
    # if the segment of dna corresponds to the key &&
            #there is a repetition of it
            #increment counter
            if DNA[i: i + l] == key:
                while DNA[i - l: i] == DNA[i: i + l]:
                    temp += 1
                    i += l
    # compare the value to the previous longest sequence &&
                # if it is longer it becomes the new max
                if temp > tempMax:
                    tempMax = temp
    # store the longest sequences in the dictionary using the correspondent key
        sequences[key] += tempMax

    with open(argv[1], newline='') as peoplefile:
        people = DictReader(peoplefile)
        for person in people:
            match = 0
            # compares the sequences to every person and prints name
            # leave the program if there is a match
            for DNA in sequences:
                if sequences[DNA] == int(person[DNA]):
                    match += 1
            if match == len(sequences):
                print(person['name'])
                exit()
        #otherwise, no match
        print("No match")


if __name__ == "__main__":
    main()