const arr = [];

for (let i = 1; i <= 6; i++) {
	arr.push(prompt(`Name of dog ${i}: `));
}
const ol = document.querySelector("#target");

arr
	.sort()
	.reverse()
	.map((i) => {
		const li = document.createElement("li");
		li.textContent = i;
		ol.appendChild(li);
	});
