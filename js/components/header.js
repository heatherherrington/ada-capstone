import React from 'react';
import { Link } from 'react-router';
import ReactDOM from 'react-dom';

class Header extends React.Component {
  render() {
    var headerStyle = {
      padding: 50,
      backgroundColor: "purple",
      color: "white",
      display: "block",
      fontFamily: "Mogra, cursive",
      fontSize: "50",
      textAlign: "center",
      textDecoration: "none",
      fontWeight: "bold"
    };

    return (
      <div>
        <Link to={`/`} style={headerStyle}>Sanctuary Secretary</Link>
      </div>
    );
  }
};

export default Header;
