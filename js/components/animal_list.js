import React from 'react';
import Main from './main';
import $ from 'jquery';

var AnimalList = React.createClass({
  getInitialState() {
    return { animals: [] }
  },

  componentDidMount() {
    var that = this;

    console.log("Component mounted");
    $.getJSON('http://sanctuarysecretary.com/sanctuary/api/animals',
    function(response) { that.setState({ animals: response }) }
  )},


  render() {
    console.log("state.animals", this.state.animals);

    // var animals = this.state.animals.map((animal) => {
      return (
        <div>
          // key={ animals }>
          //   <h3>{ animal.name }</h3>
        </div>
      )
    // });
  }
});

export default AnimalList;
