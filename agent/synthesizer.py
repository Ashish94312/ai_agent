# agent/synthesizer.py

import openai
import os
from agent.cache import load_from_cache, save_to_cache

openai.api_key = os.getenv("OPENAI_API_KEY")

def synthesize_report(query: str, content_blocks: list) -> str:
    if not content_blocks:
        return "No content available to synthesize."

    MAX_SNIPPET_LEN = 500
    combined_snippets = "\n\n".join([
        f"Source {i+1}:\n{block['snippet'][:MAX_SNIPPET_LEN]}"
        for i, block in enumerate(content_blocks)
    ])

    # Create a cache key from query and snippets
    cache_key = query + combined_snippets
    cached = load_from_cache("snippet", cache_key)
    if cached:
        print("[CACHE HIT] Synthesized snippet")
        return cached

    system_prompt = (
        "You are an expert research assistant.\n"
        "Given multiple article summaries, do the following:\n"
        "1. Identify and explain any conflicting facts (e.g., Source 1 vs Source 3).\n"
        "2. Summarize the general consensus where possible.\n"
        "3. Present a clean, unified summary for the user's query."
    )

    user_prompt = f"User Query: {query}\n\nArticle Summaries:\n{combined_snippets}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    summary = response.choices[0].message.content.strip()
    save_to_cache("snippet", cache_key, summary)
    return summary
