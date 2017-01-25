import React from "react";
import $ from "jquery";

const AnimalEventItem = React.createClass({
  getInitialState() {
    return {
      editing: false,
      task: this.props.event.task,
      due: this.props.event.due,
    };
  },

  beginEditing() {
    this.setState({editing: true});
  },

  commitEditing() {
    let self = this;
    let payload = {};
    let new_task_value = this.refs.task.value;
    let new_due_value = this.refs.due.value;

    if (new_task_value !== this.props.event.task) {
      payload["task"] = new_task_value;
    }

    if (new_due_value !== this.props.event.due) {
      payload["due"] = new_due_value;
    }

    let callback = function () {
      self.props.onCommitEdit();
      self.setState({
        editing: false,
        task: self.refs.task.value,
        due: self.refs.due.value,
      });
    };

    $.ajax({
      url: `/sanctuary/api/events/${this.props.event.id}`,
      type: 'PATCH',
      data: payload,
      complete: callback,
    });
  },

  cancelEditing() {
    this.setState(this.getInitialState());
  },

  deleteEvent() {
    var message = 'Are you sure you want to delete this task?'
    if (!confirm(message)) {
      return false
    } else {
      let callback = this.props.onDelete;
      $.ajax({
        url: `/sanctuary/api/events/${this.props.event.id}`,
        type: 'DELETE',
        complete: callback,
      });
    }
  },

  runRender: function () {
    var iconFont = {
      paddingLeft: 15,
    };

    var eventEditForm = {
      fontFamily: "Roboto, sans-serif",
      fontSize: "20",
      textAlign: "center"
    };

    if (!this.state.editing) {
      return (
        <div key={this.props.event.id}>
          <li>{ this.props.event.task }, Due date: { this.props.event.due }
            <i className="fa fa-pencil" style={iconFont} aria-hidden="true" onClick={this.beginEditing}></i>
            <i className="fa fa-trash-o" style={iconFont} aria-hidden="true" onClick={this.deleteEvent}></i>
          </li>
        </div>
      );
    } else {
      return (
        <div key={this.props.event.id}>
          <li>
            <input style={eventEditForm} ref='task' defaultValue={this.state.task}/>
            <input style={eventEditForm} ref='due' defaultValue={this.state.due}/>
            <input ref='event_id' type="hidden" value={this.props.event.id}/>
            <input ref='animal_id' type="hidden" value={this.props.event.animal_id}/>
            <i className="fa fa-check-circle-o" style={iconFont} aria-hidden="true" onClick={this.commitEditing}></i>
            <i className="fa fa-undo" style={iconFont} aria-hidden="true" onClick={this.cancelEditing}></i>
          </li>
        </div>
      );
    }
  },

  render() {
    return (
      <div>
        { this.runRender() }
      </div>
    )
  }
});

AnimalEventItem.defaultProps = {
  event: {},
  onDelete: function () {
  },
  onCommitEdit: function () {
  },
};

export default AnimalEventItem;
