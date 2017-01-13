import React from 'react';

const Animal = React.createClass({
  componentDidMount() {
    this.setState({
      // route components are rendered with useful information, like URL params
      animal: findAnimalById(this.props.params.animalId)
    })
  },

  render() {
    return (
      <div>
        <h2>{this.state.animal.name}</h2>
      </div>
    )
  }
})

export default Animal;
