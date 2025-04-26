# agent/query_analyzer.py

import openai
import os
from agent.cache import load_from_cache, save_to_cache
import json
import re
import dotenv

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def is_time_sensitive(query: str) -> bool:
    time_keywords = [
        "today", "latest", "breaking", "this week", "this month", "this year",
        "recent", "new", "currently", "now", "updated", "updates", "live",
        r"\b20\d{2}\b", r"\bQ[1-4]\b",
        "april", "may", "june", "july", "august",
        "september", "october", "november", "december"
    ]
    query_lower = query.lower()
    return any(re.search(pattern, query_lower) for pattern in time_keywords)

def analyze_query(user_query: str) -> dict:
    # Check if the query result is already cached
    cached_result = load_from_cache("query", user_query)
    if cached_result:
        print("[CACHE HIT] Query analysis")
        return cached_result

    # Define the system prompt for the OpenAI model
    system_prompt = (
        "You are a smart query analyzer.\n"
        "Return a JSON with:\n"
        "- intent: one of ['informational', 'how-to', 'news', 'opinion', 'comparative']\n"
        "- key_topics: list of important keywords or phrases\n"
    )

    # Prepare the messages for the OpenAI API call
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Query: {user_query}"}
    ]

    try:
        # Call the OpenAI API to analyze the query
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.2
        )
        content = response.choices[0].message.content.strip()
        result = json.loads(content)
        result["time_sensitivity"] = is_time_sensitive(user_query)
        # Save the result to cache for future use
        save_to_cache("query", user_query, result)
        return result

    except json.JSONDecodeError as json_err:
        # Handle JSON decoding errors
        return {"error": f"JSON decoding error: {str(json_err)}"}
    except openai.error.OpenAIError as api_err:
        # Handle OpenAI API errors
        return {"error": f"OpenAI API error: {str(api_err)}"}
    except Exception as e:
        # Handle any other exceptions
        return {"error": f"Unexpected error: {str(e)}"}
