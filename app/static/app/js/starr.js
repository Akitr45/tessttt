// Get all the radio buttons
var stars = document.querySelectorAll("input[name='rate']");

// Add an event listener to each radio button
for (var i = 0; i < stars.length; i++) {
    stars[i].addEventListener("click", function() {
        // Get the value of the clicked radio button
        var rating = this.value;

        // Do something with the rating, for example, display it on the page
        console.log("You have selected: " + rating + " star(s)");
    });
}
