function displayClock() {

    // Get current date and time
    let currentTime = new Date();


    // Get hours
    let hours = currentTime.getHours();


    // Get minutes
    let minutes = currentTime.getMinutes();


    // Get seconds
    let seconds = currentTime.getSeconds();


    // AM or PM
    let ampm = hours >= 12 ? "PM" : "AM";


    // Convert 24-hour format to 12-hour format
    hours = hours % 12;


    // If hour is 0, make it 12
    if (hours === 0) {
        hours = 12;
    }


    // Add zero before single digit
    hours = hours < 10 ? "0" + hours : hours;

    minutes = minutes < 10 ? "0" + minutes : minutes;

    seconds = seconds < 10 ? "0" + seconds : seconds;


    // Display time
    document.getElementById("clock").innerText =
        hours + " : " + minutes + " : " + seconds;


    // Display AM / PM
    document.getElementById("ampm").innerText = ampm;


    // Get current day
    let day = currentTime.toLocaleDateString("en-US", {
        weekday: "long"
    });


    // Display day
    document.getElementById("day").innerText = day;


    // Get current date
    let date = currentTime.toLocaleDateString("en-US", {
        month: "long",
        day: "numeric",
        year: "numeric"
    });


    // Display date
    document.getElementById("date").innerText = date;
}


// Run immediately
displayClock();


// Update every 1 second
setInterval(displayClock, 1000);