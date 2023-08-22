const reviewInput = document.getElementById("reviews"); // Replace with your review input ID
    const reviewSection = document.getElementById("reviewSection");

    reviewInput.addEventListener("input", function() {
        if (this.value.trim() !== "") {
            reviewSection.style.display = "block";
        } else {
            reviewSection.style.display = "none";
        }
    });