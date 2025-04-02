// add <li> element to a list when id #add_item clicked
// new element must be added to <ul> element with class .my_list

element_id = document.getElementById("add_item");
ul_element = document.querySelector("ul.my_list");


element_id.addEventListener("click", function(){

	// creating node first
	const li = document.createElement("li");
	// to add text to the <li> element, create a text node 
	const text_node = document.createTextNode("Item");

	// then append text node to the li element
	li.appendChild(text_node);

	// append new element to an existing element
	ul_element.appendChild(li);
})







