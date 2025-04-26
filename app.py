# app.py
from flask import Flask, request, render_template, send_file, make_response
from agent.query_analyzer import analyze_query
from agent.search_tool import search_web
from agent.scraper import extract_main_content
from agent.content_analyzer import analyze_content
from agent.synthesizer import synthesize_report
from agent.exporter import export_to_pdf
from agent.news_aggregator import get_latest_news
from dotenv import load_dotenv
from agent.exporter import export_to_pdf2
import os
import base64
import io
from concurrent.futures import ThreadPoolExecutor

load_dotenv()
app = Flask(__name__)
app.report_pdf = None
@app.route('/', methods=['GET', 'POST'])
def index():
    report = ""
    user_query = ""
    # pdf_ready = False
    download_url = ""
    if request.method == 'POST':
        user_query = request.form.get('query')
        query_analysis = analyze_query(user_query)
        news_blocks = []
        results = []

        if query_analysis.get("time_sensitivity"):
            news_results = get_latest_news(" ".join(query_analysis["key_topics"]))
            news_blocks = [
                {"snippet": article["summary"]}
                for article in news_results if "summary" in article
            ]

        # if "key_topics" in query_analysis:
        #     search_query = " ".join(query_analysis["key_topics"])
        #     results = search_web(search_query)

        if "key_topics" in query_analysis:
            search_query = " ".join(query_analysis["key_topics"])
            results = search_web(search_query) # LIMIT to top 3 results

          

        if results or news_blocks:
            all_blocks = results + news_blocks
            report = synthesize_report(user_query, all_blocks)
            # os.makedirs("output", exist_ok=True)
            # export_to_pdf(user_query, report)
            # Generate in-memory PDF
            pdf_file = export_to_pdf2(user_query, report)

            base64_pdf = base64.b64encode(pdf_file.getvalue()).decode('utf-8')
            download_url = f"data:application/pdf;base64,{base64_pdf}"
         

    return render_template("index.html", query=user_query, report=report, download_url=download_url)

import logging

logging.basicConfig(level=logging.DEBUG)

@app.route('/download')
def download_pdf():
    if app.report_pdf is None:
        return "No report generated yet. Please submit a query first.", 404

    response = make_response(app.report_pdf.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=report.pdf'
    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
