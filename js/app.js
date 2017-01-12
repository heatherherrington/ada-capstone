import React from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';
import Main from './components/main';
import { Link } from 'react-router';

export default React.createClass({
  render() {
    return (
      <div>
        <Header />
        <Main />
        <p><Link to="/sanctuary">Sanctuary</Link></p>
        <Footer />
      </div>
    )
  }
})
