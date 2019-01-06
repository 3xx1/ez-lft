import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';

// Containers
import PageOne from '../PageOne/loadable';
import PageTwo from '../PageTwo/loadable';

// Styles
import './style.scss';

class App extends Component {
  render() {
    return (
      <div className="app">
        <div className="app-contents">
          <Switch>
            <Route path="/page-one" component={PageOne} />
            <Route path="/page-two" component={PageTwo} />
          </Switch>
        </div>
      </div>
    );
  }
}

export default App;
