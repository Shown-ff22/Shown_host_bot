import os
import threading
import time
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running perfectly! 🚀"

def keep_alive():
    url = "https://Shown_host_bot.onrender.com"
    while True:
        try:
            requests.get(url, timeout=15)
            print("Successfully pinged!")
        except Exception as e:
            print(f"Ping failed: {e}")
        time.sleep(300) # ৫ মিনিট পর পর পিং

if __name__ == "__main__":
    # ব্যাকগ্রাউন্ড থ্রেড
    t = threading.Thread(target=keep_alive)
    t.daemon = True
    t.start()
    
    # পোর্টের জন্য ওএস এনভায়রনমেন্ট চেক করা
    port = int(os.environ.get("PORT", 9460))
    app.run(host="0.0.0.0", port=port)