(this["webpackJsonpmainapp-ui"]=this["webpackJsonpmainapp-ui"]||[]).push([[0],{33:function(e,t,c){},34:function(e,t,c){},59:function(e,t,c){"use strict";c.r(t);var n=c(0),a=c.n(n),i=c(27),s=c.n(i),r=(c(33),c(34),c(17),c(12)),l=c(11),o=c.n(l),j=c(8),d=c(1);var h=function(){var e=Object(n.useState)([]),t=Object(r.a)(e,2),c=t[0],a=t[1];return Object(n.useEffect)((function(){o()({method:"GET",url:"http://127.0.0.1:8000/api/article-test/"}).then((function(e){a(e.data.data)}))}),[]),Object(d.jsx)("div",{className:"App",children:Object(d.jsx)("main",{className:"main columns",children:c.map((function(e){return Object(d.jsx)("section",{className:"column main-column",children:Object(d.jsxs)("a",{className:"article first-article",href:"#",children:[Object(d.jsx)("figure",{className:"article-image is-4by3",children:Object(d.jsx)("img",{src:e.url_photo,alt:"No source"})}),Object(d.jsxs)("div",{className:"article-body",children:[Object(d.jsx)("h2",{className:"article-title",children:e.title}),Object(d.jsx)("p",{className:"article-content",children:e.content}),Object(d.jsx)("footer",{className:"article-info",children:Object(d.jsx)("span",{children:Object(d.jsx)(j.b,{classname:"nav-link",to:{pathname:"/post/".concat(e.id,"/"),fromDashboard:!1},children:"Go details"})})})]})]})})}))})})},b=c(2);var m=function(e){var t=e.match,c=Object(n.useState)({}),a=Object(r.a)(c,2),i=a[0],s=a[1],l=t.params.id;return document.cookie="article-test-cookie-id=".concat(l),Object(n.useEffect)((function(){o()({method:"GET",url:"http://127.0.0.1:8000/api/article/".concat(l,"/")}).then((function(e){s(e.data)}))}),[l]),Object(d.jsxs)("div",{children:["Post with id ",i.id,Object(d.jsxs)("p",{children:["Title ",Object(d.jsx)("strong",{children:i.title})]}),Object(d.jsx)("p",{children:i.content}),Object(d.jsx)("p",{children:Object(d.jsx)(j.b,{classname:"nav-link",to:{pathname:"/setcookie/".concat(i.id,"/"),fromDashboard:!1},children:"\u0425\u043e\u0447\u0443 \u0431\u043e\u043b\u044c\u0448\u0435 \u0442\u0430\u043a\u043e\u0433\u043e \u043a\u043e\u043d\u0442\u0435\u043d\u0442\u0430"})}),Object(d.jsx)("p",{children:Object(d.jsx)("a",{target:"_blank",href:i.url_article,children:"\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0441\u0442\u0430\u0442\u044c\u044e"})})]})};var u=function(){return Object(d.jsx)("div",{className:"App",children:Object(d.jsxs)(j.a,{children:[Object(d.jsx)("header",{children:Object(d.jsx)("h1",{children:Object(d.jsx)(j.b,{to:{pathname:"/",fromDashboard:!1},children:"\u0413\u043b\u0430\u0432\u043d\u0430\u044f"})})}),Object(d.jsxs)(b.c,{children:[Object(d.jsx)(b.a,{path:"/",exact:!0,component:h}),Object(d.jsx)(b.a,{path:"/post/:id",exact:!0,component:m})]})]})})},O=function(e){e&&e instanceof Function&&c.e(3).then(c.bind(null,60)).then((function(t){var c=t.getCLS,n=t.getFID,a=t.getFCP,i=t.getLCP,s=t.getTTFB;c(e),n(e),a(e),i(e),s(e)}))};s.a.render(Object(d.jsx)(a.a.StrictMode,{children:Object(d.jsx)(u,{})}),document.getElementById("root")),O()}},[[59,1,2]]]);
//# sourceMappingURL=main.0999fc28.chunk.js.map