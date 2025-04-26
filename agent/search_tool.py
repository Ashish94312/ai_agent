# agent/search_tool.py

# Import os module for accessing environment variables
import os
# Import GoogleSearch class from serpapi module for performing web searches
from serpapi import GoogleSearch
# Import additional modules for ranking
from agent.content_analyzer import analyze_content
from agent.scraper import extract_main_content

from concurrent.futures import ThreadPoolExecutor

import os

def search_web(query: str, num_results: int = 5, max_pages: int = 2):
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        raise EnvironmentError("SERPAPI_API_KEY not found in environment variables.")

    all_results = []
    for page in range(0, max_pages):
        params = {
            "q": query,
            "api_key": api_key,
            "engine": "google",
            "num": num_results,
            "start": page * num_results
        }

        try:
            search = GoogleSearch(params)
            results = search.get_dict()

            for r in results.get("organic_results", []):
                all_results.append({
                    "title": r.get("title"),
                    "link": r.get("link"),
                    "snippet": r.get("snippet")
                })

        except Exception as e:
            print(f"Error fetching page {page}: {e}")

    # ✅ Now parallelize the content fetching and analyzing
    def fetch_and_analyze(result):
        try:
            content = extract_main_content(result["link"])
            analysis = analyze_content(content, query.split())
            return (result, analysis["score"])
        except Exception as e:
            print(f"Error analyzing {result['link']}: {e}")
            return (result, 0)

    ranked_results = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_and_analyze, result) for result in all_results]
        for future in futures:
            result, score = future.result()
            if score > 0:
                ranked_results.append((result, score))

    # Sort by score descending
    ranked_results = sorted(ranked_results, key=lambda x: -x[1])

    # Return only top 5 results
    top_results = [r[0] for r in ranked_results][:5]

    return top_results
