import json
from datetime import datetime
from typing import Dict, Any


class LoggerNode:
    def __init__(self, log_path: str):
        self.log_path = log_path

    def log(self, event_type: str, payload: Dict[str, Any]):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "payload": payload,
        }

        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
