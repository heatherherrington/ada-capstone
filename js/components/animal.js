import React from 'react';
import Header from './header';
import Footer from './footer';
import AnimalEvent from './animal_event';
import EventAdd from './event_add';
import $ from 'jquery';

const Animal = React.createClass({
  getInitialState: function() {
    return { animal: null }
  },

  componentDidMount() {
    var that = this;

    console.log("Component mounted");
    $.getJSON(`http://localhost:5000/sanctuary/api/animals/${this.props.params.id}`,
    function(response) {
      that.setState({ animal: response.animal })
    }
  )},

  runRender: function() {
    if(this.state.animal != null) {
      return (
        <div>
          <h2>{this.state.animal.name}</h2>
        </div>
      )
    }
  },

  addTask: function(e) {
    var taskArray = this.state.tasks;

    taskArray.push(
      {
        text: this._inputElement.value,
        key: Date.now()
      }
    );

    this.setState({
      tasks: taskArray
    });

    this._inputElement.value = "";

    e.preventDefault();
  },

  render() {
    console.log(this.props.params.id);

    return (
      <div>
        <Header />
        { this.runRender() }
        <AnimalEvent />
        <EventAdd />
        <Footer />
      </div>
    )
  }
})

export default Animal;
