const dice = (max) => {
	return Math.floor(Math.random() * max) + 1;
};

const arr = [];
const ul = document.querySelector("#target");

const sides = parseInt(prompt("Number of sides on the dice: "));
while (true) {
	const diceRoll = dice(sides);
	arr.push(diceRoll);
	if (diceRoll === sides) {
		arr.map((value) => {
			const li = document.createElement("li");
			li.textContent = value;
			ul.appendChild(li);
		});
		break;
	}
}
