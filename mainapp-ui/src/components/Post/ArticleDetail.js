import React, { useEffect, useState } from "react";
import axios from "axios";

function ArticleDetail({ match }) {
    const [post, setPost] = useState({})
    const id = match.params.id

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
        </div>

    )
}

export default ArticleDetail;