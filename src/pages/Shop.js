import React from 'react';
import artworks from '../data/artworks'; // Adjust the path as necessary
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faShoppingCart } from '@fortawesome/free-solid-svg-icons';
import '../styles/Shop.css'; 
 // Adjust the path as necessary
function Shop() {
  return (
    <div className="shop">
      <h1>Artworks for Sale</h1>
      <div className="artworks-grid">
        {artworks.map((artwork) => (
          <div key={artwork.id} className="artwork">
            <img src={artwork.image} alt={artwork.title} />
            <h2>{artwork.title}</h2>
            <p>{artwork.price} <button><FontAwesomeIcon icon={faShoppingCart} /></button></p>  
           
            <p>{artwork.description}</p>
           
           
          </div>
        ))}
      </div>
    </div>
  );
}


export default Shop;