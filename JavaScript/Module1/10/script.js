const dice = parseInt(prompt("Dice: "));
const sum_of_dice = parseInt(prompt("Sum of Dice: "));
const throws = 10000;

let sum = 0;
for (let i = 0; i < throws; i++) {
	const nums = [];
	for (let j = 0; j < dice; j++) {
		nums.push(Math.floor(Math.random() * 6) + 1);
	}
	if (nums.reduce((a, b) => a + b, 0) == sum_of_dice) sum++;
}

const precentage = ((sum / throws) * 100).toFixed(2);

document.querySelector(
	"#target"
).innerHTML = `Probability to get sum ${sum_of_dice} with ${dice} dice is ${precentage}%
`;
