import json
import os

HISTORY_DIR = "history"
FILE = os.path.join(HISTORY_DIR, "chat.json")


def save(user, bot):
    # Create history folder if it doesn't exist
    os.makedirs(HISTORY_DIR, exist_ok=True)

    # Load existing history if available
    if os.path.exists(FILE):
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = []
    else:
        data = []

    # Add new conversation
    data.append({
        "user": user,
        "bot": bot
    })

    # Save history
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load():
    if not os.path.exists(FILE):
        return []

    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []