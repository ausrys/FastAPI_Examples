# 🧠 Wikipedia Sentence Extractor API

This is a simple FastAPI application that uses **Selenium** and **BeautifulSoup** to search Wikipedia for a given query and return the first 5 sentences from the resulting article. Each search creates (or overwrites) a file named after the query, storing the result.

---

## 🚀 Features

- Uses Selenium with headless Chrome to interact with [https://wikipedia.org](https://wikipedia.org)
- Parses the article with BeautifulSoup to extract content
- Saves results in a file named after the query (e.g. `Artificial Intelligence.txt`)
- API returns information if the scraping and writting to the file was successful
- Returns appropriate error messages if the article or content is not found
- Runs both locally and in Docker

---

## 📦 Requirements

- Python 3.9+
- Google Chrome
- [Chromedriver](https://sites.google.com/chromium.org/driver/) (installed automatically via `webdriver-manager`)

---

## 🔧 Installation (Local)

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ausrys/FastAPI_Examples/fastapi_contextmng
   cd wiki-scraper
   python -m venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

## 🔧 Installation (Docker)

 ```bash
   git clone https://github.com/ausrys/FastAPI_Examples/fastapi_contextmng
   cd wiki-scraper
   docker build -t wiki-scraper .
   docker run --rm -p 8000:8000 --cap-add=SYS_ADMIN wiki-scraper
```

## 📬 API Usage

➤ Endpoint
POST /question/

➤ Request Body
{
  "text": "Artificial Intelligence"
}

➤ Response (Success)
{
    "result": "Data successfully scraped and written to the file"
}

➤ Response (Error)
{
  "detail": "Article not found."
}

{
  "detail": "No valid paragraph found in the article."
}

## 📁 Output Files

Each query creates a .txt file in the working directory, named after the search query. Example:

Artificial Intelligence.txt
Climate Change.txt

If a file already exists, it will be overwritten with the new result.

## 🛠 Tech Stack

- Python 3.9+
- FastAPI
- Selenium + Headless Chrome
- BeautifulSoup
- Docker
