import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';

// Containers
import Analyze from '../Analyze/loadable';
import Results from '../Results/loadable';

// Styles
import './style.scss';

class App extends Component {
  render() {
    return (
      <div className="app">
        <div className="app-contents">
          <Switch>
            <Route path="/analyze" component={Analyze} />
            <Route path="/results" component={Results} />
          </Switch>
        </div>
      </div>
    );
  }
}

export default App;
