///
/// Date: 3/4/2022
/// Author: Dhruv Rayat
///

function askAge() {
  var age = prompt("How old are you?");
  return age;
}

function checkAge(age) {
  if (age >= 18) {
    console.log("You are old enough to drink");
  } else {
    console.log("You are not old enough to drink.");
  }
}

checkAge(askAge());
