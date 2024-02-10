// src/components/Header.js

import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Header.css';

function Header() {
  return (
    <div className="navbar">
      <Link to="/shop" className="active">Shop</Link>
      <Link to="/about">About</Link>
      <Link to="/contact">Contact</Link>
      {/* Add more links as needed */}
    </div>
  );
}

export default Header;