const form = document.getElementById("scan-form");
const input = document.getElementById("ip");
const button = document.getElementById("scan-button");
const dashboard = document.getElementById("dashboard");
const errorBox = document.getElementById("error");
const resultsBox = document.getElementById("results");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const ip = input.value.trim();
  if (!ip) return;

  button.disabled = true;
  button.textContent = "SCANNING...";
  errorBox.classList.add("hidden");
  dashboard.classList.add("hidden");

  try {
    const response = await fetch("/api/scan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ip })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || "Scan failed.");
    }

    document.getElementById("target").textContent = data.target;
    document.getElementById("scanned").textContent = data.scanned;
    document.getElementById("open-count").textContent = data.open_count;

    resultsBox.innerHTML = data.results.map((item) => {
      return '<div class="result">' +
        '<span class="port">' + item.port + '/TCP</span>' +
        '<span class="service">' + item.service + '</span>' +
        '<span class="state ' + item.status + '">' + item.status.toUpperCase() + '</span>' +
      '</div>';
    }).join("");

    document.getElementById("result-badge").textContent =
      data.open_count ? "OPEN PORTS FOUND" : "NO OPEN PORTS";

    dashboard.classList.remove("hidden");
  } catch (error) {
    errorBox.textContent = error.message;
    errorBox.classList.remove("hidden");
  } finally {
    button.disabled = false;
    button.innerHTML = 'SCAN <span>→</span>';
  }
});
