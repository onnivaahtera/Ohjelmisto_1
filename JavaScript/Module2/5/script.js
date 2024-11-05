const arr = [];

const promptForNumbers = () => {
	const num = parseInt(prompt("Input numbers"));
	if (arr.includes(num)) {
		return;
	} else {
		arr.push(num);
		promptForNumbers();
	}
};

promptForNumbers();
console.log(arr.sort((a, b) => a - b));
