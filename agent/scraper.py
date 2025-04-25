
import requests
from bs4 import BeautifulSoup
from newspaper import Article

def extract_main_content(url: str, timeout: int = 10) -> str:
    """
    Try BeautifulSoup first, fallback to newspaper3k if it fails.
    """
    try:
        # Primary method: requests + BeautifulSoup
        response = requests.get(url, timeout=timeout, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Clean up unwanted tags
        for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
            tag.decompose()

        # Extract main visible text
        lines = [line.strip() for line in soup.get_text(separator="\n").splitlines() if len(line.strip()) > 50]
        text = "\n\n".join(lines)

        # If text is too short, fallback
        if len(text.split()) < 100:
            raise ValueError("Too little content from BS4")

        return text

    except Exception as primary_error:
        # Fallback method: newspaper3k
        try:
            article = Article(url)
            article.download()
            article.parse()
            return article.text.strip()

        except Exception as fallback_error:
            return f"[Error fetching {url}]:\nPrimary error: {primary_error}\nFallback error: {fallback_error}"


