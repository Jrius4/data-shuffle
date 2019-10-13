import React from 'react';
import './App.css';
import Users from './users/Users';
import Visitors from './users/Visitors';


const App = () =>(
  <React.Fragment>
    <div>
      <h2>Datastore</h2>
      <h3>Users</h3>
      <Users/>
      <h3>Vistiors</h3>
      <Visitors/>
    </div>
  </React.Fragment>
)
export default App;
