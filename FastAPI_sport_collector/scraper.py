from datetime import datetime, timedelta
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def _get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=chrome_options)


def scrape_sport_news():
    driver = _get_driver()
    driver.get("https://www.bbc.com/sport")

    time.sleep(2)  # Let content load

    news_data = []
    try:
        articles = driver.find_elements(By.CSS_SELECTOR, 'div[type="article"]')
        for article in articles[:10]:  # Limit to first 10

            try:
                # Get the first <a> tag inside the article div
                link_element = article.find_element(By.TAG_NAME, 'a')
                url = link_element.get_attribute("href")

                # Get the first <span> tag inside the article div for the title
                title_element = article.find_element(By.TAG_NAME, 'span')
                title = title_element.text.strip()

                if title and url:
                    news_data.append({
                        "title": title,
                        "content": "",  # Optional
                        "url": url,
                        "published_at": datetime.utcnow()
                    })

            except Exception as inner_err:
                print(f"Skipping article due to error: {inner_err}")

    finally:
        driver.quit()

    return news_data


def scrape_sport_events():
    # Simulate event data (BBC/ESPN don't have simple event list pages)
    return [{
        "name": "Football Match: Team A vs Team B",
        "location": "London",
        "date": datetime.utcnow() + timedelta(days=3),
        "description": "Premier League match",
        "url": "https://www.bbc.com/sport/football"
    }]
