import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';
import AnimalDropdown from './components/animal_dropdown';
import Calendar from './components/calendar';

class Sanctuary extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Header />
        <AnimalDropdown />
        <Calendar />
        <Footer />
      </div>
    );
  }
}

ReactDOM.render(<Sanctuary />, document.querySelector('#sanctuary'));
