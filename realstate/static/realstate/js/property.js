document.addEventListener('DOMContentLoaded',function(){
   let btns =  document.querySelectorAll('#scrollerimgs .btn-labeled')
   console.log(btns)
    btns.forEach(function(btn){
        let att= btn.firstElementChild.src;
        console.log(att);
            btn.addEventListener('click',function(){
                document.querySelector('#main-img1').src =att;
            })
    })

  
    //   button.onclick = function() {
    //    document.querySelector('#').src='imgs/img1.jpg';
    //   }
      
  });



    // function clickedButton(btn, event) {
    //     document.getElementById('img').src = btn.getAttribute('data-src');
    //   }
      
    //   function bindClick(btn) {
    //     btn.addEventListener('click', clickedButton.bind(null,btn));
    //   }
      
    //   // Setup click handler(s) when content is loaded
     