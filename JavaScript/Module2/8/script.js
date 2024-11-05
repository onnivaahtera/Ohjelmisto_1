const concat = (arr) => {
	let str = "";
	for (let i = 0; i < arr.length; i++) {
		str = str + arr[i];
	}
	return str;
};

const names = ["Johnny", "DeeDee", "Joey", "Marky"];

document.querySelector("#target").innerHTML = concat(names);
