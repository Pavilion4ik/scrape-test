# Tesmanian Scraper

This is a Python script that scrapes the latest articles from the Tesmanian website and sends them to a Telegram chat using a Telegram bot.

## Getting started
To run this script, you need to have Python 3.7 or higher installed on your machine.

## Installation
```shell
git clone https://github.com/your_username/tesmanian-scraper.git
cd tesla_scraping
pip install -r requirements.txt
```

Create a .env file in the project directory and set the following environment variables:
BOT_TOKEN: the token of your Telegram bot.
CHAT_ID: the ID of the Telegram chat where you want to receive the messages.
You can use this:

BOT_TOKEN=6070767688:AAFvS-UpJHScUQtknrIpJuj3bmVrxtkYcTo

CHAT_ID=444378023

Just paste it to bash command below.
```shell
echo "BOT_TOKEN=your_bot_token_here\nCHAT_ID=your_chat_id_here" > .env
```

## Usage
To run the script, simply execute the following command in your terminal:
```shell
python scraper.py
```
The script will start scraping the Tesmanian website and sending the latest articles to your Telegram chat. It will run indefinitely until you stop it manually (e.g. by pressing Ctrl + C).