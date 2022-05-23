///
/// Date: 3/4/2022
/// Author: Dhruv Rayat
///

const ageChild = 3;

function GetAge() {
  const age = prompt("How old are you: ");
  return age;
}

function getTemp() {
  const temp = prompt("Enter the temperature in Celsius: ");
  return temp;
}

function checkTempAndAge(age, temp) {
  if (age <= ageChild && temp >= 38) {
    console.log("Call a doctor");
  } else if ((age) => ageChild && temp >= 39.8) {
    console.log("Stay home");
  } else {
    console.log("Check again in an hour");
  }
}

checkTempAndAge(GetAge(), getTemp());
