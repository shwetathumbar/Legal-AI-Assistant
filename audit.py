import json
from datetime import datetime

def log_action(user, action):
    log = {
        "user": user,
        "action": action,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("data/audit_logs/audit.json", "a") as f:
        f.write(json.dumps(log) + "\n")
