import login
import check
import submit
import requests

print("\n ---- running app... ---- \n")

session = requests.session()

login.login(session)

check.checking(session)

submit.submission(session)

print(" ---- finished! ----")
