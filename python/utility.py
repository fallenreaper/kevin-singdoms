import typing
from typing import List
from typing import Set
import datetime
import jwt
import base64
from config import CLIENT_ID, CLIENT_SECRET, CLIENT_URI, CLIENT_APP
import requests
import sys
import urllib                                                                                                                                                                                                                                                                                                                                                                                                                                               

def create_login_token(code_challenge, scope: List, state: str = CLIENT_APP) -> str:
    url = "https://login.eveonline.com/v2/oauth/authorize/"
    queryParams = {
        "response_type": "code",
        "redirect_uri": CLIENT_URI,
        "client_id": CLIENT_ID,
        "scope": ",".join(scope),
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "state": state
    }
    return url + '?' + urllib.parse.urlencode(queryParams)



def get_token(code, verifier):
    url = "https://login.eveonline.com/v2/oauth/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "login.eveonline.com"
    }
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": CLIENT_ID,
        "code_verifier": verifier
    }
    try:
        r = requests.post(url, headers=headers, data=payload).json()
    except:
        return None
    return r

def refresh_token(refresh_token):
    """Refresh Token with EveOnline"""
    url = "https://login.eveonline.com/v2/oauth/token"
    header_token = base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}").decode("UTF-8")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "login.eveonline.com",
        "Authorization": f"Basic {header_token}"
    }
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    try:
        r = requests.post(url, data=payload, headers=headers).json()
    except:
        return None
    return r

def get_character(character_id:int, token):
    """Private Character Information"""
    if not character_id or character_id < 0 or not token:
        return None
    url = f"https://esi.evetech.net/latest/characters/{character_id}/"
    headers = {
        "Authorization": f"Bearer {token}",
        "accept": "application/json"
    }
    try:
        r = requests.get(url, params=headers).json()
    except:
        return None
    return r

def get_corporation(corporation_id:int):
    """Public Corporation Information"""
    if not corporation_id or corporation_id < 0:
        return None
    url = f"https://esi.evetech.net/latest/corporation/{corporation_id}/"
    try:
        r = requests.get(url).json()
    except:
        return None
    return r

def get_moon_states(corporation_id, token):
    if not corporation_id or corporation_id < 0 or not token:
        return None
    url = f"https://esi.evetech.net/latest/corporation/{corporation_id}/mining/extractions/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    try:
        r = requests.get(url, headers=headers).json()
    except:
        return None
    return r