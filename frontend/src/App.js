import React, { useState } from 'react';
import './App.css';

// Assuming these are the articles and recent searches you want to display
const articles = [
  { id: 1, title: 'Market Trends', summary: 'Summary of market trends.' },
  { id: 2, title: 'Stock Analysis', summary: 'Deep dive into stock analysis.' },
  // ... other articles
];

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [recentSearches, setRecentSearches] = useState(['google', 'apple']); // Example recent searches
  const [sentiment, setSentiment] = useState('Earnings will be Up');

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    // Perform the search and update the recentSearches state
    if (searchTerm.trim() && !recentSearches.includes(searchTerm)) {
      setRecentSearches([searchTerm, ...recentSearches].slice(0, 5)); // Store up to 5 recent searches
    }
    setSearchTerm('');
  };

  const toggleSentiment = () => {
    setSentiment(prev => (prev === 'Earnings will be Up' ? 'Earnings will be Down' : 'Earnings will be Up'));
  };

  return (
    <div className="App">
      <div className="topbar">
        <div className="search-container">
          <div className="search-bar">
            <input
              type="text"
              placeholder="Enter Stock"
              value={searchTerm}
              onChange={handleSearchChange}
            />
            <button onClick={handleSearchSubmit}>
              Search
            </button>
          </div>
          <div className="recent-searches">
            {recentSearches.map((search, index) => (
              <span key={index} className="badge">
                {search}
              </span>
            ))}
          </div>
        </div>
      </div>
      
      <main className="content">
        {articles.map(article => (
          <div key={article.id} className="article-card">
            <h5>{article.title}</h5>
            <p>{article.summary}</p>
          </div>
        ))}
      </main>
      
      <footer className="footer">
        <div className="sentiment" onClick={toggleSentiment}>
          {sentiment}
        </div>
      </footer>
    </div>
  );
};

export default App;
