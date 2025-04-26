# Import the synthesize_report function from the synthesizer module
from agent.synthesizer import synthesize_report

# Test the basic functionality of the synthesize_report function
def test_synthesize_report_basic():
    # Define a query and content blocks for the test
    query = "How does solar power work?"
    blocks = [
        {"snippet": "Solar power uses photovoltaic cells to convert sunlight into electricity.", "score": 3},
        {"snippet": "Photovoltaic technology directly turns solar energy into electrical power.", "score": 2}
    ]
    # Call the synthesize_report function with the query and blocks
    report = synthesize_report(query, blocks)
    # Assert that the report is a string
    assert isinstance(report, str)
    # Assert that the report length is greater than 50 characters
    assert len(report) > 50
    # Assert that the report contains the phrase 'solar power'
    assert "solar power" in report.lower()

# Test the synthesize_report function with empty content blocks
def test_synthesize_report_empty_blocks():
    # Define a query for the test
    query = "Impact of AI on jobs"
    # Call the synthesize_report function with the query and empty blocks
    report = synthesize_report(query, [])
    # Assert that the report indicates no content is available to synthesize
    assert report == "No content available to synthesize."
