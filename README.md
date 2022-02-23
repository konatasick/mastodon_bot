# 毛象bot

简单的mastodon bot，适合举一反三写出自己的bot，之后会增加更多内容。

一些基础代码（包括本README）来自[weibo2mast](https://github.com/casouri/weibo2mast.git)。


## 安装

确保Python 3已安装。

```shell
git clone https://github.com/konatasick/mastodon_bot.git
cd mastodon_bot
conda create -n mastodon python=3.8
conda activate mastodon
pip install -r requirements.txt
```

## 配置

1. 建立bot帐号
- 新建bot帐号，在设置里选`</> 开发`——`创建新应用`，权限只需要`read`和`write`，点`提交`。
- 成功以后点进新的app里，把`你的访问令牌`对应的一串字符复制下来。

2. 写入`token.json`

本bot支持多个毛象账号，具体方法如下：
- 新建`token.json`文件。以这个模板填充内容：
```json
[
  {
    "id": "Friday_bot",
    "url": "https://retirenow.top",
    "token": "your_token"
  },
  {
    "id": "StandUp_bot",
    "url": "https://retirenow.top",
    "token": "your_token"
  }    
]
```

`id` 是bot名，`url` 是站点网址，`token`就是`你的访问令牌`，代表毛象帐号。

注意，毛象的令牌相当于于密码，所以__不要上传或分享`token.json`__。

## 运行

```shell
python Friday_bot.py
```

## 定时运行

在crontab添加任务如下：
```shell
30 9    * * 5   root    /root/anaconda3/envs/mastodon/bin/python /home/mastodon/tool/mastodon_bot/Friday_bot.py >> /home/mastodon/tool/mastodon_bot/Friday_bot.log 2>&1
```