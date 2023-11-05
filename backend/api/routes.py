# In api/routes.py
from flask import Blueprint, jsonify, request
from services.sentiment_analysis import analyze_sentiment

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment_route():
    data = request.json
    company_name = data.get('company_name', '')
    if not company_name:
        return jsonify({"error": "No company name provided"}), 400

    sentiment_result = analyze_sentiment(company_name)
    return jsonify(sentiment_result)
