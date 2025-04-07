import requests
import schedule
import time

def get_daily_power_word():
    """ZenQuotes APIから名言を取得する関数"""
    url = "https://zenquotes.io/api/today"
    response = requests.get(url)
    
    if response.status_code == 200:
        # JSONデータを取得
        data = response.json()
        if data:
            quote = data[0]['q']
            author = data[0]['a']
            return f"今日のパワーワード: \"{quote}\" - {author}"
        else:
            return "今日は名言が取得できませんでした。"
    else:
        return "APIの呼び出しに失敗しました。"

def show_power_word():
    """毎朝7時に名言を表示する関数"""
    print(get_daily_power_word())

# 毎日7時に名言を表示
schedule.every().day.at("07:00").do(show_power_word)

print("スクリプトが開始されました。毎朝7時に名言を表示します。")

# スケジュールの実行
while True:
    schedule.run_pending()  # 実行すべきタスクを待機して実行
    time.sleep(60)  # 1分ごとに次のタスクがあるか確認

