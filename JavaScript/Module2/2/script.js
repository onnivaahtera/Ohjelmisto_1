//const num = parseInt(prompt("Number of participants"));
const arr = ["Apina", "Kala", "Banaani", "Maito", "Cipuli"].sort();

/* for (let i = 1; i <= num; i++) {
	arr.push(prompt(`Name of participant ${i}: `));
} */
const ol = document.querySelector("#target");
arr.map((i) => {
	const li = document.createElement("li");
	li.textContent = i;
	ol.appendChild(li);
});
