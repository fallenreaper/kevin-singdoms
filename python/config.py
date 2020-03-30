import urllib
import psycopg2
import logging
from code_validator import create_random_code_validation

CLIENT_ID = ''
CLIENT_SECRET = ''
CLIENT_URI = urllib.parse.quote( 'https://localhost/callback' )
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
    "database": "MoonOreBot",
    "user": "postgres",
    "host": "127.0.0.1"
}
db_con = None
db_cur = None
try:
    db_con = psycopg2.connect(**sql_credentials)
    db_cur = db_con.cursor()
except:
    pass