(this.webpackJsonpclient=this.webpackJsonpclient||[]).push([[0],{29:function(t,e,a){},70:function(t,e,a){},71:function(t,e,a){"use strict";a.r(e);var n=a(2),c=a(0),s=a.n(c),o=a(17),r=a.n(o),i=(a(29),a(7)),u=a.n(i),p=a(23),h=a(18),l=a(8),d=a(22),j=a(21),m=a.n(j),b=a.p+"static/media/logo.103b5fa1.svg",g=(a(70),[{author:"Them",type:"text",data:{text:"Welcome! Here you can ask whatever questions you want about finance"}},{author:"Them",type:"text",data:{text:"Ask any question you want."}}]);var f=function(){var t=Object(c.useState)(!0),e=Object(l.a)(t,2),a=e[0],s=e[1],o=Object(c.useState)(g),r=Object(l.a)(o,2),i=r[0],j=r[1],f=function(){var t=Object(h.a)(u.a.mark((function t(e){var a,n;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,m.a.post("/chatbot/response",{data:{text:e.data.text},headers:{"content-type":"application/json"}});case 2:a=t.sent,n=a.data,j([].concat(Object(p.a)(i),[e,{author:"Them",type:"text",data:{text:n}}]));case 5:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}();return Object(n.jsxs)("div",{className:"App",children:[Object(n.jsx)("header",{className:"App-header",children:Object(n.jsx)("img",{src:b,className:"App-logo",alt:"logo"})}),Object(n.jsx)(d.a,{agentProfile:{teamName:"CS4395 Chatbot",imageUrl:"https://a.slack-edge.com/66f9/img/avatars-teams/ava_0001-34.png"},onMessageWasSent:f,messageList:i,showEmoji:!1,isOpen:a,handleClick:function(){s(!a)}})]})},x=function(t){t&&t instanceof Function&&a.e(3).then(a.bind(null,72)).then((function(e){var a=e.getCLS,n=e.getFID,c=e.getFCP,s=e.getLCP,o=e.getTTFB;a(t),n(t),c(t),s(t),o(t)}))};r.a.render(Object(n.jsx)(s.a.StrictMode,{children:Object(n.jsx)(f,{})}),document.getElementById("root")),x()}},[[71,1,2]]]);
//# sourceMappingURL=main.040b7ab4.chunk.js.map