import React from 'react';
import ReactDOM from 'react-dom';

class Header extends React.Component {
  render() {
    var headerStyle = {
      padding: 20,
      backgroundColor: "purple",
      color: "white",
      display: "block",
      fontFamily: "Mogra, cursive",
      fontSize: "32",
      textAlign: "center"
    };

    return (
      <div style={headerStyle}>
        <nav>
          <h1>Sanctuary Secretary</h1>
        </nav>
      </div>
    );
  }
};

export default Header;
