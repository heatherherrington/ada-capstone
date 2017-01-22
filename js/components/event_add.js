import React from 'react';
import $ from 'jquery';

const EventAdd = React.createClass({
  handleClick() {
    console.log("EventAdd.handleClick()");
    let task = this.refs.task.value;
    let due = this.refs.due.value;
    let callback = this.props.onAdd;
    $.ajax({
      url: '/sanctuary/api/events',
      type: 'POST',
      data: {task: task, due: due, animal_id: this.props.animalId},
      complete: callback,
    });
  },

  render: function () {
    console.log("EventAdd.render()");
    return (
      <div>
        <input ref='task' placeholder='Enter the task'/>
        <input ref='due' placeholder='Enter the due date, in month/date/year format'/>
        <input ref='animal_id' type="hidden" value={this.props.animalId}/>
        <button onClick={this.handleClick}>Add Task</button>
      </div>
    );
  }
});

EventAdd.defaultProps = {
  animalId: -1,
  onAdd: function () {
    console.log("Default callback called");
  },
};

export default EventAdd;
