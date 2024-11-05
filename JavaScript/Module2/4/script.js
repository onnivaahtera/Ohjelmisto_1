const arr = [];

const promptForNumbers = () => {
	const num = parseInt(prompt("Input numbers 0 to stop"));
	if (num === 0) return;
	else {
		arr.push(num);
		promptForNumbers();
	}
};

promptForNumbers();
console.log(arr.sort((a, b) => a - b).reverse());
