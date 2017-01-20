import React from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';
import { Link } from 'react-router';
import Main from './components/main';
import AnimalAdd from './components/animal_add'
import $ from 'jquery';

export default React.createClass({

  getInitialState: function() {
    return { animals: [] }
  },

  componentDidMount() {
    var that = this;

    $.getJSON('http://sanctuarysecretary.com/sanctuary/api/animals',
    function(response) {
      that.setState({ animals: response.animals })
    }
  )},

  // componentWillMount() {
  //   const id = setInterval(this.fetchData, 5000);
  //   this.setState({intervalId: id});
  // },
  //
  // fetchData() {
  //   var that = this;
  //
  //   $.getJSON('http://localhost:5000/sanctuary/api/animals',
  //   function(response) {
  //     that.setState({ animals: response.animals })
  //   }
  // )},

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
        <h1>Hope Haven Farm Sanctuary</h1>
        { this.runRender() }
        <AnimalAdd />
        <Footer />
      </div>
    )
  }
})
