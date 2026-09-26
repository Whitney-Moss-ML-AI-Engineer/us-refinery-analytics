let refineryData = [];

async function loadData() {
  const response = await fetch("/api/refineries");
  refineryData = await response.json();
  populateFilters(refineryData);
  render(refineryData);
}

function populateFilters(data) {
  const padd = [...new Set(data.map(d => d.padd).filter(Boolean))].sort();
  const complexity = [...new Set(data.map(d => d.complexity_tier).filter(Boolean))].sort();
  const p = document.getElementById("paddFilter");
  const c = document.getElementById("complexityFilter");
  padd.forEach(x => p.insertAdjacentHTML("beforeend", `<option>${x}</option>`));
  complexity.forEach(x => c.insertAdjacentHTML("beforeend", `<option>${x}</option>`));
  p.onchange = applyFilters;
  c.onchange = applyFilters;
}

function applyFilters() {
  const p = document.getElementById("paddFilter").value;
  const c = document.getElementById("complexityFilter").value;
  const filtered = refineryData.filter(d =>
    (p === "ALL" || d.padd === p) &&
    (c === "ALL" || d.complexity_tier === c)
  );
  render(filtered);
}

function render(data) {
  const capacity = data.map(d => Number(d.crude_capacity_bpd)).filter(Number.isFinite);
  const total = capacity.reduce((a,b) => a+b, 0);
  document.getElementById("kpis").innerHTML =
    `<div>Refineries<strong>${data.length}</strong></div>
     <div>Total capacity<strong>${total.toLocaleString()} bpd</strong></div>`;
  Plotly.newPlot("capacityChart", [{
    x: capacity, type: "histogram"
  }], {title: "Refinery Capacity Distribution"});
}

loadData();
