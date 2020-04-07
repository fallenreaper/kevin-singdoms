
from datetime import datetime

class Structure:
    structure_id: int = -1
    corporation_id: int = -1
    structure_name: str = ""
    moon_id: int = -1
    moon_name: str = ""

    chunck_arrival_time: datetime = None
    extraction_start_time: datetime = None
    natural_decay_time: datetime = None

    @staticmethod
    def from_json(js):
        s = Structure()
        s.corporation_id = js["corporation_id"] if "corporation_id" in js else -1
        s.moon_id = js["moon_id"] if "moon_id" in js else -1
        s.moon_name = js["moon_name"] if "moon_name" in js else ""
        s.structure_id = js["structure_id"] if "structure_id" in js else -1
        s.structure_name = js["structure_name"] if "structure_name" in js else -1
        s.chunk_arrival_time = datetime.fromisoformat(js["chunk_arrival_time"]) if "chunk_arrival_time" in js else None
        s.extraction_start_time = datetime.fromisoformat(js["extraction_start_time"]) if "extraction_start_time" in js else None
        s.natural_decay_time = datetime.fromisoformat(js["natural_decay_time"]) if "natural_decay_time" in js else None
        return s

    def to_json(self):
        return {
            "moon_id": self.moon_id,
            "moon_name": self.moon_name,
            "corporation_id": self.corporation_id,
            "structure_id": self.structure_id,
            "structure_name": self.structure_name,
            "chunk_arrival_time": self.chunck_arrival_time.isoformat() if self.chunck_arrival_time is not None else None,
            "extraction_start_time": self.extraction_start_time.isoformat() if self.extraction_start_time is not None else None,
            "natural_decay_time": self.natural_decay_time.isoformat() if self.natural_decay_time is not None else None
        }
