import urllib
from code_validator import create_code_validation
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
    CODE_CHALLENGE, CODE_VERIFIER = create_code_validation()