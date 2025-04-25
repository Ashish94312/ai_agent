# Import the extract_main_content function from the scraper module
from agent.scraper import extract_main_content
# Import pytest for testing
import pytest
# def test_extract_main_content_real_url():
#     url = "https://www.bbc.com/news/science-environment-68458482"
#     content = extract_main_content(url)
#     assert isinstance(content, str)
#     assert len(content) > 500  # Ensure substantial content extracted
#     assert "BBC" not in content[:50]  # Check unwanted header content removal


# Test the extraction of main content from a real URL
def test_extract_main_content_real_url():
    # Define a real URL for testing
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
    # Extract the main content from the URL
    content = extract_main_content(url)
    # Assert that the content is a string
    assert isinstance(content, str)
    # Assert that the content length is greater than 500 characters
    assert len(content) > 500


# Test the extraction of main content from an invalid URL
def test_extract_main_content_invalid_url():
    # Define an invalid URL for testing
    url = "http://thisurldoesnotexist.tld/"
    # Extract the main content from the URL
    content = extract_main_content(url)
    # Assert that the content contains an error message
    assert "Error fetching" in content
