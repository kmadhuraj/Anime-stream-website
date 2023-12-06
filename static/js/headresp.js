
    // const burger = document.querySelector('.burger');
    // const header = document.querySelector('.head');
    // const navbar = document.querySelector('.nav');
    // const right_bar = document.querySelector('.right-side-bar');

    // burger.addEventListener('click', () => {
    //     header.classList.toggle('head-height');
    //     navbar.classList.toggle('v-class-resp');
    //     right_bar.classList.toggle('v-class-resp');
    // });

    const burger = document.querySelector(".burger");
    const navbar = document.querySelector(".nav");
    
    burger.addEventListener("click", mobileMenu);
    
    function mobileMenu() {
        burger.classList.toggle("active");
        navbar.classList.toggle("active");
    }