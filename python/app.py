from flask import Flask, request
from utility import get_token, create_login_token, get_character, get_corporation, get_moon_states
from config import CODE_VERIFIER, CODE_CHALLENGE, DEBUG, FLASK_APP_URI, logger
import sys
import json
import base64


app = Flask(__name__)
DATA = {}
@app.route("/")
def home():
    return "Why are you looking for me?"

# @app.route("/login")
# def login():
#     return create_login_token(CODE_CHALLENGE))

@app.route("/callback")
def sso():
    global DATA
    code: str = request.args.get("code")
    state: str = request.args.get("state")
    r = get_token(code, CODE_VERIFIER)
    print(r)
    logger.info(json.dumps({ "code": code }))
    if r is None:
        return "No Token returned."
    try:
        r["access_token"]
    except:
        return "No Token"
    DATA["access_token"] = r["access_token"]
    _, payload, __ = r["access_token"].split(".")
    payload += '=' * (-len(payload) % 4)  # add padding
    DATA["info"] = json.loads(base64.b64decode(payload).decode("utf-8"))
    DATA["channel"], DATA["discordUser"] = state.split(":")
    return json.dumps(DATA) if DEBUG else "Thank You.  User Added."
    # TODO Finish results from this, which will update or inject user into workflow
    # pass

@app.route("/link")
def create_login_link():
    channelId = request.args.get("channelId") or None
    characterId = request.args.get("characterId") or None
    permissions = ["esi-industry.read_corporation_mining.v1"]
    link = create_login_token(CODE_CHALLENGE, permissions, state = f"{channelId}:{characterId}")
    anchor = f'<a href="{link}">Link</a>'
    return anchor if request.args.get("anchor", default=None) is not None else link

@app.route("/getCitadelInfo")
def getCitadelInfo():
    channelId = request.args.get("channelId") or None
    if channelId is None:
        return "[]"
    if str(channelId) != str(DATA["channel"] or ''):
        return "[]"
    characterID = DATA["info"]["sub"].split(":")[-1]
    token = DATA["access_token"]
    character = get_character(int(characterID), token)
    if character is None:
        return ""
    logger.info(f"fetched Character: {json.dumps(character)}")
    # return json.dumps(character)
    # try:
    #     corp = get_corporation(int(character["corporation_id"]))
    # except:
    #     return json.dumps(character)
    return json.dumps(get_moon_states(character["corporation_id"], token))

if __name__ == "__main__":
    port = sys.argv[1] if len(sys.argv) > 1 else 5000
    app.run(FLASK_APP_URI, port=port, debug=DEBUG)
    