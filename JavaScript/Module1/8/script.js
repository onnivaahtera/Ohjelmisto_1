const leap_year = (year) => {
	return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
};

const start_year = parseInt(prompt("Start year: "));
const end_year = parseInt(prompt("End year: "));

const ul = document.querySelector("#target");

for (let i = start_year; i <= end_year; i++) {
	const li = document.createElement("li");
	if (leap_year(i)) {
		li.textContent = i;
		ul.appendChild(li);
	}
}
