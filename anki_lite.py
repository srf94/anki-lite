import math
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td

FILENAME = "data.csv"
BACKUP_FOLDER = "backups"
COLS = ["q", "a", "last", "interval", "incorrect", "total"]
REVIEW_FREQ = 2
META_FILENAME = "{}/meta.csv".format(BACKUP_FOLDER)

def load_data():
    try:
        return pd.read_csv(FILENAME)
    except:
        return pd.DataFrame(columns=COLS)

def save_data(df):
    backup = "{}/{}.csv".format(BACKUP_FOLDER, dt.now().strftime("%Y%m%d_%H%M%S"))
    df.to_csv(backup, index=False)
    df.to_csv(FILENAME, index=False)

def save_meta(td):
    cols = ["date", "time_taken"] 
    try:
        df = pd.read_csv(META_FILENAME)
    except:
        df = pd.DataFrame(columns=cols)
    time_taken = int(td.total_seconds())
    df = df.append(pd.DataFrame([[dt.now(), time_taken]], columns=cols))
    df.to_csv(META_FILENAME, index=False)

def y_n_input():
    while True:
        i = input("")
        if i.lower() == "y":
            return True
        elif i.lower() == "n":
            return False
        else:
            print("Input not understood!")

def add_questions(df):
    while True:
        print("Add new question? (y/n)")
        if not y_n_input():
            return df
        df2 = add_question(df)
        print("Happy with question? (y/n)")
        i = y_n_input()
        if i:
            print("Question added")
            df = df2
        else:
            print("Question not added")

def add_question(df):
    print("Question:")
    q = input("")
    print("Answer:")
    a = input("")
    print
    print("Question: " + q)
    print("Answer: " + a)
    df = df.append(pd.DataFrame([[q, a, dt.now(), 0, 0, 0]], columns=COLS))
    return df

def due(dt_now, last, interval):
    return True
    if interval == 0:
        return True
    if interval == 1 and last + td(minutes=5) < dt_now:
        return True
    if interval == 2 and last.date() != dt_now.date():
        return True
    diff = (dt_now.date() - last.date()).days
    if diff < 1:
        return False
    if math.log(diff, REVIEW_FREQ) > interval - 2:
        return True
    return False

def project_due():
    "Testing"
    dt_now = dt(2020, 8, 2)
    last = dt(2020, 8, 1)
    interval = 1
    wait = 0
    for i in range(1000):
        # print(dt_now, last, interval)
        if due(dt_now, last, interval):
            interval += 1
            last = dt_now
            print("Wait: {}".format(wait))
            wait = 0
        wait += 1
        dt_now += td(days=1)

def review(df):
    dt_now = dt.now()
    out = []
    for r in df.to_dict(orient='records'):
        if due(dt_now, r["last"], r["interval"]):
            r = review_question(r)
        out.append(r)
    return pd.DataFrame.from_records(out) 

def review_question(r):
    print(r["q"])
    i = input("...")
    print(r["a"])
    print("(enter=correct, other=wrong)")
    i = input("")
    r["last"] = dt.now()
    r["total"] += 1
    if i == "":
        r["interval"] += 1 
    else:
        r["incorrect"] += 1
    return r

def main():
    ts = dt.now()
    df = load_data()
    df = add_questions(df)
    df = review(df)
    save_data(df)
    te = dt.now()
    save_meta(te - ts)

main()

