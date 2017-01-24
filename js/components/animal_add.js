import React from 'react';
import $ from 'jquery';

export default React.createClass({
  handleClick() {
    let callback = this.props.onAdd;
    let name = this.refs.name.value;
    $.ajax({
      url: '/sanctuary/api/animals',
      type: 'POST',
      data: {name: name},
      complete: callback,
    });
  },

  render() {
    var addingAnimalForm = {
      paddingBottom: 10,
      display: "block",
      fontFamily: "Raleway, sans-serif",
      fontSize: "20",
      textAlign: "center"
    };

    return (
      <div style={addingAnimalForm}>
        <input ref='name' placeholder='Animal name'/>
        <button onClick={this.handleClick}>Submit</button>
      </div>
    )
  }
})
