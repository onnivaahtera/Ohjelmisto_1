const numCandidates = parseInt(prompt("Enter the number of candidates: "));
const candidates = [];

for (let i = 0; i < numCandidates; i++) {
	const name = prompt(`Name for candidate ${i + 1}: `);
	candidates.push({ name: name, votes: 0 });
}

const numVoters = parseInt(prompt("Enter the number of voters: "));

for (let i = 0; i < numVoters; i++) {
	const vote = prompt(
		`Voter ${
			i + 1
		}, enter the name of the candidate you vote for (or leave blank for an empty vote): `
	);

	if (vote) {
		const candidate = candidates.find(
			(c) => c.name.toLowerCase() === vote.toLowerCase()
		);
		if (candidate) {
			candidate.votes += 1;
		}
	}
}

const winner = candidates.reduce((prev, current) =>
	prev.votes > current.votes ? prev : current
);

let results = `The winner is ${winner.name} with ${winner.votes} votes.\nResults:\n`;

candidates.forEach((candidate) => {
	results += `${candidate.name}: ${candidate.votes} votes\n`;
});

console.log(results);
