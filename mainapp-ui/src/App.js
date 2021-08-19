import React, { useState, useEffect } from "react";
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Article from "./components/Article/Article";
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom'
import ArticleDetail from "./components/Post/ArticleDetail";

function App() {

  return (
    <div className="App">
        <Router>
            <header><h1><Link to={{ pathname: `/`, fromDashboard: false }}>Главная</Link></h1></header>

            <Switch>
                <Route path="/" exact component={Article}/>
                <Route path="/post/:id" exact component={ArticleDetail}/>
            </Switch>
        </Router>

    </div>
  );
}

export default App;
