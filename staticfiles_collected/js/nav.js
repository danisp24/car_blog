const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
        navbar.classList.add("bg-dark");
        navbar.classList.add("navbar-dark");
        navbar.classList.remove("navbar-light");
    } else {
        navbar.classList.remove("bg-dark");
        navbar.classList.remove("navbar-dark");
        navbar.classList.add("navbar-light");
    }
});