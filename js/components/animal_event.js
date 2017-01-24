import React from 'react';
import $ from 'jquery';

const AnimalEvent = React.createClass({
  getInitialState: function() {
    return { events: [] }
  },

  refreshFromServer: function () {
    let that = this;
    $.getJSON(`/sanctuary/api/events/animal/${this.props.animalId}`,
      function (response) {
        that.setState({events: response.events})
      }
    );
  },

  componentDidMount() {
    this.refreshFromServer();
  },

  deleteEvent(animalEvent) {
    var message = 'Are you sure you want to delete this animal?'
    if (!confirm(message)) {
      return false
    }
    else {
      var self = this;
      var callback = this.refreshFromServer;

      $.ajax({
        url: `/sanctuary/api/events/${animalEvent.id}`,
        type: 'DELETE',
        complete: callback,
      });
    }
  },

  runRender: function () {
    var eventList = {
      padding: 5,
      display: "inline",
      fontFamily: "Raleway, sans-serif",
      fontSize: "20",
      textAlign: "center"
    };

    if (this.state.events[0] != null) {
      var animalEvents = this.state.events.map((animalEvent) => {
        return (
          <div key={animalEvent.id}>
            <li>{ animalEvent.task }, Due date: { animalEvent.due } <i className="fa fa-trash-o" aria-hidden="true" onClick={this.deleteEvent.bind(this, animalEvent)}></i></li>
          </div>
        );
      });
    }
    return (
      <ul style={eventList}>{animalEvents}</ul>
    );
  },

  render() {
    return (
      <div>
        { this.runRender() }
      </div>
    )
  }
})

AnimalEvent.defaultProps = {
  animalId: -1,
};

export default AnimalEvent;
