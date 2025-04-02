// toggles class of header element when id #toggle_header clicked

toggle_headerrr = document.getElementById("toggle_header");
headerrr = document.querySelector("header");

// trying out a different method where function is defined beforehand
function toggle_class_of_header() {
	if (headerrr.className == "red") {
		headerrr.classList.toggle("green");
	}
	else {
		headerrr.classList.toggle("red");
	}
}
// 	if (headerrr.className == "red") {
// 		headerrr.classList.toggle("red");
// 		headerrr.classList.add("green");
// 	}
// 	else if (headerrr.className == "green") {
// 		headerr.classList.toggle("green");
// 		headerr.classList.add("red");
// 	}
// }

toggle_headerrr.addEventListener("click", toggle_class_of_header());