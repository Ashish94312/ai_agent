# app.py
from flask import Flask, request, render_template, send_file
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

load_dotenv()
app = Flask(__name__)
app.report_pdf = None
@app.route('/', methods=['GET', 'POST'])
def index():
    report = ""
    user_query = ""

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

        if "key_topics" in query_analysis:
            search_query = " ".join(query_analysis["key_topics"])
            results = search_web(search_query)

        if results or news_blocks:
            all_blocks = results + news_blocks
            report = synthesize_report(user_query, all_blocks)
            # os.makedirs("output", exist_ok=True)
            # export_to_pdf(user_query, report)
            # pdf_file = export_to_pdf2(user_query, report)
            # report = pdf_file.getvalue()
            app.report_pdf = export_to_pdf2(user_query, report)

    return render_template("index.html", query=user_query, report=report)


import logging

logging.basicConfig(level=logging.DEBUG)

@app.route('/download')
def download_pdf():
    file_path = "output/report.pdf"
    if not os.path.exists(file_path):
        app.logger.error("PDF not found!")
        return "No report generated yet. Please submit a query first.", 404
    app.logger.info(f"Serving file: {file_path}")
    return send_file(app.report_pdf, as_attachment=True,  mimetype='application/pdf', download_name='report.pdf')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
