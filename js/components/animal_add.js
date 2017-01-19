import React from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery';

export default React.createClass({
  handleClick() {
    var name = this.refs.name.value;
    $.ajax({
      url: '/animal',
      type: 'POST',
      data: {name: name},
      success: (response) => {
        console.log('it worked!', response);
      }
    });
  },

  render() {
    return (
      <div>
        <input ref='name' placeholder='Enter the name of your animal' />
          <button onClick={this.handleClick}>Submit</button>
      </div>
    )
  }
})
