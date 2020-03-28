from flask import Flask, request
from utility import get_token, create_login_token
from config import CODE_VERIFIER, CODE_CHALLENGE, DEBUG, FLASK_APP_URI, logger
import sys
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Why are you looking for me?"

@app.route("/callback")
def sso():
    code: str = request.args.get("code")
    r = get_token(code, CODE_VERIFIER)
    logger.debug(json.dumps({ "code": code }))
    # TODO Finish results from this, which will update or inject user into workflow
    pass

@app.route("/link")
def create_login_link():
    permissions = ["esi-industry.read_corporation_mining.v1"]
    link = create_login_token(CODE_CHALLENGE, permissions)
    anchor = f'<a href="{link}">Link</a>'
    return anchor if request.args.get("anchor", default=None) is not None else link

if __name__ == "__main__":
    port = sys.argv[1] if len(sys.argv) > 1 else 5000
    app.run(FLASK_APP_URI, port=port, debug=DEBUG)
    