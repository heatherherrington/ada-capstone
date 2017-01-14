import React from 'react';
import Header from './header';
import $ from 'jquery';


const Animal = React.createClass({
  getInitialState: function() {
    return { animal: null }
  },

  componentDidMount() {
    var that = this;

    console.log("Component mounted");
    $.getJSON(`http://localhost:5000/sanctuary/api/animals/${this.props.params.animalId}`,
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

  render() {
    return (
      <div>
        <Header />
        { this.runRender() }
      </div>
    )
  }
})

export default Animal;