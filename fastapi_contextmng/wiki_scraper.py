import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from exceptions import ArticleNotFoundError, NoValidParagraphError


def get_first_5_sentences_from_wikipedia(query):
    options = webdriver.ChromeOptions()
    # Comment this out if you want to see the browser
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://wikipedia.org")

        wait = WebDriverWait(driver, 2)

        # Wait for the search input on main page
        search_input = wait.until(
            EC.presence_of_element_located((By.ID, "searchInput")))
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

        # Wait for article page to load
        wait.until(EC.presence_of_element_located((By.ID, "mw-content-text")))

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content = soup.find('div', {'class': 'mw-content-ltr'})

        if not content:
            raise ArticleNotFoundError(
                f"No Wikipedia article found for: {query}")

        # Extract meaningful paragraph
        paragraphs = content.find_all('p')
        full_text = None
        for para in paragraphs:
            text = para.get_text().strip()
            if len(text) > 100:
                full_text = text
                break

        if not full_text:
            raise NoValidParagraphError(
                f"No valid paragraph found in article: {query}")

        # Split and return first 5 sentences
        sentences = re.split(r'(?<=[.!?])\s+', full_text)
        return ' '.join(sentences[:5])

    finally:
        driver.quit()


if __name__ == "__main__":
    print(get_first_5_sentences_from_wikipedia("asfasfsadsad"))
