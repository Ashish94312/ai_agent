# Import regular expression module
import re

# Import List from typing module for type hinting
from typing import List

# Import additional NLP libraries for semantic and sentiment analysis
from textblob import TextBlob

import nltk
nltk.download('wordnet')

def analyze_content(content: str, key_topics: List[str]) -> dict:
    """
    Analyze the content of a web page and return a dictionary with the results.
    """
    # Check if the content is too short to analyze
    if len(content) < 100:
        return {
            "score":0,
            "reason":"Content is too short to analyze"
        }
    
    # Convert content to lowercase for case-insensitive comparison
    content_lower = content.lower()

    # Count occurrences of each key topic in the content
    topic_hits = sum(content_lower.count(topic.lower()) for topic in key_topics)

    # Check for structural elements (e.g., multiple newlines) in the content
    structure_bonus = 1 if re.search(r"\n{2,}", content) else 0

    # Perform sentiment analysis
    sentiment = TextBlob(content).sentiment.polarity

    # Calculate the score based on topic hits, structure bonus, and sentiment
    score = topic_hits + structure_bonus + (1 if sentiment > 0 else 0)

    # Return the analysis results as a dictionary
    return {
        "score": score,
        "keywords_matched": topic_hits,
        "has_structure": bool(structure_bonus),
        "sentiment": "positive" if sentiment > 0 else "negative" if sentiment < 0 else "neutral",
        "summary": content[:300].replace('\n', ' ') + "...",
    }



   
    
    