(self.webpackChunkcookbook_web=self.webpackChunkcookbook_web||[]).push([[371],{55770:function(h){h.exports={pre:"pre___3mGTW"}},7330:function(){},44320:function(h,v,e){"use strict";e.r(v);var u=e(58024),i=e(39144),m=e(17462),n=e(76772),W=e(402),O=e(53296),K=e(67294),Z=e(70844),I=e(55770),A=e.n(I),s=e(85893),x=function(T){var N=T.children;return(0,s.jsx)("pre",{className:A().pre,children:(0,s.jsx)("code",{children:(0,s.jsx)(O.Z.Text,{copyable:!0,children:N})})})};v.default=function(){return(0,s.jsx)(Z.ZP,{children:(0,s.jsxs)(i.Z,{children:[(0,s.jsx)(n.Z,{message:"\u66F4\u5FEB\u66F4\u5F3A\u7684\u91CD\u578B\u7EC4\u4EF6\uFF0C\u5DF2\u7ECF\u53D1\u5E03\u3002",type:"success",showIcon:!0,banner:!0,style:{margin:-12,marginBottom:24}}),(0,s.jsxs)(O.Z.Text,{strong:!0,children:["\u9AD8\u7EA7\u8868\u683C"," ",(0,s.jsx)("a",{href:"https://procomponents.ant.design/components/table",rel:"noopener noreferrer",target:"__blank",children:"\u6B22\u8FCE\u4F7F\u7528"})]}),(0,s.jsx)(x,{children:"yarn add @ant-design/pro-table"}),(0,s.jsxs)(O.Z.Text,{strong:!0,style:{marginBottom:12},children:["\u9AD8\u7EA7\u5E03\u5C40"," ",(0,s.jsx)("a",{href:"https://procomponents.ant.design/components/layout",rel:"noopener noreferrer",target:"__blank",children:"\u6B22\u8FCE\u4F7F\u7528"})]}),(0,s.jsx)(x,{children:"yarn add @ant-design/pro-layout"})]})})}},5467:function(h,v,e){"use strict";e.d(v,{Z:function(){return u}});function u(i){return Object.keys(i).reduce(function(m,n){return(n.substr(0,5)==="data-"||n.substr(0,5)==="aria-"||n==="role")&&n.substr(0,7)!=="data-__"&&(m[n]=i[n]),m},{})}},76772:function(h,v,e){"use strict";e.d(v,{Z:function(){return $}});var u=e(22122),i=e(96156),m=e(28481),n=e(67294),W=e(54549),O=e(15873),K=e(57119),Z=e(68628),I=e(73218),A=e(38819),s=e(68855),x=e(40847),U=e(43061),T=e(60444),N=e(94184),B=e.n(N),X=e(86032),Y=e(5467),_=e(6610),k=e(5991),w=e(10379),q=e(44144),ee=function(d){(0,w.Z)(o,d);var t=(0,q.Z)(o);function o(){var r;return(0,_.Z)(this,o),r=t.apply(this,arguments),r.state={error:void 0,info:{componentStack:""}},r}return(0,k.Z)(o,[{key:"componentDidCatch",value:function(l,C){this.setState({error:l,info:C})}},{key:"render",value:function(){var l=this.props,C=l.message,p=l.description,M=l.children,g=this.state,D=g.error,y=g.info,L=y&&y.componentStack?y.componentStack:null,R=typeof C=="undefined"?(D||"").toString():C,j=typeof p=="undefined"?L:p;return D?n.createElement($,{type:"error",message:R,description:n.createElement("pre",null,j)}):M}}]),o}(n.Component),ne=e(96159),te=function(d,t){var o={};for(var r in d)Object.prototype.hasOwnProperty.call(d,r)&&t.indexOf(r)<0&&(o[r]=d[r]);if(d!=null&&typeof Object.getOwnPropertySymbols=="function")for(var l=0,r=Object.getOwnPropertySymbols(d);l<r.length;l++)t.indexOf(r[l])<0&&Object.prototype.propertyIsEnumerable.call(d,r[l])&&(o[r[l]]=d[r[l]]);return o},re={success:A.Z,info:x.Z,error:U.Z,warning:s.Z},oe={success:O.Z,info:Z.Z,error:I.Z,warning:K.Z},F=function(t){var o,r=t.description,l=t.prefixCls,C=t.message,p=t.banner,M=t.className,g=M===void 0?"":M,D=t.style,y=t.onMouseEnter,L=t.onMouseLeave,R=t.onClick,j=t.afterClose,H=t.showIcon,ae=t.closable,S=t.closeText,b=t.action,P=te(t,["description","prefixCls","message","banner","className","style","onMouseEnter","onMouseLeave","onClick","afterClose","showIcon","closable","closeText","action"]),se=n.useState(!1),z=(0,m.Z)(se,2),G=z[0],le=z[1],ce=n.useRef(),J=n.useContext(X.E_),ie=J.getPrefixCls,de=J.direction,a=ie("alert",l),ue=function(c){var E;le(!0),(E=P.onClose)===null||E===void 0||E.call(P,c)},ve=function(){var c=P.type;return c!==void 0?c:p?"warning":"info"},me=S?!0:ae,Q=ve(),fe=function(){var c=P.icon,E=(r?oe:re)[Q]||null;return c?(0,ne.wm)(c,n.createElement("span",{className:"".concat(a,"-icon")},c),function(){return{className:B()("".concat(a,"-icon"),(0,i.Z)({},c.props.className,c.props.className))}}):n.createElement(E,{className:"".concat(a,"-icon")})},Ee=function(){return me?n.createElement("button",{type:"button",onClick:ue,className:"".concat(a,"-close-icon"),tabIndex:0},S?n.createElement("span",{className:"".concat(a,"-close-text")},S):n.createElement(W.Z,null)):null},V=p&&H===void 0?!0:H,Ce=B()(a,"".concat(a,"-").concat(Q),(o={},(0,i.Z)(o,"".concat(a,"-with-description"),!!r),(0,i.Z)(o,"".concat(a,"-no-icon"),!V),(0,i.Z)(o,"".concat(a,"-banner"),!!p),(0,i.Z)(o,"".concat(a,"-rtl"),de==="rtl"),o),g),pe=(0,Y.Z)(P);return n.createElement(T.Z,{visible:!G,motionName:"".concat(a,"-motion"),motionAppear:!1,motionEnter:!1,onLeaveStart:function(c){return{maxHeight:c.offsetHeight}},onLeaveEnd:j},function(f){var c=f.className,E=f.style;return n.createElement("div",(0,u.Z)({ref:ce,"data-show":!G,className:B()(Ce,c),style:(0,u.Z)((0,u.Z)({},D),E),onMouseEnter:y,onMouseLeave:L,onClick:R,role:"alert"},pe),V?fe():null,n.createElement("div",{className:"".concat(a,"-content")},n.createElement("div",{className:"".concat(a,"-message")},C),n.createElement("div",{className:"".concat(a,"-description")},r)),b?n.createElement("div",{className:"".concat(a,"-action")},b):null,Ee())})};F.ErrorBoundary=ee;var $=F},17462:function(h,v,e){"use strict";var u=e(43673),i=e.n(u),m=e(7330),n=e.n(m)}}]);
