import copy
import random
import collections
import string


def judge_plan(plan, required, possible):
    for cell, workers in plan.items():
        if len(workers) != required[cell]:
            return False
        for worker in workers:
            if cell not in possible[worker]:
                return False

    worked = []
    for cell in plan.keys():
        for worker in plan[cell]:
            #print(plan[cell],worker)
            if worker in worked:
                return False
            if worker != "_dummy_":
                worked.append(worker)
    return True


def get_score(plan):
    total_work = 0
    worked = {}
    for cell, workers in plan.items():
        total_work += len(workers)
        for worker in workers:
            if '_dummy_' in worker:
                pass
            elif worker in worked:
                worked[worker] += 1
            else:
                worked[worker] = 1
    total_work /= len(worked)
    score = sum(v * v for k, v in worked.items()) / len(worked)
    if score - total_work**2 < 0:
        return total_work + (total_work**2 - score)**0.5
    return (score - total_work * total_work)**0.5


def get_day_shift(shift_days, workers, possible, required, dummy_counter):
    pre_shift = {}
    plan = {}
    num_dict = {}
    tmp = ""
    for shift_day in shift_days:
            pre_shift[shift_day] = []
            num_dict[shift_day] = 0
            for worker in workers:
                if shift_day in possible[worker]:
                    pre_shift[shift_day].append(worker)
                    num_dict[shift_day] += 1
            num_dict_sorted = sorted(num_dict.items(), key = lambda x : x[1])
            for i,tupple in enumerate(num_dict_sorted):
                shift_day_ = tupple[0]
                if i != 0:
                    pre_shift[shift_day_] = list(set(pre_shift[shift_day_]) - set(plan[tmp]))
                while len(pre_shift[shift_day_]) < required[shift_day_]:
                    pre_shift[shift_day_].append("_dummy_")
                    dummy_counter += 1
                    # if "dummy" not in possible:
                    #     possible["dummy"] = []
                    # possible["dummy"].append(shift_day_)
                plan[shift_day_] = random.sample(pre_shift[shift_day_], required[shift_day_])
                tmp = shift_day_
    return plan, dummy_counter


def make_shift(required, possible, not_same_group):
    shift_list = [k for k, v in required.items()]
    workers = [k for k, v in possible.items()]
    shifts = []
    for i in range(101):
        dummy_counter = 0
        plan = {}
        for shift_days in not_same_group:
            one_plan, dummy_counter = get_day_shift(shift_days, workers, possible, required, dummy_counter)
            #print(judge_plan(one_plan, required, possible))
            for k, i in one_plan.items():
                plan[k] = i
        score = get_score(plan)
        shifts.append((score, dummy_counter, list(sorted(plan.items(), key=lambda t: t[0]))))
    return shifts


def generate_data():
    each_require = {'ランチ': 3, 'ディナー': 4}
    required = {}
    not_same_group = []
    for day in range(1, 32):
        d = ('0' + str(day))[-2:]
        for k, v in each_require.items():
            required[d + k] = v
        not_same_group.append((('0' + str(day))[-2:]+list(each_require.keys())[0] ,('0' + str(day))[-2:]+list(each_require.keys())[1]))

    workers = ['Amy', 'Basil', 'Clara', 'Desmond', 'Ernest', 'Fanny', 'George',
               'Hector', 'Ida', 'James', 'Kate', 'Leo', 'Maud', 'Neville',
               'Olive', 'Prue', 'Quentin', 'Rhoda', 'Susan', 'Titus', 'Una',
               'Victor', 'Winnie', 'Xerxes', 'Yorick', 'Zillah']

    possible = {'Amy':['02ランチ', '07ランチ', '08ランチ', '10ランチ', '12ランチ', '13ランチ', '14ランチ', '15ランチ', '15ディナー', '18ランチ', '23ランチ', '25ディナー', '28ランチ', '30ランチ', '31ディナー'],
    'Basil':['01ランチ', '01ディナー', '03ディナー', '05ディナー', '06ディナー', '07ディナー', '16ディナー', '17ランチ', '20ディナー', '21ランチ', '23ディナー', '24ランチ'],
    'Clara':['01ランチ', '03ディナー', '04ディナー', '05ディナー', '10ランチ', '13ランチ', '17ディナー', '19ディナー', '20ランチ', '22ディナー', '23ディナー', '24ランチ', '30ランチ', '30ディナー', '31ディナー'],
    'Desmond':['03ディナー', '04ランチ', '08ランチ', '15ランチ', '17ランチ', '17ディナー', '18ランチ', '24ランチ', '25ディナー', '26ランチ'],
    'Ernest':['03ディナー', '08ランチ', '11ランチ', '15ランチ', '20ディナー', '21ランチ', '24ディナー', '27ランチ', '27ディナー', '28ランチ', '31ディナー'],
    'Fanny':['01ランチ', '01ディナー', '02ディナー', '05ランチ', '05ディナー', '08ランチ', '10ディナー', '11ランチ', '11ディナー', '16ディナー', '23ランチ', '23ディナー', '24ランチ', '24ディナー', '26ランチ', '26ディナー'],
    'George':['01ランチ', '02ランチ', '04ディナー', '05ランチ', '07ディナー', '10ランチ', '10ディナー', '11ランチ', '12ディナー', '15ディナー', '16ディナー', '19ディナー', '21ランチ', '21ディナー', '27ランチ', '27ディナー', '30ディナー', '31ディナー'],
    'Hector':['02ディナー', '03ディナー', '04ランチ', '05ディナー', '07ディナー', '11ディナー', '12ランチ', '14ランチ', '14ディナー', '15ランチ', '20ディナー', '23ディナー', '24ディナー', '25ディナー', '26ディナー', '27ランチ', '29ディナー', '31ランチ'],
    'Ida':['01ディナー', '02ランチ', '02ディナー', '05ランチ', '06ランチ', '07ディナー', '09ディナー', '10ランチ', '10ディナー', '12ディナー', '14ランチ', '16ランチ', '20ディナー', '21ランチ', '23ディナー', '24ディナー', '26ディナー', '27ランチ', '27ディナー', '28ランチ'],
    'James':['01ランチ', '02ランチ', '07ディナー', '08ディナー', '11ディナー', '14ディナー', '15ディナー', '17ディナー', '18ディナー', '19ランチ', '20ランチ', '20ディナー', '26ディナー', '27ランチ', '31ランチ'],
    'Kate':['01ランチ', '02ランチ', '03ランチ', '04ディナー', '07ランチ', '07ディナー', '08ランチ', '12ランチ', '15ランチ', '15ディナー', '16ランチ', '18ランチ', '22ランチ', '27ランチ', '28ディナー', '30ディナー'],
    'Leo':['05ランチ', '05ディナー', '09ランチ', '14ランチ', '15ディナー', '17ランチ', '19ディナー', '28ランチ', '29ランチ', '31ランチ'],
    'Maud':['01ディナー', '02ランチ', '04ディナー', '06ランチ', '07ランチ', '07ディナー', '08ディナー', '12ランチ', '14ランチ', '16ディナー', '17ランチ', '19ディナー', '20ランチ', '20ディナー', '21ランチ', '22ディナー', '25ランチ', '26ディナー', '30ランチ'],
    'Neville':['02ランチ', '04ディナー', '07ランチ', '12ランチ', '15ディナー', '19ランチ', '23ランチ', '25ディナー', '26ランチ', '27ディナー', '29ランチ', '29ディナー', '30ランチ'],
    'Olive': ['01ランチ', '02ディナー', '07ランチ', '09ランチ', '10ディナー', '12ランチ', '15ディナー', '18ディナー', '24ディナー', '27ランチ', '27ディナー', '30ランチ'],
    'Prue': ['05ランチ', '06ディナー', '10ランチ', '11ディナー', '12ディナー', '15ランチ', '16ランチ', '20ディナー', '22ランチ', '28ランチ', '30ランチ', '30ディナー'],
    'Quentin': ['01ディナー', '04ディナー', '09ランチ', '13ディナー', '15ランチ', '16ランチ', '17ディナー', '21ランチ', '23ランチ', '26ランチ', '28ディナー'],
    'Rhoda': ['02ランチ', '03ディナー', '04ディナー', '11ディナー', '12ランチ', '13ディナー', '14ディナー', '16ランチ', '20ランチ', '21ディナー', '23ディナー', '24ディナー', '25ディナー', '30ディナー'],
    'Susan': ['06ディナー', '11ディナー', '12ランチ', '14ディナー', '16ランチ', '19ランチ', '24ランチ', '27ランチ', '27ディナー'],
    'Titus': ['04ディナー', '09ランチ', '12ランチ', '18ランチ', '23ディナー', '26ランチ', '28ランチ', '29ランチ'],
    'Una': ['04ランチ', '04ディナー', '08ランチ', '08ディナー', '15ランチ', '15ディナー', '24ランチ', '24ディナー', '26ランチ', '29ディナー', '30ランチ'],
    'Victor': ['01ディナー', '04ディナー', '05ディナー', '08ランチ', '12ランチ', '15ランチ', '15ディナー', '16ランチ', '20ディナー', '28ランチ', '29ディナー', '30ディナー'],
    'Winnie': ['05ランチ', '06ランチ', '07ランチ', '10ランチ', '10ディナー', '11ランチ', '12ディナー', '13ディナー', '14ランチ', '14ディナー', '20ディナー', '21ディナー', '22ディナー', '25ディナー', '27ランチ', '29ディナー', '30ランチ'],
    'Xerxes': ['01ディナー', '13ディナー', '17ディナー', '21ディナー', '23ランチ', '25ランチ', '27ランチ', '28ランチ', '29ディナー'],
    'Yorick': ['02ディナー', '03ランチ', '08ディナー', '10ディナー', '13ランチ', '16ディナー', '17ディナー', '18ディナー', '19ランチ', '20ランチ', '21ディナー', '26ランチ', '27ランチ', '30ランチ'],
    'Zillah': ['03ディナー', '05ランチ', '08ディナー', '10ランチ', '10ディナー', '13ディナー', '16ランチ', '17ランチ', '19ランチ', '20ディナー', '21ディナー', '24ランチ', '25ディナー', '27ディナー', '29ディナー', '31ランチ']}
    return required, possible, not_same_group

def get_one(plans):
    plans.sort()
    #print(*plans, sep='\n')
    return plans[0]

def main():
    print(get_one(make_shift(*generate_data())))

if __name__ == '__main__':
    main()