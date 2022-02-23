from auto_post import post_toot

if __name__ == "__main__":
    id = "Friday_bot"
    text = "今天是周五！ :ablobcatattention: "
    # text = "今天还不是周五！ :ablobcatcry:  "
    records = post_toot(text, id)
