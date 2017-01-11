import React from 'react';

class Header extends React.Component {
  render() {
    var headerStyle = {
      padding: 30,
      // margin: 10,
      backgroundColor: "lightgrey",
      color: "black",
      display: "block",
      // fontFamily: "monospace",
      fontSize: "32",
      textAlign: "center"
    };

    return (
      <div style={headerStyle}>
        <nav>
          <h1>Sanctuary Supplement</h1>
        </nav>
      </div>
    );
  }
};

export default Header;
