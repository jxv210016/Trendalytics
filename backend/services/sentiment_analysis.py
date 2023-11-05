import requests
from textblob import TextBlob

# Define the company list globally so it can be imported by other modules if needed
companies = [
    "Amazon", "Apple", "Alphabet", "Microsoft", "Meta Platforms", "Dell Technologies",
  "Intel", "HP", "IBM", "Qualcomm", "Oracle", "Honeywell International", "Jabil",
  "Broadcom", "Uber", "Salesforce", "Micron Technology", "Visa",
  "Hewlett Packard Enterprise", "PayPal Holdings", "Nvidia", "Applied Materials",
  "CDW", "Advanced Micro Devices", "Mastercard", "Coupang", "Texas Instruments",
  "Whirlpool", "Cognizant Technology Solutions", "Western Digital", "Kyndryl Holdings",
  "Fiserv", "Adobe", "Block", "Lam Research", "Booking Holdings", "DXC Technology",
  "Opendoor Technologies", "Fidelity National Information Services", "Leidos Holdings",
  "Corning", "VMware", "Intuit", "Wayfair", "Qurate Retail", "Analog Devices",
  "Expedia Group", "S&P Global", "Insight Enterprises", "Chewy", "eBay", "KLA",
  "Global Payments", "Airbnb", "Booz Allen Hamilton Holding", "ON Semiconductor",
  "Sanmina", "NCR", "Rockwell Automation", "Science Applications International",
  "ServiceNow", "Tesla", "Lockheed",
]

def fetch_articles(company_name, news_api_key):
    """
    Fetch news articles related to the company from specific sources.
    """
    sources = "reuters,bloomberg,the-wall-street-journal,cnbc,financial-times,marketwatch,the-economist,forbes,fortune,cnn,bbc-news,the-new-york-times,the-guardian,the-washington-post,associated-press"
    news_url = f'https://newsapi.org/v2/everything?q={company_name}&apiKey={news_api_key}&sources={sources}'
    
    response = requests.get(news_url)
    if response.status_code == 200:
        news_data = response.json()
        return news_data.get('articles', [])
    else:
        return None

def analyze_sentiment(company_name):
    """
    Perform sentiment analysis on news articles related to the provided company name.
    """
    # Normally, you'd retrieve the API key from a secure environment variable or secrets manager
    news_api_key = 'a6e886de6df443e4b3c72540af7fa917'  # This should be securely managed

    # Initialize variables to store sentiment polarities
    sentiment_polarities = []
    total_polarity = 0

    # Check if the provided company name is in the list of known companies
    if company_name not in companies:
        return {
            "error": "Company not found in the list.",
            "company_name": company_name
        }
    
    articles = fetch_articles(company_name, news_api_key)
    if articles is None:
        return {
            "error": "Error fetching news data.",
            "company_name": company_name
        }

    # Perform sentiment analysis on each article and calculate the average polarity
    for article in articles:
        # Use the article's description for sentiment analysis
        article_content = article.get('description', '')
        
        # Analyze the sentiment of the article content
        sentiment_score = TextBlob(article_content).sentiment.polarity
        sentiment_polarities.append(sentiment_score)

    # Calculate the average polarity
    if sentiment_polarities:
        total_polarity = sum(sentiment_polarities) / len(sentiment_polarities)
    
    # Determine if the overall sentiment is positive, negative, or neutral
    overall_sentiment = "Neutral"
    if total_polarity > 0:
        overall_sentiment = "Positive"
    elif total_polarity < 0:
        overall_sentiment = "Negative"

    # Compile the results into a dictionary
    sentiment_results = {
        "company_name": company_name,
        "average_sentiment_polarity": total_polarity,
        "overall_sentiment": overall_sentiment,
        "articles_analyzed": len(sentiment_polarities)
    }

    return sentiment_results
