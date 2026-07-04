import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import keycloak from './keycloak.js'

const root = ReactDOM.createRoot(document.getElementById('root'))

keycloak.init({ onLoad: 'login-required' })
  .then((authenticated) => {
    if (!authenticated) {
      window.location.reload();
    } else {
      console.log("Authenticated with Keycloak!");
      
      root.render(
        <React.StrictMode>
          <App />
        </React.StrictMode>,
      )
    }
  })
  .catch((error) => {
    console.error("Keycloak initialization failed. Is Docker running?", error);
    root.render(
      <div style={{ padding: '20px', color: 'red' }}>
        <h1>Error connecting to Keycloak</h1>
        <p>Make sure your Docker container is running and configured correctly!</p>
      </div>
    );
  });