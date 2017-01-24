import React from 'react';
import Header from './header';
import Footer from './footer';
import AnimalEvent from './animal_event';
import EventAdd from './event_add';
import $ from 'jquery';

const Animal = React.createClass({
  getInitialState: function() {
    return { animal: {} }
  },

  refreshFromServer: function () {
    console.log("Animal.refreshFromServer() called.");
    let that = this;
    $.getJSON(`/sanctuary/api/animals/${this.props.params.id}`,
      function (response) {
        that.setState({animal: response.animals[0]})
      }
    );
  },

  componentDidMount() {
    console.log("Animal.componentDidMount() called.");
    this.refreshFromServer();
  },

  render() {
    var animalName = {
      display: "block",
      fontFamily: "Raleway, sans-serif",
      fontSize: "28",
      textAlign: "center"
    };
    
    let self = this;
    let onAdd = function () {
      console.log("Animal onAdd callback called.");
      self.componentDidMount();
      self.refs.eventList.componentDidMount();
    };
    return (
      <div>
        <Header />
        <h2 style={animalName}>{this.state.animal.name}</h2>
        <AnimalEvent ref="eventList" animalId={this.props.params.id}/>
        <EventAdd ref="eventAdd" animalId={this.props.params.id} onAdd={onAdd}/>
        <Footer />
      </div>
    )
  }
});

export default Animal;
