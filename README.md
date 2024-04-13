WIP: epsa-webapp-captcha-bypass
---

[dev bot](https://t.me/epsa_webapp_bypass_dev_bot)


### Local setup
```shell
$ git clone git@github.com:epsilion-war-mmorpg/epsa-webapp-captcha-bypass.git
$ cd epsa-webapp-captcha-bypass
$ python3.12 -m venv venv
$ source venv/bin/activate
$ pip install -U --no-cache-dir poetry pip setuptools
$ poetry install
```


### Run webapp local
```shell
$ flask --app webapp run
$ ngrok http 80
```


### Run bot local
```shell
$ python -m bot
```