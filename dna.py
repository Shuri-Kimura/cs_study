import sys
import csv

def count_str(line, name):
    line_ = line.replace(name,"0")
    # print(line)
    count = 0
    for i in range(0, len(line_) - 1):
        if line_[i] == line_[i + 1] and line_[i] == "0":
            count += 1
        if line_[i] != line_[i + 1] and line_[i - 1] == line_[i] and line_[i - 1] == "0":
            count += 1
    return count

# line = "0000tatatatatat"
# print(count_str(line, "0"))

def judge(answer, dict_):
    key = ":".join([str(n) for n in answer])
    if key in dict_.keys():
            return dict_[key]
    # answer_ = answer
    # print(answer)
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
    dict_ = {}
    with open(sys.argv[1], "r") as f:
        for row in csv.DictReader(f):
            list_val = []
            list_name = []
            for i,v in row.items():
                if i == "name":
                    name = v
                else:
                    list_val.append(v)
                    list_name.append(i)
            dict_[":".join(list_val)] = name
    with open(sys.argv[2], "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.replace("\n","")
    print(search(list_name , dict_, line))



if __name__ == "__main__":
    main()