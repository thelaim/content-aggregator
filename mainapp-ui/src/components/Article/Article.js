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

        {/*{article.map(c =>(*/}
        {/*    <div className="card" style={{width: '18rem'}}>*/}
        {/*        <img src={c.url_photo} className="card-img-top"/>*/}
        {/*        <div className="card-body">*/}
        {/*            <h5 className="card-title">{c.title}</h5>*/}
        {/*            <p className="card-text">{c.content}</p>*/}
        {/*            <Link classname="nav-link" to={{ pathname: `/post/${c.id}/`, fromDashboard: false }}>Go</Link>*/}
        {/*        </div>*/}
        {/*    </div>*/}
        {/*))}*/}


        <main className="main columns">
            {article.map(c =>(
            <section className="column main-column">

                <div className="columns">
                    <div className="column nested-column">
                        <a className="article" href="#">
                            <figure className="article-image is-16by9">
                                <img src={c.url_photo} alt="No source" />
                            </figure>
                            <div className="article-body">
                                <h2 className="article-title">
                                    {c.title}
                                </h2>
                                <p className="article-content">
                                    {c.content}
                                </p>
                                <footer className="article-info">
                                    <span><Link classname="nav-link" to={{ pathname: `/post/${c.id}/`, fromDashboard: false }}>Go details</Link></span>
                                </footer>
                            </div>
                        </a>
                    </div>
                </div>
            </section>
         ))}
        </main>

    </div>
  );
}

export default Article;