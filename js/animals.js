import React from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';

export default React.createClass({
  render() {
    return (
      <div>
        <Header />
        <h1>Testing</h1>
        <Footer />
      </div>
    )
  }
})
