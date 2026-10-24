const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.08});
document.querySelectorAll('.reveal,.card,.stat').forEach(el=>{el.classList.add('reveal');io.observe(el)});
