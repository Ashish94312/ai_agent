# Import pytest for testing
import pytest
# Import the analyze_query function from the query_analyzer module
from agent.query_analyzer import analyze_query

# Test the intent detection of the analyze_query function
@pytest.mark.parametrize("query,expected_intents", [
    ("How does carbon capture work?", ["how-to", "informational"]),
    ("Latest news about AI regulations 2025", ["news"]),
    ("What is quantum computing?", ["informational"]),
])
def test_analyze_query_intent(query, expected_intents):
    # Analyze the query
    result = analyze_query(query)
    # Assert that the detected intent is in the expected intents
    assert result.get("intent") in expected_intents
    # Assert that key_topics is a list
    assert isinstance(result.get("key_topics"), list)

# Test the time sensitivity detection of the analyze_query function
@pytest.mark.parametrize("query,expected_sensitivity", [
    ("Latest news about AI regulations 2025", True),
    ("History of the internet", False),
])
def test_time_sensitivity_detection(query, expected_sensitivity):
    # Analyze the query
    result = analyze_query(query)
    # Assert that the time sensitivity matches the expected sensitivity
    assert result["time_sensitivity"] == expected_sensitivity
