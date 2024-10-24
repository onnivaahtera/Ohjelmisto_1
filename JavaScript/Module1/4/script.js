classes = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"];

const input = prompt("Name: ");
rand = Math.floor(Math.random() * 4);

document.querySelector("#target").innerHTML = `${input}, you are ${classes[rand]}`;
