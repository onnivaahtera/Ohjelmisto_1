let num1 = parseInt(prompt("Num 1: "));
let num2 = parseInt(prompt("Num 2: "));
let num3 = parseInt(prompt("Num 3: "));

nums = [num1, num2, num3];
sum = nums.reduce((a, b) => a + b, 0);
product = nums.reduce((a, b) => a * b, 1);

document.querySelector("#target").innerHTML = `Sum: ${sum}, Product: ${product}, Average: ${
	sum / nums.length
}`;
