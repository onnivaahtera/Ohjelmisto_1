const leap_year = (year) => {
	return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
};

input = parseInt(prompt("Year: "));

leap_year(input)
	? (document.querySelector(
			"#target"
	  ).innerHTML = `Vuosi ${input} on karkausvuosi`)
	: (document.querySelector(
			"#target"
	  ).innerHTML = `Vuosi ${input} ei ole karkausvuosi`);
