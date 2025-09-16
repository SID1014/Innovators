import React, { useEffect, useState } from "react";
import TrainCard from "../components/Traincard";
import { getTrains } from "../services/trainService";

export default function TrainView() {
  const [trains, setTrains] = useState([]);
  const [lastUpdated, setLastUpdated] = useState(null);

  const fetchData = async () => {
    try {
      const data = await getTrains();
      setTrains(data.trains || []);
      setLastUpdated(new Date().toLocaleTimeString()); // track update time
    } catch (error) {
      console.error("Error fetching trains:", error);
    }
  };

  useEffect(() => {
    fetchData(); // initial fetch
    const interval = setInterval(fetchData, 30000); // refresh every 30s
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Trains</h2>
      <p style={{ fontSize: "0.9rem", color: "gray" }}>
        Last updated: {lastUpdated || "Loading..."}
      </p>
      {trains.length > 0 ? (
        trains.map((t, idx) => <TrainCard key={idx} train={t} />)
      ) : (
        <p>No train data available</p>
      )}
    </div>
  );
}
