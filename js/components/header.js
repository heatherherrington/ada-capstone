import React from 'react';

class Header extends React.Component {
  render() {
    var headerStyle = {
      padding: 30,
      // margin: 10,
      backgroundColor: "magenta",
      color: "white",
      display: "block",
      // fontFamily: "monospace",
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
