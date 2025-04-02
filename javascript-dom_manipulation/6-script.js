// fetch character name from URl using Fetch API
// name must be displayed in HTML tag with id character

tag_with_id = document.getElementById("character");

fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
	.then (response => {
		if (!response.ok) {
			throw new Error ('Network response error');
		}
		return response.json();
	})
	.then (data => {
		const character_name = data.name;
		tag_with_id.textContent = character_name;
	})
	.catch (error => {
		console.error('ERROR:', error);
	});