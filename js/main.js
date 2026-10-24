const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.08});
document.querySelectorAll('.reveal,.card,.stat').forEach(el=>{el.classList.add('reveal');io.observe(el)});
const showAll=()=>document.querySelectorAll('.reveal:not(.in)').forEach(e=>e.classList.add('in'));
addEventListener('scroll',()=>{clearTimeout(window.__t);window.__t=setTimeout(showAll,350)},{passive:true});setTimeout(showAll,2500);
