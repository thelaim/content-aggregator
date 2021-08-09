import React, { useState, useEffect } from "react";
import axios from 'axios';
import logo from './logo.svg';
import './App.css';

function App() {

    const  [people, setPeople] = useState([])

    useEffect(() => {
        axios({
            method: "GET",
            url: "http://127.0.0.1:8000/api/test-api/"
        }).then(response => {
            setPeople(response.data)
        })
    }, [])

  return (
    <div className="App">
      <h1>Hi</h1>
        <ul>
            {people.map(p => (
                <li key={p.id}>{p.name}</li>
            ))}
        </ul>
    </div>
  );
}

export default App;
