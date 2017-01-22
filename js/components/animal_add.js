import React from 'react';
import $ from 'jquery';

export default React.createClass({
  // getInitialState: function() {
  //   return { name: null }
  // },

  handleClick() {
    let callback = this.props.onAdd;
    let name = this.refs.name.value;
    $.ajax({
      url: '/animal',
      type: 'POST',
      data: {name: name},
      complete: callback,
    });
  },

  render() {
    return (
      <div>
        <input ref='name' placeholder='Enter the name of your animal'/>
        <button onClick={this.handleClick}>Submit</button>
      </div>
    )
  }
})
