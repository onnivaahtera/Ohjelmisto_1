const form = document.getElementById("myForm");

form.addEventListener("submit", function (event) {
	event.preventDefault();

	const name = form.elements.query.value;
	const shows = getShows(name);

	console.log(shows);
});

const getShows = async (name) => {
	return await fetch(`https://api.tvmaze.com/search/shows?q=${name}`)
		.then((res) => res.json())
		.then((data) => {
			return data;
		});
};
