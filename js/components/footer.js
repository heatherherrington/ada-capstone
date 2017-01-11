import React from 'react';

class Footer extends React.Component {
  render() {
    var footerStyle = {
      padding: 10,
      // margin: 10,
      backgroundColor: "lightgrey",
      color: "black",
      display: "block",
      // fontFamily: "monospace",
      // fontSize: "32",
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
