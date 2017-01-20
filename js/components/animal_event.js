import React from 'react';
import ReactDOM from 'react-dom';

const AnimalEvent = React.createClass({
  getInitialState: function() {
    return { events: [] }
  },

  componentDidMount() {
    var that = this;

    $.getJSON(`http://www.sanctuarysecretary.com/sanctuary/api/events`,
    function(response) {
      that.setState({ events: response.events })
    }
  )},

  runRender: function() {
    if(this.state.events[0] != null) {
      var animalEvents = this.state.events.map((animalEvent) =>
        {
          if(animalEvent.animal_id == this.props.animalId) {
            return (
              <div key={animalEvent.id}>
                <li>{ animalEvent.task }, Due date: { animalEvent.due }</li>
              </div>
            )
          }
        }
      );
      return (
        <ul>{animalEvents}</ul>
      )
    }
  },

  render() {
    return (
      <div>
        { this.runRender() }
      </div>
    )
  }
})

export default AnimalEvent;
