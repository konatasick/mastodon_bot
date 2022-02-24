from datetime import datetime

from auto_post import *

if __name__ == "__main__":
    id = "StandUp_bot"
    now = datetime.now()  # 获取当前datetime
    hour = int(now.strftime("%H"))
    if hour > 12:
        hour -= 12
    text = f"{hour}点了，起来站一站走一走吧！"
    records = post_toot(text, id)
