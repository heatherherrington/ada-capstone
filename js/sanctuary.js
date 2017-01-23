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
    var self = this;

    $.ajax({
      url: `/sanctuary/api/animals/${animal.id}`,
      type: 'DELETE',
      success: function(result) {
        var animals = self.state.animals;
        self.setState({ animals: animals });
      }
    });
    this.refreshFromServer();
  },

  runRender: function () {
    if (this.state.animals[0] != null) {
      var animals = this.state.animals.map((animal) =>
      <div key={animal.id}>
        <li><Link to={`/animal/${animal.id}`}>{ animal.name }</Link> <button onClick={this.deleteAnimal.bind(this, animal)}>Delete Animal</button></li>
      </div>
    );
    return (
      <ul>{animals}</ul>
    )
    };
  },

  render() {
    let self = this;
    let onAdd = function () {
      console.log("Sanctuary onAdd callback called.");
      self.refreshFromServer();
    };
    console.log("state.animals", this.state.animals);

    return (
      <div>
        <Header />
        <h1>Hope Haven Farm Sanctuary</h1>
        { this.runRender() }
        <AnimalAdd onAdd={onAdd}/>
        <Footer />
      </div>
    )
  }
});

export default Sanctuary;
