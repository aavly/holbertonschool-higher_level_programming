// ***
// toggles class of header element when id #toggle_header clicked

hdr = document.querySelector("header");
hdr_with_id = document.getElementById("toggle_header");

hdr_with_id.addEventListener("click", function() {
	if (hdr.classList.contains("red")) {
		hdr.classList.toggle("red");
		hdr.classList.add("green");
	}
	else {
		hdr.classList.remove("green");
		hdr.classList.add("red");
	}
});