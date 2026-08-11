from deadline_checker import get_urgent_deadlines
from notifier import send_notification

def main():
    urgent = get_urgent_deadlines()

    if not urgent:
        print("締切が近い課題はありません")
        return

    lines = [f"- {item['task']}: あと{item['days_left']}日" for item in urgent]
    message = "【締切が近い課題があります】\n" + "\n".join(lines)

    send_notification(message)
    print("通知を送信しました")

if __name__ == "__main__":
    main()