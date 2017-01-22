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

  componentDidMount() {
    var that = this;

    $.getJSON(`http://localhost;5000/sanctuary/api/animals/${this.props.params.id}`,
    function(response) {
      that.setState({ animal: response.animals[0] })
    }
  )},

  // runRender: function() {
  //   console.log("Getting to animal runRender");
  //   console.log("Animal ID", this.props.params.id);
  //   console.log("animal name", this.props.params.name);
  //   if(this.props.params.id != null) {
  //     var animalName = this.props.params.name;
  //     return (
  //         <h2>{animalName}</h2>
  //     )
  //   }
  // },

  render() {
    return (
      <div>
        <Header />
        <h2>{this.state.animal.name}</h2>
        <AnimalEvent animalId={this.props.params.id} />
        <EventAdd animalId={this.props.params.id}/>
        <Footer />
      </div>
    )
  }
})

export default Animal;
