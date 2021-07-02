import sys
import csv

def count_str(line, name):
    line = line.replace(name,"0")
    count = 1
    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1] and line[i] == "0":
            count += 1
    return count


def search(list_name, dict_, line):
    answer = []

    for name in list_name:
        num = str(count_str(line, name))
        answer.append(num)
    key = ":".join(answer)
    if key in dict_.keys():
        return dict_[key]
    else:
        # return answer
        return "No match"

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