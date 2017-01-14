import React from 'react';

class Main extends React.Component {
  render() {
    var mainStyle = {
      color: "black",
      display: "block",
      width: "300",
      // fontFamily: "monospace",
      fontSize: "20",
      textAlign: "center"
    };

    return (
      <div style={mainStyle}>
        This will describe what the page is used for and the intended audience.
      </div>
    );
  }
};

export default Main;
