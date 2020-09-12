function NavSlide(){
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li')

    //Toggle Nav
    nav.classList.toggle('nav-active');

    //Animate Links
    navLinks.forEach((link,index) => {
        if(link.style.animation){
        link.style.animation = ''
        }
        else{
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 3 + 0.4}s`;
        }
    });
    //Burger Animation
    burger.classList.toggle('toggle');
}

const navSlide = () => {
    const burger = document.querySelector('.burger');
    burger.addEventListener('click', NavSlide, false);    
}

navSlide();