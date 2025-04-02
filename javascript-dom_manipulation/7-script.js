// fetch and list the title for all movies
// all movies must be in list the <ul> element with id #list_movies


const ul_with_id = document.getElementById("list_movies");


fetch("https://swapi-api.hbtn.io/api/films/?format=json")
	.then (response => {
		if (!response.ok) {
			throw new Error ('Network response error');
		}
		return response.json();
	})
	.then (data => {
		// loop through results 
		data.results.forEach(film => {
			// create an <li> element for each title
			const li = document.createElement("li");
			const text_node = document.createTextNode(film.title);

			// append text nodes (titles) to <li>
			li.appendChild(text_node);

			//append li to exising
			ul_with_id.appendChild(li);
		})
	})
	.catch (error => {
		console.error('ERROR:', error);
	});