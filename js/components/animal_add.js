import React from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery';

export default React.createClass({
  render: function() {
    return (
      <div>
        <form>
          <input placeholder="add animal name">
          </input>
          <button type="submit">Add Animal</button>
        </form>
      </div>
    );
  }
})
