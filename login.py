import constant as c
from bs4 import BeautifulSoup


def login(session):
    print("started login...")

    r = session.get(c.LOGIN_URL)
    s = BeautifulSoup(r.text, 'lxml')
    csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')

    result = session.post(c.LOGIN_URL, data={
        "csrf_token": csrf_token,
        "username": c.USER_NAME,
        "password": c.PASSWORD
    })
    result.raise_for_status()

    print("finished login!\n")
