import sys

LOGIN_URL = "https://atcoder.jp/login"
LANGUAGE_ID = 4003  # 4003 of language id is c++
USER_NAME = ""
PASSWORD = ""

args = sys.argv
contest_name = "{}{nth:03d}".format(args[1].lower(), nth=int(args[2]))
task_name = "{}_{}".format(contest_name, args[3].lower())
source_code_path = args[4]


