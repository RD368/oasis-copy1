let li_elements = document.querySelectorAll(".wrapper-left ul li")
let item_elements = document.querySelectorAll(".item")

for(let i=0;i<li_elements.length;i++){
    li_elements[i].addEventListener( "click", function(){
        li_elements.forEach(function(li){
            li.classList.remove("active");
        })

        this.classList.add("active") 

        let li_value = this.getAttribute("data-li");

        item_elements.forEach(function(item){
            item.style.display = "none";
        })

       if(li_value == "orthopaedics" ){
          document.querySelector("." + li_value).style.display = "block";
       }else if(li_value == "obstetrics"){
        document.querySelector("." + li_value).style.display = "block";

       }else if(li_value == "pediatrics"){
        document.querySelector("." + li_value).style.display = "block";

       }else if(li_value == "ndonatology"){
        document.querySelector("." + li_value).style.display = "block";

       }else if(li_value == "surgery"){
        document.querySelector("." + li_value).style.display = "block";

       }else if(li_value == "nephrology"){
        document.querySelector("." + li_value).style.display = "block";

       }else{
        console.log("")
       }
    })
}


// >>>>>>>>>>>>>>>>>>>>>>>>> Testimonial-section start <<<<<<<<<<<<<<<<<<<<<<<<<

let cardContainer = document.getElementById("test-container");


async function init(){
    let fetchTestData = await fetchTestimonial()
   

    fetchTestData.forEach((data) =>{
        // console.log("initttt",data)
        genarateTestimonial(data.img,data.name,data.condition,data.review,data.city)
    })  
}

init();



// >>>>>>>>>>>>>>>>>>>>>>>> fetch Data <<<<<<<<<<<<<<<<<<<<<<

async function fetchTestimonial(){
    try{
      let res = await fetch("../static/testimonial.json")
      let data = await res.json()
      return data;
    }catch(err){
      console.log(err)  
    }
}



//  >>>>>>>>>>>>>>>>>>>> Card-generator <<<<<<<<<<<<<<<<<<<<

let testimonialCard = ""

function genarateTestimonial(img,name,condition,review,city){
    testimonialCard +=`
     <div class="card" style="
     border: none;
     box-shadow: 10px 10px 30px rgba(0,0,0,0.3);
     border-radius: 1rem;
     overflow: hidden;
 ">
      <div class="card-img">
       <img src= ${img} class="c-img" alt=${name}/>
      </div> 
      <div class="card-text">
       <h5> ${name} </h5>
       <h5>condition - ${condition}</h5>
       <p>review - ${review}</p>
       <hr/>
       <p>city: ${city}</p>
      </div>
     </div>
    `
 
    cardContainer.innerHTML= testimonialCard;
}


// >>>>>>>>>>>>>>>>>>>>> Testimonial load button <<<<<<<<<<<<<<<<

let lodeBtn = document.querySelector(".test-btn");
let current = 3;

lodeBtn.onclick = () => {
    let card = [...document.querySelectorAll(".testimonial #test-container .card")]

    for(let i=current; i<current +4;i++ ){
    card[i].style.display = "inline-block";
    }

    current += 3;

 console.log(current , card.length)
    if(current >= card.length-1){
        lodeBtn.style.display = "none";
    }
}

let main_nav = document.querySelector('.main-nav')
console.log(window.pageYOffset);
window.onscroll = function(){
    if(window.pageYOffset > 140){
        main_nav.classList.add('sticky');
    }else{
       main_nav.classList.remove("sticky");
    }
}
