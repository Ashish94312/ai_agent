# agent/search_tool.py

# Import os module for accessing environment variables
import os
# Import GoogleSearch class from serpapi module for performing web searches
from serpapi import GoogleSearch
# Import additional modules for ranking
from agent.content_analyzer import analyze_content
from agent.scraper import extract_main_content

# Function to search the web using a query with improved relevance ranking and pagination
def search_web(query: str, num_results: int = 5, max_pages: int = 2):
    # Retrieve the API key from environment variables
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        # Raise an error if the API key is not found
        raise EnvironmentError("SERPAPI_API_KEY not found in environment variables.")

    all_results = []
    for page in range(0, max_pages):
        # Set the parameters for the search
        params = {
            "q": query,
            "api_key": api_key,
            "engine": "google",
            "num": num_results,
            "start": page * num_results
        }

        try:
            # Create a GoogleSearch object with the parameters
            search = GoogleSearch(params)
            # Execute the search and get the results as a dictionary
            results = search.get_dict()

            # Extract and append the relevant information from the search results
            for r in results.get("organic_results", []):
                all_results.append({
                    "title": r.get("title"),
                    "link": r.get("link"),
                    "snippet": r.get("snippet")
                })

        except Exception as e:
            # Log the error and continue
            print(f"Error fetching page {page}: {e}")

    # Analyze and rank results based on content relevance
    ranked_results = []
    for result in all_results:
        content = extract_main_content(result["link"])
        content_analysis = analyze_content(content, query.split())
        if content_analysis["score"] > 0:
            ranked_results.append((result, content_analysis["score"]))

    # Sort results by score in descending order
    ranked_results.sort(key=lambda x: x[1], reverse=True)

    # Return only the result part of the tuple
    return [result for result, score in ranked_results]
