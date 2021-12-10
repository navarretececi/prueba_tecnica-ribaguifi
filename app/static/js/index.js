let modes = document.querySelector("#modes_menu");
let mode_btn = document.querySelector("#modes-btn");
let dictionary = document.querySelector("#dictionary");
let search_btn = document.querySelector("#search-btn");

mode_btn.onclick = () => {
  modes.classList.toggle("displaynone");
};

search_btn.onclick = () => {
    dictionary.classList.toggle("displaynone");
  };
