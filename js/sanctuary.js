import React from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';
import { Link } from 'react-router';

export default React.createClass({
  render() {
    return (
      <div>
        <Header />
        <h1>Sanctuary</h1>
        <p><Link to="/animal">Animal</Link></p>
        <Footer />
      </div>
    )
  }
})
