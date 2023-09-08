// // WEBSITE INFOS
// console.log("working");

// fetch('https://api.ipify.org?format=json')
// .then(response => response.json())
// .then(data => {
//              userIPAddress = data.ip;
//              console.log('User IP address:', userIPAddress);
//     })
// var website = window.location.hostname.split('.')
// var web = website[1];

// console.log("website :", web);

// // WEBSITE INFO API

// function websiteinfo(){
//     var endpoint = "https://4f2e-110-226-180-229.ngrok-free.app/website/"
//     var data = {
//         userIPAddress:userIPAddress,website:web}
//     fetch(endpoint, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         }, body: JSON.stringify(data),
//       })
//         .then(response => response.json())
//         .then(data => {
//           console.log('Data sent to Django backend:', data);
//         })
//        }



// // PAGE ACCESS TIMES
// var entryInfo = JSON.parse(sessionStorage.getItem('entryInfo')) || [];
// function updateAccessList(pageName) {
//     var currentTime = new Date();
//     currentTime.setHours(currentTime.getHours() + 5);
//     currentTime.setMinutes(currentTime.getMinutes() + 30);
//     var accessTime = currentTime.toISOString();
//     entryInfo.push({ page: pageName, accessTime: accessTime });
//     sessionStorage.setItem('entryInfo', JSON.stringify(entryInfo));

// }
// window.addEventListener('load', function () {
//     var currentPath = window.location.pathname;

//     if (currentPath.includes('/faq')) {
//         updateAccessList('Questions Page');
//     } else if (currentPath.includes('/contact')) {
//         updateAccessList('Contact Page');
//     } 
//     else if (currentpath.includes('/product-page/')){
//         updateAccessList('Products Page')
// }
// else if (currentpath.includes('/cart')){
//     updateAccessList('Cart Page')
// }
// else {
//         updateAccessList('Home Page');
//     }
// });


// // API FOR PAGEINFO


// function entry(){
//     var entryInfo = JSON.parse(sessionStorage.getItem('entryInfo'))
//     var send = {'entryInfo':entryInfo,userIPAddress:userIPAddress}
//     var end = "https://4f2e-110-226-180-229.ngrok-free.app/entry/"
//     fetch(end, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         }, body: JSON.stringify(send),
//       })
//         .then(response => response.json())
//         .then(data => {
//           console.log('Data sent to Django backend:', data);
//         })
// }


// // PAGE NAMES AND CREATE LIST OF PRODUCTS
// var currentpath = window.location.href
// let page  = 'Home Page';
    
//     if (currentpath.includes('/faq')){
//         page= "Questions Page";
    
//     }
//     else if (currentpath.includes('/contact')){
//        page = 'Contact Page';
//     }
    
//     else if(currentpath.includes('/product-page/')){
//         page = 'Products Page'
//         var productname = currentpath.split('/product-page/')[1];
//         console.log('Product Name:',productname)
//         var ProductsViewed = JSON.parse(sessionStorage.getItem('ProductsViewed'))||[];
//         if (ProductsViewed.length === 0 || ProductsViewed[ProductsViewed.length - 1] !== productname) {
//         ProductsViewed.push(productname);

//         sessionStorage.setItem('ProductsViewed', JSON.stringify(ProductsViewed));

//     }
// }
//     else if (currentpath.includes('/cart')){
//         page = "Your Cart"
//     }
//     else if (currentpath.includes('')){
//         page = 'Home Page';
//     }
//     console.log("You are Currently Viewing:",page);


// // CLICK AND HOVER DATA

// function handleclick(event){
// var x = event.clientX + window.scrollX;
// var y = event.clientY + window.scrollY;
// var timeStamp = new Date();
// timeStamp.setHours(timeStamp.getHours() + 5);
// timeStamp.setMinutes(timeStamp.getMinutes() + 30); 
// var timestamp = timeStamp.toISOString();

//   const type  = 'MouseClick';

//   if (event.type==='click'){
//     const clickedElement = event.target;
//     elementName = clickedElement.innerText || clickedElement.textContent;
    



//     if (typeof(Storage) !== "undefined") {
//       var existingClicks = JSON.parse(sessionStorage.getItem('clickData')) ||  [] ;
//       existingClicks.push({ x:x, y:y,page:page, time:timestamp, 'event-type': type , place_of_click:elementName});
  
  
//       sessionStorage.setItem('clickData', JSON.stringify(existingClicks));

//     }}
//     else if (event.type === 'mouseover') {
//         const type = 'MouseHover';
//         const hoveredElement = event.target;
//         const elementName = hoveredElement.innerText || hoveredElement.textContent;
// const elementAttributes = Array.from(hoveredElement.attributes).reduce((attrs, attr) => {
//     if (attr.name !== 'class' && !attr.name.startsWith('aria')) {
//       attrs[attr.name] = attr.value;
// }
    
//     return attrs;
// }, {});
//     hoverTimer = setTimeout(() => {
//             const hoverdata = {
//                 x:x, y:y,page:page, time:timestamp, 'event-type': type , place_of_hover:elementName
//             }
//             if (Object.keys(elementAttributes).length === 0) {
//                 hoverdata.attributes = 'none';
//               } else {
//                 hoverdata.attributes = elementAttributes;
//               }

    
//           if (typeof Storage !== "undefined") {
//           var existingHovers = JSON.parse(sessionStorage.getItem('hoverData')) ||  [];
          
//           existingHovers.push(hoverdata)
    
//           sessionStorage.setItem('hoverData', JSON.stringify(existingHovers));
//         } else {
//           console.log("Local storage is not supported by this browser.");
//         }
//       },2500);
//         if (event.type === 'mouseout') {
//         clearTimeout(hoverTimer);
//     }}
// }
      

// document.addEventListener('click', handleclick);
// document.addEventListener('mouseover',handleclick)
// document.addEventListener('mouseout',handleclick)

// // API FOR HOVERDATA
// function hoverdata(){

//     var hover = JSON.parse(sessionStorage.getItem('hoverData'))
    
//     var ends = "https://4f2e-110-226-180-229.ngrok-free.app/hover/"
//     var datas = {'hover':hover,userIPAddress:userIPAddress}
//     fetch(ends, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         }, body: JSON.stringify(datas),
//       })
//         .then(response => response.json())
//         .then(data => {
//           console.log('Data sent to Django backend:', data);
//         })



// }
// // API FOR CLICK DATA

// function click(){
//     var click = JSON.parse(sessionStorage.getItem('clickData'))
//     var tosend = {'click':click,userIPAddress:userIPAddress}
//     var point = "https://4f2e-110-226-180-229.ngrok-free.app/click/"
//     fetch(point, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         }, body: JSON.stringify(tosend),
//       })
//         .then(response => response.json())
//         .then(data => {
//           console.log('Data sent to Django backend:', data);
//         })
// }

// // PAGE TRACKING


// document.addEventListener('DOMContentLoaded',function(){

    
//     var isrevisit = false

//     var atpage = window.location.href;
//     let current = 'Home Page'
//     if (atpage.includes('/faq')){
//         current = "Questions Page"
//     }
//     else if (atpage.includes('/contact')){
//         current="Contact Page"
//     }
//     else if (atpage.includes('/cart')){
//         current = "Cart Page"
//     }
//     else if (atpage.includes('/product-page/')){
//         current = "Product Page"}
    
    
//     var pages = sessionStorage.getItem('pages')
//     if(!pages){
//         pages = []    
//     }
//     else{
//         pages = JSON.parse(pages)
//     }
//     var lastpage = pages.length > 0 ? pages[pages.length - 1] : null;
//     isrevisit = current === lastpage;

//     if (!isrevisit) {
//         pages.push(current);
//         sessionStorage.setItem('pages', JSON.stringify(pages));
//         if (pages.length===1){
//             var timeStamp = new Date();
//             timeStamp.setHours(timeStamp.getHours() + 5);   
//             timeStamp.setMinutes(timeStamp.getMinutes() + 30);
//             var timeStamp = timeStamp.toISOString();
//              sessionStorage.setItem('first page access time is :',timeStamp)


//         }
//     };

//     var list = document.getElementById('list');
//     if (list) {
//         list.textContent = pages.join(', ');
//     }
// });

// // API FOR PAGES

// function listofpages(){

//     var pageinfo = JSON.parse(sessionStorage.getItem('pages'))
//     var time = sessionStorage.getItem('first page access time is :')
//     var api = "https://4f2e-110-226-180-229.ngrok-free.app/app/"
//     var data = {first_page: pageinfo[0], other_pages: pageinfo.slice(1),time:time,userIPAddress:userIPAddress}  
//     fetch(api, {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         }, body: JSON.stringify(data),
//       })
//         .then(response => response.json())
//         .then(data => {
//           console.log('Data sent to Django backend:', data);
//         })
    
// }

// function Django(){
//     Promise.all([entry(), hoverdata(), click(),websiteinfo()]).then(() => {
//         listofpages();
        
        
//     }
//       )};          
// // window.addEventListener('unload',Django);


