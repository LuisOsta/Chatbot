(this.webpackJsonpclient=this.webpackJsonpclient||[]).push([[0],{29:function(t,e,a){},70:function(t,e,a){},71:function(t,e,a){"use strict";a.r(e);var n=a(2),c=a(0),s=a.n(c),o=a(18),r=a.n(o),i=(a(29),a(8)),u=a.n(i),h=a(9),p=a(19),l=a(5),d=a(23),j=a(22),m=a.n(j),b=a.p+"static/media/logo.103b5fa1.svg",x=(a(70),[{author:"Them",type:"text",data:{text:"Welcome! Here you can ask whatever questions you want about finance"}},{author:"Them",type:"text",data:{text:"Ask any question you want."}}]),f={author:"Them",type:"text",data:{text:"Thinking..."}},g=function(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:[];return t.pop(),t};var O=function(){var t=Object(c.useState)(""),e=Object(l.a)(t,2),a=e[0],s=e[1],o=Object(c.useState)(!0),r=Object(l.a)(o,2),i=r[0],j=r[1],O=Object(c.useState)(x),v=Object(l.a)(O,2),y=v[0],k=v[1],w=function(){var t=Object(p.a)(u.a.mark((function t(e){var n,c;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return k((function(t){return[].concat(Object(h.a)(t),[e,f])})),t.next=3,m.a.post("/chatbot/response",{data:{text:e.data.text,name:a},headers:{"content-type":"application/json"}});case 3:n=t.sent,c=n.data,k((function(t){return[].concat(Object(h.a)(g(t)),[{author:"Them",type:"text",data:{text:c.text}}])})),s(c.name);case 7:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}();return Object(n.jsxs)("div",{className:"App",children:[Object(n.jsx)("header",{className:"App-header",children:Object(n.jsx)("img",{src:b,className:"App-logo",alt:"logo"})}),Object(n.jsx)("div",{children:Object(n.jsx)("div",{className:"launcher",children:Object(n.jsx)(d.a,{agentProfile:{teamName:"CS4395 Chatbot",imageUrl:"https://a.slack-edge.com/66f9/img/avatars-teams/ava_0001-34.png"},onMessageWasSent:w,messageList:y,showEmoji:!1,isOpen:i,handleClick:function(){j(!i)},className:"launcher"})})})]})},v=function(t){t&&t instanceof Function&&a.e(3).then(a.bind(null,72)).then((function(e){var a=e.getCLS,n=e.getFID,c=e.getFCP,s=e.getLCP,o=e.getTTFB;a(t),n(t),c(t),s(t),o(t)}))};r.a.render(Object(n.jsx)(s.a.StrictMode,{children:Object(n.jsx)(O,{})}),document.getElementById("root")),v()}},[[71,1,2]]]);
//# sourceMappingURL=main.13dedac6.chunk.js.map