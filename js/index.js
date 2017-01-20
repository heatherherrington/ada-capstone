import React from 'react'
import { render } from 'react-dom'
import App from './app'
import { Router, Route, browserHistory } from 'react-router'
import Animal from './components/animal'
import Sanctuary from './sanctuary'

render((
  <Router history={browserHistory}>
    <Route path="/" component={App} />
    {/* add the routes here */}
    <Route path="/animal/:id" component={Animal}/>
    <Route path="/sanctuary" component={Sanctuary}/>
  </Router>
), document.getElementById('app'))
