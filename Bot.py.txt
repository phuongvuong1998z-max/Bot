import feedparser
from telegram import Bot
import schedule
import time

# Token bot Telegram của bạn
TOKEN = YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID = YOUR_CHAT_ID

bot = Bot(token=TOKEN)

# Nguồn RSS
RSS_FEEDS = {
    # Đời sống xã hội
    VnExpress - Đời sống httpsvnexpress.netrssdoi-song.rss,
    VnExpress - Xã hội httpsvnexpress.netrssxa-hoi.rss,

    # Công nghệ & sản phẩm
    VnExpress - Công nghệ httpsvnexpress.netrssso-hoa.rss,
    Báo Mới - Công nghệ httpswww.baomoi.comrsscong-nghe.rss,

    # Pháp luật
    VnExpress - Pháp luật httpsvnexpress.netrssphap-luat.rss,
    Báo Pháp Luật httpsbaophapluat.vnrsshome.rss
}

# Từ khóa lọc tin công nghệ
TECH_KEYWORDS = [AI, trí tuệ nhân tạo, machine learning, deep learning,
                 macOS, Macbook, Apple, iPhone, sản phẩm, ra mắt, công nghệ mới]

def get_news()
    messages = []
    for name, url in RSS_FEEDS.items()
        feed = feedparser.parse(url)
        if công nghệ in name.lower()
            # Lọc chỉ giữ tin có từ khóa
            articles = [
                f{entry.title}n{entry.link}
                for entry in feed.entries
                if any(keyword.lower() in entry.title.lower() for keyword in TECH_KEYWORDS)
            ]
        else
            # Giữ nguyên tin cho các mục khác
            articles = [f{entry.title}n{entry.link} for entry in feed.entries]
        
        if articles
            top_articles = articles[5]  # Giới hạn 5 tin
            messages.append(f📰 {name}n + nn.join(top_articles))
    return nn.join(messages)

def send_news()
    news = get_news()
    bot.send_message(chat_id=CHAT_ID, text=news)

# Lịch gửi 8h sáng hàng ngày
schedule.every().day.at(0800).do(send_news)

print(Bot đang chạy...)
while True
    schedule.run_pending()
    time.sleep(1)
