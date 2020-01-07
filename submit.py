import constant as c
from bs4 import BeautifulSoup
import sys
import os


def submission(session):
    print("started submission...")

    if os.path.exists(c.source_code_path):
        f = open(c.source_code_path)
        source_code = f.read()
        f.close()
    else:
        print("source code is not exist")
        sys.exit()

    url_for_submission = "https://atcoder.jp/contests/{}/submit".format(c.contest_name)

    atcoder_jp = session.get(url_for_submission)
    atcoder_jp.raise_for_status()

    csrf_token = BeautifulSoup(atcoder_jp.text, 'lxml').find(attrs={'name': 'csrf_token'}).get('value')

    result = session.post(url_for_submission, data={
        "data.TaskScreenName": c.task_name,
        "csrf_token": csrf_token,
        "data.LanguageId": c.LANGUAGE_ID,
        "sourceCode": source_code
    })

    result.raise_for_status()

    print("finished submission!\n")
