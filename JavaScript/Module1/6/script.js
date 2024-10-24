const answer = confirm("Should I calculate the square root?");
if (answer == true) {
	const num = parseInt(prompt("Number"));
	if (num > 0) {
		document.querySelector("#target").innerHTML = `${Math.sqrt(num)}`;
	} else
		document.querySelector("#target").innerHTML =
			"The square root of a negative number is not defined";
} else {
	document.querySelector(
		"#target"
	).innerHTML = `The square root is not calculated`;
}
