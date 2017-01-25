import React from 'react';
import AnimalEventItem from './animal_event_item';
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

  eventDidUpdate(animalEvent) {
    this.refreshFromServer();
  },

  eventDidDelete(animalEvent) {
    this.refreshFromServer();
  },

  runRender: function () {
    var eventList = {
      padding: 5,
      display: "inline",
      fontFamily: "Roboto, sans-serif",
      fontSize: "20",
      textAlign: "center"
    };

    if (this.state.events[0] != null) {
      var animalEvents = this.state.events.map((animalEvent) => {
        return (
          <AnimalEventItem key={animalEvent.id}
                          event={animalEvent}
                          onDelete={this.eventDidDelete.bind(this, animalEvent)}
                          onCommitEdit={this.eventDidUpdate.bind(this, animalEvent)}/>
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
