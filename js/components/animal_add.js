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
    var iconFont = {
      paddingLeft: 15,
    };

    var addingAnimalForm = {
      paddingBottom: 10,
      display: "block",
      fontFamily: "Roboto, sans-serif",
      fontSize: "20",
      textAlign: "center"
    };

    return (
      <div style={addingAnimalForm}>
        <input ref='name' placeholder='Animal name'/>
        <i className="fa fa-paw" style={iconFont} aria-hidden="true" onClick={this.handleClick}></i>
      </div>
    )
  }
})
