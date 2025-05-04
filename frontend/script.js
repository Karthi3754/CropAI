document.getElementById("predictionForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let featuresInput = document.getElementById("features").value;
    let featuresArray = featuresInput.split(",").map(Number);

    fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ features: featuresArray })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("output").innerText = "Predicted Crop: " + data.predicted_crop;
    })
    .catch(error => {
        document.getElementById("output").innerText = "Error: " + error;
    });
});
