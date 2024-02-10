import React from 'react';

function Footer() {
  // Replace '#' with your actual Instagram link
  const instagramLink = '#'; 
  // Your email address
  const email = 'jody@example.com'; 

  return (
    <footer>
      <p>Follow us on Instagram: <a href={instagramLink} target="_blank" rel="noopener noreferrer">Instagram</a></p>
      <p>Email: <a href={`mailto:${email}`}>{email}</a></p>
    </footer>
  );
}

export default Footer;