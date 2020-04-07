
from typing import Set, List
from datetime import datetime

class User:
    discordUserId: int = -1
    eveCharacterId: int = -1
    eveCharacterName: str = ""
    eveCorporationId: int = -1
    eveCorporationName: str = ""


    @staticmethod
    def from_json(js) -> object:
        u = User()

        return u

    def to_json(self) -> dict:
        return {

        }


class Channel:
    channelId: int = -1
    assignedCharacters: Set = set()


    @staticmethod
    def from_json(js) -> object:
        c = Channel()

        return c

    def to_json(self) -> dict:
        return {

        }
