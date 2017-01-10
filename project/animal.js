import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';
import BehavioralDropdown from './components/behavioral_dropdown';
import MedicalDropdown from './components/medical_dropdown';
import Calendar from './components/calendar';

class Animal extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Header />
        <BehavioralDropdown />
        <MedicalDropdown />
        <Calendar />
        <Footer />
      </div>
    );
  }
}

ReactDOM.render(<Animal />, document.querySelector('#animal'));
