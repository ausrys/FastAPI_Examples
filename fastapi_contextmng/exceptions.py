class WikipediaScrapeError(Exception):
    """Base class for Wikipedia scraping errors."""
    pass


class ArticleNotFoundError(WikipediaScrapeError):
    """Raised when Wikipedia article content is not found."""
    pass


class NoValidParagraphError(WikipediaScrapeError):
    """Raised when no valid paragraph is found in the article."""
    pass
