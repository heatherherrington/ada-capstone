import React from 'react'
import { render } from 'react-dom'
import App from './app'
import { Router, Route, hashHistory } from 'react-router'
import Animal from './animal'
import Sanctuary from './sanctuary'

render((
  <Router history={hashHistory}>
    <Route path="/" component={App}/>
    {/* add the routes here */}
    <Route path="/animal" component={Animal}/>
    <Route path="/sanctuary" component={Sanctuary}/>
  </Router>
), document.getElementById('app'))
