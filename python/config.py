import urllib
import psycopg2
import logging
from code_validator import create_random_code_validation

URL = "108.4.242.167"
PORT = 8001

CLIENT_ID = '9bf13d93964f46b48a8d9ce4af95df83'
CLIENT_SECRET = 'CMNBKctAsYjkZtd4Kw4BPLUkd9dAcqHo7dxhEsiR'
HTTPS = False
callback = f"{URL}:{str(PORT)}" if PORT is not None else URL
CLIENT_URI = 'http{}://{}/callback'.format("s" if HTTPS else "", callback)
CLIENT_APP = 'sampleapp'
DEBUG = True
FLASK_APP_URI = "0.0.0.0"
try:
    CODE_CHALLENGE
    CODE_VERIFIER
except:
    CODE_CHALLENGE, CODE_VERIFIER = create_random_code_validation()
    
logging.basicConfig(filename="/var/log/moon_ore.log", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logger = logging.getLogger((__name__.split(".")[-1]))


sql_credentials = {
    "database": "postgres",
    "user": "postgres",
    "password": "moondbpassword",
    "host": "moondb"
}
db_con = None
db_cur = None
try:
    db_con = psycopg2.connect(**sql_credentials)
    db_cur = db_con.cursor()
except:
    print("Error Connecting to Database.")
    exit(1)