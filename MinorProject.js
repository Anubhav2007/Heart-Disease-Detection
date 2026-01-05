document.getElementById("prediction-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    // Collect user input
    const formData = new FormData(event.target);
    
    const data = {
        age: formData.get("age"),
        sex: formData.get("sex"),
        cp: formData.get("cp"),
        trestbps: formData.get("trestbps"),
        chol: formData.get("chol"),
        fbs: formData.get("fbs"),
        restecg: formData.get("restecg"),
        thalach: formData.get("thalach"),
        exang: formData.get("exang"),
        oldpeak: formData.get("oldpeak"),
        slope: formData.get("slope"),
        ca: formData.get("ca"),
        thal: formData.get("thal")
    };

    // Send data to backend model
    const response = await fetch("/predict", { // Replace with your backend endpoint
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await response.json();

    // Display result
    const resultDiv = document.getElementById("result");

if (result.prediction === "likely") {
    resultDiv.innerHTML = `
        <h2 style="color: #d9534f;">⚠️ The patient is likely to have heart disease.</h2>
        <p><strong>Why:</strong></p>
        <ul>
            ${result.explanation && result.explanation.length > 0 
                ? result.explanation.map(reason => `<li>${reason}</li>`).join('')
                : '<li>Several key health indicators suggest a higher risk.</li>'}
        </ul>
        <p>Please consult a medical professional for further evaluation.</p>
    `;
} else {
    resultDiv.innerHTML = `
        <h2 style="color: #28a745;">✅ The patient is unlikely to have heart disease.</h2>
        <p><strong>Why:</strong></p>
        <ul>
            ${result.explanation && result.explanation.length > 0 
                ? result.explanation.map(reason => `<li>${reason}</li>`).join('')
                : '<li>Vital indicators are within normal ranges.</li>'}
        </ul>
        <p><strong>Continue maintaining a healthy lifestyle and consult your doctor for routine checkups.</strong></p>
    `;
}
});
