import React from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';
import { Link } from 'react-router';
import Main from './components/main';
import $ from 'jquery';

export default React.createClass({
  // mixins: [ParseReact.Mixin],

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
    if(this.state.animals[0] != null) {
      var animals = this.state.animals.map((animal) =>
        <div key={animal.id}>
          <li><Link to={`/animal/${animal.id}`}>{ animal.name }</Link></li>
        </div>
      );
      return (
        <ul>{animals}</ul>
      )
    }
  },

  render() {
    console.log("state.animals", this.state.animals);

    return (
      <div>
        <Header />
        <h1>Sanctuary</h1>
        { this.runRender() }
        <Footer />
      </div>
    )
  }
})
