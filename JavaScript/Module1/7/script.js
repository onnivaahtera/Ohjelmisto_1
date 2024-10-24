number_of_dice = parseInt(prompt("Number of dice: "));
const nums = [];
for (let i = 0; i < number_of_dice; i++) {
	nums.push(Math.floor(Math.random() * 6) + 1);
}

document.querySelector(
	"#target"
).innerHTML = `Throws: ${nums}<br/> Sum of throws: ${nums.reduce(
	(a, b) => a + b,
	0
)}`;
