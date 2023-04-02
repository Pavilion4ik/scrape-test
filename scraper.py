import os

import requests
from bs4 import BeautifulSoup
import telegram
import asyncio
from dotenv import load_dotenv


load_dotenv()


async def scrape_and_send(url, bot, chat_id, delay=15):
    previous_results = set()
    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        blog_post_cards = soup.find_all("div", class_="blog-post-card__info")

        for card in blog_post_cards:
            a_tags = card.find_all("a", class_="")
            for a_tag in a_tags:
                result = (a_tag.text, a_tag["href"])
                if result not in previous_results:
                    previous_results.add(result)
                    message = f"{a_tag.text}\n" \
                              f"https://www.tesmanian.com{a_tag['href']}"
                    await bot.send_message(chat_id=chat_id, text=message)
        else:
            print("No new results")

        await asyncio.sleep(delay)


if __name__ == "__main__":
    bot_token = os.getenv("BOT_TOKEN")
    telegram_bot = telegram.Bot(token=bot_token)
    chat_id_key = os.getenv("CHAT_ID")
    asyncio.run(
        scrape_and_send("https://www.tesmanian.com", telegram_bot, chat_id_key)
    )
