const arr = [];
for (let i = 1; i <= 5; i++) {
	arr.push(parseInt(prompt(`Num: ${i}: `)));
}

console.log(
	arr.sort(() => {
		return 1;
	})
);
