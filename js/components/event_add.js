import React from 'react';
import $ from 'jquery';

const EventAdd = React.createClass({
  handleClick() {
    let task = this.refs.task.value;
    let due = this.refs.due.value;
    let callback = this.props.onAdd;
    $.ajax({
      url: '/sanctuary/api/events',
      type: 'POST',
      data: {task: task, due: due, animal_id: this.props.animalId},
      complete: callback,
    });
    this.refs.task.value = null;
    this.refs.due.value = null;
  },

  render: function () {
    var iconFont = {
      paddingLeft: 15,
    };

    var addingEventForm = {
      paddingBottom: 10,
      display: "block",
      fontFamily: "Roboto, sans-serif",
      fontSize: "20",
      textAlign: "center"
    };

    return (
      <div style={addingEventForm}>
        <input ref='task' placeholder='Task'/>
        <input ref='due' placeholder='Due date'/>
        <input ref='animal_id' type="hidden" value={this.props.animalId}/>
        <i className="fa fa-plus" style={iconFont} aria-hidden="true" onClick={this.handleClick}></i>
      </div>
    );
  }
});

EventAdd.defaultProps = {
  animalId: -1,
  onAdd: function () {
  },
};

export default EventAdd;
