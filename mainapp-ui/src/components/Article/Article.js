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

        <div className="main">
            {article.map(c =>(
            <div className="card">
                <img src={c.url_photo} alt="No source" />
                    <div className="container">
                        <h4><b>{c.title}</b></h4>
                        <p>{c.content}</p>
                        <footer className="article-info">
                            <span><Link classname="nav-link" to={{ pathname: `/post/${c.id}/`, fromDashboard: false }}>Go details</Link></span>
                        </footer>
                    </div>
            </div>
                ))}
        </div>

    </div>
  );
}

export default Article;