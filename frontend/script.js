document.getElementById("predictionForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    let featuresInput = document.getElementById("features").value;
    let featuresArray = featuresInput.split(",").map(Number);

    fetch("https://cropai-backend.onrender.com/predict", {
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

const featuresInput = document.getElementById("features");

featuresInput.addEventListener("input", function () {
    const values = featuresInput.value
        .split(",")
        .map(value => value.trim());

    // Feature order:
    // N, P, K, pH, Rainfall, Temp, Humidity,
    // Moisture, Soil Type, Rotation, Pest

    const ph = values[3];
    const rainfall = values[4];
    const temperature = values[5];
    const humidity = values[6];

    document.getElementById("temperatureValue").textContent =
        temperature !== undefined && temperature !== ""
            ? `${temperature}°C`
            : "--°C";

    document.getElementById("humidityValue").textContent =
        humidity !== undefined && humidity !== ""
            ? `${humidity}%`
            : "--%";

    document.getElementById("rainfallValue").textContent =
        rainfall !== undefined && rainfall !== ""
            ? `${rainfall} mm`
            : "-- mm";

    document.getElementById("phValue").textContent =
        ph !== undefined && ph !== ""
            ? ph
            : "--";
});
