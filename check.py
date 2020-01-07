import constant as c
from bs4 import BeautifulSoup
import sys
import os.path


def checking(session):
    print("started checking...\n")

    problem_url = "https://atcoder.jp/contests/{}/tasks/{}".format(c.contest_name, c.task_name)

    r = session.get(problem_url)
    soup = BeautifulSoup(r.text, 'lxml').find_all(class_="lang-ja")

    if not soup:
        print("<class=\"lang-ja\"> is missing")
        sys.exit()

    section = BeautifulSoup(str(soup[0]), 'lxml').find_all("section")

    prob_in = [BeautifulSoup(str(s), 'lxml').pre.string for s in [s for s in section if '入力例' in str(s)]]
    prob_out = [BeautifulSoup(str(s), 'lxml').pre.string for s in [s for s in section if '出力例' in str(s)]]

    if len(prob_in) != len(prob_out):
        print("Different number of sample cases")
        sys.exit()

    if not prob_in:
        print("nothing sample case")
        sys.exit()

    os.system("g++ -std=gnu++1y -O2 -o ./a.out " + c.source_code_path)

    for i in range(len(prob_in)):
        with open("./in.txt", mode='w') as f:
            f.write(prob_in[i])

        os.system("./a.out < in.txt > out.txt")

        with open("./out.txt", mode='r') as f:
            your_out = f.read()
            os.remove("./in.txt")
            os.remove("./out.txt")

            if your_out.split() != prob_out[i].split():
                print("WA")
                print("-input-")
                print(prob_in[i])
                print("-your output-")
                print(your_out)
                print("-true output-")
                print(prob_out[i])
                os.remove("./a.out")
                sys.exit()

    os.remove("./a.out")

    print("AC そのまさかだよ")
    print("\nfinished checking\n")
