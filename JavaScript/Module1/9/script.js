const is_prime = (n) => {
	if (n <= 1) return false;
	for (let i = 2, s = Math.sqrt(n); i <= s; i++) {
		if (n % i === 0) return false;
	}
	return true;
};

const num = parseInt(prompt("Number: "));

is_prime(num)
	? `${(document.querySelector(
			"#target"
	  ).innerHTML = `Number ${num} is a prime number`)}`
	: `${(document.querySelector(
			"#target"
	  ).innerHTML = `Number ${num} is not a prime number`)}`;
