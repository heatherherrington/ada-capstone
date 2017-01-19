import React from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery';

export default React.createClass({
  render: function() {
    return (
      <div>
        <form onSubmit={this.addTask}>
          <input placeholder="add task name">
          </input>
          <button type="submit">Add Task</button>
        </form>
      </div>
    );
  }
})
