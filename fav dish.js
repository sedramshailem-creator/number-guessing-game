var dishes = ["pizza", "pasta", "burger"];
console.log(dishes[0]);
console.log(dishes[1]);
console.log(dishes[2]);

console.log(dishes.length);

dishes.push("sushi");

console.log("i have " + dishes.length + "favorite dishes. ");
dishes.splice (1,1);

dishes.sort();


for (var i = 0; i < dishes.length; i++) {
    console.log(dishes[i]);
}


console.log("Now I have " + dishes.length + " favorite dishes.");

