// add class red to the header element when id #red_header is clicked
add_class_to_this = document.getElementById("red_header");

add_class_to_this.addEventListener("click", function(){
	document.querySelector("header").classList.add("red");
})