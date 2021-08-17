import os
import requests
import urllib.parse
import copy
import random
import collections
import string
import pandas as pd


from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


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

def get_one(plans):
    plans.sort()
    #print(*plans, sep='\n')
    return plans[0]

def toExcel(shift_list, path):
    data = {}
    #print(len(shift_list))
    for item, i in zip(shift_list[0::2], range(1,63,2)):
        data[int(item[0][:2])] = {",".join(shift_list[i][1]): ",".join(item[1])}
    df = pd.concat({k: pd.Series(v) for k, v in data.items()}).reset_index()
    df.columns = ['日程', 'ランチ','ディナー']
    df.to_excel(path, sheet_name='シフト候補', index=False)

def toList(shift_list):
    result = [['日程', 'ランチ','ディナー',"",'ランチ必要人数','ディナー必要人数']]
    all = []
    for item, i in zip(shift_list[0::2], range(1,63,2)):
        all = all + shift_list[i][1] + item[1]
        result.append([int(item[0][:2]), ",".join(shift_list[i][1]), ",".join(item[1]), "", str(shift_list[i][1].count("_dummy_")), str(item[1].count("_dummy_"))])
    return result, all
