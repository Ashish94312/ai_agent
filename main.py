# Import necessary functions and classes from agent modules
from agent.query_analyzer import analyze_query
from agent.search_tool import search_web
from dotenv import load_dotenv
from agent.scraper import extract_main_content
from agent.content_analyzer import analyze_content
from agent.synthesizer import synthesize_report
from agent.exporter import export_to_pdf
from agent.news_aggregator import get_latest_news

# Import os module for environment variable management
import os
# Load environment variables from a .env file
load_dotenv()

# Main function to execute the program
def main():
    # Get user input for the query
    user_query = input("Enter your query: ")
    # Analyze the user query
    query_analysis = analyze_query(user_query)
    # Print the query analysis result
    print(query_analysis)
    news_blocks = []
    # Check if the query is time-sensitive
    if query_analysis.get("time_sensitivity"):
        print("\n📰 Fetching latest news...")
        # Get the latest news based on key topics
        news_results = get_latest_news(" ".join(query_analysis["key_topics"]))

        # Print each news article
        for i, article in enumerate(news_results, 1):
            print(f"\n🗞️ News [{i}]: {article['title']}")
            print(f"URL: {article['url']}")
            print(f"Summary: {article['summary']}")

        # Prepare news blocks for report synthesis
        news_blocks = [
            {"snippet": article["summary"]}
            for article in news_results if "summary" in article
        ]

    # Check if key topics are present in the query analysis
    if "key_topics" in query_analysis:
        # Formulate a search query from key topics
        search_query = " ".join(query_analysis["key_topics"])
        print(f"\n🌐 Searching for: {search_query}")
        # Perform a web search
        results = search_web(search_query)
        print(results)
  
        # Combine top web and news articles and generate report
        if results or news_blocks:
            # top_ranked = sorted(results, key=lambda x: -x["score"])[:3]
            all_blocks = results + news_blocks

            # Synthesize a report from the collected data
            report = synthesize_report(user_query, all_blocks)
            print("\n🧠 Final Synthesized Report:\n")
            print(report)

            # Export the report to a PDF file
            export_to_pdf(user_query, report)
            print(f"\n✅ Report saved to: output/report.pdf")

    else:
        print("No key topics found in the query analysis.")

# Entry point for the script
if __name__ == "__main__":
    main()