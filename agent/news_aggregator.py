# Import requests module for making HTTP requests
import requests
# Import os module for accessing environment variables
import os

# Function to get the latest news articles on a given topic
def get_latest_news(topic: str, max_articles: int = 5):
    # Retrieve the API key from environment variables
    api_key = os.getenv("NEWSAPI_KEY")
    if not api_key:
        # Raise an error if the API key is not set
        raise EnvironmentError("NEWSAPI_KEY not set in environment.")

    # Define the URL for the news API
    url = "https://newsapi.org/v2/everything"
    # Set the parameters for the API request
    params = {
        "q": topic,
        "sortBy": "publishedAt",
        "pageSize": max_articles,
        "apiKey": api_key,
        "language": "en"
    }

    try:
        # Make a GET request to the news API
        response = requests.get(url, params=params)
        # Parse the JSON response
        data = response.json()

        # Extract the articles from the response data
        articles = data.get("articles", [])[:max_articles]
        return [
            {
                "title": a["title"],
                "url": a["url"],
                # Use description or content as a summary
                "summary": a.get("description", "") or a.get("content", "")[:300]
            }
            for a in articles
        ]
    except Exception as e:
        # Return an error message if an exception occurs
        return [{"error": str(e)}]
