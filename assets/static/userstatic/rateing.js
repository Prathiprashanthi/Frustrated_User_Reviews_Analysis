function checkRating() {
    const rating = document.getElementById("rating").value;

    if (rating === "") {
        alert("Please provide a rating before submitting!");
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}