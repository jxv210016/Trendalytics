import requests
from textblob import TextBlob

# Define the company list globally so it can be imported by other modules if needed
companies = {
    "Amazon": ["AMZN", "amazon"],
    "Apple": ["AAPL", "apple"],
    "Alphabet": ["GOOGL", "alphabet", "google"],
    "Microsoft": ["MSFT", "microsoft"],
    "Meta Platforms": ["FB", "meta", "facebook"],
    "Dell Technologies": ["DELL", "dell"],
    "Intel": ["INTC", "intel"],
    "HP": ["HPQ", "hewlett-packard", "hp"],
    "IBM": ["IBM", "ibm"],
    "Qualcomm": ["QCOM", "qualcomm"],
    "Oracle": ["ORCL", "oracle"],
    "Honeywell International": ["HON", "honeywell"],
    "Jabil": ["JBL", "jabil", "jabil circuit"],
    "Broadcom": ["AVGO", "broadcom"],
    "Uber": ["UBER", "uber"],
    "Salesforce": ["CRM", "salesforce", "salesforce.com"],
    "Micron Technology": ["MU", "micron"],
    "Visa": ["V", "visa"],
    "Hewlett Packard Enterprise": ["HPE", "hewlett packard enterprise", "hpe"],
    "PayPal Holdings": ["PYPL", "paypal"],
    "Nvidia": ["NVDA", "nvidia"],
    "Applied Materials": ["AMAT", "applied"],
    "CDW": ["CDW", "cdw"],
    "Advanced Micro Devices": ["AMD", "amd"],
    "Mastercard": ["MA", "mastercard"],
    "Coupang": ["CPNG", "coupang"],
    "Texas Instruments": ["TXN", "texas instruments", "ti"],
    "Whirlpool": ["WHR", "whirlpool"],
    "Cognizant Technology Solutions": ["CTSH", "cognizant"],
    "Western Digital": ["WDC", "western digital", "wd"],
    "Kyndryl Holdings": ["KYND", "kyndryl"],
    "Fiserv": ["FISV", "fiserv"],
    "Adobe": ["ADBE", "adobe"],
    "Block": ["SQ", "block", "square"],
    "Lam Research": ["LRCX", "lam research", "lam"],
    "Booking Holdings": ["BKNG", "booking holdings", "booking.com"],
    "DXC Technology": ["DXC", "dxc technology", "dxc"],
    "Opendoor Technologies": ["OPEN", "opendoor"],
    "Fidelity National Information Services": ["FIS", "fidelity national information services", "fis"],
    "Leidos Holdings": ["LDOS", "leidos"],
    "Corning": ["GLW", "corning"],
    "VMware": ["VMW", "vmware"],
    "Intuit": ["INTU", "intuit"],
    "Wayfair": ["W", "wayfair"],
    "Qurate Retail": ["QRTEA", "qurate retail", "qurate"],
    "Analog Devices": ["ADI", "analog devices", "adi"],
    "Expedia Group": ["EXPE", "expedia group", "expedia"],
    "S&P Global": ["SPGI", "s&p global", "s&p"],
    "Insight Enterprises": ["NSIT", "insight enterprises", "insight"],
    "Chewy": ["CHWY", "chewy"],
    "eBay": ["EBAY", "ebay"],
    "KLA": ["KLAC", "kla", "kla corporation"],
    "Global Payments": ["GPN", "global payments"],
    "Airbnb": ["ABNB", "airbnb"],
    "Booz Allen Hamilton Holding": ["BAH", "booz allen hamilton holding", "booz allen"],
    "ON Semiconductor": ["ON", "on semiconductor", "on semi"],
    "Sanmina": ["SANM", "sanmina"],
    "NCR": ["NCR", "ncr"],
    "Rockwell Automation": ["ROK", "rockwell automation", "rockwell"],
    "Science Applications International": ["SAIC", "science applications international", "saic"],
    "ServiceNow": ["NOW", "servicenow"],
    "Tesla": ["TSLA", "tesla"],
    "Lockheed Martin": ["LMT", "lockheed martin", "lockheed"],
}


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
