import feedparser
from telegram import Bot
import schedule
import time
import os

# Lấy token và chat ID từ biến môi trường Railway
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

# Nguồn RSS
RSS_FEEDS = {
    # Đời sống xã hội
    "VnExpress - Đời sống": "https://vnexpress.net/rss/doi-song.rss",
    "VnExpress - Xã hội": "https://vnexpress.net/rss/xa-hoi.rss",

    # Công nghệ & sản phẩm
    "VnExpress - Công nghệ": "https://vnexpress.net/rss/so-hoa.rss",
    "Báo Mới - Công nghệ": "https://www.baomoi.com/rss/cong-nghe.rss",

    # Pháp luật
    "VnExpress - Pháp luật": "https://vnexpress.net/rss/phap-luat.rss",
    "Báo Pháp Luật": "https://baophapluat.vn/rss/home.rss"
}

# Từ khóa lọc tin công nghệ
TECH_KEYWORDS = [
    "AI", "trí tuệ nhân tạo", "machine learning", "deep learning",
    "macOS", "Macbook", "Apple", "iPhone",
    "sản phẩm", "ra mắt", "công nghệ mới"
]

def get_news():
    messages = []
    for name, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        if "công nghệ" in name.lower():
            # Lọc tin có từ khóa
            articles = [
                f"{entry.title}\n{entry.link}"
                for entry in feed.entries
                if any(keyword.lower() in entry.title.lower() for keyword in TECH_KEYWORDS)
            ]
        else:
            # Giữ nguyên tin cho các mục khác
            articles = [f"{entry.title}\n{entry.link}" for entry in feed.entries]
        
        if articles:
            top_articles = articles[:5]  # Giới hạn 5 tin
            messages.append(f"📰 {name}:\n" + "\n\n".join(top_articles))
    return "\n\n".join(messages)

def send_news():
    news = get_news()
    bot.send_message(chat_id=CHAT_ID, text=news)

# --- Gửi tin ngay khi start bot (test) ---
send_news()

# --- Lên lịch gửi 8h sáng hàng ngày ---
schedule.every().day.at("08:00").do(send_news)

print("Bot đang chạy...")
while True:
    schedule.run_pending()
    time.sleep(1)

