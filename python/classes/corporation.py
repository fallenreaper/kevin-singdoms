
from typing import Set, List
# TODO: This is not implemented.
class Corportation:
    linkedCharacters: Set = set()
    corportationId: int = -1
    corporationName: str = ""

    structures: List = []

    @staticmethod
    def from_json(js):
        corp = Corportation()

        return corp

    def to_json(self):
        return {

        }
