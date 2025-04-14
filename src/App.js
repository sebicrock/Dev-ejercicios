import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import EventList from './components/EventList';

function App() {
  return (
    <Router>
      <div>
        <h1>Event Management App</h1>
        <Switch>
          <Route path="/" exact component={EventList} />
          {/* Add more routes as needed */}
        </Switch>
      </div>
    </Router>
  );
}

export default App;