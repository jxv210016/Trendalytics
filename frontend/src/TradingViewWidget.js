import React, { useEffect, useRef } from 'react';

const TradingViewWidget = () => {
  const widgetRef = useRef(null);

  useEffect(() => {
    // Capture the current value of the ref
    const currentWidgetRef = widgetRef.current;

    const script = document.createElement('script');
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js';
    script.async = true;
    script.type = 'text/javascript';
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

    currentWidgetRef.appendChild(script);

    // Check for the branding element and hide it
    const interval = setInterval(() => {
      const branding = currentWidgetRef.querySelector('.tradingview-widget-copyright');
      if (branding) {
        branding.style.display = 'none'; // Hides the branding element
        clearInterval(interval);
      }
    }, 100);

    return () => {
      clearInterval(interval);
      // Use the captured ref value for cleanup
      if (currentWidgetRef) {
        currentWidgetRef.removeChild(script);
      }
    };
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []); // The empty array ensures this effect runs only once

  return (
    <div className="tradingview-widget-container" ref={widgetRef}>
      {/* The widget will be rendered here by the TradingView script */}
    </div>
  );
};

export default TradingViewWidget;
