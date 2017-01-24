import React from 'react';

class Footer extends React.Component {
  render() {
    var footerStyle = {
      padding: 10,
      backgroundColor: "lightgrey",
      color: "black",
      display: "block",
      fontFamily: "Raleway, sans-serif",
      fontSize: "16",
      textAlign: "center"
    };

    return (
      <div style={footerStyle}>
        Copyright 2017
      </div>
    );
  }
};

export default Footer;
