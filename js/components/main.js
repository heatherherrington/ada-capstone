import React from 'react';

class Main extends React.Component {
  render() {
    var mainStyle = {
      paddingTop: 20,
      width: 500,
      marginLeft: "auto",
      marginRight: "auto",
      fontFamily: "Roboto, sans-serif",
      fontSize: "20",
      textAlign: "center"
    };

    return (
      <div style={mainStyle}>
        There is software available for large-scale animal sanctuaries and shelters. However, nothing exists for the "little guy". Until now. This is an open-source project specifically designed for smaller rescues, to keep track of the needs of their residents.
      </div>
    );
  }
};

export default Main;
