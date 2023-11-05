import React, { useEffect, useRef } from 'react';

const TradingViewWidget = () => {
  // Use a ref to access the DOM element where the TradingView widget will be attached
  const widgetRef = useRef(null);

  useEffect(() => {
    // Create a script element
    const script = document.createElement('script');
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js';
    script.async = true;
    script.type = 'text/javascript';
    // Define the TradingView widget settings
    script.innerHTML = JSON.stringify({
        "symbols": [
            {"description": "Apple", "proName": "NASDAQ:AAPL"},
            {"description": "Tesla", "proName": "NASDAQ:TSLA"},
            {"description": "Amazon", "proName": "NASDAQ:AMZN"},
            {"description": "Alphabet", "proName": "NASDAQ:GOOGL"},
            {"description": "Microsoft", "proName": "NASDAQ:MSFT"},
            {"description": "Meta", "proName": "NASDAQ:META"},
            {"description": "Dell", "proName": "NYSE:DELL"},
            {"description": "Intel", "proName": "NASDAQ:INTC"},
            {"description": "HP", "proName": "NYSE:HPQ"},
            {"description": "IBM", "proName": "NYSE:IBM"},
            {"description": "Oracle", "proName": "NYSE:ORCL"},
            {"description": "Uber", "proName": "NYSE:UBER"},
            {"description": "Salesforce", "proName": "NYSE:CRM"},
            {"description": "Visa", "proName": "NYSE:V"},
            {"description": "Airbnb", "proName": "NASDAQ:ABNB"},
            {"description": "Netflix", "proName": "NASDAQ:NFLX"},
            {"description": "Shopify", "proName": "NYSE:SHOP"},
            {"description": "Adobe", "proName": "NASDAQ:ADBE"},
            {"description": "Cisco", "proName": "NASDAQ:CSCO"},
            {"description": "Spotify", "proName": "NYSE:SPOT"}
          ],
          "colorTheme": "dark",
          "isTransparent": true,
          "displayMode": "adaptive",
          "locale": "en"          
    });

    // Append the script to the container
    widgetRef.current.appendChild(script);
  }, []); // The empty array causes this effect to only run on mount

  return (
    <div className="tradingview-widget-container" ref={widgetRef}>
      <div className="tradingview-widget-container__widget"></div>
      {/* You can customize this footer to fit the licensing agreement with TradingView */}
      <div className="tradingview-widget-copyright">
        <a href="https://www.tradingview.com" rel="noopener noreferrer" target="_blank">
          <span className="blue-text">Track all markets on TradingView</span>
        </a>
      </div>
    </div>
  );
};

export default TradingViewWidget;


