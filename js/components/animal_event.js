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

  runRender: function () {
    if (this.state.events[0] != null) {
      var animalEvents = this.state.events.map((animalEvent) => {
        return (
          <div key={animalEvent.id}>
            <li>{ animalEvent.task }, Due date: { animalEvent.due }</li>
          </div>
        );
      });
    }
    return (
      <ul>{animalEvents}</ul>
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
