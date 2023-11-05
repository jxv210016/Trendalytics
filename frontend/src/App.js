import React, { useState } from 'react';
import './App.css';
import TradingViewWidget from './TradingViewWidget'; // Ensure this import path is correct

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [recentSearches, setRecentSearches] = useState([]);
  const [analysisResult, setAnalysisResult] = useState('');
  const [sentiment, setSentiment] = useState('');
  const [articles, setArticles] = useState([]);
  const [showRecentSearches, setShowRecentSearches] = useState(false);

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSearchFocus = () => {
    setShowRecentSearches(true);
  };

  const handleSearchBlur = () => {
    setTimeout(() => {
      setShowRecentSearches(false);
    }, 200);
  };

  const handleSearchSubmit = async (e) => {
    e.preventDefault();
    if (!searchTerm.trim()) return;

    const newSearchTerm = searchTerm.trim();
    if (!recentSearches.includes(newSearchTerm)) {
      setRecentSearches([newSearchTerm, ...recentSearches].slice(0, 5));
    }

    try {
      const response = await fetch('/api/analyze_sentiment', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ company_name: newSearchTerm }),
      });

      const data = await response.json();
      if (response.ok) {
        setAnalysisResult(`Sentiment: ${data.overall_sentiment}`);
        setSentiment(data.overall_sentiment);
        setArticles(data.top_articles);
      } else {
        throw new Error(data.error || 'Error occurred while fetching analysis');
      }
    } catch (error) {
      setAnalysisResult('Error: Could not retrieve sentiment');
      console.error(error);
    }

    setShowRecentSearches(false);
    setSearchTerm('');
  };

  const getFooterClass = () => {
    return sentiment === 'Positive' ? 'footer-positive' : sentiment === 'Negative' ? 'footer-negative' : '';
  };

  return (
    <div className="App">
      <div className="topbar">
        <div className="search-container">
          <form className="search-bar" onSubmit={handleSearchSubmit}>
            <input
              type="text"
              placeholder="Enter company name"
              value={searchTerm}
              onChange={handleSearchChange}
              onFocus={handleSearchFocus}
              onBlur={handleSearchBlur}
            />
            <button type="submit">Analyze Sentiment</button>
          </form>
          {showRecentSearches && (
            <div className="recent-searches-dropdown">
              {recentSearches.map((search, index) => (
                <div key={index} className="dropdown-item" onClick={() => setSearchTerm(search)}>
                  {search}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      <div className={`sentiment-indicator ${getFooterClass()}`}>
        <div className="sentiment">{analysisResult}</div>
      </div>

      <main className="content">
        {articles.map((article, index) => (
          <a key={index} className="article-card" href={article.url} target="_blank" rel="noopener noreferrer">
            <div className="article-title">{article.title}</div>
            <div className="article-sentiment">Sentiment Score: {article.sentiment_score.toFixed(2)}</div>
          </a>
        ))}
      </main>

      <TradingViewWidget />

      <footer className="footer">
        {/* Footer content */}
      </footer>
    </div>
  );
};

export default App;
