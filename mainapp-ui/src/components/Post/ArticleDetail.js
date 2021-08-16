import React, { useEffect, useState } from "react";
import axios from "axios";
import {Link} from "react-router-dom";

function ArticleDetail({ match }) {
    const [post, setPost] = useState({})
    const id = match.params.id

    document.cookie = `article-test-cookie-id=${id}`;

    useEffect(()=>{
        axios({
            method: "GET",
            url: `http://127.0.0.1:8000/api/article/${id}/`
        }).then(response => {
            setPost(response.data)
        })
    }, [id])

    return (
        <div>
            Post with id {post.id}
            <p>Title <strong>{post.title}</strong></p>
            <p>{post.content}</p>
            <p><Link classname="nav-link" to={{ pathname: `/setcookie/${post.id}/`, fromDashboard: false }}>Хочу больше такого контента</Link></p>
            <p><a target="_blank" href={post.url_article}>Ссылка на статью</a></p>
        </div>

    )
}

export default ArticleDetail;