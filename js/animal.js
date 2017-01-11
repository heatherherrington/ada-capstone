import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Header from './components/header';
import Footer from './components/footer';

// class Animal extends Component {
//   constructor(props) {
//     super(props);
//   }
//
//   render() {
//     return (
//       <div>
//         <Header />
//         <h1>Animal!</h1>
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
        <h1>Animal</h1>
        <Footer />
      </div>
    )
  }
})

// export default Animal;

// ReactDOM.render(<Animal />, document.getElementById('content'));
