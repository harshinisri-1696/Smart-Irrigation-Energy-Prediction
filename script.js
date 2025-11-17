function showPage(id) {
    document.querySelectorAll(".page")
        .forEach(p => p.classList.remove("active"));

    document.getElementById(id).classList.add("active");
}

fetch("/get-averages")
    .then(res => res.json())
    .then(data => {
        document.getElementById("avgTemp").innerText = data.avgTemp + "°C";
        document.getElementById("avgHum").innerText = data.avgHum + "%";
        document.getElementById("avgEnergy").innerText = data.avgEnergy + " kWh";
    });

document.getElementById("predictForm").addEventListener("submit", (e) => {
    e.preventDefault();

    const payload = {
        temperature: parseFloat(document.getElementById("temp").value),
        humidity: parseFloat(document.getElementById("hum").value),
        soil: parseFloat(document.getElementById("soil").value)
    };

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(payload)
    })
        .then(res => res.json())
        .then(data => {
            document.getElementById("result").innerText =
                "Predicted Energy: " + data.predicted + " kWh";
        });
});
