# Import the analyze_content function from the content_analyzer module
from agent.content_analyzer import analyze_content

# Test the quality analysis of content with repeated keywords
def test_analyze_content_quality():
    # Define content with repeated keywords
    content = "Carbon capture involves trapping CO2 emissions. " * 20
    # Analyze the content
    result = analyze_content(content, ["carbon", "capture"])
    # Assert that the score is at least 2
    assert result["score"] >= 2
    # Assert that at least 2 keywords are matched
    assert result["keywords_matched"] >= 2
    # Assert that the content does not have structure
    assert result["has_structure"] is False

# Test the analysis of short content
def test_analyze_content_short_text():
    # Define short content
    short_text = "Too short content."
    # Analyze the short content
    result = analyze_content(short_text, ["carbon", "capture"])
    # Assert that the score is 0
    assert result["score"] == 0
    # Assert that the reason indicates the content is too short
    assert result["reason"] == "Content is too short to analyze"

# def test_analyze_content_no_keywords():
#     content = "This content is unrelated to the keywords."
#     result = analyze_content(content, [])
#     assert result["score"] == 0
#     assert result["reason"] == "No relevant keywords provided."

# Test the analysis of content with no relevant keywords
def test_analyze_content_no_relevant_keywords():
    content = ("This paragraph talks extensively about economics, finance, and "
               "global markets. It provides detailed analysis on stock trading, "
               "investment portfolios, and monetary policies. It specifically "
               "avoids any environmental or scientific topics entirely.") * 5

    result = analyze_content(content, ["carbon", "capture", "climate"])

    # Check that no keywords matched
    assert result["keywords_matched"] == 0

# Test the analysis of content with structure
def test_analyze_content_with_structure():
    # Define structured content
    structured_content = """
    ## What is Carbon Capture?
    Carbon capture is a technology used to trap and store CO₂ emissions.

    ### Steps involved:
    - Capture CO₂ from emission sources.
    - Transport the CO₂ to storage sites.
    - Store it underground in geological formations.

    This technology helps reduce greenhouse gas emissions significantly.
    """

    # Analyze the structured content
    result = analyze_content(structured_content, ["carbon", "CO₂", "emissions"])
    
    # Assert that the score is at least 3 (2+ keyword matches + structure bonus)
    assert result["score"] >= 3
    # Assert that at least 2 keywords are matched
    assert result["keywords_matched"] >= 2
    # Assert that the content has structure
    assert result["has_structure"] is True
