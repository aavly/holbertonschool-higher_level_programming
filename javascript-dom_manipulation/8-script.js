// fetch url and display 'hello' in HTML element with id #hello

fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
	.then (response => {
		if (!response.ok) {
			throw new Error ('Network response error');
		}
		return response.json();
	})
	.then (data => {
		const hellooo = data.hello;
		const helloooElement = document.getElementById("hello");
		helloooElement.textContent = hellooo
	})
	.catch (error => {
		console.error('ERROR:', error);
	});