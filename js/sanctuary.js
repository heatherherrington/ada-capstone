import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';

// class Sanctuary extends Component {
//   constructor(props) {
//     super(props);
//   }
//
//   render() {
//     return (
//       <div>
//         <Header />
//         <h1>Sanctuary</h1>
//         <Footer />
//       </div>
//     );
//   }
// }

export default React.createClass({
  render() {
    return (
      <div>
        <Header />
        <h1>Sanctuary</h1>
        <Footer />
      </div>
    )
  }
})

// ReactDOM.render(<Sanctuary />, document.getElementById('content'));
