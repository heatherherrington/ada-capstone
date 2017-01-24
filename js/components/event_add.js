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
    var addingEventForm = {
      paddingBottom: 10,
      display: "block",
      fontFamily: "Raleway, sans-serif",
      fontSize: "20",
      textAlign: "center"
    };

    console.log("EventAdd.render()");
    return (
      <div style={addingEventForm}>
        <input ref='task' placeholder='Task'/>
        <input ref='due' placeholder='Due date'/>
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
