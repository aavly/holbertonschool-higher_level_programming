// // update text of header element to "New Header!!!" when element with id #update_header clicked

hdr = document.querySelector("header");
hdr_with_id = document.getElementById("update_header");

hdr.addEventListener("click", function() {
	hdr_with_id.textContent = "New Header!!!";
})

