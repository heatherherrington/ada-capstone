import React from 'react';

class Main extends React.Component {
  render() {
    var mainStyle = {
      paddingTop: 20,
      width: 200,
      marginLeft: "auto",
      marginRight: "auto",
      fontFamily: "Raleway, sans-serif",
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
