import 'bootstrap/dist/css/bootstrap.min.css';
import {useEffect, useState} from "react";
import axios from 'axios';
import { Link } from "react-router-dom";

function Article() {

    const [article, setArticle] = useState([])


    useEffect(()=>{
        axios({
            method: "GET",
            url: 'http://127.0.0.1:8000/api/article-test/'
        }).then(response =>{
            setArticle(response.data.data)
        })
    }, [])

  return (
    <div className="App">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <a className="navbar-brand" href="#">Navbar</a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        {article.map(c =>(
                            <li className="nav-item">
                                <Link classname="nav-link" to={{ pathname: `/post/${c.id}/`, fromDashboard: false }}>{c.title}</Link>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </nav>
    </div>
  );
}

export default Article;