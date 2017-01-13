import React from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';
import { Link } from 'react-router';
import Main from './components/main';
import $ from 'jquery';

export default React.createClass({
  getInitialState: function() {
    return { animals: [] }
  },

  componentDidMount() {
    var that = this;

    console.log("Component mounted");
    $.getJSON('http://localhost:5000/sanctuary/api/animals',
    function(response) {
      that.setState({ animals: response.animals })
    }
  )},

  runRender: function() {
    console.log("runRender!");
    if(this.state.animals[0] != null) {
      console.log("rendering")
      var animals = this.state.animals.map((animal) =>
        <div>
          <h3>{ animal.name }</h3>
        </div>
      );
      return (
        <div>{animals}</div>
      )
      console.log("I hate this.");
    }
  },

  render() {
    console.log("state.animals", this.state.animals);

    return (
      <div>
        <Header />
        <h1>Sanctuary</h1>
        { this.runRender() }
        <p><Link to="/animal">Animal</Link></p>
        <Footer />
      </div>
    )
  }
})
