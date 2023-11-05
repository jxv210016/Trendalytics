// LogoAnimation.js or wherever your LogoAnimation component is defined
import React from 'react';
import ballImage from '/Users/jayvanam/Documents/GitHub/Trendalytics/frontend/src/ball.png';
import textImage from '/Users/jayvanam/Documents/GitHub/Trendalytics/frontend/src/text.png';
import './LogoAnimation.css';

const LogoAnimation = () => {
  return (
    <div className="logo-container">
      <div className="ball" style={{ backgroundImage: `url(${ballImage})` }}></div>
      <div className="text" style={{ backgroundImage: `url(${textImage})` }}></div>
    </div>
  );
};

export default LogoAnimation;