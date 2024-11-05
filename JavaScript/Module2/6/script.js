const dice = () => {
	return Math.floor(Math.random() * 6) + 1;
};

const arr = [];
const ul = document.querySelector("#target");

while (true) {
	const diceRoll = dice();
	arr.push(diceRoll);
	if (diceRoll === 6) {
		arr.map((value) => {
			const li = document.createElement("li");
			li.textContent = value;
			ul.appendChild(li);
		});
		break;
	}
}
