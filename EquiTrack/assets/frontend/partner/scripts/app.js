!function(n){"use strict";var o=n.querySelector("#app");o.baseUrl="/",""!==window.location.port&&"8099"!==window.location.port||(o.baseUrl="/partners/"),o.appData={baseUrl:o.baseUrl,baseSite:window.location.origin,logoutEndpoint:window.location.origin+"/accounts/logout/",userInfoEp:window.location.origin+"/users/api/profile/",userPropertiesEp:window.location.origin+"/partnership/partnerstaffmember/",interventionsEp:[window.location.origin,"api","interventions"].join("/")+"/",newIndicatorReportEp:window.location.origin+"/api/reports/indicators/",getEndpoint:{userProperties:function(n){return[window.location.origin,"partners","api","profile",n].join("/")+"/"},interventionDetails:function(n){return[window.location.origin,"api","interventions",n].join("/")+"/"},resultChainDetails:function(n){return[window.location.origin,"partners","api","resultchain",n].join("/")+"/"}},permissions:{partnerOnlyPermissions:["interventionsMenu","userInfoMenu"],defaultPermissions:["userInfoMenu"],partnerPermissions:["interventionsMenu"],managementPermissions:["statsMenu"]}},o.displayInstalledToast=function(){Polymer.dom(n).querySelector("platinum-sw-cache").disabled||Polymer.dom(n).querySelector("#caching-complete").show()},o.addEventListener("dom-change",function(){console.log("Our app is ready to rock!")}),window.addEventListener("WebComponentsReady",function(){}),window.addEventListener("paper-header-transform",function(o){var e=Polymer.dom(n).querySelector("#mainToolbar .app-name"),r=Polymer.dom(n).querySelector("#mainToolbar .middle-container"),i=Polymer.dom(n).querySelector("#mainToolbar .bottom-container"),t=o.detail,a=t.height-t.condensedHeight,s=Math.min(1,t.y/a),l=.5,c=a-t.y,p=a/(1-l),d=Math.max(l,c/p+l),u=1-s;Polymer.Base.transform("translate3d(0,"+100*s+"%,0)",r),Polymer.Base.transform("scale("+u+") translateZ(0)",i),Polymer.Base.transform("scale("+d+") translateZ(0)",e)}),o.scrollPageToTop=function(){o.$.headerPanelMain.scrollToTop(!0)},o.closeDrawer=function(){o.$.paperDrawerPanel.closeDrawer()}}(document);