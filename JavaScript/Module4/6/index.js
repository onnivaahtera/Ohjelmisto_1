const form = document.getElementById("form");
const target = document.getElementById("target");

form.addEventListener("submit", async (event) => {
	event.preventDefault();
	const value_from_input = form.elements.query.value;
	const jokes = await getJokes(value_from_input);
	jokes.result.map((joke) => {
		const article = document.createElement("article");
		const p = document.createElement("p");
		p.innerHTML = joke.value;
		console.log(joke.value);
		article.append(p);
		target.append(article);
	});
});

const getJokes = async (text) => {
	const res = await fetch(
		`https://api.chucknorris.io/jokes/search?query=${text}`
	);
	const data = await res.json();
	return data;
};
