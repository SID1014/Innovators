import React, { useEffect, useState } from "react";
import { getStations } from "../services/api";

export default function StationView() {
  const [stations, setStations] = useState([]);

  useEffect(() => {
    getStations().then(data => setStations(data.stations));
  }, []);

  return (
    <div>
      <h2>Stations</h2>
      <ul>
        {stations.map((s, idx) => <li key={idx}>{s}</li>)}
      </ul>
    </div>
  );
}
