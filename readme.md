# Web Research Agent

## Overview

The Web Research Agent is a comprehensive tool designed to analyze user queries, search the web, extract and analyze content, synthesize information, and generate reports in PDF format. It integrates various components to provide a seamless experience for users looking to gather and synthesize information from the web.

## Features

- **Query Analyzer**: Detects the intent of user queries, extracts keywords, and identifies time-sensitive queries.
- **Web Search Tool**: Searches the web for relevant information based on extracted keywords.
- **Web Scraper**: Extracts main content from web pages.
- **Content Analyzer**: Analyzes extracted content for relevance and structure.
- **Information Synthesizer**: Summarizes information from multiple sources, detecting and resolving conflicts.
- **News Aggregator**: Fetches the latest news articles related to the query.
- **PDF Exporter**: Generates PDF reports from synthesized information.
- **Caching Module**: Saves and loads query results to improve performance.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/web-research-agent.git
   cd web-research-agent
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the NLTK wordnet resource:
   ```python
   import nltk
   nltk.download('wordnet')
   ```

4. Set up environment variables by creating a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   SERPAPI_API_KEY=your_serpapi_api_key
   NEWSAPI_KEY=your_newsapi_key
   ```

## Usage

Run the main script to start the agent:
```bash
python main.py
```

Follow the prompts to enter your query and receive a synthesized report.

## Testing

The project includes comprehensive tests for each component. To run the tests, use:
```bash
pytest tests/
```

## Workflow

Below is a flowchart illustrating the workflow of the Web Research Agent:

![Workflow](flow-chart.png)


## Components

### Query Analyzer
- Detects query intent and extracts key topics.
- Identifies time-sensitive queries.

### Web Search Tool
- Searches the web and returns structured results.

### Web Scraper
- Extracts main content from URLs.

### Content Analyzer
- Analyzes content for keyword relevance and structure.

### Information Synthesizer
- Summarizes information from multiple sources.

### News Aggregator
- Fetches recent news articles.

### PDF Exporter
- Generates PDF reports.

### Caching Module
- Caches query results for faster retrieval.

## ✅ **Test Coverage**

Your Web Research Agent includes comprehensive testing covering the following key components and scenarios:

### 🧠 **Query Analyzer (`analyze_query`)**
- ✅ **Intent Detection** (Informational, How-to, News)
- ✅ **Keyword Extraction**
- ✅ **Time Sensitivity Detection** (identifies time-sensitive queries accurately)

### 🔍 **Web Search Tool (`search_web`)**
- ✅ **Search Result Structure** (verifies returned URLs, titles, and snippets)
- ✅ **Flexible Result Count Handling** (handles fewer results gracefully)
- ✅ **Missing API Key Handling** (skips test gracefully if API key is unavailable)

### 🌐 **Web Scraper (`extract_main_content`)**
- ✅ **Valid URL Content Extraction**
- ✅ **Short or Invalid Content Handling**
- ✅ **Graceful Handling of Invalid or Unreachable URLs**

### 📑 **Content Analyzer (`analyze_content`)**
- ✅ **Relevant Keywords Detection**
- ✅ **Structured Content Recognition** (headings, lists, etc.)
- ✅ **Short or Insufficient Content Handling**
- ✅ **Long Text Without Relevant Keywords**

### 🧾 **Information Synthesizer (`synthesize_report`)**
- ✅ **Multi-source Summarization**
- ✅ **Conflict Detection and Resolution**
- ✅ **Handling No Available Content Gracefully**

### 📰 **News Aggregator (`get_latest_news`)**
- ✅ **Fetching Recent News Articles**
- ✅ **Integration with Time-Sensitive Queries**

### 📄 **PDF Exporter (`export_to_pdf`)**
- ✅ **PDF Generation from Synthesized Reports**

### 🗃️ **Caching Module (`cache.py`)**
- ✅ **Cache Saving and Loading Mechanism** (via manual verification)


## Architecture

The agent is structured into several modular components, each responsible for a specific task:

- **Query Analyzer**: Utilizes OpenAI's API to detect the intent of user queries, extract keywords, and identify time-sensitive queries.
- **Web Search Tool**: Uses SERPAPI to search the web for relevant information based on extracted keywords.
- **Web Scraper**: Employs BeautifulSoup and Newspaper3k to extract main content from web pages.
- **Content Analyzer**: Analyzes extracted content for relevance and structure using keyword matching and structural recognition.
- **Information Synthesizer**: Summarizes information from multiple sources, detecting and resolving conflicts using OpenAI's API.
- **News Aggregator**: Fetches the latest news articles related to the query using NewsAPI.
- **PDF Exporter**: Generates PDF reports from synthesized information using FPDF.
- **Caching Module**: Saves and loads query results to improve performance and reduce redundant processing.

## Prompt and Instruction Design

The prompts and instructions for the AI are crafted to be clear, concise, and context-aware, guiding the AI in understanding user queries and performing tasks efficiently. Key considerations include:

- **Clarity**: Prompts are structured to minimize ambiguity, ensuring the AI understands the user's intent.
- **Contextual Awareness**: Instructions consider the context of the query, such as time-sensitivity or specific topics.
- **Flexibility**: The AI is instructed to handle a variety of query types, from informational to how-to and news-related queries.

## Integration with External Tools

The agent connects to external tools and APIs to enhance its capabilities:

- **OpenAI API**: For natural language processing and understanding user queries.
- **SERPAPI**: For web search functionalities.
- **NewsAPI**: For fetching the latest news articles.

Integration is achieved through securely stored API keys in environment variables, and each external tool is encapsulated within its module for easy updates and maintenance.

## Error Handling and Unexpected Situations

The agent is designed to handle errors gracefully, ensuring a smooth user experience even when issues arise:

- **API Failures**: Checks for API key availability and handles missing keys by skipping tests or providing informative error messages.
- **Invalid URLs**: The Web Scraper handles unreachable or invalid URLs without crashing.
- **Insufficient Content**: The Content Analyzer manages short or irrelevant content by adjusting its analysis strategy.
- **Missing NLTK Resources**: Provides instructions to download missing NLTK resources like `wordnet` to prevent runtime errors.

Fallback mechanisms include caching query results for faster retrieval and providing clear feedback to users when errors occur, suggesting possible solutions or alternative actions.

