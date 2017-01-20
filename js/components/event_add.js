import React from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery';

export default React.createClass({
  handleClick() {
    var task = this.refs.task.value;
    var due = this.refs.due.value;
    var animal_id = this.refs.animal_id.value
    console.log("task", task);
    console.log("due", due);
    $.ajax({
      url: '/task',
      type: 'POST',
      data: {task: task, due: due, animal_id: this.props.animalId},
    });
  },

  render: function() {
    console.log(this.props.animalId)
    return (
      <div>
        <input ref='task' placeholder='Enter the task' />
        <input ref='due' placeholder='Enter the due date, in month/date/year format' />
        <input ref='animal_id' type="hidden" value={this.props.animalId} />
          <button onClick={this.handleClick}>Add Task</button>
      </div>
    );
  }
})
