const API_BASE = "http://127.0.0.1:8000"; // backend

export async function getStations() {
  const res = await fetch(`${API_BASE}/stations`);
  return res.json();
}

export async function getTrains() {
  const res = await fetch(`${API_BASE}/trains`);
  return res.json();
}
