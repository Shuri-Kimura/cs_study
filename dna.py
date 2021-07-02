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
    with open(sys.argv[1], "r") as f:
        reader = DictReader(f)
        dict_list = list(reader)
    with open(sys.argv[2], "r") as f:
        lines_ = f.readlines()
    lines = []
    for line in lines_:
        line = line.replace("\n","")
        lines.append(line)

    # For each STR, compute longest run of consecutive repeats in      sequence
    max_counts = []
    for i in range(1, len(reader.fieldnames)):
        STR = reader.fieldnames[i]
        max_counts.append(0)
    # Loop through sequence to find STR
        for j in range(len(lines)):
            STR_count = 0
            # If match found, start counting repeats
            if lines[j:(j + len(STR))] == STR:
                k = 0
                while lines[(j + k):(j + k + len(STR))] == STR:
                    STR_count += 1
                    k += len(STR)
                # If new maximum of repeats, update max_counts
                if STR_count > max_counts[i - 1]:
                    max_counts[i - 1] = STR_count

    for i in range(1, len(reader.fieldnames)):
        STR = reader.fieldnames[i]
        max_counts.append(0)
        # Loop through sequence to find STR
        for j in range(len(lines)):
            STR_count = 0
            # If match found, start counting repeats
            if lines[j:(j + len(STR))] == STR:
                k = 0
                while lines[(j + k):(j + k + len(STR))] == STR:
                    STR_count += 1
                    k += len(STR)
                # If new maximum of repeats, update max_counts
                if STR_count > max_counts[i - 1]:
                    max_counts[i - 1] = STR_count
    # Compare against data
    for i in range(len(dict_list)):
        matches = 0
        for j in range(1, len(reader.fieldnames)):
            if int(max_counts[j - 1]) == int(dict_list[i]  [reader.fieldnames[j]]):
                matches += 1
            if matches == (len(reader.fieldnames) - 1):
                print(dict_list[i]['name'])
                exit(0)
    print("No match")
    # print(search(list_name , dict_, line))



if __name__ == "__main__":
    main()