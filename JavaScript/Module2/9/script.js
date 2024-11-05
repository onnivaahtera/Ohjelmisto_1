const even = (arr) => {
	const temp = [];
	arr.map((n) => {
		if (n % 2 === 0) {
			temp.push(n);
		}
	});
	return temp;
};

const nums = [2, 7, 4, 8, 6, 5];
console.log(nums);
console.log(even(nums));
