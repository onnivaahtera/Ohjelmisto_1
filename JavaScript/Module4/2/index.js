const form = document.getElementById("myForm");

form.addEventListener("submit", function (event) {
	event.preventDefault();

	const name = form.elements.query.value;
	getShows(name);
});

const getShows = async (name) => {
	return fetch(`https://api.tvmaze.com/search/shows?q=${name}`)
		.then((res) => res.json())
		.then((data) => {
			console.log(data);
		});
};
