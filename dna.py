import sys
import csv

def search(list_name, dict_, line):
    answer = []
    for name in list_name:
        num = str(line.count(name))
        answer.append(num)
    key = ":".join(answer)
    if key in dict_.keys():
        return dict_[key]
    else:
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