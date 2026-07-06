import React from 'react';
import keycloak from './keycloak';
import Dashboard from './pages/Dashboard/Dashboard';

const App= ()=> {
  
  const handleLogout = () => {
    keycloak.logout();
  };

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif', maxWidth: '800px', margin: '0 auto' }}>
      <h1>Success! You are logged in.</h1>
      <p>Welcome to your secure React application.</p>
      
      <div style={{ marginTop: '20px', padding: '15px', background: '#f0f4f8', borderRadius: '8px', border: '1px solid #d9e2ec' }}>
        <h3 style={{ margin: '0 0 10px 0' }}>Your Secure Identity Profile</h3>
        <p><strong>Username:</strong> {keycloak.tokenParsed?.preferred_username}</p>
        <p><strong>Session ID:</strong> {keycloak.sessionId}</p>
      </div>

      <button 
        onClick={handleLogout}
        style={{ 
          marginTop: '20px', 
          padding: '10px 20px', 
          backgroundColor: '#e12d39', 
          color: 'white', 
          border: 'none', 
          borderRadius: '4px',
          cursor: 'pointer',
          fontWeight: 'bold'
        }}
      >
        Logout
      </button>
      <Dashboard />
    </div>
  );
}

export default App;