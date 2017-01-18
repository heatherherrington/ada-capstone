import React from 'react';
import ReactDOM from 'react-dom';
import $ from 'jquery';

export default React.createClass({
  getInitialState: function() {
    return { events: [] }
  },

  componentDidMount() {
    var that = this;

    console.log("Component mounted");
    $.getJSON(`http://localhost:5000/sanctuary/api/events`,
    function(response) {
      that.setState({ events: response.events })
    }
  )},

  runRender: function() {
    if(this.state.events[0] != null) {
      var events = this.state.events.map((animalEvent) =>
        // {
        //   if(animalEvent.animal_id == this.params.animal.id) {
            <div key={animalEvent.id}>
              <li>{ animalEvent.task }</li>
            </div>
        //   }
        // }
      );
      return (
        <ul>{events}</ul>
      )
    }
  },

  render() {
    console.log("state.events", this.state.events);

    return (
      <div>
        { this.runRender() }
      </div>
    )
  }
})
