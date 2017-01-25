import React from 'react';
import Header from './components/header';
import Footer from './components/footer';
import { Link } from 'react-router';
import AnimalAdd from './components/animal_add'
import $ from 'jquery';

const Sanctuary = React.createClass({

  getInitialState: function() {
    return { animals: [] }
  },

  refreshFromServer: function () {
    let self = this;
    $.getJSON('/sanctuary/api/animals',
      function (response) {
        self.setState({animals: response.animals});
      }
    );
  },

  componentDidMount() {
    this.refreshFromServer();
  },

  deleteAnimal(animal) {
    var message = 'Are you sure you want to delete this animal?'
    if (!confirm(message)) {
      return false
    }
    else {
      var self = this;
      var callback = this.refreshFromServer;

      $.ajax({
        url: `/sanctuary/api/animals/${animal.id}`,
        type: 'DELETE',
        complete: callback,
      });
    }
  },

  runRender: function () {
    var animalList = {
      padding: 5,
      display: "inline",
      fontFamily: "Roboto, sans-serif",
      fontSize: "20",
      textAlign: "center"
    };

    if (this.state.animals[0] != null) {
      var animals = this.state.animals.map((animal) =>
      <div key={animal.id}>
        <li><Link to={`/animal/${animal.id}`}>{ animal.name }</Link> <i className="fa fa-trash-o" aria-hidden="true" onClick={this.deleteAnimal.bind(this, animal)}></i></li>
      </div>
    );
    return (
      <ul style={animalList}>{animals}</ul>
    )
    };
  },

  render() {
    var sanctuaryName = {
      display: "block",
      fontFamily: "Roboto, sans-serif",
      fontSize: "28",
      textAlign: "center"
    };

    let self = this;
    let onAdd = function () {
      self.refreshFromServer();
    };

    return (
      <div>
        <Header />
        <h1 style={sanctuaryName}>Hope Haven Farm Sanctuary</h1>
        { this.runRender() }
        <AnimalAdd onAdd={onAdd}/>
        <Footer />
      </div>
    )
  }
});

export default Sanctuary;
