import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';
import Main from './components/main';

class App extends Component {
  // constructor(props) {
  //   super(props);
  //
  // }

  render: function() {
    return (
      <div>
        <h1>Testing</h1>
        <Header />
        <Main  />
        <Footer />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.querySelector('#content'));
