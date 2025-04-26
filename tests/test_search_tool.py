# Import os module for accessing environment variables
import os
# Import pytest for testing
import pytest
# Import load_dotenv to load environment variables from a .env file
from dotenv import load_dotenv
# Import the search_web function from the search_tool module
from agent.search_tool import search_web

# Load environment variables from a .env file
load_dotenv()

# Test the structure of the search_web function's output
def test_search_web_structure():
    # Skip the test if the SERPAPI_API_KEY is not set
    if not os.getenv("SERPAPI_API_KEY"):
        pytest.skip("SERPAPI_API_KEY not set.")
    # Call the search_web function with a query and number of results
    results = search_web("artificial intelligence", num_results=3)
    
    # Ensure at least 1 result is returned and at most 3
    assert 1 <= len(results) <= 4
    
    # Check that each result contains the required fields
    for res in results:
        assert "title" in res
        assert "link" in res
        assert res["link"].startswith("http")
        assert "snippet" in res
