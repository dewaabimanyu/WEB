document.getElementById("calculateBtn").addEventListener("click", async () => {
  const formula = document.getElementById("formula").value.trim();
  const resultDiv = document.getElementById("result");

  if (!formula) {
    resultDiv.innerHTML = "❗ Masukkan rumus terlebih dahulu.";
    return;
  }

  resultDiv.innerHTML = "⏳ Menghitung...";

  try {
    const response = await fetch("/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ formula })
    });

    const data = await response.json();

    if (data.success) {
      resultDiv.innerHTML = `💡 Massa molar <b>${formula}</b> = <b>${data.mass} g/mol</b>`;
    } else {
      resultDiv.innerHTML = `⚠️ Error: ${data.error}`;
    }
  } catch (err) {
    resultDiv.innerHTML = "⚠️ Terjadi kesalahan koneksi.";
  }
});
