import logo from './logo.svg';
import './App.css';

<<<<<<< Updated upstream
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
=======
const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [recentSearches, setRecentSearches] = useState([]);
  const [analysisResult, setAnalysisResult] = useState('');
  const [sentiment, setSentiment] = useState('');

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSearchSubmit = async (e) => {
    e.preventDefault();
    if (!searchTerm.trim()) return;

    const newSearchTerm = searchTerm.trim();
    // Check if the searchTerm (case-insensitive) is not already in the recentSearches
    if (!recentSearches.some(search => search.toLowerCase() === newSearchTerm.toLowerCase())) {
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
      } else {
        throw new Error(data.error || 'Error occurred while fetching analysis');
      }
    } catch (error) {
      setAnalysisResult('Error: Could not retrieve sentiment');
      console.error(error);
    }

    setSearchTerm('');
  };

  // Function to get the class for the footer based on the sentiment
  const getFooterClass = () => {
    if (sentiment === 'Negative') {
      return 'footer-negative';
    } else if (sentiment === 'Positive') {
      return 'footer-positive';
    }
    return '';
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
        {/* Content could be more components or information */}
      </main>
      
      <footer className={`footer ${getFooterClass()}`}>
        <div className="sentiment">
          {analysisResult}
        </div>
      </footer>
>>>>>>> Stashed changes
    </div>
  );
}

export default App;
