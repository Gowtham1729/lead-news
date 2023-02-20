# lead-news
Sample Django News Website

## Installation
```shell
git clone https://github.com/Gowtham1729/lead-news
cd lead_news
pip install virtualenv
virtualenv lead_news_venv
source lead_news_venv/bin/activate
pip install -r requirements.txt
```

```shell
# Check django installation
python -m django --version
# do db migrate
python manage.py migrate
# set the api key as environmental variable
export NEWS_API_KEY = ""
# fetch the news of preferred topic (set the topic with --topic tag)
python manage.py populate_news --topic japan
python manage.py runserver
```

```shell
# create superuser
py manage.py createsuperuser
```