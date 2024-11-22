const form = document.getElementById("myForm");
const q = document.getElementById("query");
const target = document.querySelector("#results");

form.addEventListener("submit", async (event) => {
	event.preventDefault();
	target.innerHTML = "";
	const name = form.elements.query.value;
	const shows = await getShows(name);
	shows.map((value) => {
		const h2 = document.createElement("h2");
		const url = document.createElement("a");
		const img = document.createElement("img");
		const sum = document.createElement("div");
		const article = document.createElement("article");
		h2.innerHTML = value.show.name;
		url.target = "_blank";
		url.innerHTML = value.show.url;
		url.href = value.show.url;

		value.show.image?.medium
			? (img.src = value.show.image.medium)
			: (img.src = "https://via.placeholder.com/210x295?text=Not%20Found");

		img.src = value.show.image?.medium;
		img.alt = value.show.name;
		sum.innerHTML = value.show.summary;
		article.append(h2, url, img, sum);
		target.append(article);
	});
	q.value = "";
});

const getShows = async (name) => {
	return await fetch(`https://api.tvmaze.com/search/shows?q=${name}`)
		.then((res) => res.json())
		.then((data) => {
			return data;
		});
};
