// Greetings constants 

const mainGreeting = document.querySelector('#main-greeting');
const mainGreetingDescription = document.querySelector('#main-greeting-description');
const mainGreetingDateTime = document.querySelector('#date-and-time');

// Greetings related calculations

const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
const months = ["January", "February", "March", "April", "May", "June", "July", "August", 
                "September", "October", "November", "December"];

const currentDate = new Date();
const timeInHours = Number(currentDate.toTimeString().substring(0,2));
const dayToday = days[currentDate.getDay()];


// Times are in GMT
if (timeInHours < 6){
    mainGreeting.textContent = "Good morning, Shahzad";
    mainGreetingDescription.textContent = `Good luck with your training, 
    hope you achieve all today's tasks and get the long term benefits of this work!`;
}
else if (timeInHours >= 6 && timeInHours < 9){
    mainGreeting.textContent = "Good morning, Shahzad";
    mainGreetingDescription.textContent = `Training time is over mate, have some life :)`;
}
else if (timeInHours >= 9 && timeInHours < 13){
    mainGreeting.textContent = "Good afternoon, Shahzad";
    mainGreetingDescription.textContent = `Let's fix your eyes on office work, may you achieve
    value for yourself and the organization you work for!`;
}
else if (timeInHours >= 13 && timeInHours < 15){
    mainGreeting.textContent = "Good evening, Shahzad";
    mainGreetingDescription.textContent = `The priority 1 stuff - my kids - focus everyday and 
    results will show the efforts InshaAllah. May Allah bless your kids with knowledge that can be beneficial for them.`;
}
else if (timeInHours >= 15 && timeInHours < 17){
    mainGreeting.textContent = "Good evening, Shahzad";
    mainGreetingDescription.textContent = `Don't overwhem yourself, just a little bit more today before going for a nap`;
}
else {
    mainGreeting.textContent = "Good night, Shahzad";
    mainGreetingDescription.textContent = `You MUST be sleeping..............`;
}

mainGreetingDateTime.innerHTML = `<strong>${dayToday}</strong> - ${months[currentDate.getMonth()]} ${currentDate.getDate()}, ${currentDate.getFullYear()}`;
