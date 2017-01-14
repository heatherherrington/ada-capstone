import React from 'react'
import { render } from 'react-dom'
import App from './app'
import { Router, Route, browserHistory } from 'react-router'
import Animals from './animals'
import Animal from './components/animal'
import Sanctuary from './sanctuary'

render((
  <Router history={browserHistory}>
    <Route path="/" component={App}/>
    {/* add the routes here */}
    <Route path="/animals" component={Animals}/>
    <Route path="/animal/:animalId" component={Animal}/>
    <Route path="/sanctuary" component={Sanctuary}/>
  </Router>
), document.getElementById('app'))
