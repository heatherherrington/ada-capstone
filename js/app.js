import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';
import Main from './components/main';

class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Header />
        <Main  />
        <Footer />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('content'));
