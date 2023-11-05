import requests
from textblob import TextBlob

# Define the company list globally so it can be imported by other modules if needed
# Define the company list globally so it can be imported by other modules if needed
companies = [
    "Amazon", "Apple", "Alphabet", "Google", "Microsoft", "Meta Platforms", "Meta", "Facebook",
"Dell Technologies", "Dell", "Intel", "HP", "Hewlett-Packard", "IBM", "Qualcomm", "Oracle",
"Honeywell International", "Honeywell", "Jabil", "Jabil Circuit", "Broadcom", "Uber",
"Salesforce", "Salesforce.com", "Micron Technology", "Micron", "Visa", "Hewlett Packard Enterprise", "HPE",
"PayPal Holdings", "PayPal", "Nvidia", "Applied Materials", "Applied", "CDW", "Advanced Micro Devices", "AMD",
"Mastercard", "Coupang", "Texas Instruments", "TI", "Whirlpool", "Cognizant Technology Solutions", "Cognizant",
"Western Digital", "WD", "Kyndryl Holdings", "Kyndryl", "Fiserv", "Adobe", "Block", "Square",
"Lam Research", "Lam", "Booking Holdings", "Booking.com", "DXC Technology", "DXC", "Opendoor Technologies", "Opendoor",
"Fidelity National Information Services", "FIS", "Leidos Holdings", "Leidos", "Corning", "VMware", "Intuit",
"Wayfair", "Qurate Retail", "Qurate", "Analog Devices", "ADI", "Expedia Group", "Expedia", "S&P Global", "S&P",
"Insight Enterprises", "Insight", "Chewy", "eBay", "KLA", "KLA Corporation", "Global Payments", "Airbnb",
"Booz Allen Hamilton Holding", "Booz Allen", "ON Semiconductor", "ON Semi", "Sanmina", "NCR",
"Rockwell Automation", "Rockwell", "Science Applications International", "SAIC", "ServiceNow", "Tesla",
"Lockheed Martin", "Lockheed",
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
    # Normally, you'd retrieve the API key from a secure environment variable or secrets manager
    news_api_key = 'a6e886de6df443e4b3c72540af7fa917'  # Replace with your actual API key, this should be securely managed

    # Initialize variables to store sentiment polarities
    sentiment_polarities = []
    positive_articles = []
    negative_articles = []

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

    # Perform sentiment analysis on each article and categorize them based on sentiment polarity
    for article in articles:
        article_content = article.get('description', '')
        sentiment_score = TextBlob(article_content).sentiment.polarity
        article_data = {
            "title": article.get('title'),
            "url": article.get('url'),
            "sentiment_score": sentiment_score
        }
        sentiment_polarities.append(sentiment_score)
        if sentiment_score > 0:
            positive_articles.append(article_data)
        elif sentiment_score < 0:
            negative_articles.append(article_data)

    # Sort the positive and negative articles by the absolute value of their sentiment score
    positive_articles = sorted(positive_articles, key=lambda x: x['sentiment_score'], reverse=True)
    negative_articles = sorted(negative_articles, key=lambda x: abs(x['sentiment_score']), reverse=True)

    # Take the top 5 from each list to ensure a mix of positive and negative articles
    top_positive_articles = positive_articles[:5]
    top_negative_articles = negative_articles[:5]

    # Combine the top positive and negative articles
    top_articles = top_positive_articles + top_negative_articles

    # Calculate the average polarity of all articles
    average_polarity = sum(sentiment_polarities) / len(sentiment_polarities) if sentiment_polarities else 0

    # Determine the overall sentiment
    overall_sentiment = "Neutral"
    if average_polarity > 0:
        overall_sentiment = "Positive"
    elif average_polarity < 0:
        overall_sentiment = "Negative"

    # Compile the results into a dictionary
    sentiment_results = {
        "company_name": company_name,
        "average_sentiment_polarity": average_polarity,
        "overall_sentiment": overall_sentiment,
        "articles_analyzed": len(sentiment_polarities),
        "top_articles": top_articles  # This will include the mixed top articles in the result
    }

    return sentiment_results

# Example usage:
# result = analyze_sentiment("Apple")
# print(result)

# ... (any additional code you might have, like Flask or Django app definitions) ...
