
from typing import Set, List
from datetime import datetime

class User:
    # eveCorporationId: int = -1
    # eveCorporationName: str = ""
    character_id: int = -1
    character_name: str = ""
    refresh_token: str = ""
    date_created: datetime = None
    last_updated: datetime = None
    token_expires: datetime = None
    access_token: str = ""
    discord_user_id: int = -1
    
    @staticmethod
    def from_json(js) -> object:
        u = User()
        u.character_id = -1 if "character_id" not in js else js["character_id"]
        u.character_name = "" if "character_name" not in js else js["character_name"]
        u.discord_user_id = -1 if "discord_user_id" not in js else js["discord_user_id"]
        u.access_token = "" if "access_token" not in js else js["access_token"]
        u.refresh_token = "" if "refresh_token" not in js else js["refresh_token"]
        u.date_created = None if "date_created" not in js else js["date_created"]
        u.last_updated = None if "last_updated" not in js else js["last_updated"]
        u.token_expires = None if "token_expires" not in js else js["token_expires"]
        return u

    def to_json(self) -> dict:
        return {
            "character_id": self.character_id or -1,
            "character_name": self.character_name or "",
            "discord_user_id": self.discord_user_id or -1,
            "access_token": self.access_token or "",
            "refresh_token": self.refresh_token or "",
            "date_created": self.date_created or None,
            "last_updated": self.last_updated or None,
            "token_expires": self.token_expires or None
        }


# class Channel:
#     channelId: int = -1
#     assignedCharacters: Set = set()


#     @staticmethod
#     def from_json(js) -> object:
#         c = Channel()

#         return c

#     def to_json(self) -> dict:
#         return {

#         }
