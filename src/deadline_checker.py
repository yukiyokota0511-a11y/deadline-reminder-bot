import json
from datetime import date

def get_urgent_deadlines():
    with open("config/deadlines.json", "r", encoding="utf-8") as f:
        deadlines = json.load(f)

    today = date.today()
    urgent = []

    for item in deadlines:
        due = date.fromisoformat(item["due_date"])
        days_left = (due - today).days
        if days_left <= 3:
            urgent.append({"task": item["task"], "days_left": days_left})

    return urgent

if __name__ == "__main__":
    for item in get_urgent_deadlines():
        print(f"{item['task']}: あと{item['days_left']}日")