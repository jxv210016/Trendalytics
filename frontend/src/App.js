import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [recentSearches, setRecentSearches] = useState([]);
  const [analysisResult, setAnalysisResult] = useState('');
  const [sentiment, setSentiment] = useState('');
  const [articles, setArticles] = useState([]); // State to hold the articles

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
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
        setArticles(data.top_articles); // Set the articles in state
      } else {
        throw new Error(data.error || 'Error occurred while fetching analysis');
      }
    } catch (error) {
      setAnalysisResult('Error: Could not retrieve sentiment');
      console.error(error);
    }

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
            />
            <button type="submit">Analyze Sentiment</button>
          </form>
          <div className="recent-searches">
            {recentSearches.map((search, index) => (
              <span key={index} className="badge" onClick={() => setSearchTerm(search)}>
                {search}
              </span>
            ))}
          </div>
        </div>
      </div>
      
      <main className="content">
        {articles.map((article, index) => (
          <a key={index} className="article-card" href={article.url} target="_blank" rel="noopener noreferrer">
            <div className="article-title">{article.title}</div>
            <div className="article-sentiment">Sentiment Score: {article.sentiment_score.toFixed(2)}</div>
          </a>
        ))}
      </main>
      
      <footer className={`footer ${getFooterClass()}`}>
        <div className="sentiment">
          {analysisResult}
        </div>
      </footer>
    </div>
  );
}

export default App;
